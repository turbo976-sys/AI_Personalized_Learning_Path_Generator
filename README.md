# AI_Personalized_Learning_Path_Generator
  `
# 🎓 AI Personalized Learning Path Generator

An **AI-powered web assistant** that generates **personalized study roadmaps** based on a user's career goal.  
The system uses **Deep Learning, Natural Language Processing (NLP), Knowledge Graphs, and Transformer models** to analyze user goals, detect skill gaps, and recommend a structured learning path.

Example:

**Input**

I want to become a Machine Learning Engineer

**Output**

*   Programming Fundamentals
    
*   Python for Data Science
    
*   Mathematics for ML
    
*   Machine Learning Algorithms
    
*   Deep Learning
    
*   MLOps
    
*   Real-world Projects
    

* * *

# 🚀 Features

✅ Personalized learning roadmap generation  
✅ NLP-based goal understanding  
✅ Skill gap detection  
✅ Knowledge graph-based skill relationships  
✅ Deep learning model for roadmap generation  
✅ Interactive web assistant using Streamlit  
✅ SQL database to store user profiles and learning progress  
✅ Scalable architecture for future AI upgrades

* * *

# 🧠 AI & NLP Components

The system integrates several AI components:

### 1️⃣ Natural Language Processing

User career goals are processed using NLP techniques.

Tasks:

*   Text preprocessing
    
*   Intent detection
    
*   Keyword extraction
    
*   Career domain classification
    

Libraries:

*   `spaCy`
    
*   `NLTK`
    
*   `Transformers`
    

* * *

### 2️⃣ Skill Gap Detection

The system compares:

User skills  
VS  
Required skills for the target career

A **knowledge graph of skills** is used to determine missing skills.

Example:

Goal: **ML Engineer**

Required skills:

*   Python
    
*   Statistics
    
*   Machine Learning
    
*   Deep Learning
    
*   Data Engineering
    

Missing skills are recommended in the roadmap.

* * *

### 3️⃣ Knowledge Graph Modeling

A **skill knowledge graph** connects concepts like:

Python → NumPy → Pandas → Data Analysis  
Machine Learning → Supervised Learning → Regression  
Deep Learning → Neural Networks → CNN → NLP

This helps generate **logical learning sequences**.

Tools:

*   `NetworkX`
    
*   `Neo4j` (optional)
    
*   Graph-based skill dependency modeling
    

* * *

### 4️⃣ Roadmap Generation with T5

A **Transformer-based model (T5)** generates structured learning paths.

Model used:

*   `T5-small`
    
*   `T5-base`
    
*   `Flan-T5`
    

Example prompt to the model:

Generate a learning roadmap to become a Machine Learning Engineer

Output:

Step 1: Learn Python programming  
Step 2: Study linear algebra and statistics  
Step 3: Learn data analysis using Pandas  
Step 4: Study machine learning algorithms  
Step 5: Learn deep learning frameworks  
Step 6: Build real-world ML projects

* * *

# 🏗️ System Architecture

User Input  
   │  
   ▼  
NLP Goal Understanding  
   │  
   ▼  
Skill Gap Detection  
   │  
   ▼  
Knowledge Graph Analysis  
   │  
   ▼  
T5 Roadmap Generation  
   │  
   ▼  
Streamlit Web Assistant  
   │  
   ▼  
SQL Database (User Data)

* * *

# 🖥️ Tech Stack

### Programming

*   Python
    

### AI / ML

*   PyTorch
    
*   HuggingFace Transformers
    
*   Scikit-learn
    

### NLP

*   spaCy
    
*   NLTK
    
*   Sentence Transformers
    

### Knowledge Graph

*   NetworkX
    
*   Neo4j (optional)
    

### Backend

*   Python
    
*   SQL (SQLite / PostgreSQL)
    

### Web Interface

*   Streamlit
    

* * *

# 📂 Project Structure

AI-Learning-Path-Generator  
│  
├── app.py  
├── roadmap\_generator.py  
├── skill\_gap\_detector.py  
├── knowledge\_graph.py  
├── model/  
│   └── t5\_model.py  
│  
├── database/  
│   └── user\_data.db  
│  
├── data/  
│   └── skills\_dataset.csv  
│  
├── utils/  
│   └── text\_processing.py  
│  
├── requirements.txt  
└── README.md

* * *

# ⚙️ Installation

Clone the repository

git clone https://github.com/yourusername/AI-Learning-Path-Generator.git  
cd AI-Learning-Path-Generator

Install dependencies

pip install \-r requirements.txt

* * *

# ▶️ Run the Application

Start the Streamlit app:

streamlit run app.py

Open in browser:

http://localhost:8501

* * *

# 💻 Example Usage

User input:

I want to become a Data Scientist

Generated roadmap:

1\. Learn Python  
2\. Learn statistics and probability  
3\. Study data analysis  
4\. Learn machine learning  
5\. Learn deep learning  
6\. Work on real-world projects  

7\. Learn MLOps \`
