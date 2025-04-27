def score_predictor(x1, x2):
    """
    Predicts a score based on two input features using a simple linear regression model.
    
    Parameters:
    x1 (float): The first feature/input value.
    x2 (float): The second feature/input value.
    
    Returns:
    float: The predicted score.
    """
    # Coefficients for the linear regression model (can be adjusted as needed)
    coef_x1 = 0.5
    coef_x2 = 0.3
    intercept = 2.0
    
    # Prediction formula
    predicted_score = coef_x1 * x1 + coef_x2 * x2 + intercept
    
    return predicted_score
score = score_predictor(3.5, 7.2)
print(f"The predicted score is: {score}")
