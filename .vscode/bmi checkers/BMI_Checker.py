Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your weight in Kg: "))
Height = Height/100
BMI = Weight/(Height * Height)
print("Your Body Mass Index is: ", BMI)
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