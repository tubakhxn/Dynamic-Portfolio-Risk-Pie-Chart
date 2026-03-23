"""
risk_contribution.py
Calculates portfolio volatility and each asset's risk contribution.
"""
import numpy as np

def portfolio_volatility(weights, cov_matrix):
    """
    Calculate total portfolio volatility.
    Args:
        weights (np.ndarray): Portfolio weights (N,)
        cov_matrix (np.ndarray): Covariance matrix (N,N)
    Returns:
        float: Portfolio volatility (std dev)
    """
    return np.sqrt(weights.T @ cov_matrix @ weights)

def risk_contributions(weights, cov_matrix):
    """
    Calculate each asset's contribution to portfolio volatility.
    Args:
        weights (np.ndarray): Portfolio weights (N,)
        cov_matrix (np.ndarray): Covariance matrix (N,N)
    Returns:
        np.ndarray: Risk contributions (N,)
    """
    port_vol = portfolio_volatility(weights, cov_matrix)
    # Marginal contribution: (cov_matrix @ weights) / port_vol
    mrc = cov_matrix @ weights / port_vol
    # Component contribution: weights * marginal
    rc = weights * mrc
    # Normalize to sum to 1 (percentage contribution)
    return rc / rc.sum()
