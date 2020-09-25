def bot_response():
    name = input('Hello, this is OG bot, what is your name? \n')
    welcome_message = 'Welcome {name}, have a great time'
    return name

def user_response():
    your_name = bot_response()
    response = 'My name is {0}'.format(your_name)
    return response

user_response()

