import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network
import json
import base64

from core.nlp_extractor import detect_goal_intent, extract_skills_from_text, calculate_skill_gaps, KNOWN_SKILLS, ROLES_REQUIREMENTS
from core.graph_builder import KnowledgeGraphEngine
from core.roadmap_generator import RoadmapGenerator
from core.recommender import CourseRecommender
from database.db_ops import engine, SessionLocal
from database import models, crud
import database.setup_db as setup_db

# Initialize DB
models.Base.metadata.create_all(bind=engine)

st.set_page_config(page_title="Personalized Learning Path Generator", layout="wide")
st.title("🎓 AI Personalized Learning Path Generator")

with st.sidebar:
    st.header("👤 User Account")
    username = st.text_input("Enter Username")
    if username:
        db = SessionLocal()
        user = crud.get_user_by_username(db, username)
        if not user:
            user = crud.create_user(db, username)
        st.success(f"Logged in as {username}")
        db.close()
    else:
        st.info("Please enter a username to save your progress.")

# --- System Initialization ---
@st.cache_resource
def load_engines():
    kg_engine = KnowledgeGraphEngine()
    roadmap_gen = RoadmapGenerator()
    recommender = CourseRecommender()
    return kg_engine, roadmap_gen, recommender

kg_engine, roadmap_gen, recommender = load_engines()

st.markdown("### Tell us your goals!")
user_input = st.text_area("Describe your career goal and your current skills.", 
                          placeholder="E.g., I want to become a Machine Learning Engineer. I know basic Python and SQL.")

if st.button("Generate Learning Path"):
    if not user_input:
        st.warning("Please enter your career goal and skills.")
    else:
        with st.spinner("Analyzing your profile using NLP..."):
            # 1. NLP Processing
            target_role = detect_goal_intent(user_input)
            current_skills = extract_skills_from_text(user_input)
            missing_skills = calculate_skill_gaps(current_skills, target_role)
            
            # Save to DB if user
            if username:
                db = SessionLocal()
                user = crud.get_user_by_username(db, username)
                if user:
                    user.career_goal = target_role
                    db.commit()
                else:
                    user = crud.create_user(db, username, target_role)
                
                skills_data = [{'skill_name': s, 'status': 'current'} for s in current_skills] + \
                              [{'skill_name': s, 'status': 'missing'} for s in missing_skills]
                crud.update_user_skills(db, user.id, skills_data)
                db.close()

        st.subheader(f"🎯 Target Role Detected: **{target_role}**")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Your Current Skills")
            for skill in current_skills:
                st.write(f"✅ {skill}")
            if not current_skills:
                st.write("None detected. Time to learn from scratch!")
                
        with col2:
            st.markdown("#### Skill Gap (Missing Skills)")
            for skill in missing_skills:
                st.write(f"❌ {skill}")
            if not missing_skills:
                st.write("You have all the required skills for this role! 🎉")
        
        st.divider()
        
        # 2. Graph Traversal
        with st.spinner("Building Knowledge Graph and computing optimal path..."):
            optimal_path = kg_engine.get_learning_path(current_skills, missing_skills)
            
            # Visualize Graph
            net = Network(height='400px', width='100%', directed=True, bgcolor="#222222", font_color="white")
            for node in kg_engine.graph.nodes():
                if node in current_skills:
                    net.add_node(node, color="#00ff00") # Green for known
                elif node in optimal_path:
                    net.add_node(node, color="#ff0000") # Red for to learn
                else:
                    net.add_node(node, color="#aaaaaa") # Grey for others
            
            for edge in kg_engine.graph.edges():
                net.add_edge(edge[0], edge[1])
                
            path_graph = "graph.html"
            net.save_graph(path_graph)
            
            st.markdown("### 🕸️ Skill Dependency Graph")
            st.caption("Green: Known, Red: To Learn, Grey: Other skills")
            HtmlFile = open(path_graph, 'r', encoding='utf-8')
            source_code = HtmlFile.read() 
            components.html(source_code, height=420)
            
        st.divider()
        
        # 3. Roadmap Generation
        with st.spinner("Generating personalized study roadmap powered by T5..."):
            roadmap = roadmap_gen.generate_roadmap(target_role, missing_skills, optimal_path)
            
            # Save to DB
            if username:
                db = SessionLocal()
                user = crud.get_user_by_username(db, username)
                crud.save_roadmap(db, user.id, roadmap)
                db.close()

            st.markdown("### 🗺️ Your Personalized Learning Roadmap")
            
            # Create interactive stages
            stages = [s.strip() for s in roadmap.split("\n\n") if s.strip()]
            for stage in stages:
                with st.expander(stage, expanded=True):
                    # Extract the topic from stage text 
                    parts = stage.split(":")
                    if len(parts) > 1:
                        topic = parts[1].strip()
                        st.markdown(f"**Focus Area:** {topic}")
                        
                        # 4. Course Recommendation
                        recommendations = recommender.recommend(topic)
                        if recommendations:
                            st.write("**📚 Recommended Resources:**")
                            for rec in recommendations:
                                st.markdown(f"- [{rec['title']}]({rec['url']}) - *Course*")
                        else:
                            st.write("No specific courses found for this topic.")
                    else:
                        st.write("Review projects and capstones.")

        # Download Plan Button
        st.markdown("---")
        b64 = base64.b64encode(roadmap.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="learning_roadmap.txt">📥 Download Roadmap as Text File</a>'
        st.markdown(href, unsafe_allow_html=True)
