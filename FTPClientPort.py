from socketClient import socketClient
from FTPCommands import FTPCommands


class FTPClientPort:
    def __init__(self):
        self.commandSocket = socketClient()
        self.dataSocket = socketClient()


if __name__ == "__main__":

    # connection is made to the CS472 FTP server

    print("making a connection")

    FTPClient = FTPClientPort()
    FTPClient.commandSocket.connect('10.246.251.93', 21)

    # login into the commnad channel sending the username and password
    FTPClient.commandSocket.login('cs472', 'hw2ftp')

    print('username and password authenticated!!\n')

    command = FTPCommands(FTPClient.commandSocket, FTPClient.dataSocket)

    # pipe keep breaking when shifting from passive to epassive
    # SO QUITING AND running it in a new file

    print("\nOpening a port connection")

    command.port()
