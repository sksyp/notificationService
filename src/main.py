from src.AppUser import AppUser
from src.Event import Event


def main():
    e = Event()
    while True:
        print("Please select events from below options")
        print("addUser userName role")
        print("addTopic userName topicName")
        print("removeTopic userName topicName")
        print("viewTopics userName")
        print("subscribeTopic userName topicName")
        print("postEvent messageBody", end='\n')
        option = input().split()
        if len(option):
            if option[0].lower() == 'adduser':
                print(e.addUser(option[1], option[2]))

            elif option[0].lower() == 'addtopic':
                print(e.addTopics(option[1], option[2]))

            elif option[0].lower() == 'removetopics':
                print(e.removeTopic(option[1], option[2]))


if __name__ == '__main__':
    main()
