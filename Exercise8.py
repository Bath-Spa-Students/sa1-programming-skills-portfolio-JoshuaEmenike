# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Search for "Sam"
search_term = "Sam"
if search_term in names:
    print(f"{search_term} found in the list.")
else:
    print(f"{search_term} not found in the list.")

# Optional: Allow user input
user_input = input("Enter a name to search: ")
if user_input in names:
    print(f"{user_input} found in the list.")
else:
    print(f"{user_input} not found in the list.")
