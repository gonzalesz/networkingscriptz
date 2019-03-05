from time import sleep
import getpass
import sys
import telnetlib
global a
#HOST = "192.168.1.1"

HOST = raw_input("Enter IP address: ")
tn = telnetlib.Telnet(HOST)

def main():
    
    user = "username"                   #LOGIN
    password = "password"
    password2 = "password2"

#    user = "username1"                 #LOCAL LOGIN
#    password = "password1"
#    password2 = "password2"
    
    tn.write(user + "\n")
    tn.write(password + "\n")
    sleep(2)
    tn.write("termin len 500" + "\n")
    sleep(2)
    tn.write("enable" + "\n")
    sleep(2)
    tn.write(password2 + "\n")
    sleep(2)
    
    arp()
    dhcp()
    tcp()
    nat()
    
    tn.write("show running-config brief\n")
    tn.write("\n")
    sleep(0.3)

def close():

    tn.write("exit\n")
    a = tn.read_all()
    b = []
    b.append(a)
    f = open('{} - arp,nat,dhcp,tcp,runconf.txt'.format(HOST), 'w')
    sys.stdout = f
    print "/n".join(b)
    sys.stdout.close()


    f2 = open('{} - arp,nat,dhcp,tcp,runconf.txt'.format(HOST), 'r+')
    sys.stdout = f2
    d = f2.readlines()
    f2.seek(0)
    for i in d:
        if any(s in i for s in ("User Access Verification", "Username:", "Password:", "enable", "Technical Support:", "termin len 500")):
            pass
        elif any(j in i for j in ("show ip dhcp binding", "show ip dhcp conflict")):
            print "\n\n\n=================================== DHCP ====================================== \n\n"
        elif "show tcp brief numeric" in i:
            print "\n\n\n=================================== TCP OPEN ====================================== \n\n"
        elif "show ip nat trans" in i:
            print "\n\n\n=================================== NAT XLATIONS ====================================== \n\n"
        elif "show running-config brief" in i:
            print "\n\n\n=================================== RUNNING CONFIG ====================================== \n\n"
        else:    
            f2.write(i)
    f2.truncate()
    f2.close()

def arp():
    sleep(0.2)
    tn.write("show arp \n")

def nat():
    sleep(0.2)
    tn.write("show ip nat trans \n")

def dhcp():
    sleep(0.2)
    tn.write("show ip dhcp binding \n")
    tn.write("show ip dhcp conflict \n")   
    
def tcp():
    sleep(0.2)
    tn.write("show tcp brief numeric \n")
    
if __name__ == "__main__":

        print 'Fetching results...'
        main()
        close()


