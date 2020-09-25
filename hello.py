import time

def respond(message):
    time.sleep(0.5)
    return "I can hear you, you said: {0}".format(message)


def send_message():
    message = input("")
    return respond(message)


print(send_message())