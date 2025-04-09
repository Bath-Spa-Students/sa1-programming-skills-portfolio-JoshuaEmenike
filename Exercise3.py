def biography():
    name = input("Enter your full name: ")
    hometown = input("Enter your hometown: ")
    age = input("Enter your age: ")  # No while loop, just take the input as is

    bio = {"Name": name, "Hometown": hometown, "Age": age}
    print(f"\nName: {bio['Name']}\nHometown: {bio['Hometown']}\nAge: {bio['Age']}")

biography()
