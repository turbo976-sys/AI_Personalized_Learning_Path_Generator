import json
import os
import networkx as nx

class KnowledgeGraphEngine:
    def __init__(self, data_path: str = None):
        if not data_path:
            # Default to the data file we generated
            data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "skill_graph.json")
            
        self.graph = nx.DiGraph()
        self._load_graph(data_path)

    def _load_graph(self, filepath: str):
        with open(filepath, 'r') as f:
            edges = json.load(f)
            
        for edge in edges:
            self.graph.add_edge(edge["source"], edge["target"], weight=edge["weight"])

    def get_prerequisites(self, target_skill: str) -> list:
        """Returns immediate prerequisites for a given skill."""
        if target_skill in self.graph:
            return list(self.graph.predecessors(target_skill))
        return []

    def get_learning_path(self, start_nodes: list, target_nodes: list) -> list:
        """
        Calculates a logical sequence of skills to learn.
        If start_nodes are empty, finds the topological sort of the subgraph leading to target_nodes.
        For simplicity, we do a topological sort on the subgraph formed by ancestors of target_nodes.
        """
        # Get all ancestors
        needed_nodes = set(target_nodes)
        for target in target_nodes:
            if target in self.graph:
                needed_nodes.update(nx.ancestors(self.graph, target))
                
        # Remove already known skills (start_nodes)
        for start in start_nodes:
            needed_nodes.discard(start)
            # Remove descendants of start nodes that may also be satisfied implicitly? No, keep it simple.

        subgraph = self.graph.subgraph(needed_nodes)
        
        try:
            # Sort chronologically based on dependencies
            ordered_path = list(nx.topological_sort(subgraph))
            return ordered_path
        except nx.NetworkXUnfeasible:
            # If cycle exists, just return the nodes
            return list(needed_nodes)
