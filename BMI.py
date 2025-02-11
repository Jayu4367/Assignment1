# bmi_calculator.py
def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI given weight in kg and height in meters
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers")
    return weight_kg / (height_m ** 2)

def get_bmi_category(bmi):
    """
    Return BMI category based on the calculated BMI
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        print(f"Your BMI is: {bmi:.1f}")
        print(f"Category: {category}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

# test_bmi_calculator.py
import pytest
from bmi_calculator import calculate_bmi, get_bmi_category

def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == pytest.approx(22.86)
    
def test_invalid_inputs():
    with pytest.raises(ValueError):
        calculate_bmi(-70, 1.75)
    with pytest.raises(ValueError):
        calculate_bmi(70, -1.75)

def test_bmi_categories():
    assert get_bmi_category(17) == "Underweight"
    assert get_bmi_category(22) == "Normal weight"
    assert get_bmi_category(27) == "Overweight"
    assert get_bmi_category(32) == "Obese"

