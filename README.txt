This is the FTP client ReadME

There are three programs that are runnable 
FTPClient.py--uses passive commands to send and recieve data
FTPClientEPSV.py--uses epassive commands to send and reciece data
FTPClientPort.py--uses port to make a connection failed to make data connectin



This program is absolutly chaotic in coming together run the two files sepratly to 
see the results of the both programs running 


All commands working 
expect for port/eport where data channel not being establihed. I have no idea why?



Read in passive only works when you commnet out the write command it is beacues I am cloosing teh data cahnnel after I write