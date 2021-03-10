# This is a comment
# This is a print method. Print will echo out anything within the round brackets to terminal when we run the file. 

print("This is my very fist python script.")

# name= variable, kenny= data
# variables are placeholders with dynamic values --> things that can change
# they get stored in memory and referenced later
name = "Kenny"
age = 26
hairColour = "pink"
eyeColour = "blue"

#A better way to do this..
#plant1 = "pothos"
#plant2 = "snake"
#plant3 = "spider"
#..Is to do this:

cars = ["pothos", "snake", "spider"]
# ^ arrays are variables on steroids. they allow us to store multiple values in one variable -->to help us group data
# this makes our scripting files easier to understand

print ("My name is " + name)


# input waits for a response (type something and hit enter)
name = input("What is YOUR name?")
print("My name is now " + name)

print("My age is " + str(age))

# you can create new variables instead of using pre existing ones i.e, instead of name, alternateName