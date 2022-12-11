import socket


class UDPServer:
    def __init__(self, ip_address = 'localhost', port = 20001, buffer_size = 1024):
        self.ip_address = ip_address
        self.port = port
        self.buffer_size = buffer_size
        
    def _initialize(self):
        udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)    
        udp_socket.bind((self.ip_address, self.port))
        return udp_socket
    
    def _respond(self, udp_socket, content, respond_to):
        print(respond_to)
        udp_socket.sendto(content.encode('utf-8'), respond_to)
        
    def _get_command(self, payload):
        print(payload[1].split(':'))
        return payload[1].split(':')[1][2:]

    def run(self):
        response = None
        socket_server = self._initialize()
        print("UDP server up and listening")
        
        while True:
            bytes_response = socket_server.recvfrom(self.buffer_size)

            message, address = bytes_response[0], bytes_response[1]

            client_msg = "Message from Client:{}".format(message)

            if client_msg == 'shutdown':
                break

            _, *params = client_msg.split(' ')
            command = self._get_command(params)

            if command == 'set':
                channel, channel_state = params[2], params[3][:-1]
                response = f'Set {channel} to {channel_state}'
            elif command == 'check':
                channel = params[2][:-1]
                response = f'{channel} has value 1'
            else:
                response = 'No command'

            self._respond(socket_server, response, address)
