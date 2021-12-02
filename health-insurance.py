import time

#Constants
INTRO = '''
 Health Insurance Calculator

 Follow the instructions throughout the program and answer all the questions honestly in order to determine how much of an insurance risk you currently are.

 Enjoy!
'''

BLOODCHART = '''
    Bloodpressure instructions: Enter the number (1-5) that correlates to your current bloodpressure situation from the graphic below.

                                                Systolic mm HG          Diastolic mm HG
            -Bloodpressure Category-            (Upper Number)          (Lower Number)

        Enter 1 for normal bloodpressure        Less than 120    and      Less than 80

        Enter 2 for elevated bloodpressure      120 - 129        and      Less than 80

        Enter 3 for stage 1 hypertension        130 - 139        or       80-89

        Enter 4 for stage 2 hypertension        140 or Higher    or       90 or Higher

        Enter 5 for hypertensive crisis         180 or Higher    or       120 or Higher
        '''

HEIGHT = '''
 ~Height Instructiosn~
 For this section you will be asked 2 questions. The first of which will ask for how many feet tall you are and then the following question will ask how many inches remain.
 For example, if you ar 5'11", you would enter 5 for the first question and 11 for the second.
    '''

# Input Variables
a = "Please enter you age: "
b = "Please enter your weight in LBs: "
c = "Please enter how many feet tall you are:  "
c1 = "Now enter inches: "
d = "Please enter your blood pressure condition: "
e = "Do you have a family history of diabetes? "
f = "Do you have a family history of alzheimers? "
g = "Do you have a family history of cancer? "

# Countdown Function
def countdown (t):
  while t > 0:
    print(t)
    t -= 1
    time.sleep(1)
    print("Calculating...")

print (INTRO)

