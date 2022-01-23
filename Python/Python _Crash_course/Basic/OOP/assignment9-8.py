### Assignment Chapter 9 - Instances
## 9-8
class User():
    """"Class for user information"""
    def __init__(self,first_name,last_name,age,email,location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = last_name
        self.location = location.title()
        self.email = email
        self.age = 0
        self.login_attemts = 0
    def describe_user(self):
        print(f"\
        First Name: {self.first_name}\n\
        Last Name: {self.last_name}\n\
        Age: {self.age}\n\
        username: {self.username}\n\
        Email: {self.email}\n\
        Location: {self.location}")
    def greet_user(self):
        print(f"Welcome {self.first_name} !!!")
    def login_attempts(self):
        self.login_attemts +=  1
    def reset_login_attempts(self):
        self.login_attemts = 0           

class Admin(User):
    """"A user with administrative privileges."""

    def  __init__(self, first_name, last_name, age, email, location):
        """"Initialize the admin."""
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()

class Privileges():
    """"A class to share an admin's privilages."""
    def __init__(self,privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """"Display the privileges this administrator has."""
        print("\nPrivileges:")
        if self.privileges:
            for pivilege in self.privileges:
                print(f" - {pivilege}")
        else:
            print('- This user has no privileges.')                      


# users = ['ashik','abir','lamia']
profile =  User('ashik','mahmud',25,'bmmahmud@gmail.com','Mirpur')
bm =  Admin('ashik','mahmud',25,'bmmahmud@gmail.com','Mirpur')
profile.describe_user()
profile.greet_user() 
# Priviledge
bm.privileges.show_privileges()

print("\nAdding privileges...")
bm_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
bm.privileges.privileges = bm_privileges 
print("After adding privilage") 
bm.privileges.show_privileges()
# login attempts
profile.login_attempts()
profile.login_attempts()
profile.login_attempts()
#
print(f"Login attemp : {profile.login_attemts}") 
profile.reset_login_attempts() 
print(f"After Reset, Login attemp : {profile.login_attemts}") 