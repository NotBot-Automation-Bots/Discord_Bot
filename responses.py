import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hi' or p_message == 'hello' or p_message == 'hey':
        return p_message.capitalize() + '!  😊. \n \n \n What\'s your name?'

    if "my name is" in p_message:
        return 'Nice to meet you, ' + p_message[11:].capitalize() + '! 😊  \n \n \n What\' your age?'

    if "i am" in p_message:
        return 'Glad to know, that you are ' + p_message[5:] + ' years old! \n \n \n What\'s your mobile number?'

    if "my mobile number is" in p_message:
        return 'Thanks for sharing your mobile number, ' + p_message[20:]

    if p_message == 'bye':
        return 'Bye! 😍'

    if p_message == 'help':
        return '`Try typing like my name is ---- when asked about name. \n \n \n Try typing like I am ----  when asked about age. \n \n \n Try typing like my mobile number is ---- when asked about mobile number. \n\n\n Type !create <channel name> to create the channel.`'

    return 'I didn\'t understand what you wrote. Try typing "!help".'


def create_channel(message: str) -> str:
    return f'Channel "{message.lower()}" has been created.'