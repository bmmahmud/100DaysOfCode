## Sololarn Course- Python Data Structure 
## Assignment - Balanced Parentheses
## https://www.sololearn.com/learning/eom-project/1159/1114

def balanced(expression):
    #your code goes here
    bracket_stack = []
    for char in expression:
        if char == "(":
            bracket_stack.insert(0, char)
        elif char == ")":
            try:
                bracket_stack.pop(0)
            except IndexError:
                return False
    
    return bracket_stack == []


print(balanced(input()))