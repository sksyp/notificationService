class Message:
    def __init__(self, id, topicName, text):
        self.id = id
        self.topicName = topicName
        self.text = text

    def getId(self):
        return self.id

    def getTopicName(self):
        return self.topicName

    def getText(self):
        return self.text

    def setId(self, id):
        self.id = id

    def setTopicName(self, name):
        self.topicName = name

    def setText(self, text):
        self.text = text
