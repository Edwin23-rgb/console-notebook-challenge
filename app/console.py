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

        self.tags = []

    def add_tag(self, tag: str):
        """Agrega una etiqueta a la lista de tags si no existe ya."""
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        """Retorna una cadena de texto con el formato especificado."""
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"

