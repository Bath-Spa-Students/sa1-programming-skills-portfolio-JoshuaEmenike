
#creating a biography
def biography():
    name = input("Enter your full name: ")# asking for input from user
    hometown = input("Enter your hometown: ")#asking the user to type his hometown
    age = input("Enter your age: ")  # No while loop, just take the input as is

    bio = {"Name": name, "Hometown": hometown, "Age": age}
    print(f"\nName: {bio['Name']}\nHometown: {bio['Hometown']}\nAge: {bio['Age']}")

biography()
