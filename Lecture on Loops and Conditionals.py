import random
a = 30
b = int(input("How many people will show up?"))
# always put in "int" or it won't run correctly
c = random.randint(1,16)

food = ["Turkey","Apple Pie","Potatoes", "Mac and Cheese"]

total = a+b+c

print("Welcome to the Thanksgiving program!")

answer = "n"

while answer != "y":
    for item in food:
        print("We need" + str(total) + " " + item)
    answer = input("Do you want to keep going? Type y to exit.")

# ctrl C will end an infinite loop
