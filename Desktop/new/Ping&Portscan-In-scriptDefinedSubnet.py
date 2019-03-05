#QUICK AND DIRTY PING AND SCAN SCRIPT FOR ANY /24 SUBNET. TESTED ON WINDOWS 7. 
#DEFINE A RANGE WITHIN THIS SCRIPT TO PING&SCAN A /24 TARGET SUBNET. GOOD FOR SCHEDULED JOBS ETC.
#INCLUDES OPTIONAL SMTP FEATURE (SEND RESULTS TO YOUR EMAIL)

from time import sleep
from datetime import datetime
import Queue
import shlex
import socket, threading
import sys
import subprocess
import smtplib

pingresultprint = []        #ping results
scanresult = []             #portscan results
lock = threading.Lock()


def main():     #==== DEFINE IP & PORTS HERE =======#

                global pingtarget

#                t1 = datetime.now()                 #timer start
                
                pingtarget = "172.30.1."          #define the first 3 octets
                ping_range(226,228)                    #define last /24 octet range (from .. to ..)
                
                fp = int(1)                         #define port scan range (from..)
                tp = int(1024)                     #define port scan range (to..)
                for host_ip in pingresultprint:
                    scan_ports(host_ip,fp,tp)

#                t2 = datetime.now()                 #timer end
#                total =  t2 - t1                
#                print '\n', 'Ping&scan test completed in total time:' , total, '\n\n'

def ping(ip):

    ipsubnet = pingtarget + ip
    result = subprocess.Popen(['ping', ipsubnet, '-n','2', '-w', '3000'], stdout=subprocess.PIPE, shell=True)
    pingres = result.communicate()[0]
    if ('unreachable' in pingres) or ('timed out' in pingres) or ('unknown' in pingres) or ('expired' in pingres):           
#            print("{} did not respond".format(ipsubnet)) + '\n'         #for testing (speed, concurrency etc.)
            pass
    else:
            print ("{} replied".format(ipsubnet))
            pingresultprint.extend([ipsubnet])                          #this data feeds into port scanner


def ping_range(start,end):
#        global pinginfo
        print '======= Pinging subnet in progress... ======= \n'

        
        r = 1
        for ip in range(start,end):
            with lock:
                t = threading.Thread(target=ping, args=(str(ip),))     
                r += 1
                t.start()
                sleep(0.2)


#        pinginfo = "Response from: ".join(pingresultprint)
#        print "\n".join(pingresultprint)
        sleep(3)
        print '\n', 'Ping test completed.\n'



def TCP_con(host_ip, port):
                successprint = "{}:{} \n".format(host_ip, port)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)

                try:
                    con = s.connect((host_ip, port))
#                    a = str(host_ip, ':', port)
#                    print ('\n {} is open'.format(port))
                    scanresult.extend(successprint)
                    con.close()
                except:
                    pass

def scan_ports(host_ip, fp, tp):

                print '======= Scanning IP address:' + host_ip + ' ======='
                      
                r = 1
                for port in range(fp,tp):       #change 'range()' to a 'targetports[]' list for definable port range scanning (E.G. targetports = [25, 80, 443])
                    with lock:
                        t = threading.Thread(target=TCP_con, args=(host_ip, port)) 
                        r += 1     
                        t.start()


def smtp():
                
                server = smtplib.SMTP('smtp.emaildomain.com', 587)
                server.starttls()
                server.login("youremail@emaildomain.com", "youremailpassword")                
                
                msg = 'Subject: PING n SCAN results \n\n' + 'Ping response from hosts: \n' + str("\n".join(pingresultprint)) + '\n\n\n' + 'Opened ports: \n' + str("".join(scanresult))
                                
                server.sendmail("youremail@emaildomain.com", "youremail@emaildomain.com", msg)
                server.quit()

                
if __name__ == "__main__":
        main()
#        smtp()     #optional SMTP
        print '\n\n', 'Ping response from hosts: \n', ("\n".join(pingresultprint)), '\n\n', 'Opened ports: \n', "".join(scanresult)
