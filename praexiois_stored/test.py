from subprocess import getoutput
port = getoutput('getAvailablePort')
print (int(port))
