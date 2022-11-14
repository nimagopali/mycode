greeting = {
        0: "Hello",
        1: "Good"}
for i in range(len(greeting)):
    print(greeting[i], end= " ")

print(len(greeting))
age = int(input("How old are you?"))

if age>=30:
    print(" You are in your thirties.")
elif age >= 40:
    print("You are older than forty.")
else:
    print("Youngster")

