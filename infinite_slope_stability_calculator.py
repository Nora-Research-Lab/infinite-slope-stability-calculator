import math

def calculate_factor_of_safety(c_prime, phi_prime, beta, gamma, z, h_w):
    """
    Calculate the factor of safety for infinite slope stability.
    
    Parameters:
    - c_prime: Effective cohesion (kPa)
    - phi_prime: Effective friction angle (degrees)
    - beta: Slope angle (degrees)
    - gamma: Soil unit weight (kN/m³)
    - z: Depth to potential failure plane (m)
    - h_w: Water height above failure plane (m)
    
    Returns:
    - Factor of safety (FS)
    - Stability classification
    """
    # Constants
    gamma_w = 9.81  # Water unit weight in kN/m³
    
    # Convert angles to radians
    beta_rad = math.radians(beta)
    phi_prime_rad = math.radians(phi_prime)
    
    # Check for flat slope condition (beta = 0)
    if abs(beta_rad) < 1e-9:  # effectively zero
        return 999.0, "Flat slope - no sliding potential"
    
    # Compute effective normal stress term
    sigma_n_prime = (gamma * z * math.cos(beta_rad)**2) - (gamma_w * h_w * math.cos(beta_rad)**2)
    
    # Compute shear stress term
    tau = gamma * z * math.sin(beta_rad) * math.cos(beta_rad)
    
    # Calculate factor of safety
    if abs(tau) < 1e-9:  # Avoid division by zero if tau is very close to zero
        fs = 999.0
    else:
        fs = (c_prime + sigma_n_prime * math.tan(phi_prime_rad)) / tau
    
    # Classify stability based on FS value
    if fs < 1.0:
        classification = "Unstable"
    elif 1.0 <= fs < 1.25:
        classification = "Marginal"
    elif 1.25 <= fs <= 1.5:
        classification = "Fair"
    else:
        classification = "Good"
    
    return fs, classification
