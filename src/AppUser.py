class AppUser:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        # self.topics = []

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getUserRole(self):
        return self.role

    def setUserRole(self, role):
        self.role = role

    # def addTopic(self, topic):
    #     if topic not in self.topics:
    #         self.topics.append(topic)
    #         return "Topic added successfully"
    #
    #     else:
    #         return "Topic already subscribed"
    #
    # def removeTopic(self, topic):
    #     if topic in self.topics:
    #         self.topics.pop(topic)
    #         return "Topic removed successfully"
    #     else:
    #         return "Topic not subscribed"

