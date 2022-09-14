'''You're writing code to control your town's traffic lights.
You need a function to handle each change from green, to yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing the current state of the light
  and returns a string representing the state the light should change to.

For example, when the input is green, output should be yellow.



Test Case 1
Input
Green
Output
Yellow



Test Case 2
Input
Red
Output
Green'''

def trafic_update(current):
    if current=="Red":
        return "Green"
    elif current=="Green":
        return "Yellow"
    else:
        return "Red"

current=input("Enter the cuuent light")
print(trafic_update(current))

#Output:
    
##Enter the cuuent lightGreen
##Yellow
##
##Enter the cuuent lightYello
##Red














    
