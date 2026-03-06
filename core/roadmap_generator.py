import textwrap

class RoadmapGenerator:
    def __init__(self, model_name: str = "google/flan-t5-small"):
        """
        Initialize the generative model.
        In a real scenario, this would load the model:
        from transformers import pipeline
        self.pipe = pipeline("text2text-generation", model=model_name)
        """
        self.model_name = model_name
        self.is_mock = True 

    def generate_roadmap(self, goal: str, missing_skills: list, optimal_path: list) -> str:
        """
        Generates a roadmap based on the missing skills and graph path.
        Using a mock generation for speed, but interface mimics T5 output.
        """
        prompt = f"Goal: {goal}. Path: {', '.join(optimal_path)}. Generate Roadmap:"
        
        if self.is_mock:
            stages = []
            for i, skill in enumerate(optimal_path):
                stages.append(f"Stage {i+1}: {skill}")
            if not optimal_path and missing_skills:
                # Fallback if graph path is empty
                for i, skill in enumerate(missing_skills):
                    stages.append(f"Stage {i+1}: {skill}")
                    
            stages.append(f"Stage {len(stages)+1}: Capstone Projects & Deployment")
            roadmap_text = "\n\n".join(stages)
            return roadmap_text
        else:
            # Real execution
            # return self.pipe(prompt, max_length=150)[0]['generated_text']
            pass
