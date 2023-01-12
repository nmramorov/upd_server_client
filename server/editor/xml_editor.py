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
        with open(self.xml_path, 'r') as xml_bytes_file:
            data = xml_bytes_file.readlines()
        with open(self.xml_path, 'w') as xml_bytes_file:
            if state == 'UP' or state == 'DOWN':
                if channel == '1' or channel == '2' or channel == '3' or channel == '4' or channel == '5' or channel == '6':
                    data[int(channel)] = channel + ':' + state +'\n'
                    xml_bytes_file.writelines(data)
                else:
                    return 'Wrong channel'
            else:
                return 'Wrong state'
    
    def read(self, channel):
        """
        Упражнение 2: сделать так, чтобы при передаче ПРАВИЛЬНОГО аргумента channel выводился статус 
        этого канала из файла config
        """
        with open(self.xml_path, 'r') as xml_bytes_file:
            for index, line in enumerate(xml_bytes_file):
                if int(channel) == index:
                    return line.split(':')[1][:-1]
            

e = XmlEditor()

e.write('1', 'UP')
assert e.read('1') == 'UP'
e.write('3', 'UP')
assert e.read('3') == 'UP'
e.write('3', 'DOWN')
assert e.read('3') == 'DOWN'