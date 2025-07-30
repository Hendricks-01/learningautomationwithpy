# this program says hello and asks for my name
print('Hello World!')
print('What is your name?')  # ask for their name
myName = input()  # input function waits for user input
print('It is good to meet you, ' + myName)
print('The length of your name is:' + str(len(myName)))  # prints the length of the name
print('What is your age?')  # ask for their age
myAge = input()  # input function waits for user input
print('You will be ' + str(int(myAge) + 1) + ' in a year.')  # tells the user their age next year