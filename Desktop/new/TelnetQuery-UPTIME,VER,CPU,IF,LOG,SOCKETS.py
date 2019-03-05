from time import sleep
import sys
import telnetlib
global a


HOST = raw_input("Enter IP address: ")
print 'Fetching results ... '
tn2 = telnetlib.Telnet(HOST)

def main():

    user = "user1"                      #USERNAME
    password = "cisco123"               #USER EXEC LOGIN PASSWORD
    password2 = "cisco123"              #PRIVILEGE EXEC LOGIN PASSWORD



    tn2.write(user + "\n")
    tn2.write(password + "\n")
    sleep(2)
    tn2.write("termin len 0" + "\n")
    sleep(2)
    tn2.write("enable" + "\n")
    sleep(2)
    tn2.write(password2 + "\n")
    sleep(2)
    
    uptime()
    proc()
    ipintb()
    interf()
    shlog()
    shopenports()
    
    sleep(0.2)
    
def close():

    tn2.write("exit\n")
    a = tn2.read_all()
    b = []
    b.append(a)
    f = open('{} - uptime,ver,cpu,if.txt'.format(HOST), 'w')
    sys.stdout = f
    print "/n".join(b)
    sys.stdout.close()


    f2 = open('{} - uptime,ver,cpu,if.txt'.format(HOST), 'r+')
    sys.stdout = f2
    d = f2.readlines()
    f2.seek(0)
    for i in d:
        if any(s in i for s in ("User Access Verification", "Username:", "Password:", "enable", "Technical Support:", "termin len 0", "show inventory", "sh proc cpu history")):
            pass
        elif any(j in i for j in ("sh ver | s up", "sh ip int b", "sh interfaces", "term shell")):
            print "\n\n====================================================================================== \n" 
        else:    
            f2.write(i)
    f2.truncate()
    f2.close()

def uptime():
    tn2.write("show inventory\n")
    tn2.write("sh ver | s up\n")

def proc():
    sleep(0.2)
    tn2.write("sh proc cpu history \n")

def ipintb():
    sleep(0.2)
    tn2.write("sh ip int b\n")
    tn2.write("\n")

def interf():
    sleep(0.2)
    tn2.write("sh interfaces \n")

def shlog():    
    sleep(0.2)
    tn2.write("term shell \n")          #only works with Cisco model 1900 serie onward
    tn2.write("sh log | tail \n")

def shopenports():
    sleep(0.2)
    tn2.write("sh control-plane host open-p \n")
    
if __name__ == "__main__":
        main()
        close()

