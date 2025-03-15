"""
reinforcement_learning.py: Implements a simple reinforcement learning (RL) module for dynamic pricing.
This example uses a Q-learning algorithm for demonstration purposes.
"""

import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ReinforcementLearning")

class PricingAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.95, exploration_rate=1.0, exploration_decay=0.99):
        self.actions = actions
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_rate
        self.epsilon_decay = exploration_decay
        # Initialize Q-table as a dictionary: state -> action values
        self.q_table = {}

    def get_state_key(self, state):
        # Convert state tuple to a string key for dictionary lookup
        return str(state)

    def choose_action(self, state):
        key = self.get_state_key(state)
        if key not in self.q_table:
            self.q_table[key] = np.zeros(len(self.actions))
        # Epsilon-greedy strategy
        if np.random.rand() < self.epsilon:
            action = np.random.choice(self.actions)
            logger.info("Exploring: Choosing random action %s for state %s", action, state)
            return action
        else:
            action = self.actions[np.argmax(self.q_table[key])]
            logger.info("Exploiting: Choosing best action %s for state %s", action, state)
            return action

    def update_q(self, state, action, reward, next_state):
        key = self.get_state_key(state)
        next_key = self.get_state_key(next_state)
        if key not in self.q_table:
            self.q_table[key] = np.zeros(len(self.actions))
        if next_key not in self.q_table:
            self.q_table[next_key] = np.zeros(len(self.actions))
        action_index = self.actions.index(action)
        best_next_action = np.max(self.q_table[next_key])
        td_target = reward + self.gamma * best_next_action
        td_error = td_target - self.q_table[key][action_index]
        self.q_table[key][action_index] += self.lr * td_error
        # Decay exploration rate
        self.epsilon *= self.epsilon_decay

if __name__ == "__main__":
    # Define a simple scenario: State represents current demand level, actions are price adjustments.
    actions = [-10, 0, 10]  # Price change: decrease, no change, increase
    agent = PricingAgent(actions)

    # Example simulation: 10 iterations
    current_state = (100,)  # e.g., current booking count
    for i in range(10):
        action = agent.choose_action(current_state)
        # Simulate reward: higher bookings lead to higher revenue
        reward = np.random.rand() * 10 + action  # Simplified reward function
        next_state = (current_state[0] + np.random.randint(-5, 6),)
        agent.update_q(current_state, action, reward, next_state)
        current_state = next_state
        logger.info("Iteration %d, New state: %s, Reward: %.2f", i+1, current_state, reward)
