class User:

    def __init__(self,id,username):
        print("User is being created....")
        self.id= id
        self.username=username
        self.followers = 0
        self.following =0

    def follow(self,user):
        user.followers+=1
        self.following+=1

#creating user
user1 = User("1","Angela")
user2 = User("2", "Jack")
print(user1.id + " " + user1.username)
user2.follow(user1)

print(f"{user2.username} is following {user2.following}")