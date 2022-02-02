from admin import Admin

new_user = Admin('ashik','mahmud',26,'bmmahmud@gmail.com','Mirpur')
print(new_user.describe_user())
user_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
new_user.privileges.privileges= user_privileges
print(new_user.privileges.show_privileges())