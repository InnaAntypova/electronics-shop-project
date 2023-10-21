class InstantiateCSVError(Exception):
    """ Класс для исключения при поврежденном файле"""

    def __init__(self):
        self.message = "Файл поврежден"

    def __str__(self):
        return self.message

