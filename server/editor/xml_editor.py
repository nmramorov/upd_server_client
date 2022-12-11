from os import path


class XmlEditor:
    def __init__(self) -> None:
        """
        Упражнение 3: погуглить как сохранить файл config в бинарном виде и работать дальше уже с ним
        """
        self.xml_path = path.abspath('') + '/storage/config.xml'

    def write(self, channel, state):
        """
        Упражнение 1: сделать так, чтобы при вызове этой функции и передачи ПРАВИЛЬНЫХ 
        аргументов channel и state в файле config появлялась измененная запись
        """
        with open(path.abspath('') + '/storage/config', 'w', encoding="utf-8") as xml_bytes_file:
            ...
    
    def read(self, channel):
        """
        Упражнение 2: сделать так, чтобы при передаче ПРАВИЛЬНОГО аргумента channel выводился статус 
        этого канала из файла config
        """
        with open(path.abspath('') + '/storage/config', 'rb') as xml_bytes_file:
            ...
            

e = XmlEditor()

e.write('1', 'UP')
assert e.read('1') == 'UP'
e.write('3', 'UP')
assert e.read('3') == 'UP'
e.write('3', 'DOWN')
assert e.read('3') == 'DOWN'