def parser(str):
    if str.startswith("/"):
        command = str.split(" ")[0]
        message = str[len(command):].strip()
        return command, message
    return None, str