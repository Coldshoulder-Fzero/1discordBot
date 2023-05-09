def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == ' hello':
        return 'Hey there!'

    if p_message == '!help':
        return " use !rage + username to increment"