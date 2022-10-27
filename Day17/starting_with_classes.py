class User:
    def __init__(self, user_id, name):  # self refer to the obj being created,
        # the constructor runs everytime an obj is created
        self.id = user_id  # initializing attribute for all objects
        self.name = name
        self.followers = 0
        self.following = 0
        print("A new fxn has been created...")

    def follow(self, obj_of_user_to_be_followed):
        obj_of_user_to_be_followed.followers += 1
        self.following += 1  # self == object that called the method(fxn attached to obj)


user_1 = User(1,"Victor")
user_2 = User(2, "Micah")
print(user_2.name)
user_1.follow(user_2)

print(user_1.followers) #0
print(user_1.following) #1

print(user_2.followers) #1
print(user_2.following) #0
