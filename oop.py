class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_to_file(self):
        filename = f"{self.username}_profile.txt"
        with open(filename, 'w') as file:
            file.write(f"Username: {self.username}\n")
            file.write(f"Email: {self.email}\n")
        print(f"Profile saved to {filename}")

  
    def read_from_file(self):
        filename = f"{self.username}_profile.txt"
        
        try:
           
            with open(filename, 'r') as file:
                content = file.read()
                print(f"\n--- Loading {filename} ---")
                print(content)
                
        except FileNotFoundError:
            print(f"\nError: The file {filename} does not exist yet!")


user1 = User("alex_dev", "alex@example.com")
user2 = User("irfan", "irfan@gmail.com")

user1.save_to_file()
user2.save_to_file()

user2.read_from_file()
user1.read_from_file()