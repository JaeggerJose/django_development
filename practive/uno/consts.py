from enum import Enum

class MessagesType(Enum):
    info = 'info'
    warning = 'warning'
    error = 'error'
    danger = 'danger'

MessagesType.info.label = 'Nachrichten'
MessagesType.warning.label = 'Achtung'
MessagesType.error.lable = 'Falsch'
MessagesType.danger.label = 'unsicher'

MessagesType.info.color = 'green'
MessagesType.warning.color = 'orange'
MessagesType.error.color = 'gray'
MessagesType.danger.color = 'red'

SenstiveWord = ['Happy', 'lachen']