# MediPhysical
Project in Python

Student: Chris Pellegrino
Instructions: I did not use any third party modules. You should be able to run the main.py file. To see all the features, you need to input features of an overweight person or an underweight person (height, weight), in addition to a normal weight person. There are different outcomes for all of them.
Example to see overweight youth (<21):
Username: x
Age: 19
Current Weight: 200
Height (inches): 70
Sex: male
It will show the user is overweight and ask for a healthy goal weight. If itís too low, it will let you know and reprompt you. 
Goal weight: 199
After it reprompts you:
Goal weight: 150

Criteria and locations:
container type: multiple lists in diagnoses_data.py
iteration type: while loops in main.py
conditional statements: in main.py
try block: in main.py at top
user-defined functions in user_class.py and main.py
input in main.py
output in user_class.py and main.py
user defined class: in user_class.py, imported into main.py at the top
1 private self attribute: username
2 public self attributes: sex, height
1 private method that takes arguments, returns values, and used: set_goal_weight(self, goal_weight)
1 public method that takes arguments, returns values, and used: weight_status_category(self, bmi) in user_class.py
init() method that takes at least 1 argument: def __init__(self, username = str(), age = int(), current_weight = int(), goal_weight = int(), height = int(), sex = str()): in user_class.py
repr() method: function in user_class.py at bottom, defined and called in main.py
unit test(s) using assert statement: assert float(user.get_goal_weight()) > 0.0 in main.py. Also one for username if you use "Chris". 

