from os import path


ENCODING = 'utf-8'

class XmlEditor:
    def __init__(self) -> None:
        self.xml_path = path.abspath('') + '/storage/config.bin'

    def write(self, channel, state):
        with open(self.xml_path, 'rb') as xml_bytes_file:
            data = xml_bytes_file.readlines()
            data = [word.decode(ENCODING) for word in data]
        with open(self.xml_path, 'wb') as xml_bytes_file:
            if state == 'UP' or state == 'DOWN':
                if channel == '1' or channel == '2' or channel == '3' or channel == '4' or channel == '5' or channel == '6':
                    data[int(channel)] = channel + ':' + state +'\n'
                    xml_bytes_file.writelines([word.encode(ENCODING) for word in data])
                else:
                    return 'Wrong channel'
            else:
                return 'Wrong state'
    
    def read(self, channel):
        with open(self.xml_path, 'rb') as xml_bytes_file:
            for index, line in enumerate(xml_bytes_file):
                if int(channel) == index:
                    return line.decode(ENCODING).split(':')[1][:-1]
            

e = XmlEditor()

e.write('1', 'UP')
assert e.read('1') == 'UP'
e.write('3', 'UP')
assert e.read('3') == 'UP'
e.write('3', 'DOWN')
assert e.read('3') == 'DOWN'