class Topic:
    def __init__(self, user, name):
        self.created_by = user
        self.name = name


    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    # def addUsers(self, user):
    #     if user not in self.users:
    #         self.users.append(user)
    #         return 'User added successfully'
    #
    #     else:
    #         return 'User already Exists'
    #
    # def removeUsers(self, user):
    #     if user in self.users:
    #         self.users.pop(user)
    #         return "User removed Successfully"
    #     else:
    #         return "User Does not Exists"




