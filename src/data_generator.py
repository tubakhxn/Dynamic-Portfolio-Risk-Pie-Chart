"""
data_generator.py
Generates synthetic returns for a set of assets.
"""
import numpy as np

def generate_synthetic_returns(num_assets=4, num_periods=500, seed=42):
    """
    Generate synthetic returns for a given number of assets and periods.
    Args:
        num_assets (int): Number of assets.
        num_periods (int): Number of time periods.
        seed (int): Random seed for reproducibility.
    Returns:
        np.ndarray: Returns matrix of shape (num_periods, num_assets)
        list: Asset names
    """
    np.random.seed(seed)
    means = np.random.uniform(0.0005, 0.002, num_assets)
    stds = np.random.uniform(0.01, 0.03, num_assets)
    returns = np.random.normal(loc=means, scale=stds, size=(num_periods, num_assets))
    asset_names = [f"Asset {chr(65+i)}" for i in range(num_assets)]
    return returns, asset_names
