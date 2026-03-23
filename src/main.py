"""
main.py
Runs the simulation and launches the animated pie chart.
"""
import numpy as np
from data_generator import generate_synthetic_returns
from risk_contribution import risk_contributions
from visualization import animate_pie_chart

def main():
    # Generate synthetic returns
    returns, asset_names = generate_synthetic_returns(num_assets=4, num_periods=500)
    cov_matrix = np.cov(returns, rowvar=False)
    initial_weights = np.ones(len(asset_names)) / len(asset_names)

    def get_rc(weights):
        return risk_contributions(weights, cov_matrix)

    animate_pie_chart(asset_names, get_rc, initial_weights)

if __name__ == "__main__":
    main()
