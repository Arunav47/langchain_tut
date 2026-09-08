#This is the parser to extract the command and the prompt
def parser(str):
    if str.startswith("/"):
        command = str.split(" ")[0]
        message = str[len(command):].strip()
        return command, message
    return None, str