#Insurance Calulator Loop
while True:
    try:
        # Age Input and Print
        while True:
            try:
                age = int(input(a))
                if age >= 0 and age < 30:
                    agePoints = 0
                    break;
                elif age >= 30 and age < 45:
                    agePoints = 10
                    break;
                elif age >= 45 and age < 60:
                    agePoints = 20
                    break;
                elif age >= 60 and age <=120:
                    agePoints = 30
                    break;
                else:
                    print("")
                    print("Please enter a numer 0-120")
                    print("")
                    continue
            except ValueError:
                print("")
                print("Please enter a number 0-120")
                print("")
            continue
        print("")
        time.sleep(1)
        print("Your age risk factor is " + str(agePoints))
        print("")
        time.sleep(1)

        # Body Weight Input
        while True:
            try:
                bodyWeight = float(input(b))
                if bodyWeight > 0 and bodyWeight <= 700:
                    break;
                else:
                    print("")
                    print("Please enter your actual weight")
                    print("")
                    continue
            except ValueError:
                print("")
                print("Please enter your actual weight in numbers")
                print("")
            continue
        time.sleep(1)

        # Height Instructions
        print(HEIGHT)
        print("")
        time.sleep(1)

        # Feet Input
        while True:
            try:
                heightfeet = float(input(c))
                if heightfeet >=1 and heightfeet <=8:
                    break;
                else:
                    print("")
                    print("Please enter your actual height")
                    print("")
                    continue
            except ValueError:
                print("")
                print("Please enter your actual height in numbers.")
                print("")
            continue 
        print("")
        time.sleep(1)

        # Inches Input
        while True:
            try:
                heightinches = float(input(c1))
                if heightinches >= 0 and heightinches < 12:
                    break;
                else:
                    print("")
                    print("Please enter your actual height")
                    print("")
                    continue
            except ValueError:
                print("")
                print("Please enter your actual height in numbers.")
                print("")
            continue 
        print("")
        time.sleep(1)

        # BMI Calculation
        weightKG = (bodyWeight /  2.2046)
        heightInchesConversion = heightfeet * 12
        height = heightinches+ heightInchesConversion
        heightMeters = (height * 0.0254)
        BMI = float(weightKG/ (heightMeters**2))
        BMI = round(BMI, 3)

        # BMI Print Statement
        if BMI <18.5: 
            BMIPoints = 30
        elif BMI >= 18.5 and BMI <= 24.9:
            BMIPoints = 0
        elif BMI > 24.9 and BMI <= 29.9:
            BMIPoints = 30
        elif BMI > 29.9:
            BMIPoints = 75
        print("")
        print("Your BMI is " + str(BMI) + ". Giving you a BMI risk factor of " + str(BMIPoints))
        print("")
        time.sleep(2)

        #Blood Pressure Instructions
        print(BLOODCHART)
        

        # Bloodpressure Input and Print
        while True:
            try:
                bloodpressure = int(input(d))
                if bloodpressure == 1:
                    bloodpressurepoints = 0
                    break;
                elif bloodpressure == 2:
                    bloodpressurepoints = 15
                    break;
                elif bloodpressure == 3:
                    bloodpressurepoints = 30
                    break;
                elif bloodpressure == 4:
                    bloodpressurepoints = 75
                    break;
                elif bloodpressure == 5:
                    bloodpressurepoints = 100
                    break;
                else:
                    print("")
                    print("Please enter a number 1-5 that corresponds to your currnet bloodpressure condition" )
                    print("")
                    continue
            except ValueError:
                print("")
                print("Please enter a number 1-5 that corresponds to your currnet bloodpressure condition" )
                print("")
            continue
        print("")
        time.sleep(1)
        print("Your bloodpressure risk factor is " + str(bloodpressurepoints))
        print("")
        time.sleep(1)

        # Hereditary Instructions
        print("For the following questions, input 1 for no, and 2 for yes.")
        print("")
        time.sleep(1)

        # Diabetes Input
        while True:
            try:
                diabetes = int(input(e))
                if diabetes == 1:
                    diabetespoints = 0
                    break;
                elif diabetes == 2:
                    diabetespoints = 10
                    break;
                else:
                    print("")
                    print("Please enter 1 for yes, 2 for no")
                    print("")
                    continue
            except ValueError:
                print("")
                print("Please enter 1 for yes, 2 for no")
                print("")
            continue
        print("")
        time.sleep(1)

        # Altheimerz Input
        while True:
            try:
                altheimerz = int(input(f))
                if altheimerz == 1:
                    altheimerzpoints = 0
                    break;
                elif altheimerz == 2:
                    altheimerzpoints = 10
                    break;
                else:
                    print("")
                    print("Please enter 1 for yes, 2 for no")
                    print("")
                    continue
            except ValueError:
                print("")
                print("Please enter 1 for yes, 2 for no")
                print("")
            continue
        print("")
        time.sleep(1)

        # Cancer Input
        while True:
            try:
                cancer = int(input(g))
                if cancer == 1:
                    cancerPoints = 0
                    break;
                elif cancer == 2:
                    cancerPoints = 10
                    break;
                else:
                    print("")
                    print("Please enter 1 for yes, 2 for no")
                    print("")
                    continue
            except ValueError:
                print("")
                print("Please enter 1 for yes, 2 for no")
                print("")
            continue
        print("")
        time.sleep(1)

        # Hereditary Calculations and Print Statement
        hereditarytotal= (cancerPoints + altheimerzpoints + diabetespoints)
        print("Your hereditary risk factor is " + str(hereditarytotal))
        print("")
        time.sleep(1)

        # Final Calculation and Print Statement
        print("")
        print("Calculating Insurance Risk.")
        countdown(3)
        print("")
        print("Calculated!")
        print("")
        totalPoints = (agePoints + BMIPoints + cancerPoints + bloodpressurepoints + altheimerzpoints + diabetespoints)
        if totalPoints <= 20:
            print("Your total risk factor is " + str(totalPoints) + ". This makes you a low risk for insurance")
        elif totalPoints <= 50:
            print("Your total risk factor is " + str(totalPoints) + ". This makes you a moderate risk for insurance")
        elif totalPoints <= 75:
            print("Your total risk factor is " + str(totalPoints) + ". This makes you a high risk for insurance ")
        else:
            print("Your total risk factor is " + str(totalPoints) + ". This makes you uninsurable ")
        
        # Ending Print Statement
        print("")
        print("You can exit the program by pressing control + c or you may continue on and calculate the insurance risk for another individual")
        print("")
    except KeyboardInterrupt:
        break
