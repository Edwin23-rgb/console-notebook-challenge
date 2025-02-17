# TODO: Agrega el código de las clases de la interfaz de usuario aquí. Borra este comentario al terminar.
from datetime import datetime


class Note:

    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'

    def __init__(self,code: str,title: str,text: str,importance: str):
        self.code: str= code
        self.title: str=title
        self.text: str=text
        self.importance: str=importance
        self.creation_date = datetime.now()



