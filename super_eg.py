class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class UserData(User):
    def __init__(self, name, age, email, profile, bio):
        super().__init__(name, age)
        self.email = email
        self.profile = profile
        self.bio = bio

obj = UserData("Suriya", 27, "suriyag1198@gmail.com", "suriyag1198_profile", "Hello, I'm Suriya!")

obj.name

print(obj.age)



