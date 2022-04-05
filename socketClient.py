import socket
from FTPCommands import FTPCommands


class socketClient:
    # initiate a channel that the client will be using to send and recieve
    # requests/data

    def __init__(self):
        self.channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = None
        self.port = None
        self.command = None
        self.response = None
        self.signedIn = False

    # Function takes in the command argumnets provided
    # sends the commnad through the channel

    def send(self, *args):
        self.command = ' '.join(args)
        self.command += '\r\n'

        try:
            self.channel.send(self.command.encode('ascii'))

        except Exception as ex:
            print(ex)

    def recieve(self):
        self.response = self.channel.recv(1024).decode('ascii')[:-2]
        print(self.response)

    def connect(self, host, port):
        try:
            self.channel.connect((host, port))
            self.response = self.channel.recv(1024).decode('ascii')
            self.connected = True
            self.host = host
            print(self.response)
        except Exception as ex:
            print("error")

    # login is used to send the username and the password to
    # the open connection to establish and open a command channel
    def login(self, user, password):

        user = 'USER {u}\r\n'.format(u=user).encode('ascii')

        password = 'PASS {p}\r\n'.format(p=password).encode('ascii')
        self.channel.send(user)
        print(self.channel.recv(1024).decode('ascii'))
        self.channel.send(password)
        print(self.channel.recv(1024).decode('ascii'))
