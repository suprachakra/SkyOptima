"""
Implements a network disruption module using a Graph Neural Network (GNN) approach.
This module predicts cascading effects of disruptions in real time.
Note: This is a simplified version for demonstration.
"""

import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NetworkDisruption")

class DisruptionPredictor:
    def __init__(self, network_graph: dict):
        """
        Initializes the predictor with a given network graph.
        
        Args:
            network_graph (dict): Keys are nodes (e.g., airports) and values are lists of connected nodes.
        """
        self.network_graph = network_graph
        logger.info("DisruptionPredictor initialized with network graph.")

    def predict_cascading_effects(self, delay_event: dict) -> dict:
        """
        Predict cascading effects for a given delay event using a mock GNN approach.
        
        Args:
            delay_event (dict): Contains keys 'node' and 'delay'.
        
        Returns:
            dict: Predicted delays on connected nodes.
        """
        affected_nodes = {}
        source = delay_event.get("node")
        base_delay = delay_event.get("delay", 0)
        if source in self.network_graph:
            for neighbor in self.network_graph[source]:
                propagated_delay = base_delay * np.random.uniform(0.3, 0.7)
                affected_nodes[neighbor] = round(propagated_delay, 2)
        logger.info("Predicted cascading effects: %s", affected_nodes)
        return affected_nodes

if __name__ == "__main__":
    # Example network graph
    network_graph = {
        "Airport_A": ["Airport_B", "Airport_C"],
        "Airport_B": ["Airport_A", "Airport_D"],
        "Airport_C": ["Airport_A", "Airport_D"],
        "Airport_D": ["Airport_B", "Airport_C"]
    }
    predictor = DisruptionPredictor(network_graph)
    delay_event = {"node": "Airport_A", "delay": 30}
    impact = predictor.predict_cascading_effects(delay_event)
    print("Cascading Impact:", impact)
