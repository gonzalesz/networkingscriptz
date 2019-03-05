#QUICK AND DIRTY PING AND SCAN SCRIPT FOR ANY /24 SUBNET. TESTED ON WINDOWS 7.
#PROMPTS FOR USER INPUT FROM SHELL FOR TARGET RANGE, TO PING/SCAN A /24 TARGET SUBNET.
#INCLUDES OPTIONAL SMTP FEATURE (SEND RESULTS TO YOUR EMAIL)

from time import sleep
from datetime import datetime
import Queue
import shlex
import socket, threading
import sys
import subprocess
import smtplib

pingresultprint = []    #ping results
scanresult = []         #portscan results
lock = threading.Lock()


def main():

                t1 = datetime.now()             #timer start

                global subnet
                global fromport
                global toport
                hostname = socket.gethostname()
                IPaddr = socket.gethostbyname(hostname)
                
                print 'Your IP is: ', IPaddr, '\n'                
                first3octet_IP = raw_input("Enter the first 3 octets for subnet (e.g. xxx.xxx.xxx. ) to ping:  ")
                subnet = first3octet_IP
                fromip = input("Enter last octet (from ip) for subnet to ping&scan (e.g. 1):  ")
                toip = input("Enter last octet (to ip) for subnet to ping&scan (e.g. 24):  ")
                fromport = input("Enter starting range for port scan:  ")
                toport = input("Enter ending range for port scan:  ")
                from_p = fromport
                to_p = toport

                ping_range(fromip,toip)

                for host_ip in pingresultprint:
                    scan_ports(host_ip)
                
                t2 = datetime.now()             #timer end
                total = t2 - t1
                print '\n', 'Ping & Scanning ports completed in total time: ', total

def ping(ip):
    
    ipsubnet = str(subnet + ip)
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
                sleep(0.5)


#        pinginfo = "Response from: ".join(pingresultprint)
#        print "\n".join(pingresultprint)
        sleep(3)
        print '\n', 'Ping test completed.'
#        print '\n', 'Ping test completed in total time:' , total, '\n\n'


def TCP_con(host_ip, port):
                successprint = "{}:{} \n".format(host_ip, port)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)

                try:
                    con = s.connect((host_ip, port))
#                    a = str(host_ip, ':', port)
#                    print ('\n {} is open'.format(port))
                    scanresult.extend(successprint)
                    con.close()
                except:
                    pass

def scan_ports(host_ip):
    
                from_p = fromport
                to_p = toport
                print '======= Scanning IP address:' + host_ip + ' ======='
                                
                r = 1
                for port in range(from_p,to_p):       #change 'range()' to 'targetports' for definable port range (E.G. targetports = [25, 80, 443])
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
