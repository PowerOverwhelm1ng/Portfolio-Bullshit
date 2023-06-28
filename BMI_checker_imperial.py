weight_in_lbs = float(input("Enter your weight in pounds: "))
height_in_feet = float(input("Enter your height in feet: "))
height_in_inches = float(input("Enter the remaining inches in your height: "))

#convert the total

height_in_total_inches = height_in_feet * 12 + height_in_inches

#Calculate BMI

BMI = (weight_in_lbs /(height_in_total_inches ** 2)) * 703
print("Your BMI is: ", BMI)
if(BMI>0):
    if (BMI <= 16):
        print("You are dangerously underweight")
    elif (BMI <= 18.5):
        print("You are under target wight")
    elif(BMI <= 25):
        print("You are at target weight/body mass")
    elif(BMI <= 30):
        print("You are overweight")
    else:
        print("You are morbidbly obese")
else:("Please enter valid details!")