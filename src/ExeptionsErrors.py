class InstantiateCSVError(Exception):
    """ Класс для исключения при поврежденном файле"""

    def __init__(self):
        self.message = f"Файл поврежден"

    def __str__(self):
        return self.message

