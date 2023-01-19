import socket
from threading import Thread


class UDPClient:
    def __init__(self, server_ip='localhost', server_port=20001, buffer_size=1024):
        self.server_ip = server_ip
        self.server_port = server_port
        self.buffer_size = buffer_size
        self.COMMANDS = ('check', 'set', 'shutdown', 'register')

    def _initialize(self):
        udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        return udp_socket

    def check(self, client_socket):
        while True:
            try:
                response = client_socket.recvfrom(self.buffer_size)
                print(f'Received response: {response[0]}')
            except OSError:
                continue

    def run(self):
        client_socket = self._initialize()

        print('UDP Client is running...')
        listening_thread = Thread(target=self.check, args=[client_socket])

        while True:
            user_input = input()

            if user_input == 'quit':
                break
            if not listening_thread.is_alive():
                listening_thread.start()

            if user_input.split(' ')[0] in self.COMMANDS:
                client_socket.sendto(user_input.encode('utf-8'), (self.server_ip, self.server_port))
            else:
                print(f'No such command {user_input}')
        listening_thread.join(timeout=1.0)
