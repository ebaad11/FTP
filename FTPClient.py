
from socketClient import socketClient
from FTPCommands import FTPCommands
from logger import logger


class FTPClient:

    COMMANDS = ['login', 'cd', 'quit', ' port', 'dir', 'pwd',
                'ls', 'sys', 'help', 'read', 'write',
                'passive', 'eport' 'epassive']

    #  typical FTP session operates using two channels between the FTP client and server:
    # a command channel and a data channel. As their names imply, the command channel is used
    # for transmitting commands as well as replies to those commands, while the data channel
    # is used for transferring data.

    def __init__(self):
        self.commandSocket = socketClient()
        self.dataSocket = socketClient()
        # self.logger = logger()


if __name__ == "__main__":

    # connection is made to the CS472 FTP server

    print("making a connection")

    FTPClient = FTPClient()
    FTPClient.commandSocket.connect('10.246.251.93', 21)

    # login into the commnad channel sending the username and password
    FTPClient.commandSocket.login('cs472', 'hw2ftp')

    print('username and password authenticated!!\n')

    # running basic commandsbasic commands

    # FTPCommand is a class that takes in a commnad and data socket and runs
    # commands through them
    command = FTPCommands(FTPClient.commandSocket, FTPClient.dataSocket)

    # USING THE EXED FUNCTION TO RUN A COMMAND

    # help
    command.help()

    # sys
    c1 = 'sys'
    commandStr = "command." + c1+'()'
    exec(commandStr)

    # pwd
    c2 = 'pwd'
    commandStr = "command." + c2+'()'
    exec(commandStr)

    # cd changes the directory to /home

    command.cd("/home")
    print("directory changed\n")

    # bad input for cd
    print('executing bad cd command\n ')
    command.cd("/nothome")

    # change dir back to home/CS472
    command.cd("/home/cs472")

    # Trying to read data with out opening a port or passive connection

    # ls
    print('\nExecuting ls write and read with out opening a data channel')
    command.ls()

    # write with out opening a data connection
    command.write()

    # read with out opening a data connection
    command.read()

    # opening passive mode
    print("ENTERING PASSIVE MODE HERE")

    command.passive()

    # write--passive

    command.write()

    # UNCOMMENT THE READ COMMADS TO RUN A READ

    # read--passive--user input
    # command.read()

    # read--passive--default value
    # command.read('ebaad3.txt')

    command.quit()
