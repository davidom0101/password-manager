import json

# Function to add a password entry for a given service
def add_password(service, username, password, data_file='passwords.json'):
    try:
        # Try to load existing passwords from the file
        with open(data_file, 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        # If file does not exist, start with an empty dictionary
        passwords = {}

    # Add or update the password entry for the service
    passwords[service] = {"username": username, "password": password}

    # Save the updated password data back to the file
    with open(data_file, 'w') as file:
        json.dump(passwords, file, indent=4)

    print(f"Password for {service} added successfully!")

# Function to retrieve and display password for a given service
def get_password(service, data_file='passwords.json'):
    try:
        # Load the passwords from the file
        with open(data_file, 'r') as file:
            passwords = json.load(file)

        # Check if the service exists in the stored data
        if service in passwords:
            print(f"\nService: {service}")
            print(f"Username: {passwords[service]['username']}")
            print(f"Password: {passwords[service]['password']}\n")
        else:
            print(f"No entry found for {service}.")
    except FileNotFoundError:
        # If the file does not exist, prompt the user to add passwords first
        print("No password data found. Please add passwords first.")

# Function to display the menu options
def menu():
    print("Password Manager")
    print("1. Add a new password")
    print("2. Retrieve a password")
    print("3. Exit")

# Main loop for handling user interaction
def main():
    while True:
        menu()  # Show the menu options
        choice = input("Enter your choice: ")  # Take user input for menu choice

        if choice == "1":
            # Add a new password
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(service, username, password)  # Call add_password function
        elif choice == "2":
            # Retrieve an existing password
            service = input("Enter the service name to retrieve: ")
            get_password(service)  # Call get_password function
        elif choice == "3":
            # Exit the program
            print("Exiting...")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please select a valid option.")

# Run the main program
if __name__ == "__main__":
    main()
