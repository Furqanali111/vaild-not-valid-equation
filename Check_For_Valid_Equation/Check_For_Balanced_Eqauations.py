#!/usr/bin/env python
# coding: utf-8

# In[24]:



from collections import deque


# start of class/stack
class Stack:
    # constructor
    def __init__(self):
        self.equation = deque()

    # push function use to push a value in equation deque
    def push(self, value):
        self.equation.append(value)

    # pop function use to get the value that is on top of the deque
    def pop(self):
        return self.equation.pop()

    # empty function use to know if the stack is empty or not
    def is_empty(self):
        if len(self.equation) == 0:
            return True
        else:
            return False

    # size function use to get the cureent size of the stack
    def size(self):
        return len(self.equation)

    # top fuction is used to get the value that is on top without removing it
    def top(self):
        if self.is_empty():
            return False
        else:
            return self.equation[-1]


# creating a try block which will help us if we get any index error
try:
    # creating a variable that will be used to get the functions from the stack class
    stack = Stack()
    # taking an input from the user
    equation = str(input("Enter Equation: "))
    # creating a variable that will keep a check on if the euqation is true or not
    isequation = True
    # variable to keep check on Qutation mark("")
    count = 0
    # runing our first loop that will check if the brackets are balanced or not
    for i in equation:
        if i == '(' or i == '{' or i == '[':
            # if the above condition is true we will push a value in stack
            stack.push(i)
        elif stack.top() == '(' and i == ')':
            # if the above condition is true we willl pop a value from stack
            stack.pop()
        elif stack.top() == '{' and i == '}':
            stack.pop()
        elif stack.top() == '[' and i == ']':
            stack.pop()

    if stack.size() == 0:
        # runing our 2nd loop that will check different conditions related to Quotion marks
        for i in range(0, len(equation)):
            # if opening quotation mark and ending qutation mark are present together then eqauation is not balanced
            if equation[i] == '"' and equation[i + 1] != '"':
                # checking if the quotation mark runing in the cureent loop is in even or odd number
                if count % 2 == 0:
                    count += 1
                    # if quotation mark is in odd number and their is an closing bracket next to it then it will be an unbalanced equation
                    if equation[i + 1] == ')' or equation[i + 1] == '}' or equation[i + 1] == ']' or equation[
                        i + 1] == '"':
                        isequation = False
                    else:
                        isequation = True
                # if the quotation mark is in even number then clossing brakets are allowed
                elif count % 2 != 0:
                    isequation = True
                    count += 1
            else:
                isequation = False
        # checking if the quotation marks are in even or odd number because odd number quotation mark represent an unbalanced equation
        if count % 2 == 0:
            isequation = True
        else:
            isequation = False
        # printing the output
    else:
        isequation = False
    if isequation:
        print("The Eqauation is valid")
    else:
        print("The Eqauation is not a valid")
except (IndexError):
    print("The Eqauation is not a valid")

# In[ ]:


# In[ ]:
