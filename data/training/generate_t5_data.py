import pandas as pd
import random
import os

# Sample concepts
goals = ["Machine Learning Engineer", "Data Scientist", "NLP Engineer", "Deep Learning Researcher"]
skills = ["Python", "SQL", "Statistics", "Data Manipulation", "Machine Learning", "Deep Learning", "NLP"]

data = []

for _ in range(100):
    goal = random.choice(goals)
    num_curr = random.randint(1, 4)
    curr_skills = random.sample(skills, num_curr)
    missing_skills = [s for s in skills if s not in curr_skills]
    
    # Prompt formulation
    input_text = f"Goal: {goal}. Current Skills: {', '.join(curr_skills)}. Missing Skills: {', '.join(missing_skills)}. Generate Roadmap:"
    
    # Target formulation
    stages = []
    for idx, ms in enumerate(missing_skills):
        stages.append(f"Stage {idx+1}: {ms}")
    stages.append(f"Stage {len(missing_skills)+1}: Projects & Deployment")
    
    target_text = " -> ".join(stages)
    
    data.append({"input_text": input_text, "target_text": target_text})

df = pd.DataFrame(data)
output_path = os.path.join(os.path.dirname(__file__), "t5_dataset.csv")
df.to_csv(output_path, index=False)

print(f"Generated {len(df)} synthetic examples for T5 fine-tuning at {output_path}")
