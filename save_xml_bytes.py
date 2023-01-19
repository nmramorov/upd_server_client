from os import path


with open(path.abspath('') + '/storage/config.xml', 'r') as xml_file:
    content = xml_file.readlines()

print(content)
bytes_content = [word.encode('utf-8') for word in content]
print(bytes_content)
with open(path.abspath('') + '/storage/config.bin', 'wb') as xml_byte_file:
    xml_byte_file.writelines(bytes_content)
