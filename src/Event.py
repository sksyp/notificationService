from src.AppUser import AppUser
from src.Topic import Topic


class Event:
    def __init__(self):
        self.users = []
        self.topics = []

    def addUser(self, user, role):
        flag = False
        for i in self.users:
            if user == i.name:
                flag = True
                break
        if not flag:
            self.users.append(AppUser(user, role))
            return "User added successfully"
        return "User already exists"

    def removeUser(self, user):
        for i in self.users:
            if user.name == i.name:
                self.users.pop(user)
                return "User removed successfully"
        return "User does not exists"

    def addTopics(self, topic, userName):
        flag = False
        for i in self.topics:
            if topic == i.name:
                flag = True
                break
        role = self.getRole(userName)
        print(role)
        if not flag and role == 'admin':
            self.topics.append(Topic(topic, userName))
            return "Topic added successfully"

        if role != 'admin':
            return "You don't have admin access"

        return "Topic already exists"

    def removeTopic(self, topic, userName):
        role = self.getRole(userName)
        if role == 'admin':
            for i in self.topics:
                if topic.name == i.name:
                    self.topics.pop(topic)
                    return "Topic removed successfully"
        else:
            return "You are not an admin"
        return "Topic does not exists"

    def getRole(self, userName):
        for i in self.users:
            if i.name == userName:
                return i.role
