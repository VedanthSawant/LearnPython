class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Vedanth")
user_2 = User("002", "Ambuja")

user_1.follow(user_2)

print(f"User 1 followers: {user_1.followers}")
print(f"User 1 following: {user_1.following}")
print(f"User 2 followers: {user_2.followers}")
print(f"User 2 following: {user_2.following}")


# Here we have first created a class called User. It has init method, which is predefined method used for initiazing
# anything. We have created two object of this class they are user_1 and user_2. When objected are created, init method
# of the class is automatically called and what's inside init method gets executed.