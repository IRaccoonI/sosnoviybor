def msg_start():
    message = (
        "Привет!, Приступим"
    )
    return message

def msg_info():
    message = (
        "Что умеет бот:\n"
        "))"
    )
    return message

def msg_auth():
    message = (
        "Авторизация.\n"
        "Введите логин:"
    )
    return message

def msg_auth_pswd():
    message = (
        "Введите пароль:"
    )
    return message

def msg_auth_succsess(new_role):
    message = (
        "Поздравляю теперь вы {}!".format(new_role)
    )
    return message

def msg_auth_error():
    message = (
        "Увы, но ничего не изменилось)"
    )
    return message
