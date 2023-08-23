**BMI Calculator and Health Advice**

This Python script calculates the Body Mass Index (BMI) based on user-input weight and height, and provides an interpretation of the BMI along with corresponding health advice. BMI is a numerical value that indicates a person's body weight relative to their height, commonly used as an indicator of overall health and nutritional status.

**How to Use:**

1. Make sure you have Python installed on your system.
2. Copy and paste the provided code into a new Python script file (e.g., `bmi_calculator.py`).
3. Save the file.
4. Open a terminal or command prompt and navigate to the directory containing the script.
5. Run the script by entering: `python bmi_calculator.py`.

**Script Explanation:**

1. The `calculate_bmi()` function takes `weight` (in kilograms) and `height` (in meters) as input and calculates the BMI by dividing weight by the square of height.
2. The `interpret_bmi()` function takes a calculated BMI value as input and returns an interpretation based on different BMI ranges, categorizing the interpretation into "Niedowaga" (Underweight), "Normalna waga" (Normal Weight), "Nadwaga" (Overweight), or "Otyłość" (Obesity).
3. The `get_bmi_advice()` function provides health advice based on the calculated BMI value, giving tailored recommendations for each BMI range.
4. In the `main()` function:
   - The user is prompted to enter their weight and height using `input()`.
   - The entered values are converted to floating-point numbers.
   - BMI is calculated using the `calculate_bmi()` function, and interpretation and advice are obtained using the respective functions.
   - The calculated BMI, interpretation, and advice are displayed to the user.

**Note:**

This script is a simple BMI calculator and provides general health advice based on BMI ranges. It's important to note that BMI is just one indicator of health and doesn't account for factors like muscle mass, bone density, and other individual differences. For accurate health assessment, it's recommended to consult a healthcare professional.

The provided script is suitable for educational purposes and raising awareness about BMI-related health considerations. For practical use or more comprehensive health assessment, additional factors and medical guidance should be considered.

Feel free to modify and improve the script to meet your specific needs or integrate it into a larger health-related application.
