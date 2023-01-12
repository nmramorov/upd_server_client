import socket


class UDPClient:
    def __init__(self, server_ip='localhost', server_port=20001, buffer_size=1024):
        self.server_ip = server_ip
        self.server_port = server_port
        self.buffer_size = buffer_size
        self.COMMANDS = ('check', 'set', 'shutdown', 'register')
        
    def _initialize(self):
        udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        return udp_socket
    
    def run(self):
        client_socket = self._initialize()
        
        print('UDP Client is running...')
        while True:
            user_input = input()
            
            if user_input == 'quit':
                break
            
            if user_input.split(' ')[0] in self.COMMANDS:
                client_socket.sendto(user_input.encode('utf-8'), (self.server_ip, self.server_port))
                response = client_socket.recvfrom(self.buffer_size)
                    
                print(response)
                print(f'Response from server: {response[0]}')
            else:
                print(f'No such command {user_input}')
 