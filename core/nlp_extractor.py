import json
import os
from typing import List

# A mock for NER skill extraction. In production, this would use a Spacy or BERT NER model.
# Since we are focusing on ML/AI, we have a predefined skill set.
KNOWN_SKILLS = [
    "Python", "SQL", "Statistics", "Data Manipulation", "Data Visualization",
    "Machine Learning", "Deep Learning", "NLP", "Computer Vision",
    "LLMs", "MLOps", "Git"
]

ROLES_REQUIREMENTS = {
    "Machine Learning Engineer": ["Python", "SQL", "Data Manipulation", "Machine Learning", "MLOps", "Git"],
    "Data Scientist": ["Python", "SQL", "Statistics", "Data Manipulation", "Data Visualization", "Machine Learning"],
    "NLP Engineer": ["Python", "Machine Learning", "Deep Learning", "NLP", "LLMs"],
    "Deep Learning Researcher": ["Python", "Mathematics", "Machine Learning", "Deep Learning", "Computer Vision", "NLP"]
}

def extract_skills_from_text(text: str) -> List[str]:
    """Extracts known skills from user text input based on keywords."""
    found_skills = []
    text_lower = text.lower()
    for skill in KNOWN_SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)
    return found_skills

def detect_goal_intent(text: str) -> str:
    """Simple intent matching for goal. Production would use sentence-transformers."""
    text_lower = text.lower()
    for role in ROLES_REQUIREMENTS.keys():
        if role.lower() in text_lower:
            return role
    return "Machine Learning Engineer" # Default fallback

def calculate_skill_gaps(current_skills: List[str], target_role: str) -> List[str]:
    """Identifies missing skills required for the target role."""
    required = ROLES_REQUIREMENTS.get(target_role, [])
    # Case insensitive comparison
    curr_lower = [s.lower() for s in current_skills]
    missing = [req for req in required if req.lower() not in curr_lower]
    return missing
