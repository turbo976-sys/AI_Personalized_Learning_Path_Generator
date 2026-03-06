from core.nlp_extractor import detect_goal_intent, extract_skills_from_text, calculate_skill_gaps
from core.graph_builder import KnowledgeGraphEngine
from core.roadmap_generator import RoadmapGenerator
from core.recommender import CourseRecommender

def main():
    print("--- Starting End-to-End Test Flow ---\n")
    
    # 1. User Input
    user_input = "I want to become a Machine Learning Engineer. I have some experience with Python and SQL."
    print(f"User Input: '{user_input}'\n")

    # 2. NLP Processing
    target_role = detect_goal_intent(user_input)
    current_skills = extract_skills_from_text(user_input)
    missing_skills = calculate_skill_gaps(current_skills, target_role)

    print(f"Detected Target Role: {target_role}")
    print(f"Current Skills Found: {current_skills}")
    print(f"Skill Gap Identified: {missing_skills}\n")

    # 3. Knowledge Graph
    print("Initializing Knowledge Graph Engine...")
    kg_engine = KnowledgeGraphEngine()
    optimal_path = kg_engine.get_learning_path(current_skills, missing_skills)
    print(f"Optimal Learning Path (Graph Traversal): {optimal_path}\n")

    # 4. Roadmap Generation
    print("Generating Roadmap with generative module...")
    roadmap_gen = RoadmapGenerator()
    roadmap = roadmap_gen.generate_roadmap(target_role, missing_skills, optimal_path)
    print("Generated Roadmap:\n")
    print(roadmap)
    print("\n")

    # 5. Course Recommendation
    print("Fetching Recommended Courses for First Topic in Roadmap...")
    recommender = CourseRecommender()
    first_topic = optimal_path[0] if optimal_path else missing_skills[0]
    
    recs = recommender.recommend(first_topic)
    for rec in recs:
        print(f"- {rec['title']} ({rec['type']}): {rec['url']}")
        
    print("\n--- End-to-End Test Completed ---")

if __name__ == "__main__":
    main()
