import json
import os
import numpy as np

class CourseRecommender:
    def __init__(self, data_path: str = None):
        if not data_path:
            data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "courses_dataset.json")
            
        with open(data_path, 'r') as f:
            self.courses = json.load(f)
            
        self.is_mock = True
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            self.is_mock = False
            self._build_embeddings()
        except ImportError:
            print("Warning: sentence-transformers not installed. Using keyword matching fallback.")

    def _build_embeddings(self):
        # Create texts to embed: Title + Topics
        texts = [f"{c['title']} {' '.join(c['topics'])}" for c in self.courses]
        self.course_embeddings = self.model.encode(texts)

    def recommend(self, topic: str, top_k: int = 3) -> list:
        if self.is_mock:
            # Fallback simple keyword match
            topic_lower = topic.lower()
            scored_courses = []
            for c in self.courses:
                score = 0
                if topic_lower in c['title'].lower(): score += 2
                for t in c['topics']:
                    if topic_lower in t.lower() or t.lower() in topic_lower:
                        score += 1
                scored_courses.append((score, c))
            # Sort by score descending
            scored_courses.sort(key=lambda x: x[0], reverse=True)
            return [c for score, c in scored_courses[:top_k] if score > 0]
        else:
            from sklearn.metrics.pairwise import cosine_similarity
            query_embedding = self.model.encode([topic])
            similarities = cosine_similarity(query_embedding, self.course_embeddings)[0]
            
            # Get top_k indices
            top_indices = np.argsort(similarities)[::-1][:top_k]
            
            recommendations = []
            for idx in top_indices:
                if similarities[idx] > 0.2: # basic syntax threshold
                    recommendations.append(self.courses[idx])
            return recommendations
