#Christopher Pellegrino
#CS 521 02, Final Project, main

from user_class import User

try:
    from diagnoses_data import *
except ImportError:
    raise ImportError("Could not find module")

def main(): #main function
    
    #Greeting
    print("Welcome to MediPhysical, the at-home physical you can do by yourself!")
    
#User registration
    #create user object
    user = User()
    #set username
    user.set_username(input("Enter a username: "))
    while True:
        if user.get_username() == "":
            print("Your username must have at least 1 character")
            user.set_username(input("Enter a username: "))
        else:
            break
    assert user.get_username() != "Chris" #reserved name for me
    #set age
    user.set_age(input("Enter your age in years (integers only): "))
    while True:
        age = user.get_age()
        if not age.isdigit():
            print("Age must be an integer")
            user.set_age(input("Enter your age in years (integers only): "))
        else:
            break
    #set current weight
    user.set_current_weight(input("Please enter a positive integer for your current weight (measured in pounds): "))
    while True:
        current_weight = user.get_current_weight()
        if not current_weight.isdigit():
            print("Current weight must be an integer")
            user.set_current_weight(input("Please enter a positive integer for your current weight (measured in pounds): "))
        else:
            break
    user.set_height(input("Please enter your height in inches (integers only): "))
    #set height
    while True:
        height = user.get_height()
        if not height.isdigit():
            print("Height must be an integer")
            user.set_height(input("Please enter your height in inches (integers only): "))
        else:
            break
    #set sex
    user.set_sex(input("Please enter your sex ('male' or 'female' only): "))
    while True:
        sex = user.get_sex()
        if sex not in ('male', 'female'):
            print("Sex must be either 'male' or 'female', please enter again.")
            user.set_sex(input("Please enter your sex ('male' or 'female' only): "))
        else:
            break
    #User's Profile
    print("User's MediPhysical Profile")
    print("Username:", user.get_username())
    print("Age:", user.get_age(), "years")
    print("Current weight:", user.get_current_weight(), "pounds")
    bmi = user.get_body_mass_index()
    print("Height:", user.get_height(), "inches")
    print("Your body mass index is:", round(bmi, 2))
    print("According to your BMI, you are:", user.weight_status_category(bmi))
    #conditional statements
    if user.get_body_mass_index() > 24.9:
        print("You need to lose some weight to acheive a healthy BMI of 18.5 to 24.9")
        #set goal weight
        user.set_goal_weight(int(input("Enter goal weight as a positive integer: ")))
        print("Goal weight:", user.get_goal_weight(), "pounds")
        print("Your goal is to lose:", round(user.get_current_goal_difference(), 2), "pounds")
        new_bmi = round((float(user.get_goal_weight()) / float(user.get_height())**2) * 703, 2)
        print("Your new BMI will be:", new_bmi)
        print("According to your projected BMI, you will be:", user.weight_status_category(new_bmi))
    if round((float(user.get_goal_weight()) / float(user.get_height())**2) * 703, 2) > 24.9:
        print("BMI still in unhealthy range. You need to lose more weight")
        user.set_goal_weight(input("Please enter a positive integer for your goal weight (measured in pounds): "))
        print("Your new BMI will be:", round((float(user.get_goal_weight()) / float(user.get_height())**2) * 703, 2))
        print("According to your projected BMI, you will be:", user.weight_status_category(round((float(user.get_goal_weight()) / float(user.get_height())**2) * 703, 2)))
    assert float(user.get_goal_weight()) > 0.0
    print("Your current BMI has the following risks/diagnoses:")
    user.diagnoses()
    #repr
    rep = user.__repr__()
    print(rep)
    print("Your physical is over, don't forget to make an appointment with your real doctor at least once a year!")

main() #Call main function