# if statement

# voting machine

name = input("Enter voter name: ")
age = int(input("Enter voter's age: "))

# if age < 18:
#     print(name, " you are not elligible to vote, you are below 18 years")
# else:
#     print(name, " go and vote")



print("*"*20)

# age 18 or above and you have voter id card
voter_id = input("Voter id availability? Y or N: ")

if age < 18 and voter_id == "N": 
    print(name, " you are not elligible to vote, you are below 18 years and you don't have voter's id")

elif age < 18 and voter_id == "Y": 
    print(name, " you are not elligible to vote, you are below 18 years and you have voter's id")

elif age >= 18 and voter_id == "N" :
      print(name, " you are not elligible to vote, you are above 18 years and you don't have voter's id")

else:
    print(name, " go and vote")