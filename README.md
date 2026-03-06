# AI_Personalized_Learning_Path_Generator
🎓 AI Personalized Learning Path Generator
==========================================

An **AI-powered web assistant** that generates **personalized study roadmaps** based on a user's career goal.The system uses **Deep Learning, Natural Language Processing (NLP), Knowledge Graphs, and Transformer models** to analyze user goals, detect skill gaps, and recommend a structured learning path.

Example:

**Input**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   I want to become a Machine Learning Engineer   `

**Output**

*   Programming Fundamentals
    
*   Python for Data Science
    
*   Mathematics for ML
    
*   Machine Learning Algorithms
    
*   Deep Learning
    
*   MLOps
    
*   Real-world Projects
    

🚀 Features
===========

✅ Personalized learning roadmap generation✅ NLP-based goal understanding✅ Skill gap detection✅ Knowledge graph-based skill relationships✅ Deep learning model for roadmap generation✅ Interactive web assistant using Streamlit✅ SQL database to store user profiles and learning progress✅ Scalable architecture for future AI upgrades

🧠 AI & NLP Components
======================

The system integrates several AI components:

### 1️⃣ Natural Language Processing

User career goals are processed using NLP techniques.

Tasks:

*   Text preprocessing
    
*   Intent detection
    
*   Keyword extraction
    
*   Career domain classification
    

Libraries:

*   spaCy
    
*   NLTK
    
*   Transformers
    

### 2️⃣ Skill Gap Detection

The system compares:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   User skillsVSRequired skills for the target career   `

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

### 3️⃣ Knowledge Graph Modeling

A **skill knowledge graph** connects concepts like:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Python → NumPy → Pandas → Data AnalysisMachine Learning → Supervised Learning → RegressionDeep Learning → Neural Networks → CNN → NLP   `

This helps generate **logical learning sequences**.

Tools:

*   NetworkX
    
*   Neo4j (optional)
    
*   Graph-based skill dependency modeling
    

### 4️⃣ Roadmap Generation with T5

A **Transformer-based model (T5)** generates structured learning paths.

Model used:

*   T5-small
    
*   T5-base
    
*   Flan-T5
    

Example prompt to the model:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Generate a learning roadmap to become a Machine Learning Engineer   `

Output:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Step 1: Learn Python programmingStep 2: Study linear algebra and statisticsStep 3: Learn data analysis using PandasStep 4: Study machine learning algorithmsStep 5: Learn deep learning frameworksStep 6: Build real-world ML projects   `

🏗️ System Architecture
=======================

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   User Input   │   ▼NLP Goal Understanding   │   ▼Skill Gap Detection   │   ▼Knowledge Graph Analysis   │   ▼T5 Roadmap Generation   │   ▼Streamlit Web Assistant   │   ▼SQL Database (User Data)   `

🖥️ Tech Stack
==============

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
    

📂 Project Structure
====================

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   AI-Learning-Path-Generator│├── app.py├── roadmap_generator.py├── skill_gap_detector.py├── knowledge_graph.py├── model/│   └── t5_model.py│├── database/│   └── user_data.db│├── data/│   └── skills_dataset.csv│├── utils/│   └── text_processing.py│├── requirements.txt└── README.md   `

⚙️ Installation
===============

Clone the repository

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/yourusername/AI-Learning-Path-Generator.gitcd AI-Learning-Path-Generator   `

Install dependencies

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

▶️ Run the Application
======================

Start the Streamlit app:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit run app.py   `

Open in browser:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://localhost:8501   `

💻 Example Usage
================

User input:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   I want to become a Data Scientist   `

Generated roadmap:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   1. Learn Python2. Learn statistics and probability3. Study data analysis4. Learn machine learning5. Learn deep learning6. Work on real-world projects7. Learn MLOps   `
