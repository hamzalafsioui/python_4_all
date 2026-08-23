"""
PROJECT: Vectors, Matrices, and NumPy

This project demonstrates the power of Matrix Multiplication by simulating a
Markov Chain. A Markov Chain is an AI / statistical model used to predict a sequence 
of events based entirely on probabilities of moving from one state to another.

Scenario: Customer Behavior on an E-Commerce Website.
"""

import numpy as np
import time

# =====================================================================
# THE MARKOV CHAIN SIMULATOR
# =====================================================================

class CustomerBehaviorSimulator:
    def __init__(self):
        # The 4 possible states a customer can be in:
        self.states = ["Browsing", "In Cart", "Checked Out", "Left Site"]
        
        # TRANSITION MATRIX
        # Rows represent the CURRENT state, Columns represent the NEXT state.
        # Values are probabilities (must sum to 1.0 across each row).
        # Order: [Browsing, In Cart, Checked Out, Left Site]
        self.transition_matrix = np.array([
            # From Browsing: 60% stay browsing, 20% add to cart, 0% checkout, 20% leave
            [0.60, 0.20, 0.00, 0.20],
            
            # From In Cart: 10% go back to browse, 50% stay in cart, 30% checkout, 10% leave
            [0.10, 0.50, 0.30, 0.10],
            
            # From Checked Out: Terminal state (100% stay here once reached)
            [0.00, 0.00, 1.00, 0.00],
            
            # From Left Site: Terminal state (100% stay here once reached)
            [0.00, 0.00, 0.00, 1.00]
        ])
        
    def verify_matrix(self):
        """Verifies that all rows in the transition matrix sum to 1.0"""
        row_sums = np.sum(self.transition_matrix, axis=1)
        is_valid = np.allclose(row_sums, 1.0)
        
        print(f"Verifying Transition Matrix probabilities sum to 1.0: {is_valid}")
        if not is_valid:
            print(f"Error: Row sums are {row_sums}")
        print("-" * 50)
            
    def simulate(self, initial_population, time_steps):
        """
        Simulates customer movement across the site over time.
        Uses pure Matrix Multiplication (X @ M)
        """
        # Ensure our input is a floating point numpy array
        current_state = np.array(initial_population, dtype=float)
        total_customers = int(np.sum(current_state))
        
        print(f"\n--- SIMULATION START: {total_customers} Customers ---")
        self._print_state(0, current_state)
        
        for step in range(1, time_steps + 1):
            # THE CORE AI MECHANIC:
            # We multiply the current population vector by the transition matrix.
            # This instantly calculates the new distribution of all customers!
            current_state = current_state @ self.transition_matrix
            
            self._print_state(step, current_state)
            time.sleep(0.1) # Small pause for visual effect
            
        print("-" * 60)
        print("SIMULATION COMPLETE.")
        
    def _print_state(self, step, state_vector):
        """Helper to beautifully print the state vector"""
        if step == 0:
            print(f"Time Step {step} (Initial State):")
        else:
            print(f"Time Step {step}:")
            
        # Format the numbers nicely
        output = []
        for name, count in zip(self.states, state_vector):
            output.append(f"  {name}: {int(count):>5}")
            
        print(" | ".join(output))

# =====================================================================
# MAIN EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("=== AI MARKOV CHAIN ENGINE ===")
    print("=" * 60)
    
    simulator = CustomerBehaviorSimulator()
    simulator.verify_matrix()
    
    # We start with 10,000 customers currently browsing the site, 
    # 0 in cart, 0 checked out, 0 left.
    # Shape: (4,)
    initial_customers = [10000, 0, 0, 0]
    
    # Simulate their journey over 10 time steps (e.g., 10 minutes)
    simulator.simulate(initial_population=initial_customers, time_steps=10)
