#!/usr/bin/env python
# Peri
# 2021.11.19
# Lab Exercise 6
# HealthCalculator.py
# Using Mu.1.1.0.beta.6
# Takes user input and displays BMI and Target Training Zone

# Get user stats
print("Please enter the follow values for the user...")

# Check if height input is valid
while True:
    try:
        in_height = float(input("Height in inches: "))
        if in_height <= 21.5:
            print("Are you Chandra Bahadur Dangi?")
            continue
        elif in_height >= 98.8:
            print("Are you Sultan Kösen?")
            continue
        else:
            break
    except ValueError:
        print("Enter a number!")
        continue

# Check if weight input is valid
while True:
    try:
        lbs_weight = float(input("Weight in pounds: "))
        break
    except ValueError:
        print("Enter a number!")
        continue

# Check if age input is valid
while True:
    try:
        age = int(input("Current age: "))
        if age <= 0:
            print("No newborns!")
            continue
        elif age >= 118:
            print("Are you Kane Tanaka?")
            continue
        else:
            break
    except ValueError:
        print("Enter a number!")
        continue

# Check if resting heart rate input is valid
while True:
    try:
        resting_hr = int(input("Resting heart rate: "))
        if resting_hr < 40:
            print("You're dying ☻")
            print("No, you don't get to input something else.")
            print("Because I do believe that you're dying ♡")
            break
        elif resting_hr > 100:
            print("You're dying ☻")
            print("No, you don't get to input something else.")
            print("Because I do believe that you're dying ♡")
            break
        else:
            break
    except ValueError:
        print("Enter a number!")
        continue

# Define BMI function
def calc_bmi():
    # Convert pounds to kilos
    kgs_weight = lbs_weight * 0.45359237
    # Convert inches to meters
    m_height = in_height * 0.0254
    # Calculate BMI
    bmi = kgs_weight / m_height**2
    # Display results
    ## BMI must be considered against other facts, so I'm saying allegedly ( ͡° ͜ʖ ͡°)
    print("Results...")
    if bmi < 18.5:
        print("Your BMI is:", "{:.2f}".format(bmi), "--Underweight, allegedly")
    elif bmi >= 30:
        print("Your BMI is:", "{:.2f}".format(bmi), "--Obese, allegedly")
    elif 24.9 <= bmi >= 18.5:
        print("Your BMI is:", "{:.2f}".format(bmi), "--Normal, allegedly")
    elif 29.9 <= bmi >= 25:
        print("Your BMI is:", "{:.2f}".format(bmi), "--Overweight, allegedly")

# Define Target Training Zone function
def calc_ttz():
    # Set intensity starting point
    intensity = .50
    # Display headers
    print("Exercise Intensity Heart Rates")
    print("Intensity\tTarget Training Zone")
    print(" " * 10)
    while True:
        if 1 >= intensity >= .5:
            # Calculate Target Training Zone
            max_hr = 220 - age
            hr_reserve = max_hr - resting_hr
            max_tz = hr_reserve * intensity
            target_tz = max_tz + resting_hr
            # Display results
            print('{:.2f}'.format(intensity), int(target_tz), sep='\t'*3)
            intensity = intensity + .05
            continue
        else:
            break

# Define functions to be called
def main():
    calc_bmi()
    calc_ttz()

# Call functions
if __name__ == "__main__":
    main()