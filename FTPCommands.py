
from re import split


class FTPCommands():
    def __init__(self, commandSocket, dataSocket):
        self.commandSocket = commandSocket
        self.dataSocket = dataSocket

    # basic commands
    # pwd gets the working directory for the user
    def pwd(self):

        self.commandSocket.send('PWD')
        self.commandSocket.recieve()

    def sys(self):

        self.commandSocket.send('SYST')
        self.commandSocket.recieve()

    def cd(self, new_dir=None):
        if not new_dir:
            new_dir = input('Choose a directory to switch to: ')
        self.commandSocket.send('CWD', new_dir)
        self.commandSocket.recieve()

    # Quit commadn sidconnects from the serve

    def quit(self):
        self.commandSocket.send('QUIT')
        self.close()

    # the implementation is incomplete
    # only get the list for ./ to prove the concept further work
    # needed

    def ls(self):
        if (self.dataSocket.signedIn == False):
            print('Use PORT or PASV first')
            return

        self.commandSocket.send('LIST')
        self.commandSocket.recieve()
        # gets the list but it is a mess to read
        print("cleaning of data not implemneted :0")
        data = self.dataSocket.channel.recv(2048)
        print(data)

    def passive(self):
        # initiate the passive command and get the port number
        # closing the already existing data channel so a new data channel
        # be opened
        if (self.dataSocket.signedIn == True):
            self.dataSocket.channel.close()
            print("closing previous data config")

            return

        self.commandSocket.send('PASV')
        self.commandSocket.recieve()
        pesvResponse = self.commandSocket.response

        # extracing the substring out of the pesv response
        # converting it to an array

        start = self.commandSocket.response.find("(") + len("(")
        end = pesvResponse.find(")")
        vals = (pesvResponse[start:end]).split(",")

        try:

            self.dataSocket.host = '.'.join(vals[:-2])
            self.dataSocket.port = int(vals[-2])*256+int(vals[-1])

            # using the port numnber and host to open a data channel with the server
            data_connection = (self.dataSocket.host, self.dataSocket.port)

            self.dataSocket.channel.connect(
                data_connection)
            self.dataSocket.signedIn = True

        except Exception as ex:
            print(ex)

    def epassive(self):
        # if (self.dataSocket.signedIn == True):
        #     self.dataSocket.channel.close()
        #     print("closing previous data config")

        self.commandSocket.send('EPSV')
        self.commandSocket.recieve()
        epesvResponse = self.commandSocket.response

        port = split('[|()]', epesvResponse)[4]
        print(self.commandSocket.host, port)

        data_connection = ('10.246.251.93', int(port))
        print(data_connection)

        try:

            self.dataSocket.channel.connect(
                data_connection)
            self.dataSocket.signedIn = True
            print('connected')

        except Exception as ex:

            print("data channel not established error here ")
            print("keeps breaking here :(")
            print(ex)

    def write(self, file_name=None):
        if (self.dataSocket.signedIn == False):
            print('Use PORT or PASV first')
            return

        # To write to a file we need to open a passive channel between
        # the server and the client.
        if self.commandSocket.response.startswith('425'):
            return

        file_name = input('Input a filename: ')
        self.commandSocket.send("STOR", file_name)

        # pesvResponse = command_socket.recv(2048).decode('ascii')[:-2]
        self.commandSocket.recieve()
        data = input('Input what you want to write: ')
        data += '\r\n'

        self.dataSocket.send(data)

        # self.dataSocket.recieve()
        self.dataSocket.channel.close()

    def read(self, file_name=None):
        if (self.dataSocket.signedIn == False):
            print('Use PORT or PASV first')
            return

        if not file_name:
            file_name = input('File you will like to retrive: ')

        self.commandSocket.send("RETR", file_name)
        self.commandSocket.recieve()

        if self.commandSocket.response.startswith('5'):
            return
        try:

            data = self.dataSocket.channel.recv(2048)
            print(data)
        except Exception as ex:
            print(ex)

    def port(self):

        if (self.dataSocket.signedIn == True):
            self.dataSocket.channel.close()
            print("closing previous data config")
            return

        port1 = str(112)
        port2 = str(43)
        host = '10.250.76.53'

        conn = ','.join(host.split('.'))

        port = int(port1)*256+int(port2)
        host = self.commandSocket.host

        # conn = ','.join(host.split('.')) + ',' + port1 + ',' + port2

        # self.commandSocket.send("PORT", conn)
        # self.commandSocket.response()

        self.commandSocket.channel.send(
            'PORT {h},{p1},{p2}\r\n'.format(h=conn, p1=port1, p2=port2).encode('ascii'))
        print(self.commandSocket.channel.recv(2048).decode('ascii'))

        # self.dataSocket.channel.close()

        # data_connection = (host, port)
        print(
            "unable to connect to the dataSocket for streaming back data using port command")

        data_connection = ('10.246.251.93', 51243)

        self.dataSocket.channel.connect(
            data_connection)
        self.dataSocket.signedIn = True

    # Facilitates the closing of the client.
    # Both the command and data sockets are closed,
    # as is the logger.

    def help(self):
        print("here are the only valid commands ")

        print(
            'login cd  quit port dir\n pwd ls sys help read\nwrite passive eport epassive')

    def close(self):

        self.commandSocket.channel.close()
        self.dataSocket.channel.close()
        self.commandSocket.signedIn = False
        self.dataSocket.signedIn = False
        print("all ports are closed ")
