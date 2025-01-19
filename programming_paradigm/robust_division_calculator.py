def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling errors like division by zero
    and non-numeric inputs.
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."

        # Perform division
        result = num / denom
        return f"The result of the division is {result:.2f}"

    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."