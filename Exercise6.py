# Define the correct password
correct_password = "12345"

# Set the maximum number of attempts
max_attempts = 5

# Start the loop and initialize the attempt counter
attempts = 0

# Start a loop to keep asking for the password until it's correct or attempts are exhausted
while attempts < max_attempts:
    # Ask the user for the password
    entered_password = input("Enter the password: ")
    
    # Check if the entered password is correct
    if entered_password == correct_password:
        print("Password correct! Access granted.")
        break  # Exit the loop when the correct password is entered
    else:
        attempts += 1  # Increment the attempts counter
        print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")
        
# If the loop ends without success (i.e., 5 attempts exhausted)
if attempts == max_attempts:
    print("Maximum attempts reached. Authorities have been alerted.")
