#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import paramiko
from Tkinter import *
import tkMessageBox
from Tkinter import Menu
import subprocess
from tkSimpleDialog import askstring

localip = "172.30.112.214"    #the ip address of your Syslog svr (for the 'debugging' function)




port = 22
jumphostusername = "user"
jumphostpassword = "JHOSTTest123"
username = "cisco"
ciscoauthpassword = "cisco123"
ciscoenablepassword = "ciscoenable"


def loginjumphost():
    global remote_conn
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname=jumphostip, port=int(port), username=jumphostusername, password=jumphostpassword)
    except:
        tkMessageBox.showinfo('Error', 'Tiempo de conexión agotado; no se puede conectar al dispositivo.')
        quit()
        
    print "Conexión exitosa", jumphostip
    sleep(0.5)
    remote_conn = ssh_client.invoke_shell()    
    remote_conn.send("ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no " + ip + " \n")
    sleep(2)
    remote_conn.send(ciscoauthpassword + "\n")
    sleep(2)
    remote_conn.send("terminal len 0 \n")
    sleep(2)
    remote_conn.send("en \n")
    sleep(2)
    remote_conn.send(ciscoenablepassword + "\n")


def login():
    global remote_conn
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname=ip, port=int(port), username=username, password=ciscoauthpassword)
    except:
        tkMessageBox.showinfo('Error', 'Tiempo de conexión agotado; no se puede conectar al dispositivo.')
        quit()
    
    print "Conexión exitosa", ip

    remote_conn = ssh_client.invoke_shell()
    remote_conn.send("terminal len 0\n")
    sleep(0.3)
    remote_conn.send("en\n")
    sleep(0.3)
    remote_conn.send(enablepassword + "\n")
    


    

def main():
    
    global window
##    global new_item
##    global administration
##    global advanced
##    global debug
##    global cli
    global menu
    window = Tk()
    window.title("Revelation")
    window.geometry('650x600')
    menu = Menu(window)
##    new_item = Menu(menu, tearoff=0)
##    administration = Menu(menu, tearoff=0)
##    advanced = Menu(menu, tearoff=0)
##    cli = Menu(menu, tearoff=0)
##    debug = Menu(menu, tearoff=0)    
##    subwindows()



def subwindows():
    
    def route():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("Routing Control")
        window.geometry('600x735')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)

        negframe=LabelFrame(window,text=" Negate ",font=('verdana', 8, 'bold'),padx=10,pady=10,width=100,height=100)
        negframe.grid(row=0,column=1)
        
        chk_state_neg = BooleanVar()
        chk_state_neg.set(False)
        chk = Checkbutton(negframe, variable=chk_state_neg)
        chk.grid(column=1, row=0)



        basicrouteframe=LabelFrame(window,text=" Basic routing ",font=('verdana', 8, 'bold'),padx=10,pady=2,width=100,height=100)
        basicrouteframe.grid(row=0,column=0, sticky=("nsew"))

        chk_state_mcast = BooleanVar()
        chk_state_mcast.set(False)
        chk = Checkbutton(basicrouteframe, text='Multicast', variable=chk_state_mcast)
        chk.grid(column=4, row=2)

        lbl = Label(basicrouteframe, text="Add static route:")    
        lbl.grid(column=0, row=2)
        staticip = Entry(basicrouteframe, bg='white', width=15, fg='grey')
        staticip.grid(column=1, row=2)
        staticip.insert(0, "IP")
        def handle_focus_in(_):
            if staticip.cget('fg') != 'black':
                staticip.delete(0, END)
                staticip.config(fg='black')
        def handle_focus_out(_):
            if staticip.get() == "":
                staticip.delete(0, END)
                staticip.config(fg='grey')
                staticip.insert(0, "IP")    
        staticip.bind("<FocusOut>", handle_focus_out)
        staticip.bind("<FocusIn>", handle_focus_in)
        
        staticmask = Entry(basicrouteframe, bg='white', width=15, fg='grey')
        staticmask.grid(column=2, row=2)
        staticmask.insert(0, "Subnet Mask")
        def handle_focus_in(_):
            if staticmask.cget('fg') != 'black':
                staticmask.delete(0, END)
                staticmask.config(fg='black')
        def handle_focus_out(_):
            if staticmask.get() == "":
                staticmask.delete(0, END)
                staticmask.config(fg='grey')
                staticmask.insert(0, "Subnet Mask")    
        staticmask.bind("<FocusOut>", handle_focus_out)
        staticmask.bind("<FocusIn>", handle_focus_in)
        
        staticgw = Entry(basicrouteframe, bg='white', width=15, fg='grey')
        staticgw.grid(column=3, row=2)
        staticgw.insert(0, "gateway IP")
        def handle_focus_in(_):
            if staticgw.cget('fg') != 'black':
                staticgw.delete(0, END)
                staticgw.config(fg='black')
        def handle_focus_out(_):
            if staticgw.get() == "":
                staticgw.delete(0, END)
                staticgw.config(fg='grey')
                staticgw.insert(0, "gateway IP")    
        staticgw.bind("<FocusOut>", handle_focus_out)
        staticgw.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(basicrouteframe, text="Optional:").grid(column=0, row=3)
        Metricopt = Entry(basicrouteframe, bg='white', width=7, fg='grey')
        Metricopt.place(y=30, x=92)
        Metricopt.insert(0, "Metric")
        def handle_focus_in(_):
            if Metricopt.cget('fg') != 'black':
                Metricopt.delete(0, END)
                Metricopt.config(fg='black')
        def handle_focus_out(_):
            if Metricopt.get() == "":
                Metricopt.delete(0, END)
                Metricopt.config(fg='grey')
                Metricopt.insert(0, "Metric")    
        Metricopt.bind("<FocusOut>", handle_focus_out)
        Metricopt.bind("<FocusIn>", handle_focus_in)        
        Trackopt = Entry(basicrouteframe, bg='white', width=7, fg='grey')
        Trackopt.place(y=30, x=152)
        Trackopt.insert(0, "Track")
        def handle_focus_in(_):
            if Trackopt.cget('fg') != 'black':
                Trackopt.delete(0, END)
                Trackopt.config(fg='black')
        def handle_focus_out(_):
            if Trackopt.get() == "":
                Trackopt.delete(0, END)
                Trackopt.config(fg='grey')
                Trackopt.insert(0, "Track")    
        Trackopt.bind("<FocusOut>", handle_focus_out)
        Trackopt.bind("<FocusIn>", handle_focus_in) 
        VRFopt = Entry(basicrouteframe, bg='white', width=7, fg='grey')
        VRFopt.place(y=30, x=212)
        VRFopt.insert(0, "VRF")
        def handle_focus_in(_):
            if VRFopt.cget('fg') != 'black':
                VRFopt.delete(0, END)
                VRFopt.config(fg='black')
        def handle_focus_out(_):
            if VRFopt.get() == "":
                VRFopt.delete(0, END)
                VRFopt.config(fg='grey')
                VRFopt.insert(0, "VRF")    
        VRFopt.bind("<FocusOut>", handle_focus_out)
        VRFopt.bind("<FocusIn>", handle_focus_in)
        
        Nameopt = Entry(basicrouteframe, bg='white', width=7, fg='grey')
        Nameopt.place(y=30, x=272)
        Nameopt.insert(0, "Name")
        def handle_focus_in(_):
            if Nameopt.cget('fg') != 'black':
                Nameopt.delete(0, END)
                Nameopt.config(fg='black')
        def handle_focus_out(_):
            if Nameopt.get() == "":
                Nameopt.delete(0, END)
                Nameopt.config(fg='grey')
                Nameopt.insert(0, "Name")    
        Nameopt.bind("<FocusOut>", handle_focus_out)
        Nameopt.bind("<FocusIn>", handle_focus_in)
        
        Tagopt = Entry(basicrouteframe, bg='white', width=6, fg='grey')
        Tagopt.place(y=30, x=332)
        Tagopt.insert(0, "Tag")
        def handle_focus_in(_):
            if Tagopt.cget('fg') != 'black':
                Tagopt.delete(0, END)
                Tagopt.config(fg='black')
        def handle_focus_out(_):
            if Tagopt.get() == "":
                Tagopt.delete(0, END)
                Tagopt.config(fg='grey')
                Tagopt.insert(0, "Tag")    
        Tagopt.bind("<FocusOut>", handle_focus_out)
        Tagopt.bind("<FocusIn>", handle_focus_in)
        

        def staticro():
            defiproutecmd = "ip route " + staticip.get() + " " + staticmask.get() + " " + staticgw.get()
            defipvrfroutecmd = "ip route vrf " + VRFopt.get() + " " + staticip.get() + " " + staticmask.get() + " " + staticgw.get()
            defiproutecmdneg = "no ip route " + staticip.get() + " " + staticmask.get() + " " + staticgw.get()
            defipvrfroutecmdneg = "no ip route vrf " + VRFopt.get() + " " + staticip.get() + " " + staticmask.get() + " " + staticgw.get()
            defipmroutecmd = "ip mroute " + staticip.get() + " " + staticmask.get() + " " + staticgw.get()
            defipvrfmroutecmd = "ip mroute vrf " + VRFopt.get() + " " + staticip.get() + " " + staticmask.get() + " " + staticgw.get()
            defipmroutecmdneg = "no ip mroute " + staticip.get() + " " + staticmask.get() + " " + staticgw.get()
            defipvrfmroutecmdneg = "no ip mroute vrf " + VRFopt.get() + " " + staticip.get() + " " + staticmask.get() + " " + staticgw.get()            
            if staticip.get() == "" or staticip.get() == "IP" or staticmask.get() == "" or staticmask.get() == "Subnet Mask" or staticgw.get() == "" or\
            staticgw.get() == "gateway IP":
                tkMessageBox.showinfo('Error', 'Please input the minimum required information - IP, subnet mask and next hop gateway.', parent=window)
            else:
                if chk_state_neg.get() == False:
                    if chk_state_mcast.get() == False:
                        if VRFopt.get() == "" or VRFopt.get() == "VRF":
                            if Metricopt.get() != "" and Metricopt.get() != "Metric":
                                defiproutecmd = defiproutecmd + " " + Metricopt.get()
                            else:
                                pass
                            if Trackopt.get() != "" and Trackopt.get() != "Track":
                                defiproutecmd  = defiproutecmd + " track " + Trackopt.get()
                            else:
                                pass
                            if Nameopt.get() != "" and Nameopt.get() != "Name":
                                defiproutecmd  = defiproutecmd + " name " + Nameopt.get()
                            else:
                                pass
                            if Tagopt.get() != "" and Tagopt.get() != "Tag":
                                defiproutecmd  = defiproutecmd + " tag " + Tagopt.get()
                            else:
                                pass
                            remote_conn.send("conf t \n")
                            sleep(0.5)
                            remote_conn.send(defiproutecmd + "\n")
                            sleep(0.5)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('IP route', 'Static IP route added.', parent=window)

                        else:
                            if Metricopt.get() != "" and Metricopt.get() != "Metric":
                                defipvrfroutecmd = defipvrfroutecmd + " " + Metricopt.get()
                            else:
                                pass
                            if Trackopt.get() != "" and Trackopt.get() != "Track":
                                defipvrfroutecmd  = defipvrfroutecmd + " track " + Trackopt.get()
                            else:
                                pass
                            if Nameopt.get() != "" and Nameopt.get() != "Name":
                                defipvrfroutecmd  = defipvrfroutecmd + " name " + Nameopt.get()
                            else:
                                pass
                            if Tagopt.get() != "" and Tagopt.get() != "Tag":
                                defipvrfroutecmd  = defipvrfroutecmd + " tag " + Tagopt.get()
                            else:
                                pass
                            remote_conn.send("conf t \n")
                            sleep(0.5)
                            remote_conn.send(defipvrfroutecmd + "\n")
                            sleep(0.5)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('IP route', 'Static IP (VRF) route added.', parent=window)

           
                    else:
                        if (Trackopt.get() != "Track" and Trackopt.get() != "") or (Nameopt.get() != "Name" and Nameopt.get() != "")\
                           or (Tagopt.get() != "Tag" and Tagopt.get() != ""):
                            tkMessageBox.showinfo('Error', 'Track, name and tags cannot be used with multicast routes.', parent=window)
                        else:                            
                            if VRFopt.get() == "" or VRFopt.get() == "VRF":
                                if Metricopt.get() != "" and Metricopt.get() != "Metric":
                                    defipmroutecmd = defipmroutecmd + " " + Metricopt.get()
                                else:
                                    pass                                
                                remote_conn.send("conf t\n")
                                sleep(0.5)
                                remote_conn.send(defipmroutecmd + "\n")
                                sleep(0.5)
                                remote_conn.send("exit \n")
                                tkMessageBox.showinfo('IP route', 'Static IP multicast (RPF) route added.', parent=window)
                            else:
                                if Metricopt.get() != "" and Metricopt.get() != "Metric":
                                    defipvrfmroutecmd = defipvrfmroutecmd + " " + Metricopt.get()
                                else:
                                    pass                                
                                remote_conn.send("conf t\n")
                                sleep(0.5)
                                remote_conn.send(defipvrfmroutecmd + "\n")
                                sleep(0.5)
                                remote_conn.send("exit \n")
                                tkMessageBox.showinfo('IP route', 'Static VRF IP multicast (RPF) route added.', parent=window)                                
                else:
                    if chk_state_mcast.get() == False:
                        if VRFopt.get() == "" or VRFopt.get() == "VRF":
                            if Metricopt.get() != "" and Metricopt.get() != "Metric":
                                defiproutecmdneg = defiproutecmdneg + " " + Metricopt.get()
                            else:
                                pass
                            if Trackopt.get() != "" and Trackopt.get() != "Track":
                                defiproutecmdneg  = defiproutecmdneg + " track " + Trackopt.get()
                            else:
                                pass
                            if Nameopt.get() != "" and Nameopt.get() != "Name":
                                defiproutecmdneg  = defiproutecmdneg + " name " + Nameopt.get()
                            else:
                                pass
                            if Tagopt.get() != "" and Tagopt.get() != "Tag":
                                defiproutecmdneg  = defiproutecmdneg + " tag " + Tagopt.get()
                            else:
                                pass
                            remote_conn.send("conf t \n")
                            sleep(0.5)
                            remote_conn.send(defipvrfroutecmdneg + "\n")
                            sleep(0.5)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('IP route', 'Static IP route removed.', parent=window)
                        else:
                            if Metricopt.get() != "" and Metricopt.get() != "Metric":
                                defipvrfroutecmdneg = defipvrfroutecmdneg + " " + Metricopt.get()
                            else:
                                pass
                            if Trackopt.get() != "" and Trackopt.get() != "Track":
                                defipvrfroutecmdneg  = defipvrfroutecmdneg + " track " + Trackopt.get()
                            else:
                                pass
                            if Nameopt.get() != "" and Nameopt.get() != "Name":
                                defipvrfroutecmdneg  = defipvrfroutecmdneg + " name " + Nameopt.get()
                            else:
                                pass
                            if Tagopt.get() != "" and Tagopt.get() != "Tag":
                                defipvrfroutecmdneg  = defipvrfroutecmdneg + " tag " + Tagopt.get()
                            else:
                                pass
                            remote_conn.send("conf t \n")
                            sleep(0.5)
                            remote_conn.send(defipvrfroutecmdneg + "\n")
                            sleep(0.5)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('IP route', 'Static IP (VRF) route removed.', parent=window)
           
                    else:
                        if (Trackopt.get() != "Track" and Trackopt.get() != "") or (Nameopt.get() != "Name" and Nameopt.get() != "")\
                           or (Tagopt.get() != "Tag" and Tagopt.get() != ""):
                            tkMessageBox.showinfo('Error', 'Track, name and tags cannot be used with multicast routes.', parent=window)
                        else:                            
                            if VRFopt.get() == "" or VRFopt.get() == "VRF":
                                if Metricopt.get() != "" and Metricopt.get() != "Metric":
                                    defipmroutecmdneg = defipmroutecmdneg + " " + Metricopt.get()
                                else:
                                    pass                                
                                remote_conn.send("conf t\n")
                                sleep(0.5)
                                remote_conn.send(defipmroutecmdneg + "\n")
                                sleep(0.5)
                                remote_conn.send("exit \n")
                                tkMessageBox.showinfo('IP route', 'Static IP multicast (RPF) route removed.', parent=window)
                            else:
                                if Metricopt.get() != "" and Metricopt.get() != "Metric":
                                    defipvrfmroutecmdneg = defipvrfmroutecmdneg + " " + Metricopt.get()
                                else:
                                    pass                                
                                remote_conn.send("conf t\n")
                                sleep(0.5)
                                remote_conn.send(defipvrfmroutecmdneg + "\n")
                                sleep(0.5)
                                remote_conn.send("exit \n")
                                tkMessageBox.showinfo('IP route', 'Static VRF IP multicast (RPF) route removed.', parent=window)                                    
        btn = Button(basicrouteframe, text="Aplicar", bg="orange", command=staticro)
        btn.grid(column=4, row=3)



        
        OSPFframe=LabelFrame(window,text=" OSPF ",font=('verdana', 8, 'bold'),padx=10,pady=2,width=100,height=100)
        OSPFframe.grid(row=1,column=0, sticky=("nsew"))
        
        lbl = Label(OSPFframe, text="Enable PID(+VRF):")    
        lbl.grid(column=0, row=2)
        txtospfpid = Entry(OSPFframe, bg='white', width=15, fg='grey')
        txtospfpid.grid(column=1, row=2)
        txtospfpid.insert(0, "eg. 15(MyVRF)")
        def handle_focus_in(_):
            if txtospfpid.cget('fg') != 'black':
                txtospfpid.delete(0, END)
                txtospfpid.config(fg='black')
        def handle_focus_out(_):
            if txtospfpid.get() == "":
                txtospfpid.delete(0, END)
                txtospfpid.config(fg='grey')
                txtospfpid.insert(0, "eg. 15(MyVRF)")    
        txtospfpid.bind("<FocusOut>", handle_focus_out)
        txtospfpid.bind("<FocusIn>", handle_focus_in)        
        lbl = Label(OSPFframe, text="Advertise network, mask, area:")    
        lbl.grid(column=0, row=3)
        txtospfadv = Entry(OSPFframe,width=15)
        txtospfadv.grid(column=1, row=3)
        txtospfmask = Entry(OSPFframe, bg='white', width=15, fg='grey')
        txtospfmask.grid(column=2, row=3)
        txtospfmask.insert(0, "eg. 0.0.0.255")
        def handle_focus_in(_):
            if txtospfmask.cget('fg') != 'black':
                txtospfmask.delete(0, END)
                txtospfmask.config(fg='black')
        def handle_focus_out(_):
            if txtospfmask.get() == "":
                txtospfmask.delete(0, END)
                txtospfmask.config(fg='grey')
                txtospfmask.insert(0, "eg. 0.0.0.255")    
        txtospfmask.bind("<FocusOut>", handle_focus_out)
        txtospfmask.bind("<FocusIn>", handle_focus_in)


        txtospfarea = Entry(OSPFframe,width=5)
        txtospfarea.grid(column=3, row=3)

        def enospf():
            vrffind = txtospfpid.get()
            vrf = vrffind[vrffind.find("(")+1:vrffind.find(")")]
            osvrfpid = ""
            if "(" in txtospfpid.get():
                osvrfpid = vrffind.split("(",1)[0]
            else:
                pass
            defospfcmd = "router ospf " + txtospfpid.get() + "\n"
            vrfospfcmd = "router ospf " + osvrfpid + " vrf " + vrf + "\n"
            a = txtospfpid.get()
            b = txtospfadv.get()
            c = txtospfmask.get()
            d = txtospfarea.get()
            if (a == '' or a == 'eg. 15(MyVRF)'):
                tkMessageBox.showinfo('Error', 'Please enter a OSPF PID (and VRF if required).', parent=window)
            else:
                if "(" in txtospfpid.get():
                    remote_conn.send("sh ip vrf " + vrf + " \n")
                    sleep(0.2)
                    output = remote_conn.recv(2048).decode("utf-8")
                    sleep(2)
                    stripp = output.strip()
                    sleep(0.2)
                    if "No VRF" in stripp:
                        sleep(0.2)
                        tkMessageBox.showinfo('Error', 'VRF not found.. Please create the VRF first. Aborting.', parent=window)
                        return
                    else:
                        pass
                else:
                    pass
                
                if chk_state_neg.get() == False:
                    if (b == '') and ((c == '') or (c == 'eg. 0.0.0.255')) and (d == ''):
                        remote_conn.send("conf t\n")
                        sleep(0.5)
                        if "(" not in txtospfpid.get():
                            remote_conn.send(defospfcmd)
                        else:
                            remote_conn.send(vrfospfcmd)   
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        res = "OSPF enabled, no networks advertised."
                        tkMessageBox.showinfo('OSPF ' + txtospfpid.get(), res, parent=window)
                    elif (b != '') and ((c != '') or (c != 'eg. 0.0.0.255'))  and (d != ''):
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        if "(" not in txtospfpid.get():
                            remote_conn.send(defospfcmd)
                        else:
                            remote_conn.send(vrfospfcmd)
                        sleep(0.2)
                        remote_conn.send("network  " + txtospfadv.get() + " " + txtospfmask.get() + " area " + txtospfarea.get() + " \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        res = "OSPF enabled, advertised " + txtospfadv.get() + " in area " + txtospfarea.get() + " ."
                        tkMessageBox.showinfo('OSPF ' + txtospfpid.get(), res, parent=window)
                    else:
                        tkMessageBox.showinfo('Error', 'Please enter area, route and mask to advertise; else, leave all 3 blank to enable an OSPF process.', parent=window)                        
                else:  
                    if b == '' and c == ''  and d == '':
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        if "(" not in txtospfpid.get():
                            remote_conn.send("no " + defospfcmd)
                        else:
                            remote_conn.send("no " + vrfospfcmd)
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")        
                        res = "OSPF disabled."
                        tkMessageBox.showinfo('OSPF ' + txtospfpid.get(), res, parent=window)
                    elif (b != '') or (c != '')  or (d != ''):
                        remote_conn.send("conf t\n")
                        sleep(0.5)
                        if "(" not in txtospfpid.get():
                            remote_conn.send(defospfcmd)
                        else:
                            remote_conn.send(vrfospfcmd)
                        sleep(0.2)    
                        remote_conn.send("no network  " + txtospfadv.get() + " " + txtospfmask.get() + " area " + txtospfarea.get() + "\n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        res = "OSPF network " + txtospfadv.get() + " unadvertised from area " + txtospfarea.get() + " ."
                        tkMessageBox.showinfo('OSPF ' + txtospfpid.get(), res, parent=window)
                    else:
                        tkMessageBox.showinfo('Error', 'Please enter area, route and mask to unadvertise; else, leave all 3 blank to disable an OSPF process.', parent=window)
        btn = Button(OSPFframe, text="Enable/Advertise", font=('helvetica', 8), bg="orange", command=enospf)
        btn.grid(column=2, row=2)



        def option_changed_OSPFoptiface(*args):
            if getOSPFoptiface.get() == "Hello timer":
                text = 'eg. 10'
                ospfopt1.delete(0, END)
                ospfopt1.config(fg='grey')
                ospfopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt1.cget('fg') != 'black':
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt1.get() == "":
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='grey')
                        ospfopt1.insert(0, text)
                ospfopt1.bind("<FocusOut>", handle_focus_out)
                ospfopt1.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptiface.get() == "Dead timer":
                text = 'eg. 40'
                ospfopt1.delete(0, END)
                ospfopt1.config(fg='grey')
                ospfopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt1.cget('fg') != 'black':
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt1.get() == "":
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='grey')
                        ospfopt1.insert(0, text)
                ospfopt1.bind("<FocusOut>", handle_focus_out)
                ospfopt1.bind("<FocusIn>", handle_focus_in)                
            elif getOSPFoptiface.get() == "Passive int'face":
                text = 'NoInputRequired'
                ospfopt1.delete(0, END)
                ospfopt1.config(fg='grey')
                ospfopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt1.cget('fg') != 'black':
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt1.get() == "":
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='grey')
                        ospfopt1.insert(0, text)
                ospfopt1.bind("<FocusOut>", handle_focus_out)
                ospfopt1.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptiface.get() == "Cost Metric":
                text = 'eg. 1 (1-65535)'
                ospfopt1.delete(0, END)
                ospfopt1.config(fg='grey')
                ospfopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt1.cget('fg') != 'black':
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt1.get() == "":
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='grey')
                        ospfopt1.insert(0, text)
                ospfopt1.bind("<FocusOut>", handle_focus_out)
                ospfopt1.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptiface.get() == "Link Priority":
                text = 'eg. 1 (0-255)'
                ospfopt1.delete(0, END)
                ospfopt1.config(fg='grey')
                ospfopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt1.cget('fg') != 'black':
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt1.get() == "":
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='grey')
                        ospfopt1.insert(0, text)
                ospfopt1.bind("<FocusOut>", handle_focus_out)
                ospfopt1.bind("<FocusIn>", handle_focus_in)                
            elif getOSPFoptiface.get() == "Network type":
                text = 'eg. broadcast'
                ospfopt1.delete(0, END)
                ospfopt1.config(fg='grey')
                ospfopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt1.cget('fg') != 'black':
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt1.get() == "":
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='grey')
                        ospfopt1.insert(0, text)
                ospfopt1.bind("<FocusOut>", handle_focus_out)
                ospfopt1.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptiface.get() == "Authentication":
                text = '<keyID> <passwd>'
                ospfopt1.delete(0, END)
                ospfopt1.config(fg='grey')
                ospfopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt1.cget('fg') != 'black':
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt1.get() == "":
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='grey')
                        ospfopt1.insert(0, text)
                ospfopt1.bind("<FocusOut>", handle_focus_out)
                ospfopt1.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptiface.get() == "Set Area":
                text = '<AreaID>'
                ospfopt1.delete(0, END)
                ospfopt1.config(fg='grey')
                ospfopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt1.cget('fg') != 'black':
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt1.get() == "":
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='grey')
                        ospfopt1.insert(0, text)
                ospfopt1.bind("<FocusOut>", handle_focus_out)
                ospfopt1.bind("<FocusIn>", handle_focus_in)
            else:
                text = 'NoInputRequired'
                ospfopt1.delete(0, END)
                ospfopt1.config(fg='grey')
                ospfopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt1.cget('fg') != 'black':
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt1.get() == "":
                        ospfopt1.delete(0, END)
                        ospfopt1.config(fg='grey')
                        ospfopt1.insert(0, text)
                ospfopt1.bind("<FocusOut>", handle_focus_out)
                ospfopt1.bind("<FocusIn>", handle_focus_in)
                
        OPTIONS = [
        "Hello timer",
        "Dead timer",
        "Passive int'face",
        "Cost Metric",
        "Link Priority",
        "Network type",
        "Authentication",
        "Set Area",
        "BFD"
        ]
        getOSPFoptiface = StringVar(OSPFframe)
        getOSPFoptiface.set(OPTIONS[0])    # default value
        getOSPFoptiface.trace("w", option_changed_OSPFoptiface)
        dropbox1 = OptionMenu(OSPFframe, getOSPFoptiface, *OPTIONS)   
        dropbox1.grid(column=0, row=5)
        ospfopt1 = Entry(OSPFframe, bg='white', width=21, fg='grey')
        ospfopt1.grid(column=1, row=5, columnspan=2, sticky='w')
        ospfopt1.insert(0, "eg. 10")
        def handle_focus_in(_):
            if ospfopt1.cget('fg') != 'black':
                ospfopt1.delete(0, END)
                ospfopt1.config(fg='black')
        def handle_focus_out(_):
            if ospfopt1.get() == "":
                ospfopt1.delete(0, END)
                ospfopt1.config(fg='grey')
                ospfopt1.insert(0, "eg. 10")    
        ospfopt1.bind("<FocusOut>", handle_focus_out)
        ospfopt1.bind("<FocusIn>", handle_focus_in)

        
        ospfoptiface = Entry(OSPFframe, bg='white', width=8, fg='grey')
        ospfoptiface.grid(column=2, row=5, sticky='e')
        ospfoptiface.insert(0, "eg. fa0/0")
        def handle_focus_in(_):
            if ospfoptiface.cget('fg') != 'black':
                ospfoptiface.delete(0, END)
                ospfoptiface.config(fg='black')
        def handle_focus_out(_):
            if ospfoptiface.get() == "":
                ospfoptiface.delete(0, END)
                ospfoptiface.config(fg='grey')
                ospfoptiface.insert(0, "eg. fa0/0")    
        ospfoptiface.bind("<FocusOut>", handle_focus_out)
        ospfoptiface.bind("<FocusIn>", handle_focus_in)        
        def ospfifaceopt():
            vrffind = txtospfpid.get()
            vrf = vrffind[vrffind.find("(")+1:vrffind.find(")")]
            osvrfpid = ""
            if "(" in txtospfpid.get():
                osvrfpid = vrffind.split("(",1)[0]
            else:
                pass
            defospfcmd = "router ospf " + txtospfpid.get() + "\n"
            vrfospfcmd = "router ospf " + osvrfpid + " vrf " + vrf + "\n"

            if ospfoptiface.get() == "" or ospfoptiface.get() == "eg. fa0/0":
                tkMessageBox.showinfo('Error', 'Please enter an interface first.', parent=window)
            else:
                remote_conn.send("conf t \n")
                sleep(0.2)
                if chk_state_neg.get() == False:
                    if getOSPFoptiface.get() == "Hello timer":                        
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("ip ospf hello-int " + ospfopt1.get() + " \n")
                        tkMessageBox.showinfo('OSPF Hello', 'Timer set.', parent=window)
                    elif getOSPFoptiface.get() == "Dead timer":
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("ip ospf dead-int " + ospfopt1.get() + " \n")
                        tkMessageBox.showinfo('OSPF Dead', 'Timer set.', parent=window)
                    elif getOSPFoptiface.get() == "Passive int'face":
                        if txtospfpid.get() == "" or txtospfpid.get() == "eg. 15(MyVRF)":
                            tkMessageBox.showinfo('Error', 'Please also enter the OSPF process ID above.', parent=window)
                        else:
                            if "(" not in txtospfpid.get():
                                remote_conn.send(defospfcmd)
                            else:
                                remote_conn.send(vrfospfcmd)                    
                            sleep(0.2)
                            remote_conn.send("passive-int " + ospfoptiface.get() + " \n")
                            tkMessageBox.showinfo('OSPF Passive', 'OSPF process disabled for interface ' + ospfoptiface.get() + '.', parent=window)
                    elif getOSPFoptiface.get() == "Cost Metric":
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("ip ospf cost " + ospfopt1.get() + " \n")
                        tkMessageBox.showinfo('OSPF Cost', 'OSPF cost modified.', parent=window)
                    elif getOSPFoptiface.get() == "Link Priority":
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("ip ospf prio " + ospfopt1.get() + " \n")
                        tkMessageBox.showinfo('OSPF Priority', 'OSPF priority modified.', parent=window)
                    elif getOSPFoptiface.get() == "Network type":
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)
                        remote_conn.send("ip ospf network " + ospfopt1.get() + " \n")
                        tkMessageBox.showinfo('OSPF Network type', 'OSPF network type modified.', parent=window)
                    elif getOSPFoptiface.get() == "Authentication":
                        option = ospfopt1.get()
                        keynum = int(re.search(r'\d+', option).group())
                        md5str = option.split(" ",1)[1]
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)
                        remote_conn.send("ip ospf message-digest-key " + keynum + " md5 " + md5str + " \n")
                        sleep(0.2)
                        remote_conn.send("ip ospf authentication message-digest \n")                
                        tkMessageBox.showinfo('OSPF Authentication', 'OSPF md5 authentication enabled. REMEMBER to create the keychain.', parent=window)
                    elif getOSPFoptiface.get() == "Set Area":
                        if txtospfpid.get() == "" or txtospfpid.get() == "eg. 15(MyVRF)" or txtospfarea.get() == "" or ("(" in txtospfpid.get()):
                            tkMessageBox.showinfo('Error', 'Please also enter both the OSPF process ID (non-VRF only) and area above.', parent=window)
                        else:
                            remote_conn.send("int " + ospfoptiface.get() + " \n")
                            sleep(0.2)
                            remote_conn.send("ip ospf " + txtospfpid.get() + " area " + txtospfarea.get() + " \n")
                            tkMessageBox.showinfo('OSPF Area', 'This interface has been put into area ' + txtospfarea.get() + '.', parent=window)
                    else:
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("ip ospf bfd \n")
                        tkMessageBox.showinfo('BFD', 'BFD configured for this interface.', parent=window)
                else:
                    if getOSPFoptiface.get() == "Hello timer":                        
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("no ip ospf hello-int " + ospfopt1.get() + " \n")
                        tkMessageBox.showinfo('OSPF Hello', 'Timer reset.', parent=window)
                    elif getOSPFoptiface.get() == "Dead timer":
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("no ip ospf dead-int " + ospfopt1.get() + " \n")
                        tkMessageBox.showinfo('OSPF Dead', 'Timer reset.', parent=window)
                    elif getOSPFoptiface.get() == "Passive int'face":
                        if txtospfpid.get() == "" or txtospfpid.get() == "eg. 15(MyVRF)":
                            tkMessageBox.showinfo('Error', 'Please also enter the OSPF process ID above.', parent=window)
                        else:
                            if "(" not in txtospfpid.get():
                                remote_conn.send(defospfcmd)
                            else:
                                remote_conn.send(vrfospfcmd)                    
                            sleep(0.2)
                            remote_conn.send("no passive-int " + ospfoptiface.get() + " \n")
                            tkMessageBox.showinfo('OSPF Passive', 'OSPF process enabled for interface ' + ospfoptiface.get() + '.', parent=window)
                    elif getOSPFoptiface.get() == "Cost Metric":
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("no ip ospf cost " + ospfopt1.get() + " \n")
                        tkMessageBox.showinfo('OSPF Cost', 'OSPF cost reset.', parent=window)
                    elif getOSPFoptiface.get() == "Link Priority":
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("no ip ospf prio " + ospfopt1.get() + " \n")
                        tkMessageBox.showinfo('OSPF Priority', 'OSPF priority reset.', parent=window)
                    elif getOSPFoptiface.get() == "Network type":
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)
                        remote_conn.send("no ip ospf network " + ospfopt1.get() + " \n")
                        tkMessageBox.showinfo('OSPF Network type', 'OSPF network type reset.', parent=window)
                    elif getOSPFoptiface.get() == "Authentication":
                        option = ospfopt1.get()
                        keynum = int(re.search(r'\d+', option).group())
                        md5str = option.split(" ",1)[1]
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)
                        remote_conn.send("ip ospf authentication null \n")                
                        tkMessageBox.showinfo('OSPF Authentication', 'OSPF md5 authentication enabled. REMEMBER to create the keychain.', parent=window)
                    elif getOSPFoptiface.get() == "Set Area":
                        if txtospfpid.get() == "" or txtospfpid.get() == "eg. 15(MyVRF)" or txtospfarea.get() == "" or ("(" in txtospfpid.get()):
                            tkMessageBox.showinfo('Error', 'Please also enter both the OSPF process ID (non-VRF only) and area above.', parent=window)
                        else:
                            remote_conn.send("int " + ospfoptiface.get() + " \n")
                            sleep(0.2)
                            remote_conn.send("no ip ospf " + txtospfpid.get() + " area " + txtospfarea.get() + " \n")
                            tkMessageBox.showinfo('OSPF Area', 'Interface ' + ospfoptiface.get() + ' has been removed from area ' + txtospfarea.get() + '.', parent=window)
                    else:
                        remote_conn.send("int " + ospfoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("ip ospf bfd disable \n")
                        tkMessageBox.showinfo('BFD', 'BFD configured for this interface.', parent=window)
                sleep(0.2)
                remote_conn.send("exit \n")
                sleep(0.2)
                remote_conn.send("exit \n")
        btn = Button(OSPFframe, text="Aplicar", bg="orange", command=ospfifaceopt)
        btn.grid(column=4, row=5)

        def option_changed_getOSPFoptdevice(*args):
            if getOSPFoptdevice.get() == "Router-ID":
                text = 'eg. 1.1.1.1'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptdevice.get() == "Static neighbor":
                text = '<Neigh_IP>'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)                
            elif getOSPFoptdevice.get() == "Propagate * route":
                text = '[always][metric{-type} <>][route-m <>]'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptdevice.get() == "Stub type":
                text = '[Stub | Total-Stub | NSSA | Total-NSSA]'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptdevice.get() == "Virt link":
                text = '<remote_Router-ID>'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptdevice.get() == "Max paths":
                text = 'eg. 4'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptdevice.get() == "Area auth":
                text = 'NoInputRequired'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptdevice.get() == "Cost reference":
                text = 'eg. 100, 1000, 10000'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptdevice.get() == "AD(all, per rte)":
                text = '<1-255> [<network> <wcard> [<ACL>]]'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptdevice.get() == "AD(area type)":
                text = '[intra <1-255>] [inter <1-255>][ext <1-255>]'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptdevice.get() == "Inter-area filter":
                text = '<pfxlistname> + in/out'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)
            elif getOSPFoptdevice.get() == "Intra-area filter":
                text = '<pfxlistname> + in/out [<interface>]'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)
            else:
                text = '<net> <mask> [tag <> | not-adv]'
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if ospfopt2.cget('fg') != 'black':
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='black')
                def handle_focus_out(_):
                    if ospfopt2.get() == "":
                        ospfopt2.delete(0, END)
                        ospfopt2.config(fg='grey')
                        ospfopt2.insert(0, text)
                ospfopt2.bind("<FocusOut>", handle_focus_out)
                ospfopt2.bind("<FocusIn>", handle_focus_in)

                
        OPTIONS = [
        "Router-ID",
        "Static neighbor",
        "Propagate * route",
        "Stub type",
        "Virt link",
        "Max paths",
        "Area auth",
        "Cost reference",
        "AD(all, per rte)",
        "AD(area type)",
        "Inter-area filter",
        "Intra-area filter",
        "Summary route"
        ]
        getOSPFoptdevice = StringVar(OSPFframe)
        getOSPFoptdevice.set(OPTIONS[0])    # default value
        getOSPFoptdevice.trace("w", option_changed_getOSPFoptdevice)
        dropbox2 = OptionMenu(OSPFframe, getOSPFoptdevice, *OPTIONS)   
        dropbox2.grid(column=0, row=6)
        ospfopt2 = Entry(OSPFframe, bg='white', width=35, fg='grey')
        ospfopt2.grid(column=1, row=6, columnspan=3, sticky='w')
        ospfopt2.insert(0, "eg. 1.1.1.1")
        def handle_focus_in(_):
            if ospfopt2.cget('fg') != 'black':
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='black')
        def handle_focus_out(_):
            if ospfopt2.get() == "":
                ospfopt2.delete(0, END)
                ospfopt2.config(fg='grey')
                ospfopt2.insert(0, "eg. 1.1.1.1")    
        ospfopt2.bind("<FocusOut>", handle_focus_out)
        ospfopt2.bind("<FocusIn>", handle_focus_in)
        
        def ospfotheropt():
            vrffind = txtospfpid.get()
            vrf = vrffind[vrffind.find("(")+1:vrffind.find(")")]
            osvrfpid = ""
            if "(" in txtospfpid.get():
                osvrfpid = vrffind.split("(",1)[0]
            else:
                pass
            defospfcmd = "router ospf " + txtospfpid.get() + "\n"
            vrfospfcmd = "router ospf " + osvrfpid + " vrf " + vrf + "\n"                
            if txtospfpid.get() == "" or txtospfpid.get() == "eg. 15(MyVRF)":
                tkMessageBox.showinfo('Error', 'Please also enter the OSPF process ID above.', parent=window)
            else:
                remote_conn.send("conf t \n")
                sleep(0.2)                
                if "(" not in txtospfpid.get():
                    remote_conn.send(defospfcmd)
                else:
                    remote_conn.send(vrfospfcmd)                    
                sleep(0.2)
                if chk_state_neg.get() == False:                
                    if getOSPFoptdevice.get() == "Router-ID":
                        remote_conn.send("router-id " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'Rotuer-id has been set.', parent=window)
                    elif getOSPFoptdevice.get() == "Static neighbor":
                        remote_conn.send("neighbor " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'Static neighbor has been set.', parent=window)
                    elif getOSPFoptdevice.get() == "Propagate * route":
                        remote_conn.send("default-information originate " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'Default route has been propagated.', parent=window)
                    elif getOSPFoptdevice.get() == "Stub type":
                        if txtospfarea.get() == "":
                            tkMessageBox.showinfo('Error', 'Please also enter an OSPF area above.', parent=window)
                        else:
                            if ospfopt2.get() == "Stub":
                                remote_conn.send("area " + txtospfarea.get() + " stub \n")
                                tkMessageBox.showinfo('OSPF', 'Area ' + txtospfarea.get() + ' changed to stub area.', parent=window)
                            elif ospfopt2.get() == "Total-Stub":
                                remote_conn.send("area " + txtospfarea.get() + " stub no-summ \n")
                                tkMessageBox.showinfo('OSPF', 'Area ' + txtospfarea.get() + ' changed to Total-stub area.', parent=window)
                            elif ospfopt2.get() == "NSSA":
                                remote_conn.send("area " + txtospfarea.get() + " nssa \n")
                                tkMessageBox.showinfo('OSPF', 'Area ' + txtospfarea.get() + ' changed to NSSA area.', parent=window)
                            elif ospfopt2.get() == "Total-NSSA":
                                remote_conn.send("area " + txtospfarea.get() + " nssa no-summ \n")
                                tkMessageBox.showinfo('OSPF', 'Area ' + txtospfarea.get() + ' changed to Total-NSSA area.', parent=window)
                            else:
                                tkMessageBox.showinfo('Error', 'Please enter ONE stub type to configure the area.', parent=window)
                    elif getOSPFoptdevice.get() == "Virt link":
                        if txtospfarea.get() == "":
                            tkMessageBox.showinfo('Error', 'Please also enter an OSPF area above.', parent=window)
                        else:
                            remote_conn.send("area " + txtospfarea.get() + " virtual-l " + ospfopt2.get() + " \n")
                            tkMessageBox.showinfo('OSPF', 'Virtual link has been configured. NOTE: If this area is already a stub area, will not work.', parent=window)
                    elif getOSPFoptdevice.get() == "Max paths":
                        remote_conn.send("maximum-paths " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF maximum paths configured.', parent=window)
                    elif getOSPFoptdevice.get() == "Area auth":
                        if txtospfarea.get() == "":
                            tkMessageBox.showinfo('Error', 'Please also enter an OSPF area above.', parent=window)
                        else:
                            remote_conn.send("area " + txtospfarea.get() + " authen message-d \n")
                            tkMessageBox.showinfo('OSPF', 'OSPF authentication configured. NOTE: you still need to configure the interface authentication cmd.', parent=window)
                    elif getOSPFoptdevice.get() == "Cost reference":
                        remote_conn.send("auto-cost reference-bandw " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF reference bandwidth modified.', parent=window)
                    elif getOSPFoptdevice.get() == "AD(all, per rte)":
                        remote_conn.send("distance " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF administrative distance modified.', parent=window)
                    elif getOSPFoptdevice.get() == "AD(area type)":
                        remote_conn.send("distance ospf " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF administrative distance modified.', parent=window)
                    elif getOSPFoptdevice.get() == "Inter-area filter":
                        if txtospfarea.get() == "":
                            tkMessageBox.showinfo('Error', 'Please also enter an OSPF area above.', parent=window)
                        else:
                            remote_conn.send("area " + txtospfarea.get() + " filter-list prefix " + ospfopt2.get() + " \n")
                            tkMessageBox.showinfo('OSPF', 'OSPF inter-area filter configured.', parent=window)
                    elif getOSPFoptdevice.get() == "Intra-area filter":
                        remote_conn.send("distribute-list prefix " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF intra-area filter configured.', parent=window)
                    else:
                        remote_conn.send("summary-address " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF aggregate address configured.', parent=window)
                else:
                    if getOSPFoptdevice.get() == "Router-ID":
                        remote_conn.send("no router-id " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'Router-id has been removed.', parent=window)
                    elif getOSPFoptdevice.get() == "Static neighbor":
                        remote_conn.send("no neighbor " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'Static neighbor has been removed.', parent=window)
                    elif getOSPFoptdevice.get() == "Propagate * route":
                        remote_conn.send("no default-information originate " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'Default route has been removed.', parent=window)
                    elif getOSPFoptdevice.get() == "Stub area":
                        if txtospfarea.get() == "":
                            tkMessageBox.showinfo('Error', 'Please also enter an OSPF area above.', parent=window)
                        else:
                            remote_conn.send("no area " + txtospfarea.get() + " stub " + ospfopt2.get() + " \n")
                            tkMessageBox.showinfo('OSPF', 'Area ' + txtospfarea.get() + ' no longer stub area.', parent=window)
                    elif getOSPFoptdevice.get() == "Virt link":
                        if txtospfarea.get() == "":
                            tkMessageBox.showinfo('Error', 'Please also enter an OSPF area above.', parent=window)
                        else:
                            remote_conn.send("no area " + txtospfarea.get() + " virtual-l " + ospfopt2.get() + " \n")
                            tkMessageBox.showinfo('OSPF', 'Virtual link has been removed.', parent=window)
                    elif getOSPFoptdevice.get() == "Max paths":
                        remote_conn.send("no maximum-paths " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF maximum paths reset.', parent=window)
                    elif getOSPFoptdevice.get() == "Area auth":
                        if txtospfarea.get() == "":
                            tkMessageBox.showinfo('Error', 'Please also enter an OSPF area above.', parent=window)
                        else:
                            remote_conn.send("no area " + txtospfarea.get() + " authen message-d " + ospfopt2.get() + " \n")
                            tkMessageBox.showinfo('OSPF', 'OSPF authentication removed.', parent=window)
                    elif getOSPFoptdevice.get() == "Cost reference":
                        remote_conn.send("no auto-cost reference-bandw " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF reference bandwidth reset.', parent=window)
                    elif getOSPFoptdevice.get() == "AD(all, per rte)":
                        remote_conn.send("no distance " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF administrative distance reset.', parent=window)
                    elif getOSPFoptdevice.get() == "AD(area type)":
                        remote_conn.send("no distance ospf " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF administrative distance reset.', parent=window)
                    elif getOSPFoptdevice.get() == "Inter-area filter":
                        if txtospfarea.get() == "":
                            tkMessageBox.showinfo('Error', 'Please also enter an OSPF area above.', parent=window)
                        else:
                            remote_conn.send("no area " + txtospfarea.get() + " filter-list prefix " + ospfopt2.get() + " \n")
                            tkMessageBox.showinfo('OSPF', 'OSPF inter-area filter removed.', parent=window)
                    elif getOSPFoptdevice.get() == "Intra-area filter":
                        remote_conn.send("no distribute-list prefix " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF intra-area filter removed.', parent=window)
                    else:
                        remote_conn.send("no summary-address " + ospfopt2.get() + " \n")
                        tkMessageBox.showinfo('OSPF', 'OSPF aggregate address removed.', parent=window)                    
            sleep(0.2)
            remote_conn.send("exit \n")
            sleep(0.2)
            remote_conn.send("exit \n")
        btn = Button(OSPFframe, text="Aplicar", bg="orange", command=ospfotheropt)
        btn.grid(column=4, row=6)




        OPTIONS = [
        "RIP",
        "OSPF",
        "EIGRP",
        "BGP"
        ]
        getOSPFoptredist = StringVar(OSPFframe)
        getOSPFoptredist.set(OPTIONS[0])    # default value
        dropbox2 = OptionMenu(OSPFframe, getOSPFoptredist, *OPTIONS)   
        dropbox2.grid(column=0, row=7)
        
        ospfredisttoprocnum = Entry(OSPFframe, bg='white', width=13, fg='grey')
        ospfredisttoprocnum.place(x=166, y=115)
        ospfredisttoprocnum.insert(0, "eg. 15(MyVRF)")
        def handle_focus_in(_):
            if ospfredisttoprocnum.cget('fg') != 'black':
                ospfredisttoprocnum.delete(0, END)
                ospfredisttoprocnum.config(fg='black')
        def handle_focus_out(_):
            if ospfredisttoprocnum.get() == "":
                ospfredisttoprocnum.delete(0, END)
                ospfredisttoprocnum.config(fg='grey')
                ospfredisttoprocnum.insert(0, "eg. 15(MyVRF)")    
        ospfredisttoprocnum.bind("<FocusOut>", handle_focus_out)
        ospfredisttoprocnum.bind("<FocusIn>", handle_focus_in)
        
        ospfredistFilter = Entry(OSPFframe, bg='white', width=6, fg='grey')
        ospfredistFilter.place(x=260, y=115)
        ospfredistFilter.insert(0, "r-map")
        def handle_focus_in(_):
            if ospfredistFilter.cget('fg') != 'black':
                ospfredistFilter.delete(0, END)
                ospfredistFilter.config(fg='black')
        def handle_focus_out(_):
            if ospfredistFilter.get() == "":
                ospfredistFilter.delete(0, END)
                ospfredistFilter.config(fg='grey')
                ospfredistFilter.insert(0, "r-map")    
        ospfredistFilter.bind("<FocusOut>", handle_focus_out)
        ospfredistFilter.bind("<FocusIn>", handle_focus_in)
        
        ospfredistMetric = Entry(OSPFframe, bg='white', width=6, fg='grey')
        ospfredistMetric.place(x=304, y=115)
        ospfredistMetric.insert(0, "Metric")
        def handle_focus_in(_):
            if ospfredistMetric.cget('fg') != 'black':
                ospfredistMetric.delete(0, END)
                ospfredistMetric.config(fg='black')
        def handle_focus_out(_):
            if ospfredistMetric.get() == "":
                ospfredistMetric.delete(0, END)
                ospfredistMetric.config(fg='grey')
                ospfredistMetric.insert(0, "Metric")    
        ospfredistMetric.bind("<FocusOut>", handle_focus_out)
        ospfredistMetric.bind("<FocusIn>", handle_focus_in)

        ospfredistTag = Entry(OSPFframe, bg='white', width=5, fg='grey')
        ospfredistTag.place(x=350, y=115)
        ospfredistTag.insert(0, "Tag")
        def handle_focus_in(_):
            if ospfredistTag.cget('fg') != 'black':
                ospfredistTag.delete(0, END)
                ospfredistTag.config(fg='black')
        def handle_focus_out(_):
            if ospfredistTag.get() == "":
                ospfredistTag.delete(0, END)
                ospfredistTag.config(fg='grey')
                ospfredistTag.insert(0, "Tag")    
        ospfredistTag.bind("<FocusOut>", handle_focus_out)
        ospfredistTag.bind("<FocusIn>", handle_focus_in)
        
        def ospfredistribute():
            vrffind = txtospfpid.get()
            vrf = vrffind[vrffind.find("(")+1:vrffind.find(")")]
            osvrfpid = ""
            if "(" in txtospfpid.get():
                osvrfpid = vrffind.split("(",1)[0]
            else:
                pass
            defospfcmd = "router ospf " + txtospfpid.get() + "\n"
            vrfospfcmd = "router ospf " + osvrfpid + " vrf " + vrf + "\n"
            
            vrffind2 = ospfredisttoprocnum.get()                        #find (PID+vrf) learned protocol
            PIDextract = re.search(r'\d+', vrffind2).group()            #filter PID from learned protocol
            vrf2 = vrffind2[vrffind2.find("(")+1:vrffind2.find(")")]    #filter vrf from learned protocol
            redistcmd = "redistribute " + getOSPFoptredist.get() + " " + PIDextract + " subnets "
            redistRIPcmd = "redistribute " + getOSPFoptredist.get() + " subnets "
            redistospfvrfcmd = "redistribute " + getOSPFoptredist.get() + " " + PIDextract + " vrf " + vrf2 + " subnets "
            
            if chk_state_neg.get() == False:
                if txtospfpid.get() == "" or txtospfpid.get() == "eg. 15(MyVRF)":
                        tkMessageBox.showinfo('Error', 'Please also enter the OSPF process ID above.', parent=window)
                else:
                    if getOSPFoptredist.get() == "RIP":
                        remote_conn.send("conf t \n")
                        sleep(0.2)                        
                        if "(" not in txtospfpid.get():
                            remote_conn.send(defospfcmd)
                        else:
                            remote_conn.send(vrfospfcmd)

                        cmd = redistRIPcmd

                        if ospfredistFilter.get() != "" and ospfredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + ospfredistFilter.get()
                        else:
                            pass
                        if ospfredistMetric.get() != "" and ospfredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + ospfredistMetric.get()
                        else:
                            pass
                        if ospfredistTag.get() != "" and ospfredistTag.get() != "Tag":
                            cmd = cmd + " tag " + ospfredistTag.get()
                        else:
                            pass
                        remote_conn.send(cmd + "\n")
                        sleep(0.3)
                        tkMessageBox.showinfo('OSPF redistribution', 'Learned ' + getOSPFoptredist.get() + '.', parent=window)

                    elif getOSPFoptredist.get() == "EIGRP" or getOSPFoptredist.get() == "BGP":
                        remote_conn.send("conf t \n")
                        sleep(0.2)                        
                        if "(" not in txtospfpid.get():
                            remote_conn.send(defospfcmd)
                        else:
                            remote_conn.send(vrfospfcmd)

                        cmd = redistcmd
                            
                        if ospfredistFilter.get() != "" and ospfredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + ospfredistFilter.get()
                        else:
                            pass
                        if ospfredistMetric.get() != "" and ospfredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + ospfredistMetric.get()
                        else:
                            pass
                        if ospfredistTag.get() != "" and ospfredistTag.get() != "Tag":
                            cmd = cmd + " tag " + ospfredistTag.get()
                        else:
                            pass
                        remote_conn.send(cmd + "\n")
                        sleep(0.2)
                        tkMessageBox.showinfo('OSPF redistribution', 'Learned ' + getOSPFoptredist.get() + '.', parent=window)

                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.2)                        
                        if "(" not in txtospfpid.get():
                            remote_conn.send(defospfcmd)
                        else:
                            remote_conn.send(vrfospfcmd)
                            
                        if "(" not in ospfredisttoprocnum.get():
                            cmd = redistcmd
                        else:
                            cmd = redistospfvrfcmd
                            
                        if ospfredistFilter.get() != "" and ospfredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + ospfredistFilter.get()
                        else:
                            pass
                        if ospfredistMetric.get() != "" and ospfredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + ospfredistMetric.get()
                        else:
                            pass
                        if ospfredistTag.get() != "" and ospfredistTag.get() != "Tag":
                            cmd = cmd + " tag " + ospfredistTag.get()
                        else:
                            pass
                        remote_conn.send(cmd + "\n")
                        sleep(0.2)
                        tkMessageBox.showinfo('OSPF redistribution', 'Learned ' + getOSPFoptredist.get() + '.', parent=window)
            else:
                if txtospfpid.get() == "" or txtospfpid.get() == "eg. 15(MyVRF)":
                        tkMessageBox.showinfo('Error', 'Please also enter the OSPF process ID above.', parent=window)
                else:
                    if getOSPFoptredist.get() == "RIP":
                        remote_conn.send("conf t \n")
                        sleep(0.2)                        
                        if "(" not in txtospfpid.get():
                            remote_conn.send(defospfcmd)
                        else:
                            remote_conn.send(vrfospfcmd)

                        cmd = redistRIPcmd
                        
                        if ospfredistFilter.get() != "" and ospfredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + ospfredistFilter.get()
                        else:
                            pass
                        if ospfredistMetric.get() != "" and ospfredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + ospfredistMetric.get()
                        else:
                            pass
                        if ospfredistTag.get() != "" and ospfredistTag.get() != "Tag":
                            cmd = cmd + " tag " + ospfredistTag.get()
                        else:
                            pass
                        remote_conn.send("no " + cmd + " \n")
                        sleep(0.2)
                        tkMessageBox.showinfo('OSPF redistribution', 'Unlearned ' + getOSPFoptredist.get() + '.', parent=window)
                    elif getOSPFoptredist.get() == "EIGRP" or getOSPFoptredist.get() == "BGP":
                        remote_conn.send("conf t \n")
                        sleep(0.2)                        
                        if "(" not in txtospfpid.get():
                            remote_conn.send(defospfcmd)
                        else:
                            remote_conn.send(vrfospfcmd)
                        
                        cmd = redistcmd
                        
                        if ospfredistFilter.get() != "" and ospfredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + ospfredistFilter.get()
                        else:
                            pass
                        if ospfredistMetric.get() != "" and ospfredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + ospfredistMetric.get()
                        else:
                            pass
                        if ospfredistTag.get() != "" and ospfredistTag.get() != "Tag":
                            cmd = cmd + " tag " + ospfredistTag.get()
                        else:
                            pass
                        remote_conn.send("no " + cmd + " \n")
                        sleep(0.2)
                        tkMessageBox.showinfo('OSPF redistribution', 'Unlearned ' + getOSPFoptredist.get() + '.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.2)                        
                        if "(" not in txtospfpid.get():
                            remote_conn.send(defospfcmd)
                        else:
                            remote_conn.send(vrfospfcmd)
                        if "(" not in ospfredisttoprocnum.get():
                            cmd = redistcmd
                        else:
                            cmd = redistospfvrfcmd
                        if ospfredistFilter.get() != "" and ospfredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + ospfredistFilter.get()
                        else:
                            pass
                        if ospfredistMetric.get() != "" and ospfredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + ospfredistMetric.get()
                        else:
                            pass
                        if ospfredistTag.get() != "" and ospfredistTag.get() != "Tag":
                            cmd = cmd + " tag " + ospfredistTag.get()
                        else:
                            pass
                        remote_conn.send("no " + cmd + "\n")
                        sleep(0.2)
                        tkMessageBox.showinfo('OSPF redistribution', 'Unlearned ' + getOSPFoptredist.get() + '.', parent=window)
            sleep(0.2)
            remote_conn.send("exit \n")
            sleep(0.2)
            remote_conn.send("exit \n")            
        btn = Button(OSPFframe, text="Learn", bg="orange", command=ospfredistribute)
        btn.grid(column=4, row=7)




        EIGRPframe=LabelFrame(window,text=" EIGRP ",font=('verdana', 8, 'bold'),padx=10,pady=2,width=100,height=100)
        EIGRPframe.grid(row=2,column=0, sticky=("nsew"))

        lbl = Label(EIGRPframe, text="Enable PID(+VRF)+AS:")    
        lbl.grid(column=0, row=6)
        txteigrppid = Entry(EIGRPframe, bg='white', width=16, fg='grey')
        txteigrppid.grid(column=1, row=6)
        txteigrppid.insert(0, "eg. 15(MyVRF)AS1")
        def handle_focus_in(_):
            if txteigrppid.cget('fg') != 'black':
                txteigrppid.delete(0, END)
                txteigrppid.config(fg='black')
        def handle_focus_out(_):
            if txteigrppid.get() == "":
                txteigrppid.delete(0, END)
                txteigrppid.config(fg='grey')
                txteigrppid.insert(0, "eg. 15(MyVRF)AS1")
        txteigrppid.bind("<FocusOut>", handle_focus_out)
        txteigrppid.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(EIGRPframe, text="Advertise network, mask:")    
        lbl.grid(column=0, row=7)
        txteigrpadv = Entry(EIGRPframe,width=15)
        txteigrpadv.grid(column=1, row=7)
        txteigrpmask = Entry(EIGRPframe, bg='white', width=15, fg='grey')
        txteigrpmask.grid(column=2, row=7)
        txteigrpmask.insert(0, "eg. 0.0.0.255")
        def handle_focus_in(_):
            if txteigrpmask.cget('fg') != 'black':
                txteigrpmask.delete(0, END)
                txteigrpmask.config(fg='black')
        def handle_focus_out(_):
            if txteigrpmask.get() == "":
                txteigrpmask.delete(0, END)
                txteigrpmask.config(fg='grey')
                txteigrpmask.insert(0, "eg. 0.0.0.255")    
        txteigrpmask.bind("<FocusOut>", handle_focus_out)
        txteigrpmask.bind("<FocusIn>", handle_focus_in)



        def eneigrp():
            d = txteigrppid.get()
            e = txteigrpadv.get()
            f = txteigrpmask.get()

            if (d == '' or d == 'eg. 15(MyVRF)AS1'):
                tkMessageBox.showinfo('Error', 'Please enter minimum required information (EIGRP PID).', parent=window)
            elif ("(" in d) and ("AS" not in d):
                tkMessageBox.showinfo('Error', 'Please enter both the EIGRP PID VRF and AS number.', parent=window)
            elif ("AS" in d) and ("(" not in d):
                tkMessageBox.showinfo('Error', 'Please enter both the EIGRP PID VRF and AS number.', parent=window)
            else:
                vrffind = txteigrppid.get()
                eivrf = vrffind[vrffind.find("(")+1:vrffind.find(")")]
                eivrfpid = ""
                EiAS = ""
                
                if "AS" in txteigrppid.get():
                    remote_conn.send("sh ip vrf " + eivrf + " \n")
                    print (eivrf)
                    sleep(0.2)
                    output = remote_conn.recv(2048).decode("utf-8")
                    sleep(2)
                    stripp = output.strip()
                    sleep(0.2)
                    if "No VRF" in stripp:
                        sleep(0.2)
                        tkMessageBox.showinfo('Error', 'VRF not found.. Please create the VRF first. Aborting.', parent=window)
                        return
                    else:
                        pass
                
                    eivrfpid = vrffind.split("(",1)[0]
                    EiAS = vrffind.split("AS",1)[1]
                else:
                    pass
                
                defeigrpcmd = "router eigrp " + txteigrppid.get() + "\n"
                vrfeigrpcmd = "router eigrp " + eivrfpid + " \n " + "address-f ipv4 vrf " + eivrf + " \n " + "autonom " + EiAS + "\n"
            
                if chk_state_neg.get() == False:
                    if (e == '') and ((f == '') or (f == 'eg. 0.0.0.255')):
                        remote_conn.send("conf t\n")
                        sleep(0.5)
                        if "(" not in txteigrppid.get():
                            remote_conn.send(defeigrpcmd)
                        else:
                            remote_conn.send(vrfeigrpcmd)
                        sleep(0.5)
                        remote_conn.send("exit \n")
                        sleep(0.5)
                        remote_conn.send("exit \n")
                        if "(" in txteigrppid.get():
                            sleep(0.2)
                            remote_conn.send("exit \n")
                        else:
                            pass
                        res = "EIGRP enabled, proc id: " + txteigrppid.get() + ", no networks advertised."
                        tkMessageBox.showinfo('EIGRP ' + txteigrppid.get(), res, parent=window)
                    elif (e == '') or (f == '') or (f == 'eg. 0.0.0.255'):
                        tkMessageBox.showinfo('Error', 'Please enter both route and mask to advertise.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.5)
                        if "(" not in txteigrppid.get():
                            remote_conn.send(defeigrpcmd)
                        else:
                            remote_conn.send(vrfeigrpcmd)
                        sleep(0.5)
                        remote_conn.send("network  " + txteigrpadv.get() + " " + txteigrpmask.get() + "\n")
                        sleep(0.5)
                        remote_conn.send("exit \n")
                        sleep(0.5)
                        remote_conn.send("exit \n")
                        res = "EIGRP enabled, proc id: " + txteigrppid.get() + ", advertised " + txteigrpadv.get() + "."
                        if "(" in txteigrppid.get():
                            sleep(0.2)
                            remote_conn.send("exit \n")
                        else:
                            pass
                        tkMessageBox.showinfo('EIGRP ' + txteigrppid.get(), res, parent=window)

                else:  
                    if (e == '') and ((f == '') or (f == 'eg. 0.0.0.255')):
                        remote_conn.send("conf t\n")
                        sleep(0.5)
                        if "(" not in txteigrppid.get():
                            remote_conn.send("no " + defeigrpcmd)
                        else:
                            remote_conn.send("no router eigrp " + eivrfpid)
                        sleep(0.5)
                        remote_conn.send("exit \n")
                        sleep(0.5)
                        remote_conn.send("exit \n")
                        res = "EIGRP disabled, proc id: " + txteigrppid.get() + "."
                        tkMessageBox.showinfo('EIGRP ' + txteigrppid.get(), res, parent=window)
                    elif (e == '') or (f == '') or (f == 'eg. 0.0.0.255'):
                        tkMessageBox.showinfo('Error', 'Please enter both route and mask to unadvertise.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.5)
                        if "(" not in txteigrppid.get():
                            remote_conn.send(defeigrpcmd)
                        else:
                            remote_conn.send(vrfeigrpcmd)                    
                        remote_conn.send("no network  " + txteigrpadv.get() + " " + txteigrpmask.get() + "\n")
                        sleep(0.5)
                        remote_conn.send("exit \n")
                        sleep(0.5)
                        remote_conn.send("exit \n")
                        res = "EIGRP network " + txteigrpadv.get() + " unadvertised."
                        tkMessageBox.showinfo('EIGRP ' + txteigrppid.get(), res, parent=window)
                        if "(" in txteigrppid.get():
                            sleep(0.2)
                            remote_conn.send("exit \n")
                        else:
                            pass

        btn = Button(EIGRPframe, text="Enable/Advertise", font=('helvetica', 8), bg="orange", command=eneigrp)
        btn.grid(column=2, row=6)


        def option_changed_getEIGRPoptiface(*args):
            if getEIGRPoptiface.get() == "Hello timer":
                text = 'eg. 5'
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='grey')
                eigrpopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt1.cget('fg') != 'black':
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt1.get() == "":
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='grey')
                        eigrpopt1.insert(0, text)
                eigrpopt1.bind("<FocusOut>", handle_focus_out)
                eigrpopt1.bind("<FocusIn>", handle_focus_in)
            elif getEIGRPoptiface.get() == "Hold timer":
                text = 'eg. 15'
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='grey')
                eigrpopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt1.cget('fg') != 'black':
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt1.get() == "":
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='grey')
                        eigrpopt1.insert(0, text)
                eigrpopt1.bind("<FocusOut>", handle_focus_out)
                eigrpopt1.bind("<FocusIn>", handle_focus_in)                
            elif getEIGRPoptiface.get() == "Static neighbor":
                text = '<neigh_IP>'
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='grey')
                eigrpopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt1.cget('fg') != 'black':
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt1.get() == "":
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='grey')
                        eigrpopt1.insert(0, text)
                eigrpopt1.bind("<FocusOut>", handle_focus_out)
                eigrpopt1.bind("<FocusIn>", handle_focus_in)
            elif getEIGRPoptiface.get() == "Passive int'face":
                text = 'NoInputRequired'
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='grey')
                eigrpopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt1.cget('fg') != 'black':
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt1.get() == "":
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='grey')
                        eigrpopt1.insert(0, text)
                eigrpopt1.bind("<FocusOut>", handle_focus_out)
                eigrpopt1.bind("<FocusIn>", handle_focus_in)
            elif getEIGRPoptiface.get() == "Bandwidth":
                text = 'eg. 10000 (Kbps)'
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='grey')
                eigrpopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt1.cget('fg') != 'black':
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt1.get() == "":
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='grey')
                        eigrpopt1.insert(0, text)
                eigrpopt1.bind("<FocusOut>", handle_focus_out)
                eigrpopt1.bind("<FocusIn>", handle_focus_in)                
            elif getEIGRPoptiface.get() == "Summary route":
                text = '<net> <mask> [<AD>]'
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='grey')
                eigrpopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt1.cget('fg') != 'black':
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt1.get() == "":
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='grey')
                        eigrpopt1.insert(0, text)
                eigrpopt1.bind("<FocusOut>", handle_focus_out)
                eigrpopt1.bind("<FocusIn>", handle_focus_in)
            elif getEIGRPoptiface.get() == "Filter adv'tised":
                text = '<acl_no.> | prefix-l <> + i/o'
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='grey')
                eigrpopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt1.cget('fg') != 'black':
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt1.get() == "":
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='grey')
                        eigrpopt1.insert(0, text)
                eigrpopt1.bind("<FocusOut>", handle_focus_out)
                eigrpopt1.bind("<FocusIn>", handle_focus_in)
            elif getEIGRPoptiface.get() == "Filter metric FD":
                text = '<acl_no.> + i/o + offset_val'
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='grey')
                eigrpopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt1.cget('fg') != 'black':
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt1.get() == "":
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='grey')
                        eigrpopt1.insert(0, text)
                eigrpopt1.bind("<FocusOut>", handle_focus_out)
                eigrpopt1.bind("<FocusIn>", handle_focus_in)                
            elif getEIGRPoptiface.get() == "Authentication":
                text = '<keychain_name>'
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='grey')
                eigrpopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt1.cget('fg') != 'black':
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt1.get() == "":
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='grey')
                        eigrpopt1.insert(0, text)
                eigrpopt1.bind("<FocusOut>", handle_focus_out)
                eigrpopt1.bind("<FocusIn>", handle_focus_in)
            else:
                text = 'NoInputRequired'
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='grey')
                eigrpopt1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt1.cget('fg') != 'black':
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt1.get() == "":
                        eigrpopt1.delete(0, END)
                        eigrpopt1.config(fg='grey')
                        eigrpopt1.insert(0, text)
                eigrpopt1.bind("<FocusOut>", handle_focus_out)
                eigrpopt1.bind("<FocusIn>", handle_focus_in)
                
                
        OPTIONS = [
        "Hello timer",
        "Hold timer",
        "Static neighbor",
        "Passive int'face",
        "Bandwidth",
        "Summary route",
        "Filter adv'tised",
        "Filter metric FD",
        "Authentication",
        "BFD"
        ]
        getEIGRPoptiface = StringVar(EIGRPframe)
        getEIGRPoptiface.set(OPTIONS[0])    # default value
        getEIGRPoptiface.trace("w", option_changed_getEIGRPoptiface)
        dropbox2 = OptionMenu(EIGRPframe, getEIGRPoptiface, *OPTIONS)   
        dropbox2.grid(column=0, row=8)
        eigrpopt1 = Entry(EIGRPframe, bg='white', width=22, fg='grey')
        eigrpopt1.grid(column=1, row=8, columnspan=2, sticky='w')
        eigrpopt1.insert(0, "eg. 5")
        eigrpopt1.config(font=("TkDefaultFont", 8))
        def handle_focus_in(_):
            if eigrpopt1.cget('fg') != 'black':
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='black')
        def handle_focus_out(_):
            if eigrpopt1.get() == "":
                eigrpopt1.delete(0, END)
                eigrpopt1.config(fg='grey')
                eigrpopt1.insert(0, "eg. 15(MyVRF)")    
        eigrpopt1.bind("<FocusOut>", handle_focus_out)
        eigrpopt1.bind("<FocusIn>", handle_focus_in)
        
        eigrpoptiface = Entry(EIGRPframe, bg='white', width=8, fg='grey')
        eigrpoptiface.grid(column=2, row=8, sticky='e')
        eigrpoptiface.insert(0, "eg. fa0/0")
        def handle_focus_in(_):
            if eigrpoptiface.cget('fg') != 'black':
                eigrpoptiface.delete(0, END)
                eigrpoptiface.config(fg='black')
        def handle_focus_out(_):
            if eigrpoptiface.get() == "":
                eigrpoptiface.delete(0, END)
                eigrpoptiface.config(fg='grey')
                eigrpoptiface.insert(0, "eg. fa0/0")    
        eigrpoptiface.bind("<FocusOut>", handle_focus_out)
        eigrpoptiface.bind("<FocusIn>", handle_focus_in)        
        def eigrpifaceopt():
            vrffind = txteigrppid.get()
            eivrf = vrffind[vrffind.find("(")+1:vrffind.find(")")]
            eivrfpid = ""
            EiAS = ""
            if "AS" in txteigrppid.get():
                eivrfpid = vrffind.split("(",1)[0]
                EiAS = vrffind.split("AS",1)[1]
            else:
                pass
            defeigrpcmd = "router eigrp " + txteigrppid.get() + "\n"
            vrfeigrpcmd = "router eigrp " + eivrfpid + " \n " + "address-f ipv4 vrf " + eivrf + " \n " + "autonom " + EiAS + "\n"              
            if txteigrppid.get() == "" or txteigrppid.get() == "eg. 15(MyVRF)AS1":
                tkMessageBox.showinfo('Error', 'Please also enter the EIGRP PID above.', parent=window)
            elif "(" in txteigrppid.get() and "AS" not in txteigrppid.get():
                tkMessageBox.showinfo('Error', 'Please enter both the EIGRP PID VRF and AS number.', parent=window)
            elif "AS" in txteigrppid.get() and "(" not in txteigrppid.get():
                tkMessageBox.showinfo('Error', 'Please enter both the EIGRP PID VRF and AS number.', parent=window)
            elif eigrpoptiface.get() == "" or eigrpoptiface.get() == "eg. fa0/0":
                tkMessageBox.showinfo('Error', 'Please enter an interface first.', parent=window)
            else:
                remote_conn.send("conf t \n")
                sleep(0.2)
                if chk_state_neg.get() == False:
                    if getEIGRPoptiface.get() == "Hello timer":
                        if eigrpopt1.get() == "" or eigrpopt1.get() == "eg. 5":
                            tkMessageBox.showinfo('Error', 'Please enter a Hello timer value.', parent=window)
                        else:
                            remote_conn.send("int " + eigrpoptiface.get() + " \n")
                            sleep(0.2)                
                            remote_conn.send("ip hello-int eig " + txteigrppid.get + " " + eigrpopt1.get() + " \n")
                            tkMessageBox.showinfo('EIGRP Timer', 'Hello timer set.', parent=window)
                    elif getEIGRPoptiface.get() == "Hold timer" or eigrpopt1.get() == "eg. 15":
                        if eigrpopt1.get() == "":
                            tkMessageBox.showinfo('Error', 'Please enter a Hold timer value.', parent=window)
                        else:
                            remote_conn.send("int " + eigrpoptiface.get() + " \n")
                            sleep(0.2)                
                            remote_conn.send("ip hold-t eig " + txteigrppid.get + " " + eigrpopt1.get() + " \n")
                            tkMessageBox.showinfo('EIGRP Timer', 'Hold timer set.', parent=window)
                    elif getEIGRPoptiface.get() == "Static neighbor":
                        if eigrpopt1.get() == "" or eigrpopt1.get() == "<neigh_IP>":
                            tkMessageBox.showinfo('Error', 'Please enter a neighbor IP address.', parent=window)
                        else:
                            remote_conn.send("neighbor " + eigrpopt1.get() + " " + eigrpoptiface.get() + " \n")
                            tkMessageBox.showinfo('EIGRP', 'Static neighbor has been configured.', parent=window)
                    elif getEIGRPoptiface.get() == "Passive int'face":
                        if "(" not in txteigrppid.get():
                            remote_conn.send(defeigrpcmd)
                        else:
                            remote_conn.send(vrfeigrpcmd)                    
                        sleep(0.2)
                        remote_conn.send("passive-int " + eigrpoptiface.get() + " \n")
                        tkMessageBox.showinfo('EIGRP Passive', 'EIGRP process enabled for interface ' + eigrpoptiface.get() + '.', parent=window)
                    elif getEIGRPoptiface.get() == "Bandwidth":
                        if eigrpopt1.get() == "" or eigrpopt1.get() == "eg. 10000 (Kbps)":
                            tkMessageBox.showinfo('Error', 'Please enter a bandwidth value.', parent=window)
                        else:
                            remote_conn.send("int " + eigrpoptiface.get() + " \n")
                            sleep(0.2)
                            remote_conn.send("bandwidth " + eigrpopt1.get() + " \n")
                            tkMessageBox.showinfo('Interface Bandwidth', 'Interface bandwidth configured. NOTE: Will affect any applied %-based QoS policy on this interface.', parent=window)                       
                    elif getEIGRPoptiface.get() == "Summary route":
                        if eigrpopt1.get() == "" or eigrpopt1.get() == "<net> <mask> [<AD>]":
                            tkMessageBox.showinfo('Error', 'Please enter a summary-address <<ip> <mask> [AD]> value.', parent=window)
                        else:
                            remote_conn.send("int " + eigrpoptiface.get() + " \n")
                            sleep(0.2)
                            remote_conn.send("ip summary-address eigrp " + txteigrppid.get() + " " + eigrpopt1.get() + " \n")
                            tkMessageBox.showinfo('EIGRP summary-address', 'Configured.', parent=window)
                    elif getEIGRPoptiface.get() == "Filter adv'tised":
                        if eigrpopt1.get() == "" or eigrpopt1.get() == "<acl_no.> | prefix-l <> + i/o":
                            tkMessageBox.showinfo('Error', 'Please specify the <<ACL/prefix<pfxlist>> <in/out>>.', parent=window)
                        else:
                            if "(" not in txteigrppid.get():
                                remote_conn.send(defeigrpcmd)
                            else:
                                remote_conn.send(vrfeigrpcmd)
                            sleep(0.2)
                            remote_conn.send("distribute-l " + eigrpopt1.get() + " " + eigrpoptiface.get() + " \n")
                            tkMessageBox.showinfo('EIGRP Route Filter', 'EIGRP distribute list filtering configured - remember to create the ACL/pfxlist.', parent=window)
                    elif getEIGRPoptiface.get() == "Filter metric FD":
                        if eigrpopt1.get() == "" or eigrpopt1.get() == "<acl_no.> + i/o + offset_val":
                            tkMessageBox.showinfo('Error', 'Please specify the <<ACL> <in/out> <metric-offset-val>>.', parent=window)
                        else:
                            if "(" not in txteigrppid.get():
                                remote_conn.send(defeigrpcmd)
                            else:
                                remote_conn.send(vrfeigrpcmd)                    
                            sleep(0.2)
                            remote_conn.send("offset-l " + eigrpopt1.get() + " " + eigrpoptiface.get() + " \n")
                            tkMessageBox.showinfo('EIGRP Metric Filter', 'EIGRP offset list filtering configured - remember to create the ACL/pfxlist.', parent=window)
                    elif getEIGRPoptiface.get() == "Authentication":
                        if eigrpopt1.get() == "" or eigrpopt1.get() == "<keychain_name>":
                            tkMessageBox.showinfo('Error', 'Please specify a Keychain name.', parent=window)
                        else:
                            remote_conn.send("int " + eigrpoptiface.get() + " \n")
                            sleep(0.2)
                            remote_conn.send("ip authentication mode eigrp " + txteigrppid.get() + " md5 \n")
                            sleep(0.2)
                            remote_conn.send("ip authentication key-chain eigrp " + txteigrppid.get() + " " + eigrpopt1.get() + " \n")
                            sleep(0.2)
                            tkMessageBox.showinfo('EIGRP Authentication', 'Configured - remember to create the Key Chain !', parent=window)
                    else:
                        if "(" not in txteigrppid.get():
                            remote_conn.send(defeigrpcmd)
                        else:
                            remote_conn.send(vrfeigrpcmd)                    
                        sleep(0.2)
                        remote_conn.send("bfd int " + eigrpoptiface.get() + "\n")
                        sleep(0.2)
                        tkMessageBox.showinfo('BFD', 'BFD configured for interface.', parent=window)
                        
                else:
                    if getEIGRPoptiface.get() == "Hello timer":                        
                        remote_conn.send("int " + eigrpoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("no ip hello-int eig " + txteigrppid.get + " " + eigrpopt1.get() + " \n")
                        tkMessageBox.showinfo('EIGRP Timer', 'Hello timer reset.', parent=window)
                    elif getEIGRPoptiface.get() == "Hold timer":
                        remote_conn.send("int " + eigrpoptiface.get() + " \n")
                        sleep(0.2)                
                        remote_conn.send("no ip hold-t eig " + txteigrppid.get + " " + eigrpopt1.get() + " \n")
                        tkMessageBox.showinfo('EIGRP Timer', 'Hold timer reset.', parent=window)
                    elif getEIGRPoptiface.get() == "Static neighbor":
                        if eigrpopt1.get() == "" or eigrpopt1.get() == "<neigh_IP>":
                            tkMessageBox.showinfo('Error', 'Please enter a neighbor IP address.', parent=window)
                        else:
                            remote_conn.send("no neighbor " + eigrpopt1.get() + " " + eigrpoptiface.get() + " \n")
                            tkMessageBox.showinfo('EIGRP', 'Static neighbor has been removed.', parent=window)
                    elif getEIGRPoptiface.get() == "Passive int'face":
                        if "(" not in txteigrppid.get():
                            remote_conn.send(defeigrpcmd)
                        else:
                            remote_conn.send(vrfeigrpcmd)                    
                        sleep(0.2)
                        remote_conn.send("no passive-int " + eigrpoptiface.get() + " \n")
                        tkMessageBox.showinfo('EIGRP Passive', 'EIGRP process disabled for interface ' + eigrpoptiface.get() + '.', parent=window)
                    elif getEIGRPoptiface.get() == "Bandwidth":
                            remote_conn.send("int " + eigrpoptiface.get() + " \n")
                            sleep(0.2)                
                            remote_conn.send("no bandwidth \n")
                            tkMessageBox.showinfo('EIGRP Bandwidth', 'Interface bandwidth has been reset.', parent=window)                     
                    elif getEIGRPoptiface.get() == "Summary route":
                        if eigrpopt1.get() == "" or eigrpopt1.get() == "<net> <mask> [<AD>]":
                            tkMessageBox.showinfo('Error', 'Please enter a summary-address <<ip> <mask> [AD]> value.', parent=window)
                        else:
                            remote_conn.send("int " + eigrpoptiface.get() + " \n")
                            sleep(0.2)                
                            remote_conn.send("no ip summary-address eigrp " + txteigrppid.get() + " " + eigrpopt1.get() + " \n")
                            tkMessageBox.showinfo('EIGRP summary-address', 'Reset.', parent=window)
                    elif getEIGRPoptiface.get() == "Filter adv'tised":
                        if eigrpopt1.get() == "" or eigrpopt1.get() == "<acl_no.> | prefix-l <> + i/o":
                            tkMessageBox.showinfo('Error', 'Please specify the <<ACL/prefix<pfxlist>> <in/out>>.', parent=window)
                        else:
                            if "(" not in txteigrppid.get():
                                remote_conn.send(defeigrpcmd)
                            else:
                                remote_conn.send(vrfeigrpcmd)
                            sleep(0.2)
                            remote_conn.send("no distribute-l " + eigrpopt1.get() + " " + eigrpoptiface.get() + " \n")
                            tkMessageBox.showinfo('EIGRP Route Filter', 'EIGRP distribute list filtering removed.', parent=window)
                    elif getEIGRPoptiface.get() == "Filter metric FD":
                        if eigrpopt1.get() == "" or eigrpopt1.get() == "<acl_no.> + i/o + offset_val":
                            tkMessageBox.showinfo('Error', 'Please specify the <<ACL> <in/out>>.', parent=window)
                        else:
                            if "(" not in txteigrppid.get():
                                remote_conn.send(defeigrpcmd)
                            else:
                                remote_conn.send(vrfeigrpcmd)
                            sleep(0.2)
                            remote_conn.send("no offset-l " + eigrpopt1.get() + " " + eigrpoptiface.get() + " \n")
                            tkMessageBox.showinfo('EIGRP Metric Filter', 'EIGRP offset list filtering removed.', parent=window)
                    elif getEIGRPoptiface.get() == "Authentication":
                        remote_conn.send("int " + eigrpoptiface.get() + " \n")
                        sleep(0.2)
                        remote_conn.send("no ip authentication mode eigrp " + txteigrppid.get() + " md5 \n")
                        sleep(0.2)
                        tkMessageBox.showinfo('EIGRP Authentication', 'Authentication disabled.', parent=window)
                    else:
                        if "(" not in txteigrppid.get():
                            remote_conn.send(defeigrpcmd)
                        else:
                            remote_conn.send(vrfeigrpcmd)
                        sleep(0.2)
                        remote_conn.send("no bfd int " + eigrpoptiface.get() + "\n")
                        sleep(0.2)
                        tkMessageBox.showinfo('BFD', 'BFD configured for interface.', parent=window)
                remote_conn.send("exit \n")
                sleep(0.2)
                remote_conn.send("exit \n")
                sleep(0.2)
        btn = Button(EIGRPframe, text="Aplicar", bg="orange", command=eigrpifaceopt)
        btn.grid(column=5, row=8)


        def option_changed_getEIGRPoptdevice(*args):
            if getEIGRPoptdevice.get() == "Router-ID":
                text = 'eg. 1.1.1.1'
                eigrpopt2.delete(0, END)
                eigrpopt2.config(fg='grey')
                eigrpopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt2.cget('fg') != 'black':
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt2.get() == "":
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='grey')
                        eigrpopt2.insert(0, text)
                eigrpopt2.bind("<FocusOut>", handle_focus_out)
                eigrpopt2.bind("<FocusIn>", handle_focus_in) 
            elif getEIGRPoptdevice.get() == "Auto Summary" or getEIGRPoptdevice.get() == "Propagate * route":
                text = 'NoInputRequired'
                eigrpopt2.delete(0, END)
                eigrpopt2.config(fg='grey')
                eigrpopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt2.cget('fg') != 'black':
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt2.get() == "":
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='grey')
                        eigrpopt2.insert(0, text)
                eigrpopt2.bind("<FocusOut>", handle_focus_out)
                eigrpopt2.bind("<FocusIn>", handle_focus_in)
            elif getEIGRPoptdevice.get() == "Variance":
                text = '<1-128>'
                eigrpopt2.delete(0, END)
                eigrpopt2.config(fg='grey')
                eigrpopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt2.cget('fg') != 'black':
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt2.get() == "":
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='grey')
                        eigrpopt2.insert(0, text)
                eigrpopt2.bind("<FocusOut>", handle_focus_out)
                eigrpopt2.bind("<FocusIn>", handle_focus_in)
            elif getEIGRPoptdevice.get() == "Stub":
                text = '[conn][receive-only][redist][static][summ]'
                eigrpopt2.delete(0, END)
                eigrpopt2.config(fg='grey')
                eigrpopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt2.cget('fg') != 'black':
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt2.get() == "":
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='grey')
                        eigrpopt2.insert(0, text)
                eigrpopt2.bind("<FocusOut>", handle_focus_out)
                eigrpopt2.bind("<FocusIn>", handle_focus_in)
            elif getEIGRPoptdevice.get() == "Max paths":
                text = '<1-16>'
                eigrpopt2.delete(0, END)
                eigrpopt2.config(fg='grey')
                eigrpopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt2.cget('fg') != 'black':
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt2.get() == "":
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='grey')
                        eigrpopt2.insert(0, text)
                eigrpopt2.bind("<FocusOut>", handle_focus_out)
                eigrpopt2.bind("<FocusIn>", handle_focus_in)
            elif getEIGRPoptdevice.get() == "AD(int ext)":
                text = '<1-255> [<1-255>]'
                eigrpopt2.delete(0, END)
                eigrpopt2.config(fg='grey')
                eigrpopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt2.cget('fg') != 'black':
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt2.get() == "":
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='grey')
                        eigrpopt2.insert(0, text)
                eigrpopt2.bind("<FocusOut>", handle_focus_out)
                eigrpopt2.bind("<FocusIn>", handle_focus_in)
            elif getEIGRPoptdevice.get() == "Selective AD(int)":
                text = '<AD> <net> <wildcard> [acl_no.]'
                eigrpopt2.delete(0, END)
                eigrpopt2.config(fg='grey')
                eigrpopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt2.cget('fg') != 'black':
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt2.get() == "":
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='grey')
                        eigrpopt2.insert(0, text)
                eigrpopt2.bind("<FocusOut>", handle_focus_out)
                eigrpopt2.bind("<FocusIn>", handle_focus_in)
            else:
                text = '<0-255> <0-255> <0-255> <0-255> <0-255>'
                eigrpopt2.delete(0, END)
                eigrpopt2.config(fg='grey')
                eigrpopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if eigrpopt2.cget('fg') != 'black':
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='black')
                def handle_focus_out(_):
                    if eigrpopt2.get() == "":
                        eigrpopt2.delete(0, END)
                        eigrpopt2.config(fg='grey')
                        eigrpopt2.insert(0, text)
                eigrpopt2.bind("<FocusOut>", handle_focus_out)
                eigrpopt2.bind("<FocusIn>", handle_focus_in)

        OPTIONS = [
        "Router-ID",
        "Auto Summary",
        "Propagate * route",
        "Variance",
        "Stub",
        "Max paths",
        "AD(int ext)",
        "Selective AD(int)",
        "Default Metric"
        ]
        getEIGRPoptdevice = StringVar(EIGRPframe)
        getEIGRPoptdevice.set(OPTIONS[0])    # default value
        getEIGRPoptdevice.trace("w", option_changed_getEIGRPoptdevice)
        dropbox2 = OptionMenu(EIGRPframe, getEIGRPoptdevice, *OPTIONS)   
        dropbox2.grid(column=0, row=9)
        eigrpopt2 = Entry(EIGRPframe, bg='white', width=35, fg='grey')
        eigrpopt2.grid(column=1, row=9, columnspan=4, sticky='w')
        eigrpopt2.insert(0, "eg. 1.1.1.1")
        eigrpopt2.config(font=("TkDefaultFont", 8))
        def handle_focus_in(_):
            if eigrpopt2.cget('fg') != 'black':
                eigrpopt2.delete(0, END)
                eigrpopt2.config(fg='black')
        def handle_focus_out(_):
            if eigrpopt2.get() == "":
                eigrpopt2.delete(0, END)
                eigrpopt2.config(fg='grey')
                eigrpopt2.insert(0, "eg. 15(MyVRF)")    
        eigrpopt2.bind("<FocusOut>", handle_focus_out)
        eigrpopt2.bind("<FocusIn>", handle_focus_in)

        
        def eigrpotheropt():
            vrffind = txteigrppid.get()
            eivrf = vrffind[vrffind.find("(")+1:vrffind.find(")")]
            eivrfpid = ""
            EiAS = ""
            if "AS" in txteigrppid.get():
                eivrfpid = vrffind.split("(",1)[0]
                EiAS = vrffind.split("AS",1)[1]
            else:
                pass
            defeigrpcmd = "router eigrp " + txteigrppid.get() + "\n"
            vrfeigrpcmd = "router eigrp " + eivrfpid + " \n " + "address-f ipv4 vrf " + eivrf + " \n " + "autonom " + EiAS + "\n"
            
            if txteigrppid.get() == "" or txteigrppid.get() == "eg. 15(MyVRF)AS1":
                tkMessageBox.showinfo('Error', 'Please also enter the EIGRP PID above.', parent=window)
            elif "(" in txteigrppid.get() and "AS" not in txteigrppid.get():
                tkMessageBox.showinfo('Error', 'Please enter both the EIGRP PID VRF and AS number.', parent=window)
            elif "AS" in txteigrppid.get() and "(" not in txteigrppid.get():
                tkMessageBox.showinfo('Error', 'Please enter both the EIGRP PID VRF and AS number.', parent=window)
            else:
                remote_conn.send("conf t \n")
                sleep(0.2)                
                if "(" not in txteigrppid.get():
                    remote_conn.send(defeigrpcmd)
                else:
                    remote_conn.send(vrfeigrpcmd)
                sleep(0.2)
                if chk_state_neg.get() == False:
                    if getEIGRPoptdevice.get() == "Router-ID":
                        if eigrpopt2.get() == "" or eigrpopt2.get() == "eg. 1.1.1.1":
                            tkMessageBox.showinfo('Error', 'Please enter Router ID (IP) value.', parent=window)
                        else:
                            remote_conn.send("eigrp router-id " + eigrpopt2.get() + " \n")
                            tkMessageBox.showinfo('EIGRP', 'Router-id has been set.', parent=window)
                    elif getEIGRPoptdevice.get() == "Auto Summary":
                        remote_conn.send("auto \n")
                        tkMessageBox.showinfo('EIGRP', 'Auto summarization has been enabled.', parent=window)
                    elif getEIGRPoptdevice.get() == "Propagate * route":
                        tkMessageBox.showinfo('EIGRP', 'Few ways to do this:\n  - create a default static route and Learn it\n  -  Use the "Summary route" \
above to propagate at interface level\n - ', parent=window)                        
                    elif getEIGRPoptdevice.get() == "Variance":
                        if eigrpopt2.get() == "" or eigrpopt2.get() == "<1-128>":
                            tkMessageBox.showinfo('Error', 'Please enter variance (1-128) value.', parent=window)
                        else:
                            remote_conn.send("variance " + eigrpopt2.get() + " \n")
                            tkMessageBox.showinfo('EIGRP Unequal Cost Load Balancing', 'Variance multiplier ' + + eigrpopt1.get() + '*FD has been set.', parent=window)
                    elif getEIGRPoptdevice.get() == "Stub":
                        if eigrpopt2.get() == "" or eigrpopt2.get() == "[conn][receive-only][redist][static][summ]":
                            remote_conn.send("eigrp stub \n")
                            res = "Stub (default) has been configured."
                        else:
                            remote_conn.send("eigrp stub " + eigrpopt2.get() + " \n")
                            res = "Stub (custom) has been configured."
                        tkMessageBox.showinfo('EIGRP', res, parent=window)
                    elif getEIGRPoptdevice.get() == "Max paths":
                        if eigrpopt2.get() == "" or eigrpopt2.get() == "<1-16>":
                            tkMessageBox.showinfo('Error', 'Please enter a value.', parent=window)
                        else:
                            remote_conn.send("maximum-pa " + eigrpopt2.get() + " \n")
                            tkMessageBox.showinfo('EIGRP', 'Max paths has been configured.', parent=window)                        
                    elif getEIGRPoptdevice.get() == "AD(int ext)":
                        if eigrpopt2.get() == "" or eigrpopt2.get() == "<1-255> [<1-255>]":
                            tkMessageBox.showinfo('Error', 'Please enter AD values.', parent=window)
                        else:
                            remote_conn.send("distance eigrp " + eigrpopt2.get() + " \n")
                            tkMessageBox.showinfo('EIGRP', 'Distance has been configured.', parent=window)
                    elif getEIGRPoptdevice.get() == "Selective AD(int)":
                        if eigrpopt2.get() == "" or eigrpopt2.get() == "<AD> <net> <wildcard> [acl_no.]":
                            tkMessageBox.showinfo('Error', 'Please enter required values.')
                        else:
                            remote_conn.send("distance " + eigrpopt2.get() + " \n")
                            tkMessageBox.showinfo('EIGRP', 'Distance has been configured.', parent=window)
                    else:
                        if eigrpopt2.get() == "" or eigrpopt2.get() == "<0-255> <0-255> <0-255> <0-255> <0-255>":
                            tkMessageBox.showinfo('Error', 'Please enter all 5 (K1-K5) weight values.', parent=window)
                        else:
                            remote_conn.send("metric weights 0 " + eigrpopt2.get() + " \n")
                            tkMessageBox.showinfo('EIGRP', 'Default metric weights has been configured.', parent=window)
                else:
                    if getEIGRPoptdevice.get() == "Router-ID":
                        remote_conn.send("no eigrp router-id \n")
                        tkMessageBox.showinfo('EIGRP', 'Router-id has been removed.', parent=window)
                    elif getEIGRPoptdevice.get() == "Auto Summary":
                        remote_conn.send("no auto \n")
                        tkMessageBox.showinfo('EIGRP', 'Auto summarization has been disabled.', parent=window)
                    elif getEIGRPoptdevice.get() == "Propagate * route":
                        tkMessageBox.showinfo('EIGRP', 'Few ways to do this:\n  - create a default static route and Learn it\n  -  Use the "Summary route"\
above to propagate at interface level\n - ', parent=window)                        
                    elif getEIGRPoptdevice.get() == "Variance":
                        remote_conn.send("no variance \n")
                        tkMessageBox.showinfo('EIGRP Unequal Cost Load Balancing', 'Variance multiplier has been removed.', parent=window)
                    elif getEIGRPoptdevice.get() == "Stub":
                        remote_conn.send("no eigrp stub \n")
                        tkMessageBox.showinfo('EIGRP', 'Stub has been removed.', parent=window)
                    elif getEIGRPoptdevice.get() == "Max paths":
                        remote_conn.send("no maximum-path \n")
                        tkMessageBox.showinfo('EIGRP', 'Max paths has been reset.', parent=window)                        
                    elif getEIGRPoptdevice.get() == "AD(int ext)":                  
                        remote_conn.send("no distance eigrp \n")
                        tkMessageBox.showinfo('EIGRP', 'Distance has been reset.', parent=window)
                    elif getEIGRPoptdevice.get() == "Selective AD(int)":
                        if eigrpopt2.get() == "" or eigrpopt2.get() == "<AD> <net> <wildcard> [acl_no.]":
                            tkMessageBox.showinfo('Error', 'Please enter required values.', parent=window)
                        else:
                            remote_conn.send("no distance " + eigrpopt2.get() + " \n")
                            tkMessageBox.showinfo('EIGRP', 'Distance has been removed.', parent=window)
                    else:
                        remote_conn.send("no metric weights \n")
                        tkMessageBox.showinfo('EIGRP', 'Metric weights has been reset to default.', parent=window)
                remote_conn.send("exit \n")
                sleep(0.2)
                remote_conn.send("exit \n")
                sleep(0.2)                        
        btn = Button(EIGRPframe, text="Aplicar", bg="orange", command=eigrpotheropt)
        btn.grid(column=5, row=9)



        OPTIONS = [
        "RIP",
        "OSPF",
        "EIGRP",
        "BGP"
        ]
        getEIGoptredist = StringVar(EIGRPframe)
        getEIGoptredist.set(OPTIONS[0])    # default value
        dropbox2 = OptionMenu(EIGRPframe, getEIGoptredist, *OPTIONS)   
        dropbox2.grid(column=0, row=10)
        
        eigrpredisttoprocnum = Entry(EIGRPframe, bg='white', width=13, fg='grey')
        eigrpredisttoprocnum.place(x=138, y=115)
        eigrpredisttoprocnum.insert(0, "eg. 15(MyVRF)")
        def handle_focus_in(_):
            if eigrpredisttoprocnum.cget('fg') != 'black':
                eigrpredisttoprocnum.delete(0, END)
                eigrpredisttoprocnum.config(fg='black')
        def handle_focus_out(_):
            if eigrpredisttoprocnum.get() == "":
                eigrpredisttoprocnum.delete(0, END)
                eigrpredisttoprocnum.config(fg='grey')
                eigrpredisttoprocnum.insert(0, "eg. 15(MyVRF)")    
        eigrpredisttoprocnum.bind("<FocusOut>", handle_focus_out)
        eigrpredisttoprocnum.bind("<FocusIn>", handle_focus_in)
        
        eigrpredistFilter = Entry(EIGRPframe, bg='white', width=6, fg='grey')
        eigrpredistFilter.place(x=232, y=115)
        eigrpredistFilter.insert(0, "r-map")
        def handle_focus_in(_):
            if eigrpredistFilter.cget('fg') != 'black':
                eigrpredistFilter.delete(0, END)
                eigrpredistFilter.config(fg='black')
        def handle_focus_out(_):
            if eigrpredistFilter.get() == "":
                eigrpredistFilter.delete(0, END)
                eigrpredistFilter.config(fg='grey')
                eigrpredistFilter.insert(0, "r-map")    
        eigrpredistFilter.bind("<FocusOut>", handle_focus_out)
        eigrpredistFilter.bind("<FocusIn>", handle_focus_in)
        
        eigrpredistMetric = Entry(EIGRPframe, bg='white', width=6, fg='grey')
        eigrpredistMetric.place(x=276, y=115)
        eigrpredistMetric.insert(0, "Metric")
        def handle_focus_in(_):
            if eigrpredistMetric.cget('fg') != 'black':
                eigrpredistMetric.delete(0, END)
                eigrpredistMetric.config(fg='black')
        def handle_focus_out(_):
            if eigrpredistMetric.get() == "":
                eigrpredistMetric.delete(0, END)
                eigrpredistMetric.config(fg='grey')
                eigrpredistMetric.insert(0, "Metric")    
        eigrpredistMetric.bind("<FocusOut>", handle_focus_out)
        eigrpredistMetric.bind("<FocusIn>", handle_focus_in)

        eigrpredistTag = Entry(EIGRPframe, bg='white', width=5, fg='grey')
        eigrpredistTag.grid(column=4, row=10)
        eigrpredistTag.insert(0, "Tag")
        def handle_focus_in(_):
            if eigrpredistTag.cget('fg') != 'black':
                eigrpredistTag.delete(0, END)
                eigrpredistTag.config(fg='black')
        def handle_focus_out(_):
            if eigrpredistTag.get() == "":
                eigrpredistTag.delete(0, END)
                eigrpredistTag.config(fg='grey')
                eigrpredistTag.insert(0, "Tag")    
        eigrpredistTag.bind("<FocusOut>", handle_focus_out)
        eigrpredistTag.bind("<FocusIn>", handle_focus_in)
        
        def eigrpredistribute():
            vrffind = txteigrppid.get()
            eivrf = vrffind[vrffind.find("(")+1:vrffind.find(")")]
            eivrfpid = ""
            EiAS = ""
            if "AS" in txteigrppid.get():
                eivrfpid = vrffind.split("(",1)[0]
                EiAS = vrffind.split("AS",1)[1]
            else:
                pass
            defeigrpcmd = "router eigrp " + txteigrppid.get() + "\n"
            vrfeigrpcmd = "router eigrp " + eivrfpid + " \n " + "address-f ipv4 vrf " + eivrf + " \n " + "autonom " + EiAS + "\n"
            
            vrffind2 = eigrpredisttoprocnum.get()
            PIDextract = re.search(r'\d+', vrffind2).group()
            osvrf = vrffind2[vrffind2.find("(")+1:vrffind2.find(")")]            
            redistcmd = "redistribute " + getEIGoptredist.get() + " " + PIDextract
            redistRIPcmd = "redistribute " + getEIGoptredist.get()
            #redistospfvrfcmd = "redistribute " + getEIGoptredist.get() + " vrf " + osvrf


            
            if chk_state_neg.get() == False:
                if txteigrppid.get() == "" or txteigrppid.get() == "eg. 15(MyVRF)AS1":
                    tkMessageBox.showinfo('Error', 'Please also enter the EIGRP process ID above.', parent=window)
                elif "(" in txteigrppid.get() and "AS" not in txteigrppid.get():
                    tkMessageBox.showinfo('Error', 'Please enter both the EIGRP PID VRF and AS number.', parent=window)
                elif "AS" in txteigrppid.get() and "(" not in txteigrppid.get():
                    tkMessageBox.showinfo('Error', 'Please enter both the EIGRP PID VRF and AS number.', parent=window)
                else:

                    if eigrpredistMetric.get() != "" and eigrpredistMetric.get() != "Metric":

                        match = re.findall(r'[0-9]+', eigrpredistMetric.get())
                        if len(match) != 5:
                            tkMessageBox.showinfo('Error', 'Please enter proper EIGRP Metric (bandwidth, delay, reliability, load, MTU) seperated by spaces: e.g. 1000 100 255 1 1500', parent=window)
                            return
                        else:
                            pass
                    else:
                        pass

                    
                    if getEIGoptredist.get() == "RIP":
                        remote_conn.send("conf t \n")
                        sleep(0.2)

                        cmd = redistRIPcmd
                        
                        if "(" not in txteigrppid.get():
                            remote_conn.send(defeigrpcmd)
                        else:
                            remote_conn.send(vrfeigrpcmd)
                            
                        if eigrpredistFilter.get() != "" and eigrpredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + eigrpredistFilter.get()
                        else:
                            pass
                        if eigrpredistMetric.get() != "" and eigrpredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + eigrpredistMetric.get()
                        else:
                            pass

                        remote_conn.send(cmd + "\n")
                        sleep(0.2)
                        if "(" in txteigrppid.get():
                            sleep(0.2)
                            remote_conn.send("exit \n")
                        else:
                            pass
                        tkMessageBox.showinfo('EIGRP redistribution', 'Learned ' + getEIGoptredist.get() + '.', parent=window)
                        
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.2)                        
                        if "(" not in txteigrppid.get():
                            remote_conn.send(defeigrpcmd)
                        else:
                            remote_conn.send(vrfeigrpcmd)

                        cmd = redistcmd
                        
                        if eigrpredistFilter.get() != "" and eigrpredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + eigrpredistFilter.get()
                        else:
                            pass
                        if eigrpredistMetric.get() != "" and eigrpredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + eigrpredistMetric.get()
                        else:
                            pass

                        remote_conn.send(cmd + "\n")
                        sleep(0.2)
                        if "(" in txteigrppid.get():
                            sleep(0.2)
                            remote_conn.send("exit \n")
                        else:
                            pass
                        tkMessageBox.showinfo('EIGRP redistribution', 'Learned ' + getEIGoptredist.get() + '.', parent=window)
                            
##                    else:
##                        remote_conn.send("conf t \n")
##                        sleep(0.2)                        
##                        if "(" not in txteigrppid.get():
##                            remote_conn.send(defeigrpcmd)
##                        else:
##                            remote_conn.send(vrfeigrpcmd)
##                        if "(" not in eigrpredisttoprocnum.get():
##                            cmd = redistcmd
##                        else:
##                            cmd = redistospfvrfcmd
##                        if eigrpredistFilter.get() != "" and eigrpredistFilter.get() != "r-map":
##                            cmd = cmd + " route-map " + eigrpredistFilter.get()
##                        else:
##                            pass
##                        if eigrpredistMetric.get() != "" and eigrpredistMetric.get() != "Metric":
##                            cmd = cmd + " metric " + eigrpredistMetric.get()
##                        else:
##                            pass
##                        if eigrpredistTag.get() != "" and eigrpredistTag.get() != "Tag":
##                            cmd = cmd + " tag " + eigrpredistTag.get()
##                        else:
##                            pass
##                        remote_conn.send(cmd + "\n")
##                        sleep(0.2)
##                        tkMessageBox.showinfo('EIGRP redistribution', 'Learned ' + getEIGoptredist.get() + '.', parent=window)
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
            else:
                if txteigrppid.get() == "" or txteigrppid.get() == "eg. 15(MyVRF)AS1":
                    tkMessageBox.showinfo('Error', 'Please also enter the EIGRP process ID above.', parent=window)
                elif "(" in txteigrppid.get() and "AS" not in txteigrppid.get():
                    tkMessageBox.showinfo('Error', 'Please enter both the EIGRP PID VRF and AS number.', parent=window)
                elif "AS" in txteigrppid.get() and "(" not in txteigrppid.get():
                    tkMessageBox.showinfo('Error', 'Please enter both the EIGRP PID VRF and AS number.', parent=window)
                else:
                    if getEIGoptredist.get() == "RIP":


                        
                        remote_conn.send("conf t \n")
                        sleep(0.2)                        

                        cmd = redistRIPcmd
                        
                        if "(" not in txteigrppid.get():
                            remote_conn.send(defeigrpcmd)
                        else:
                            remote_conn.send(vrfeigrpcmd)
                            
                        if eigrpredistFilter.get() != "" and eigrpredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + eigrpredistFilter.get()
                        else:
                            pass
                        if eigrpredistMetric.get() != "" and eigrpredistMetric.get() != "Metric":
                            cmd = cmd #+ " metric " + eigrpredistMetric.get()
                        else:
                            pass

                        
                        remote_conn.send("no " + cmd + "\n")
                        sleep(0.2)
                        if "(" in txteigrppid.get():
                            sleep(0.2)
                            remote_conn.send("exit \n")
                        else:
                            pass
                        tkMessageBox.showinfo('EIGRP redistribution', 'Unlearned ' + getEIGoptredist.get() + '.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.2)
                        
                        cmd = redistcmd
                        
                        if "(" not in txteigrppid.get():
                            remote_conn.send(defeigrpcmd)
                        else:
                            remote_conn.send(vrfeigrpcmd)
                            
                        if eigrpredistFilter.get() != "" and eigrpredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + eigrpredistFilter.get()
                        else:
                            pass
                        if eigrpredistMetric.get() != "" and eigrpredistMetric.get() != "Metric":
                            cmd = cmd #+ " metric " + eigrpredistMetric.get()
                        else:
                            pass
                        remote_conn.send("no " + cmd + "\n")
                        sleep(0.2)
                        if "(" in txteigrppid.get():
                            sleep(0.2)
                            remote_conn.send("exit \n")
                        else:
                            pass
                        tkMessageBox.showinfo('EIGRP redistribution', 'Unlearned ' + getEIGoptredist.get() + '.', parent=window)
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
        btn = Button(EIGRPframe, text="Learn", bg="orange", command=eigrpredistribute)
        btn.grid(column=5, row=10)


        

        BGPframe=LabelFrame(window,text=" BGP ",font=('verdana', 8, 'bold'),padx=10,pady=2,width=100,height=100)
        BGPframe.grid(column=0, row=3, sticky=("nsew"))
        
        lbl = Label(BGPframe).grid(column=0, row=0, pady=6)
        
        AFIvar = IntVar()
        AFIvar.set(1)
        R1 = Radiobutton(BGPframe, text="Def_AF", variable=AFIvar, value=1)
        R1.place(x=10, y=0)
        R2 = Radiobutton(BGPframe, text="v4", variable=AFIvar, value=2)
        R2.place(x=70, y=0)
        R3 = Radiobutton(BGPframe, text="v6", variable=AFIvar, value=3)
        R3.place(x=110, y=0)
        R4 = Radiobutton(BGPframe, text="VPNv4", variable=AFIvar, value=4)
        R4.place(x=150, y=0)
        R5 = Radiobutton(BGPframe, text="VPNv6", variable=AFIvar, value=5)
        R5.place(x=210, y=0)

        OPTIONS = [
        "Unicast",
        "Multicast",
        "MDT",
        "MVPN"
        ]
        SAFIopt = StringVar(BGPframe)
        SAFIopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(BGPframe, SAFIopt, *OPTIONS)
        dropbox.place(x=310, y=0)
            
        lbl = Label(BGPframe, text="Enable PID(+VRF):")    
        lbl.grid(column=0, row=2)
        bgpproc = Entry(BGPframe, bg='white', width=15, fg='grey')
        bgpproc.grid(column=1, row=2)
        bgpproc.insert(0, "eg. 15(MyVRF)")
        def handle_focus_in(_):
            if bgpproc.cget('fg') != 'black':
                bgpproc.delete(0, END)
                bgpproc.config(fg='black')
        def handle_focus_out(_):
            if bgpproc.get() == "":
                bgpproc.delete(0, END)
                bgpproc.config(fg='grey')
                bgpproc.insert(0, "eg. 15(MyVRF)")
        bgpproc.bind("<FocusOut>", handle_focus_out)
        bgpproc.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(BGPframe, text="Establish neighbor:")
        lbl.grid(column=0, row=3)
        bgpneighip = Entry(BGPframe, bg='white', width=15, fg='grey')
        bgpneighip.grid(column=1, row=3)
        bgpneighip.insert(0, "Neighbor IP")
        def handle_focus_in(_):
            if bgpneighip.cget('fg') != 'black':
                bgpneighip.delete(0, END)
                bgpneighip.config(fg='black')
        def handle_focus_out(_):
            if bgpneighip.get() == "":
                bgpneighip.delete(0, END)
                bgpneighip.config(fg='grey')
                bgpneighip.insert(0, "Neighbor IP")    
        bgpneighip.bind("<FocusOut>", handle_focus_out)
        bgpneighip.bind("<FocusIn>", handle_focus_in)        
        bgpneigh = Entry(BGPframe, bg='white', width=15, fg='grey')
        bgpneigh.grid(column=2, row=3)
        bgpneigh.insert(0, "Neighbor AS no.")
        def handle_focus_in(_):
            if bgpneigh.cget('fg') != 'black':
                bgpneigh.delete(0, END)
                bgpneigh.config(fg='black')
        def handle_focus_out(_):
            if bgpneigh.get() == "":
                bgpneigh.delete(0, END)
                bgpneigh.config(fg='grey')
                bgpneigh.insert(0, "Neighbor AS no.")    
        bgpneigh.bind("<FocusOut>", handle_focus_out)
        bgpneigh.bind("<FocusIn>", handle_focus_in)        

        chk_localAS = BooleanVar()
        chk_localAS.set(False)
        chk = Checkbutton(BGPframe, text="Local AS",variable=chk_localAS)
        chk.grid(column=3, row=3, columnspan = 3)

        
        lbl = Label(BGPframe, text="Advertise network & mask:")
        lbl.grid(column=0, row=4)        
        bgpadv = Entry(BGPframe,width=15)
        bgpadv.grid(column=1, row=4)
        
        bgpmask = Entry(BGPframe, bg='white', width=15, fg='grey')
        bgpmask.grid(column=2, row=4)
        bgpmask.insert(0, "eg. 255.255.255.0")
        def handle_focus_in(_):
            if bgpmask.cget('fg') != 'black':
                bgpmask.delete(0, END)
                bgpmask.config(fg='black')
        def handle_focus_out(_):
            if bgpmask.get() == "":
                bgpmask.delete(0, END)
                bgpmask.config(fg='grey')
                bgpmask.insert(0, "eg. 255.255.255.0")    
        bgpmask.bind("<FocusOut>", handle_focus_out)
        bgpmask.bind("<FocusIn>", handle_focus_in)
        def enbgp():
            vrffind = bgpproc.get()
            PIDextract = re.search(r'\d+', vrffind).group()
            bgvrf = vrffind[vrffind.find("(")+1:vrffind.find(")")]
            bgvrfpid = ""
            if "(" in bgpproc.get():
                bgvrfpid = vrffind.split("(",1)[0]
            else:
                pass
            defbgpcmd = "router bgp " + bgpproc.get() + "\n"
            defbgpcmd2 = "router bgp " + PIDextract + "\n"
            vrfbgpcmd = "router bgp " + bgvrfpid + " \n " + "address-f ipv4 vrf " + bgvrf + " \n "
            

            i = bgpproc.get()
            j = bgpneighip.get()
            k = bgpneigh.get()
            l = bgpadv.get()
            m = bgpmask.get()
            
            if chk_state_neg.get() == False:
                if (i == '') or (i == 'eg. 15(MyVRF)'):
                    tkMessageBox.showinfo('Error' + bgpproc.get(), 'Error - Please enter a BGP PID (AS number)', parent=window)
                else:
                    if "(" in bgpproc.get():
                        remote_conn.send("sh ip vrf " + bgvrf + " \n")
                        sleep(0.2)
                        output = remote_conn.recv(2048).decode("utf-8")
                        sleep(2)
                        stripp = output.strip()
                        sleep(0.2)
                        if "No VRF" in stripp:
                            sleep(0.2)
                            tkMessageBox.showinfo('Error', 'VRF not found.. Please create the VRF first. Aborting.', parent=window)
                            return
                        else:
                            pass
                    else:
                        pass

                    
                    remote_conn.send("sh ip proto | i bgp \n")
                    sleep(0.5)
                    output = remote_conn.recv(2048).decode("utf-8")
                    sleep(0.5)
                    stripp = output.strip()
                    sleep(0.5)
                    test = str(output)
                    test2 = re.findall(r'bgp (\w+)', test)
                    checkbgp = ''.join(test2)
                    if 'is "bgp' in stripp and ((("(" not in bgpproc.get()) and (i not in checkbgp)) or (("(" in bgpproc.get()) and \
                                                                                                   ((i.split("(",1)[0]) not in checkbgp))):
                        sleep(0.5)
                        tkMessageBox.showinfo('Error', 'BGP AS ' + checkbgp + ' already exists. Only 1 BGP AS/process can be running at any time.', parent=window)
##                    elif 'is "bgp' in stripp and ((j == '') or (j == 'Neighbor IP')) and ((k == '') or (k == 'Neighbor AS no.')) and (l == '') and \
##                         ((m == '') or (m == 'eg. 255.255.255.0')) and ((("(" not in bgpproc.get()) and (i in output)) or (("(" in bgpproc.get()) and \
##                         ((i.split("(",1)[0]) in output))):     #if have/not_have vrf and BGP AS in output, inform
##                            tkMessageBox.showinfo('BGP ' + i, 'This BGP process is already running', parent=window)
                    elif 'is "bgp' in stripp and ((j == '') or (j == 'Neighbor IP')) and ((k == '') or (k == 'Neighbor AS no.')) and (l == '') and \
                         ((m == '') or (m == 'eg. 255.255.255.0')) and ((("(" not in bgpproc.get()) and (i in output))):     #if not_have vrf and BGP AS in output, inform
                            tkMessageBox.showinfo('BGP ' + i, 'This BGP process is already running', parent=window)                            
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.2)
                        if "(" not in bgpproc.get():
                            remote_conn.send(defbgpcmd)
                        else:
                            remote_conn.send(defbgpcmd2)
                        sleep(0.3)
                        print (AFIvar.get())
                        if AFIvar.get() == 1:
                            if "(" not in bgpproc.get():
                                bgpcomment = 'BGP enabled.'
                            else:
                                remote_conn.send("exit \n")
                                sleep(0.2)
                                remote_conn.send("exit \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Error', 'BGP enabled, AF is not. Please select either an IPv4 or IPv6 AF to Aplicar VRFs.', parent=window)
                                sleep(0.2)
                                return
                        elif AFIvar.get() == 2:
                            if "(" not in bgpproc.get():
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " \n")
                                sleep(0.2)
                                bgpcomment = 'BGP v4 enabled.'
                            else:
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " vrf " +  bgvrf + "\n")
                                sleep(0.2)
                                bgpcomment = 'BGP v4VRF enabled.'
                        elif AFIvar.get() == 3:
                            if "(" not in bgpproc.get():
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " \n")
                                sleep(2)
                                output = remote_conn.recv(2048).decode("utf-8")
                                sleep(2)
                                stripp = output.strip()
                                sleep(0.2)
                                if "not enabled" in stripp:
                                    remote_conn.send("exit \n")
                                    sleep(0.2)
                                    remote_conn.send("exit \n")
                                    sleep(0.2)
                                    tkMessageBox.showinfo('Error', 'IPv6 not running.. Please enable it first. Aborting.', parent=window)
                                    return
                                else:
                                    pass
                                sleep(0.2)
                                bgpcomment = 'BGP v6 enabled.'
                            else:
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " vrf " +  bgvrf + "\n")
                                sleep(2)
                                output = remote_conn.recv(2048).decode("utf-8")
                                sleep(2)
                                stripp = output.strip()
                                sleep(0.2)
                                if "not enabled" in stripp:
                                    remote_conn.send("exit \n")
                                    sleep(0.2)
                                    remote_conn.send("exit \n")
                                    sleep(0.2)
                                    tkMessageBox.showinfo('Error', 'IPv6 not running.. Please enable it first. Aborting.', parent=window)
                                    return
                                else:
                                    pass
                                sleep(0.2)
                                bgpcomment = 'BGP v6VRF enabled.'

                        elif AFIvar.get() == 4:
                            remote_conn.send("address-f vpnv4 " + SAFIopt.get() + " \n")
                            sleep(0.2)
                            bgpcomment = 'BGP vpnv4 enabled.'
                        else:
                            remote_conn.send("address-f vpnv6 " + SAFIopt.get() + " \n")
                            sleep(0.2)
                            bgpcomment = 'BGP vpnv6 enabled.'
                        
##                        remote_conn.send("conf t\n")
##                        sleep(0.5)
##                        if "(" not in bgpproc.get():
##                            remote_conn.send(defbgpcmd)
##                            if (AFIvar.get() == 1) and (SAFIopt.get() == "Unicast"):
##                                sleep(0.3)
##                            elif AFIvar.get() == 2:
##                                remote_conn.send("no bgp default ipv4-unicast \n")
##                                sleep(0.3)
##                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " \n")
##                                sleep(0.3)
##                                remote_conn.send("exit \n")
##                            elif AFIvar.get() == 3:
##                                remote_conn.send("no bgp default ipv4-unicast \n")
##                                sleep(0.3)
##                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " \n")
##                                sleep(0.3)
##                                remote_conn.send("exit \n")
##                            elif AFIvar.get() == 4:
##                                remote_conn.send("no bgp default ipv4-unicast \n")
##                                sleep(0.3)
##                                remote_conn.send("address-f vpnv4 " + SAFIopt.get() + " \n")
##                                sleep(0.3)
##                                remote_conn.send("exit \n")
##                            else:
##                                remote_conn.send("no bgp default ipv4-unicast \n")
##                                sleep(0.3)
##                                remote_conn.send("address-f vpnv6 " + SAFIopt.get() + " \n")
##                                sleep(0.3)
##                                remote_conn.send("exit \n")
##                            sleep(0.5)
##                            bgpcomment = 'BGP enabled.'
##                        else:
##                            remote_conn.send(vrfbgpcmd)
##                            sleep(0.5)
##                            bgpcomment = 'BGP VRF enabled.'

                        if (j != '') and (j != 'Neighbor IP') and (k != '') and (k != 'Neighbor AS no.'):
                            sleep(0.2)
                            if chk_localAS.get() == False:
                                remote_conn.send("neigh " + bgpneighip.get() + " remote-as " + bgpneigh.get() + " \n")
                                sleep(0.5)
                                bgpcomment = bgpcomment + ' Neighbor established.'
                            else:
                                remote_conn.send("neigh " + bgpneighip.get() + " local-as " + bgpneigh.get() + " \n")
                                sleep(0.5)
                                bgpcomment = bgpcomment + ' Neighbor (Local AS) established.'
                            remote_conn.send("no auto \n")
                            sleep(0.5)
                        else:
                            pass
                        if (l != '') and (m != '') and (m != 'eg. 255.255.255.0'):
                            sleep(0.5)
                            remote_conn.send("network " + bgpadv.get() + " mask " + bgpmask.get() + " \n")
                            sleep(0.5)
                            bgpcomment = bgpcomment + ' Network advertised.'
                        else:
                            pass
                        tkMessageBox.showinfo('BGP' + bgpproc.get(), bgpcomment, parent=window)
                        remote_conn.send("exit \n")
                        sleep(0.5)
                        remote_conn.send("exit \n")
                        #sleep(0.5)
                        #remote_conn.send("exit \n")
                      
            else:  
                if (i == '') or (i == 'eg. 15(MyVRF)'):
                    tkMessageBox.showinfo('Error' + bgpproc.get(), 'Error - Please enter a BGP PID (AS number)', parent=window)
                else:
                    remote_conn.send("sh ip proto | i bgp \n")
                    sleep(0.5)
                    output = remote_conn.recv(2048).decode("utf-8")
                    sleep(0.5)
                    stripp = output.strip()
                    sleep(0.5)
                    test = str(output)
                    test2 = re.findall(r'bgp (\w+)', test)
                    checkbgp = ''.join(test2)
                    if 'is "bgp' in stripp and ("(" not in bgpproc.get()) and (i not in checkbgp):
                        checkbgp = output.split("     ",1)[1]
                        bgprunningAS = str(checkbgp.partition('\n')[0])
                        sleep(0.5)
                        tkMessageBox.showinfo('Error', bgprunningAS + ' already exists. Please input correct AS number to remove.', parent=window)
                    elif 'is "bgp' in stripp and ("(" in bgpproc.get()) and ((i.split("(",1)[0]) not in checkbgp):
                        checkbgp = output.split("     ",1)[1]
                        bgprunningAS = str(checkbgp.partition('\n')[0])
                        sleep(0.5)
                        tkMessageBox.showinfo('Error', bgprunningAS + ' already exists. Please input correct AS number to remove.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.5)
                        if ((j == '') or (j == 'Neighbor IP')) and ((k == '') or (k == 'Neighbor AS no.')) and (l == '') and ((m == '') or \
                         (m == 'eg. 255.255.255.0')):
                            if "(" not in bgpproc.get():
                                if AFIvar.get() == 1:
                                    remote_conn.send("no " + defbgpcmd)
                                    sleep(0.3)
                                elif AFIvar.get() == 2:
                                    remote_conn.send(defbgpcmd)
                                    sleep(0.3)
                                    remote_conn.send("no address-f ipv4 " + SAFIopt.get() + " \n")
                                    sleep(0.3)
                                    remote_conn.send("exit \n")
                                elif AFIvar.get() == 3:
                                    remote_conn.send(defbgpcmd)
                                    sleep(0.3)
                                    remote_conn.send("no address-f vpnv4 " + SAFIopt.get() + " \n")
                                    sleep(0.3)
                                    remote_conn.send("exit \n")
                                elif AFIvar.get() == 4:
                                    remote_conn.send(defbgpcmd)
                                    sleep(0.3)
                                    remote_conn.send("no address-f ipv6 " + SAFIopt.get() + " \n")
                                    sleep(0.3)
                                    remote_conn.send("exit \n")
                                else:
                                    remote_conn.send(defbgpcmd)
                                    sleep(0.3)
                                    remote_conn.send("no address-f vpnv6 " + SAFIopt.get() + " \n")
                                    sleep(0.3)
                                    remote_conn.send("exit \n")
                            else:
                                remote_conn.send("router bgp " + bgvrfpid)
                                sleep(0.5)
                                remote_conn.send("no address-f ipv4 vrf " + bgvrf + " \n ")
                                sleep(0.5)
                                remote_conn.send("exit \n")
                            sleep(0.5)
                            tkMessageBox.showinfo('BGP', 'BGP ' + bgpproc.get() + ' disabled', parent=window)
                        else:
                            bgpcomment = ''
                            if "(" not in bgpproc.get():
                                remote_conn.send(defbgpcmd)
                                sleep(0.3)
                                if AFIvar.get() == 1:
                                    sleep(0.3)
                                elif AFIvar.get() == 2:
                                    remote_conn.send("address-f ipv4 " + SAFIopt.get() + " \n")
                                    sleep(0.3)
                                elif AFIvar.get() == 3:
                                    remote_conn.send("address-f vpnv4 " + SAFIopt.get() + " \n")
                                    sleep(0.3)
                                elif AFIvar.get() == 4:
                                    remote_conn.send("address-f ipv6 " + SAFIopt.get() + " \n")
                                    sleep(0.3)
                                else:
                                    remote_conn.send("address-f vpnv6 " + SAFIopt.get() + " \n")
                                    sleep(0.3)
                            else:
                                remote_conn.send(vrfbgpcmd)
                                sleep(0.3)
                            if (j != '') and (j != 'Neighbor IP') and (k != '') and (k != 'Neighbor AS no.'):
                                sleep(0.5)
                                if chk_localAS.get() == False: 
                                    remote_conn.send("no neigh " + bgpneighip.get() + " remote-as " + bgpneigh.get() + " \n")
                                    sleep(0.5)
                                    bgpcomment = bgpcomment + ' BGP neighbor removed.'
                                else:
                                    remote_conn.send("no neigh " + bgpneighip.get() + " local-as " + bgpneigh.get() + " \n")
                                    sleep(0.5)                                    
                                    bgpcomment = bgpcomment + ' BGP (Local AS) neighbor removed.'
                            else:
                                pass
                            if (l != '') and (m != '') and (m != 'eg. 255.255.255.0'):
                                sleep(0.5)
                                remote_conn.send("no network " + bgpadv.get() + " mask " + bgpmask.get() + " \n")
                                sleep(0.5)
                                bgpcomment = bgpcomment + ' Network unadvertised.'
                            else:
                                pass
                            if (AFIvar.get() != 1):
                                sleep(0.3)
                                remote_conn.send("exit \n")
                            else:
                                pass
                            if AFIvar.get() == 1:
                                sleep(0.5)
                                remote_conn.send("exit \n")
                            else:
                                sleep(0.5)
                                remote_conn.send("exit \n")
                                sleep(0.5)
                                remote_conn.send("exit \n")
                            tkMessageBox.showinfo('BGP ' + bgpproc.get(), bgpcomment, parent=window)
                        sleep(0.5)
                        remote_conn.send("exit \n")
                        #sleep(0.5)
                        #remote_conn.send("exit \n")
        btn = Button(BGPframe, text="Enable/Advertise", font=('helvetica', 8), bg="orange", command=enbgp)
        btn.grid(column=2, row=2)




        def option_changed_getBGPoptdevice(*args):
            if getBGPoptdevice.get() == "Router-ID":
                text = 'eg. 1.1.1.1'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in)
            elif getBGPoptdevice.get() == "*Basic timers":
                text = '<hello> <hold> (sec)'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in)
            elif getBGPoptdevice.get() == "Scan timer":
                text = '<5-60> (sec)'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "*Update Source":
                text = 'eg. lo0'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "*TTL Sec":
                text = '<1-254 (hops)>'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "*Password":
                text = 'eg. MyPassword'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "Create Peer Grp":
                text = 'eg. MyPeerGroup'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "*Enable Peer Grp":
                text = 'eg. MyPeerGroup'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "*Transport mode":
                text = 'Active | Passive'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in)
            elif getBGPoptdevice.get() == "*Max Prefixes":
                text = 'eg. 20'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "Max AS":
                text = 'eg. 50'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "Max Paths":
                text = 'eg. 5'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "AD(ext int loc)":
                text = '<1-255> <1-255> <1-255>'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "Selective AD(ext)":
                text = '<1-255> <net> <wildcard> [acl_no.]'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in)
            elif getBGPoptdevice.get() == "Summary route":
                text = '<net> <mask> [summary-only] [route-m <>]'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "*Adv filter":
                text = '<pfxlist> in/out'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "*AS Path filter":
                text = '<ASPATH_acl_no.> in/out'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "*Path Control" or getBGPoptdevice.get() == "*Community:":
                text = '<r-map-name> in/out'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            elif getBGPoptdevice.get() == "Conditional adv":
                text = '<r-map1(to adv)> <r-map2(if nonexist)>'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in)
            elif getBGPoptdevice.get() == "Conditional de-agg":
                text = '<r-map1(to adv)> <r-map2(if exist)>'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in)
            elif getBGPoptdevice.get() == "Dampening":
                text = '<half-life><reuse><suppress><max-suppr>'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 
            else:
                text = 'NoInputRequired'
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if bgpoptvalue1.cget('fg') != 'black':
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='black')
                def handle_focus_out(_):
                    if bgpoptvalue1.get() == "":
                        bgpoptvalue1.delete(0, END)
                        bgpoptvalue1.config(fg='grey')
                        bgpoptvalue1.insert(0, text)
                bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
                bgpoptvalue1.bind("<FocusIn>", handle_focus_in) 

                
        OPTIONS = [
        "Router-ID",
        "Auto Summary",
        "Synchronization",
        "*AF Activate",
        "*Basic timers",
        "Scan timer",
        "*Next-hop self",
        "*Update Source",
        "*TTL Sec",
        "*Password",
        "Create Peer Grp",
        "*Enable Peer Grp",
        "*ReflectorClient",
        "*Transport mode",
        "*Soft-reconfig in",
        "*Propagate * route",
        "*Max Prefixes",
        "Max AS",
        "Max Paths",
        "AD(ext int loc)",
        "Selective AD(ext)",
        "Summary route",
        "*Adv filter",
        "*AS Path filter",
        "*Path Control",
        "*Community",
        "Send Ext Comm.",
        "Conditional adv",
        "Conditional de-agg",
        "Dampening",
        "Neighbor logging",
        "*Shut Peer",
        "BFD"
        ]
        getBGPoptdevice = StringVar(BGPframe)
        getBGPoptdevice.set(OPTIONS[0])    # default value
        getBGPoptdevice.trace("w", option_changed_getBGPoptdevice)
        dropbox2 = OptionMenu(BGPframe, getBGPoptdevice, *OPTIONS)
        dropbox2.grid(column=0, row=9)

        bgpoptvalue1 = Entry(BGPframe, bg='white', width=35, fg='grey')
        bgpoptvalue1.grid(column=1, row=9, columnspan=4, sticky='w')
        bgpoptvalue1.config(font=("TkDefaultFont", 8))
        bgpoptvalue1.insert(0, "eg. 1.1.1.1")
        def handle_focus_in(_):
            if bgpoptvalue1.cget('fg') != 'black':
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='black')
        def handle_focus_out(_):
            if bgpoptvalue1.get() == "":
                bgpoptvalue1.delete(0, END)
                bgpoptvalue1.config(fg='grey')
                bgpoptvalue1.insert(0, "eg. 1.1.1.1")    
        bgpoptvalue1.bind("<FocusOut>", handle_focus_out)
        bgpoptvalue1.bind("<FocusIn>", handle_focus_in)
        


        
        def bgpotheropt():
            vrffind = bgpproc.get()
            bgvrf = vrffind[vrffind.find("(")+1:vrffind.find(")")]
            bgvrfpid = ""
            if "(" in bgpproc.get():
                bgvrfpid = vrffind.split("(",1)[0]
            else:
                pass
            defbgpcmd = "router bgp " + bgpproc.get() + " \n"
            vrfbgpcmd = "router bgp " + bgvrfpid + " \n " + "address-f ipv4 vrf " + bgvrf + " \n "
            i = bgpproc.get()
            j = bgpneighip.get()
            if chk_state_neg.get() == False:
                if (i == '') or (i == 'eg. 15(MyVRF)') or (j == '') or (j == 'Neighbor IP'):
                    tkMessageBox.showinfo('Error' + bgpproc.get(), 'Error - Please enter a BGP PID (AS number) and Neighbor IP', parent=window)
                else:
                    remote_conn.send("sh ip proto | i bgp \n")
                    sleep(0.5)
                    output = remote_conn.recv(2048).decode("utf-8")
                    sleep(0.5)
                    stripp = output.strip()
                    sleep(0.5)
                    test = str(output)
                    test2 = re.findall(r'bgp (\w+)', test)
                    checkbgp = ''.join(test2)
                    if 'is "bgp' in stripp and ((("(" not in bgpproc.get()) and (i not in checkbgp)) or (("(" in bgpproc.get()) and \
                                                                                                   ((i.split("(",1)[0]) not in checkbgp))):
                        sleep(0.5)
                        tkMessageBox.showinfo('Error', 'BGP AS ' + checkbgp + ' already exists. Only 1 BGP AS/process can be running at any time.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("ip bgp-comm new-f \n")
                        sleep(0.2)    
                        if "(" not in bgpproc.get():
                            if AFIvar.get() == 1:
                                remote_conn.send(defbgpcmd)
                                sleep(0.3)
                            elif AFIvar.get() == 2:
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " \n")
                                sleep(0.3)
                            elif AFIvar.get() == 3:
                                remote_conn.send("address-f vpnv4 " + SAFIopt.get() + " \n")
                                sleep(0.3)
                            elif AFIvar.get() == 4:
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " \n")
                                sleep(0.3)
                            else:
                                remote_conn.send("address-f vpnv6 " + SAFIopt.get() + " \n")
                                sleep(0.3)
                        else:
                            remote_conn.send(vrfbgpcmd)

                        if getBGPoptdevice.get() == "Router-ID":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. 1.1.1.1":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("bgp router-id" + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Router-id has been configured.', parent=window)
                        elif getBGPoptdevice.get() == "Auto Summary":
                            remote_conn.send("auto \n")
                            tkMessageBox.showinfo('BGP', 'Auto summarization has been enabled.', parent=window)
                        elif getBGPoptdevice.get() == "Synchronization":
                            remote_conn.send("sync \n")
                            tkMessageBox.showinfo('BGP', 'Synchronization has been enabled.', parent=window)                         
                        elif getBGPoptdevice.get() == "*Activate":
                            remote_conn.send("neighbor " + bgpneighip.get() + " activate \n")
                            tkMessageBox.showinfo('BGP', 'Neighbor AF has been activated.', parent=window)
                        elif getBGPoptdevice.get() == "*Next-hop self":
                            remote_conn.send("neighbor " + bgpneighip.get() + " next-hop-s \n")
                            tkMessageBox.showinfo('BGP', 'Network updates toward neighbor will utilize the source IP address of this router.', parent=window)
                        elif getBGPoptdevice.get() == "*Basic timers":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<hello> <hold> (sec)":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neighbor " + bgpneighip.get() + " timers " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Keepalive & Hold timers has been configured.', parent=window)
                        elif getBGPoptdevice.get() == "Scan timer":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<5-60> (sec)":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("bgp scan-time " + bgpoptvalue1.get() + " \n")                            
                                tkMessageBox.showinfo('BGP', 'Scan timer has been configured. This timer will scan BGP table for changes.', parent=window)
                        elif getBGPoptdevice.get() == "*Update Source":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. lo0":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neighbor " + bgpneighip.get() + " update-so " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'All BGP updates will be sent from interface ' + bgpoptvalue1.get() + '.', parent=window)
                        elif getBGPoptdevice.get() == "*TTL Sec":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<1-254 (hops)>":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neighbor " + bgpneighip.get() + " ttl-sec hops " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'TTL Security has been activated.', parent=window)
                        elif getBGPoptdevice.get() == "*Password":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. MyPassword":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neighbor " + bgpneighip.get() + " password " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'MD5 password has been configured for this peer.', parent=window)
                        elif getBGPoptdevice.get() == "Create Peer Grp":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. MyPeerGroup":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neighbor " + bgpoptvalue1.get() + " peer-group \n")
                                tkMessageBox.showinfo('BGP', 'Peer Group has been created.', parent=window)
                        elif getBGPoptdevice.get() == "*Enable Peer Grp":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. MyPeerGroup":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neighbor " + bgpneighip.get() + " peer-gro " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Peer Group has been configured on neighbor.', parent=window)                            
                        elif getBGPoptdevice.get() == "*ReflectorClient":
                            remote_conn.send("neighbor " + bgpneighip.get() + " route-ref \n")
                            tkMessageBox.showinfo('BGP', 'Neighbor has been configured as a route reflector client.', parent=window)
                        elif getBGPoptdevice.get() == "*Transport mode":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "Active | Passive":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neighbor " + bgpneighip.get() + " transport connection-m " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Transport state configured.', parent=window)
                        elif getBGPoptdevice.get() == "*Soft-reconfig in":
                            remote_conn.send("neighbor " + bgpneighip.get() + " soft-reconfig in \n")
                            tkMessageBox.showinfo('BGP', 'Soft reconfiguration enabled. You now can Reset BGP(soft) to use this feature.', parent=window)
                        elif getBGPoptdevice.get() == "*Propagate * route":
                            remote_conn.send("default-info orig \n")
                            tkMessageBox.showinfo('BGP', 'Default route has been propagated.', parent=window)
                        elif getBGPoptdevice.get() == "*Max Prefixes":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. 20":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neighbor " + bgpneighip.get() + " maximum-pref " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Maximum prefixes able to be learnt has been configured.', parent=window)
                        elif getBGPoptdevice.get() == "Max AS":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. 50":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("bgp maxas-limit " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Maximum ASes able to be learnt has been configured.', parent=window)
                        elif getBGPoptdevice.get() == "Max Paths":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. 5":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("maximum-paths " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Maximum paths for iBGP ECMP has been configured.', parent=window)                            
                        elif getBGPoptdevice.get() == "AD(ext int loc)":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<1-255> <1-255> <1-255>":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("distance bgp " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Administrative distance for eBGP, iBGP and local routes has been configured.', parent=window)
                        elif getBGPoptdevice.get() == "Selective AD(ext)":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<1-255> <net> <wildcard> [acl_no.]":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("distance " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'eBGP administrative distance for a specific network has been configured.', parent=window)
                        elif getBGPoptdevice.get() == "Summary route":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<net> <mask> [summary-only] [route-m <>]":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("aggregate-addr " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Aggregate/summarized address has been configured.', parent=window)
                        elif getBGPoptdevice.get() == "*Adv filter":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<pfxlist> in/out":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neighbor " + bgpneighip.get() + " prefix-l " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Prefix list has been configured to filter updates.', parent=window)
                        elif getBGPoptdevice.get() == "*AS Path filter":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<ASPATH_acl_no.> in/out":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neighbor " + bgpneighip.get() + " filter-l " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Filter list has been configured to filter updates.', parent=window)
                        elif getBGPoptdevice.get() == "*Path Control":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<r-map-name> in/out":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neighbor " + bgpneighip.get() + " route-m " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Path control configured. NOTE: Basic ones are Weight, LocalPref, AS prepending and MED.', parent=window)
                        elif getBGPoptdevice.get() == "*Community":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<r-map-name> in/out":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("neigh " + bgpneighip.get() + " send-community \n")
                                sleep(0.5)
                                remote_conn.send("neigh " + bgpneighip.get() + " route-m " + bgpoptvalue1.get() + " \n")
                                sleep(0.5)
                                tkMessageBox.showinfo('BGP', 'Community has been configured. NOTE: New format enabled (eg. xx:xx) and send-community\
enabled. Remember to create a route-map to "set community" for appending community info to your ADVERTISED routes, or create community-lists and route-map\
to "match" RECEIVED communities from peer routes to set a policy. Check w/ your provider for info on those community values.', parent=window)
                        elif getBGPoptdevice.get() == "Send Ext Comm.":
                                remote_conn.send("neigh " + bgpneighip.get() + " send-comm ext \n")
                                sleep(0.5)
                                tkMessageBox.showinfo('BGP', 'Extended communities (eg. route-target info) are being sent.', parent=window)
                        elif getBGPoptdevice.get() == "Conditional adv":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<r-map1(to adv)> <r-map2(if nonexist)>":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                optstr = bgpoptvalue1.get()
                                rtemap1 = optstr.split(" ",1)[0]
                                rtemap2 = optstr.split(" ",1)[1]
                                remote_conn.send("neigh " + bgpneighip.get() + " advertise-map " + rtemap1 + " non-exist-map "\
                                                 + rtemap2 + " \n")
                                tkMessageBox.showinfo('BGP', 'Conditional advertisement configured - rte-map ' + bgpoptvalue1.get() + ' will be advertised \
when rte-map ' + bgpoptvalue2.get() + ' is not in the BGP routing table.', parent=window)
                        elif getBGPoptdevice.get() == "Conditional de-agg":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<r-map1(to adv)> <r-map2(if exist)>":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                optstr = bgpoptvalue1.get()
                                rtemap1 = optstr.split(" ",1)[0]
                                rtemap2 = optstr.split(" ",1)[1]
                                remote_conn.send("neigh " + bgpneighip.get() + " inject-map " + rtemap1 + " exist-map "\
                                                 + rtemap2 + " \n")
                                tkMessageBox.showinfo('BGP', 'Conditional de-aggregate advertisement configured - rte-map ' + bgpoptvalue1.get() + ' \
(specific pfx) will be advertised when rte-map ' + bgpoptvalue2.get() + ' (aggregate pfx) is in the BGP routing table.', parent=window)
                        elif getBGPoptdevice.get() == "Dampening":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<half-life><reuse><suppress><max-suppr>":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("bgp dampening " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Route dampening has been enabled. NOTE: You can also create route map to "match" specific\
routes and "set dampening ..." to dampen them.', parent=window)
                        elif getBGPoptdevice.get() == "Neighbor logging":
                            remote_conn.send("bgp log-neigh \n")
                            sleep(0.5)
                            tkMessageBox.showinfo('BGP logging', 'Neighbor changes are being logged.', parent=window)
                        elif getBGPoptdevice.get() == "*Shut Peer":
                            remote_conn.send("neigh " + bgpneighip.get() + " shut \n")
                            sleep(0.5)
                            tkMessageBox.showinfo('BGP', 'Peering has been shutdown.', parent=window)
                        else:
                            remote_conn.send("neigh " + bgpneighip.get() + " fall-over bfd \n")
                            sleep(0.3)
                            tkMessageBox.showinfo('BFD', 'BFD monitoring enabled for neighbor.', parent=window)

            else:
                if (i == '') or (i == 'eg. 15(MyVRF)') or (j == '') or (j == 'Neighbor IP'):
                    tkMessageBox.showinfo('Error' + bgpproc.get(), 'Error - Please enter a BGP PID (AS number) and Neighbor IP', parent=window)
                else:
                    remote_conn.send("sh ip proto | i bgp \n")
                    sleep(0.5)
                    output = remote_conn.recv(2048).decode("utf-8")
                    sleep(0.5)
                    stripp = output.strip()
                    sleep(0.5)
                    test = str(output)
                    test2 = re.findall(r'bgp (\w+)', test)
                    checkbgp = ''.join(test2)
                    if 'is "bgp' in stripp and ((("(" not in bgpproc.get()) and (i not in checkbgp)) or (("(" in bgpproc.get()) and \
                                                                                                   ((i.split("(",1)[0]) not in checkbgp))):
                        sleep(0.5)
                        tkMessageBox.showinfo('Error', 'BGP AS ' + checkbgp + ' already exists. Only 1 BGP AS/process can be running at any time.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.5)
                        if "(" not in bgpproc.get():
                            if AFIvar.get() == 1:
                                remote_conn.send(defbgpcmd)
                                sleep(0.3)
                            elif AFIvar.get() == 2:
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " \n")
                                sleep(0.3)
                            elif AFIvar.get() == 3:
                                remote_conn.send("address-f vpnv4 " + SAFIopt.get() + " \n")
                                sleep(0.3)
                            elif AFIvar.get() == 4:
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " \n")
                                sleep(0.3)
                            else:
                                remote_conn.send("address-f vpnv6 " + SAFIopt.get() + " \n")
                                sleep(0.3)
                        else:
                            remote_conn.send(vrfbgpcmd)

                        if getBGPoptdevice.get() == "Router-ID":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. 1.1.1.1":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no bgp router-id" + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Router-id has been removed.', parent=window)
                        elif getBGPoptdevice.get() == "Auto Summary":
                            remote_conn.send("no auto \n")
                            tkMessageBox.showinfo('BGP', 'Auto summarization has been disabled.', parent=window)
                        elif getBGPoptdevice.get() == "Synchronization":
                            remote_conn.send("no sync \n")
                            tkMessageBox.showinfo('BGP', 'Synchronization has been disabled.', parent=window)                  
                        elif getBGPoptdevice.get() == "*Activate":
                            tkMessageBox.showinfo('BGP', 'ERROR / WARNING: This command has been removed for safety; deactivating an AF will also\
delete all config associated along with that specific AF.', parent=window)
                        elif getBGPoptdevice.get() == "*Next-hop self":
                            remote_conn.send("neighbor " + bgpneighip.get() + " next-hop-unc \n")
                            tkMessageBox.showinfo('BGP', 'Network updates toward neighbor will utilize the source IP address of the "originating" router.', parent=window)
                        elif getBGPoptdevice.get() == "*Basic timers":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<hello> <hold> (sec)":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neighbor " + bgpneighip.get() + " timers " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Keepalive & Hold timers has been reset.', parent=window)
                        elif getBGPoptdevice.get() == "Scan timer":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<5-60> (sec)":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no bgp scan-time " + bgpoptvalue1.get() + " \n")                            
                                tkMessageBox.showinfo('BGP', 'Scan timer has been reset.', parent=window)
                        elif getBGPoptdevice.get() == "*Update Source":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. lo0":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neighbor " + bgpneighip.get() + " update-so " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'All BGP updates will NOT be sent from interface ' + bgpoptvalue1.get() + '.', parent=window)
                        elif getBGPoptdevice.get() == "*TTL Sec":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<1-254 (hops)>":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neighbor " + bgpneighip.get() + " ttl-sec hops " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'TTL Security has been deactivated.', parent=window)
                        elif getBGPoptdevice.get() == "*Password":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. MyPassword":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neighbor " + bgpneighip.get() + " password " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'MD5 password has been removed for this peer.', parent=window)
                        elif getBGPoptdevice.get() == "Create Peer Grp":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. MyPeerGroup":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neighbor " + bgpneighip.get() + " " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Peer Group has been deleted.', parent=window)
                        elif getBGPoptdevice.get() == "*Enable Peer Grp":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. MyPeerGroup":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neighbor " + bgpneighip.get() + " peer-g " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Peer Group has been disabled.', parent=window)                            
                        elif getBGPoptdevice.get() == "*ReflectorClient":
                            remote_conn.send("no neighbor " + bgpneighip.get() + " route-ref \n")
                            tkMessageBox.showinfo('BGP', 'Neighbor is no longer a route reflector client.', parent=window)
                        elif getBGPoptdevice.get() == "*Transport mode":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "Active | Passive":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neighbor " + bgpneighip.get() + " transport connection-m " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Transport state reset.', parent=window)
                        elif getBGPoptdevice.get() == "*Soft-reconfig in":
                            remote_conn.send("no neighbor " + bgpneighip.get() + " soft-reconfig in \n")
                            tkMessageBox.showinfo('BGP', 'Soft reconfiguration disabled. You now can Reset BGP(soft) to use this feature.', parent=window)
                        elif getBGPoptdevice.get() == "*Propagate * route":
                            remote_conn.send("no default-info orig \n")
                            tkMessageBox.showinfo('BGP', 'Default route is no longer propagated.', parent=window)
                        elif getBGPoptdevice.get() == "*Max Prefixes":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "eg. 20":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neighbor " + bgpneighip.get() + " maximum-pref " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Maximum prefixes able to be learnt has been removed.', parent=window)
                        elif getBGPoptdevice.get() == "Max AS":
                            remote_conn.send("no bgp maxas-limit \n")
                            tkMessageBox.showinfo('BGP', 'Maximum ASes able to be learnt has been reset.', parent=window)
                        elif getBGPoptdevice.get() == "Max Paths":
                            remote_conn.send("no maximum-paths " + bgpoptvalue1.get() + " \n")
                            tkMessageBox.showinfo('BGP', 'Maximum paths for BGP ECMP has been reset.', parent=window)                          
                        elif getBGPoptdevice.get() == "AD(ext int loc)":
                            remote_conn.send("no distance bgp \n")
                            tkMessageBox.showinfo('BGP', 'Administrative distance for eBGP, iBGP and local routes has been reset.', parent=window)
                        elif getBGPoptdevice.get() == "Selective AD(ext)":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<1-255> <net> <wildcard> [acl_no.]":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no distance " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'eBGP administrative distance for a specific network has been removed.', parent=window)
                        elif getBGPoptdevice.get() == "Summary route":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<net> <mask> [summary-only] [route-m <>]":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no aggregate-addr " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Aggregate/summarized address has been removed.', parent=window)
                        elif getBGPoptdevice.get() == "*Adv filter":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<pfxlist> in/out":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neighbor " + bgpneighip.get() + " prefix-l " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Prefix list has been removed.', parent=window)
                        elif getBGPoptdevice.get() == "*AS Path filter":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<ASPATH_acl_no.> in/out":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neighbor " + bgpneighip.get() + " filter-l " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Filter list has been removed.', parent=window)
                        elif getBGPoptdevice.get() == "*Path Control":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<r-map-name> in/out":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neighbor " + bgpneighip.get() + " route-m " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Path control removed. HINT: Basic ones are Weight, LocalPref, AS prepending and MED.', parent=window)
                        elif getBGPoptdevice.get() == "*Community":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<r-map-name> in/out":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no neigh " + bgpneighip.get() + " route-m " + bgpoptvalue1.get() + " \n")
                                sleep(0.5)
                                tkMessageBox.showinfo('BGP', 'Community has been removed. NOTE: send-community will still be enabled.', parent=window)
                        elif getBGPoptdevice.get() == "Send Ext Comm.":
                                remote_conn.send("no neigh " + bgpneighip.get() + " send-comm ext \n")
                                sleep(0.5)
                                tkMessageBox.showinfo('BGP', 'Extended communities (eg. route-target info) are NOT being sent.', parent=window)
                        elif getBGPoptdevice.get() == "Conditional adv":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<r-map1(to adv)> <r-map2(if nonexist)>":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                optstr = bgpoptvalue1.get()
                                rtemap1 = optstr.split(" ",1)[0]
                                rtemap2 = optstr.split(" ",1)[1]
                                remote_conn.send("no neigh " + bgpneighip.get() + " advertise-map " + rtemap1 + " non-exist-map "\
                                                 + rtemap2 + " \n")
                                tkMessageBox.showinfo('BGP', 'Conditional advertisement removed.', parent=window)
                        elif getBGPoptdevice.get() == "Conditional de-agg":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<r-map1(to adv)> <r-map2(if exist)>":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                optstr = bgpoptvalue1.get()
                                rtemap1 = optstr.split(" ",1)[0]
                                rtemap2 = optstr.split(" ",1)[1]
                                remote_conn.send("no neigh " + bgpneighip.get() + " inject-map " + rtemap1 + " exist-map "\
                                                 + rtemap2 + " \n")
                                tkMessageBox.showinfo('BGP', 'Conditional de-aggregate advertisement removed.', parent=window)
                        elif getBGPoptdevice.get() == "Dampening":
                            if bgpoptvalue1.get() == "" or bgpoptvalue1.get() == "<half-life><reuse><suppress><max-suppr>":
                                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                            else:
                                remote_conn.send("no bgp dampening " + bgpoptvalue1.get() + " \n")
                                tkMessageBox.showinfo('BGP', 'Route dampening has been disabled.', parent=window)
                        elif getBGPoptdevice.get() == "Neighbor logging":
                            remote_conn.send("no bgp log-neigh \n")
                            sleep(0.5)
                            tkMessageBox.showinfo('BGP logging', 'Neighbor changes are NOT being logged.', parent=window)
                        elif getBGPoptdevice.get() == "*Shut Peer":
                            remote_conn.send("no neigh " + bgpneighip.get() + " shut \n")
                            sleep(0.5)
                            tkMessageBox.showinfo('BGP', 'Peering has been re-enabled.', parent=window)
                        else:
                            remote_conn.send("no neigh " + bgpneighip.get() + " fall-over bfd \n")
                            sleep(0.3)
                            tkMessageBox.showinfo('BFD', 'BFD monitoring disabled for neighbor.', parent=window)                            
            remote_conn.send("exit \n")
            sleep(0.5)
            remote_conn.send("exit \n")
            sleep(0.5)
        btn = Button(BGPframe, text="Aplicar", bg="orange", command=bgpotheropt)
        btn.grid(column=5, row=9)


        OPTIONS = [
        "RIP",
        "OSPF",
        "EIGRP",
        "BGP"
        ]
        getBGPoptredist = StringVar(BGPframe)
        getBGPoptredist.set(OPTIONS[0])    # default value
        dropbox2 = OptionMenu(BGPframe, getBGPoptredist, *OPTIONS)   
        dropbox2.grid(column=0, row=10)
        
        bgpredisttoprocnum = Entry(BGPframe, bg='white', width=13, fg='grey')
        bgpredisttoprocnum.place(x=148, y=141)
        bgpredisttoprocnum.insert(0, "eg. 15(MyVRF)")
        def handle_focus_in(_):
            if bgpredisttoprocnum.cget('fg') != 'black':
                bgpredisttoprocnum.delete(0, END)
                bgpredisttoprocnum.config(fg='black')
        def handle_focus_out(_):
            if bgpredisttoprocnum.get() == "":
                bgpredisttoprocnum.delete(0, END)
                bgpredisttoprocnum.config(fg='grey')
                bgpredisttoprocnum.insert(0, "eg. 15(MyVRF)")    
        bgpredisttoprocnum.bind("<FocusOut>", handle_focus_out)
        bgpredisttoprocnum.bind("<FocusIn>", handle_focus_in)
        
        bgpredistFilter = Entry(BGPframe, bg='white', width=6, fg='grey')
        bgpredistFilter.place(x=239, y=141)
        bgpredistFilter.insert(0, "r-map")
        def handle_focus_in(_):
            if bgpredistFilter.cget('fg') != 'black':
                bgpredistFilter.delete(0, END)
                bgpredistFilter.config(fg='black')
        def handle_focus_out(_):
            if bgpredistFilter.get() == "":
                bgpredistFilter.delete(0, END)
                bgpredistFilter.config(fg='grey')
                bgpredistFilter.insert(0, "r-map")    
        bgpredistFilter.bind("<FocusOut>", handle_focus_out)
        bgpredistFilter.bind("<FocusIn>", handle_focus_in)
        
        bgpredistMetric = Entry(BGPframe, bg='white', width=6, fg='grey')
        bgpredistMetric.place(x=285, y=141)
        bgpredistMetric.insert(0, "Metric")
        def handle_focus_in(_):
            if bgpredistMetric.cget('fg') != 'black':
                bgpredistMetric.delete(0, END)
                bgpredistMetric.config(fg='black')
        def handle_focus_out(_):
            if bgpredistMetric.get() == "":
                bgpredistMetric.delete(0, END)
                bgpredistMetric.config(fg='grey')
                bgpredistMetric.insert(0, "Metric")    
        bgpredistMetric.bind("<FocusOut>", handle_focus_out)
        bgpredistMetric.bind("<FocusIn>", handle_focus_in)

        bgpredistTag = Entry(BGPframe, bg='white', width=5, fg='grey')
        bgpredistTag.grid(column=4, row=10)
        bgpredistTag.insert(0, "Tag")
        def handle_focus_in(_):
            if bgpredistTag.cget('fg') != 'black':
                bgpredistTag.delete(0, END)
                bgpredistTag.config(fg='black')
        def handle_focus_out(_):
            if bgpredistTag.get() == "":
                bgpredistTag.delete(0, END)
                bgpredistTag.config(fg='grey')
                bgpredistTag.insert(0, "Tag")    
        bgpredistTag.bind("<FocusOut>", handle_focus_out)
        bgpredistTag.bind("<FocusIn>", handle_focus_in)
        
        def bgpredistribute():
            vrffind = bgpproc.get()
            PIDextract = re.search(r'\d+', vrffind).group()
            bgvrf = vrffind[vrffind.find("(")+1:vrffind.find(")")]
            bgvrfpid = ""
            if "(" in bgpproc.get():
                bgvrfpid = vrffind.split("(",1)[0]
            else:
                pass
            defbgpcmd = "router bgp " + bgpproc.get() + "\n"
            defbgpcmd2 = "router bgp " + PIDextract + "\n"
            vrfbgpcmd = "router bgp " + bgvrfpid + " \n " + "address-f ipv4 vrf " + bgvrf + " \n "
            
            vrffind2 = bgpredisttoprocnum.get()
            PIDextract = re.search(r'\d+', vrffind2).group()
            bgvrf2 = vrffind2[vrffind2.find("(")+1:vrffind2.find(")")]            
            redistcmd = "redistribute " + getBGPoptredist.get() + " " + PIDextract
            redistRIPcmd = "redistribute " + getBGPoptredist.get()
            redistospfvrfcmd = "redistribute " + getBGPoptredist.get() + " " + PIDextract +  " vrf " + bgvrf2


            
            if chk_state_neg.get() == False:
                if getBGPoptredist.get() == "RIP" or getBGPoptredist.get() == "EIGRP" or getBGPoptredist.get() == "BGP":
                    if bgpproc.get() == "" or bgpproc.get() == "eg. 15(MyVRF)":
                        tkMessageBox.showinfo('Error', 'Please also enter the BGP process ID above.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.2)
                        if "(" not in bgpproc.get():
                            remote_conn.send(defbgpcmd)
                        else:
                            remote_conn.send(defbgpcmd2)
                        sleep(0.3)
                        if AFIvar.get() == 1:
                            if "(" not in bgpproc.get():
                                pass
                            else:
                                remote_conn.send("exit \n")
                                sleep(0.2)
                                remote_conn.send("exit \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Error', 'Please select either an IPv4 or IPv6 AF to Aplicar VRFs.', parent=window)
                                return
                        elif AFIvar.get() == 2:
                            if "(" not in bgpproc.get():
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " \n")
                            else:
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " vrf " +  bgvrf2 + "\n")
                        elif AFIvar.get() == 3:
                            remote_conn.send("address-f vpnv4 " + SAFIopt.get() + " \n")
                        elif AFIvar.get() == 4:
                            if "(" not in bgpproc.get():
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " \n")
                            else:
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " vrf " +  bgvrf2 + "\n")
                        else:
                            remote_conn.send("address-f vpnv6 " + SAFIopt.get() + " \n")

                        if getBGPoptredist.get() == "RIP":
                            cmd = redistRIPcmd
                        else:
                            cmd = redistcmd
                        
                        sleep(0.2)
                        remote_conn.send("bgp redistribute-internal \n")
                        sleep(0.2)
                        if bgpredistFilter.get() != "" and bgpredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + bgpredistFilter.get()
                        else:
                            pass
                        if bgpredistMetric.get() != "" and bgpredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + bgpredistMetric.get()
                        else:
                            pass
                        if bgpredistTag.get() != "" and bgpredistTag.get() != "Tag":
                            cmd = cmd + " tag " + bgpredistTag.get()
                        else:
                            pass
                        remote_conn.send(cmd + "\n")
                        sleep(0.2)
                        if "(" in bgpproc.get() and (AFIvar.get() == 2 or AFIvar.get() == 4):
                            sleep(0.2)
                            remote_conn.send("exit \n")
                        else:
                            pass
                        tkMessageBox.showinfo('BGP redistribution', 'Learned ' + getBGPoptredist.get() + '.', parent=window)
                else:
                    if bgpproc.get() == "" or bgpproc.get() == "eg. 15(MyVRF)":
                        tkMessageBox.showinfo('Error', 'Please also enter the BGP process ID above.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.2)
                        if "(" not in bgpproc.get():
                            remote_conn.send(defbgpcmd)
                        else:
                            remote_conn.send(defbgpcmd2)
                        sleep(0.3)
                        if AFIvar.get() == 1:
                            if "(" not in bgpproc.get():
                                pass
                            else:
                                remote_conn.send("exit \n")
                                sleep(0.2)
                                remote_conn.send("exit \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Error', 'Please select either an IPv4 or IPv6 AF to Aplicar VRFs.', parent=window)
                                return
                        elif AFIvar.get() == 2:
                            if "(" not in bgpproc.get():
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " \n")
                            else:
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " vrf " +  bgvrf2 + "\n")
                        elif AFIvar.get() == 3:
                            remote_conn.send("address-f vpnv4 " + SAFIopt.get() + " \n")
                        elif AFIvar.get() == 4:
                            if "(" not in bgpproc.get():
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " \n")
                            else:
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " vrf " +  bgvrf2 + "\n")
                        else:
                            remote_conn.send("address-f vpnv6 " + SAFIopt.get() + " \n")

                            
                        sleep(0.2)
                        remote_conn.send("bgp redistribute-internal \n")
                        sleep(0.2)
                        if "(" not in bgpredisttoprocnum.get():
                            cmd = redistcmd
                        else:
                            cmd = redistospfvrfcmd
                        if bgpredistFilter.get() != "" and bgpredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + bgpredistFilter.get()
                        else:
                            pass
                        if bgpredistMetric.get() != "" and bgpredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + bgpredistMetric.get()
                        else:
                            pass
                        if bgpredistTag.get() != "" and bgpredistTag.get() != "Tag":
                            cmd = cmd + " tag " + bgpredistTag.get()
                        else:
                            pass
                        remote_conn.send(cmd + "\n")
                        sleep(0.2)
                        if "(" in bgpproc.get() and (AFIvar.get() == 2 or AFIvar.get() == 4):
                            sleep(0.2)
                            remote_conn.send("exit \n")
                        else:
                            pass
                        tkMessageBox.showinfo('BGP redistribution', 'Learned ' + getBGPoptredist.get() + '.', parent=window)
            else:
                if getBGPoptredist.get() == "RIP" or getBGPoptredist.get() == "EIGRP" or getBGPoptredist.get() == "BGP":
                    if bgpproc.get() == "" or bgpproc.get() == "eg. 15(MyVRF)":
                        tkMessageBox.showinfo('Error', 'Please also enter the BGP process ID above.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.2)
                        remote_conn.send(defbgpcmd)
                        sleep(0.3)
                        if AFIvar.get() == 1:
                            if "(" not in bgpproc.get():
                                pass
                            else:
                                remote_conn.send("exit \n")
                                sleep(0.2)
                                remote_conn.send("exit \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Error', 'Please select either an IPv4 or IPv6 AF to Aplicar VRFs.', parent=window)
                                return
                        elif AFIvar.get() == 2:
                            if "(" not in bgpproc.get():
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " \n")
                            else:
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " vrf " +  bgvrf2 + "\n")
                        elif AFIvar.get() == 3:
                            remote_conn.send("address-f vpnv4 " + SAFIopt.get() + " \n")
                        elif AFIvar.get() == 4:
                            if "(" not in bgpproc.get():
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " \n")
                            else:
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " vrf " +  bgvrf2 + "\n")
                        else:
                            remote_conn.send("address-f vpnv6 " + SAFIopt.get() + " \n")


                        if getBGPoptredist.get() == "RIP":
                            cmd = redistRIPcmd
                        else:
                            cmd = redistcmd
                            
                        if bgpredistFilter.get() != "" and bgpredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + bgpredistFilter.get()
                        else:
                            pass
                        if bgpredistMetric.get() != "" and bgpredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + bgpredistMetric.get()
                        else:
                            pass
                        if bgpredistTag.get() != "" and bgpredistTag.get() != "Tag":
                            cmd = cmd + " tag " + bgpredistTag.get()
                        else:
                            pass
                        remote_conn.send("no " + cmd + "\n")
                        sleep(0.2)
                        if "(" in bgpproc.get() and (AFIvar.get() == 2 or AFIvar.get() == 4):
                            sleep(0.2)
                            remote_conn.send("exit \n")
                        else:
                            pass
                        tkMessageBox.showinfo('BGP redistribution', 'Unlearned ' + getBGPoptredist.get() + '.', parent=window)
                else:
                    if bgpproc.get() == "" or bgpproc.get() == "eg. 15(MyVRF)":
                        tkMessageBox.showinfo('Error', 'Please also enter the BGP process ID above.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.2)
                        remote_conn.send(defbgpcmd)
                        sleep(0.3)
                        if AFIvar.get() == 1:
                            if "(" not in bgpproc.get():
                                pass
                            else:
                                remote_conn.send("exit \n")
                                sleep(0.2)
                                remote_conn.send("exit \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Error', 'Please select either an IPv4 or IPv6 AF to Aplicar VRFs.', parent=window)
                                return
                        elif AFIvar.get() == 2:
                            if "(" not in bgpproc.get():
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " \n")
                            else:
                                remote_conn.send("address-f ipv4 " + SAFIopt.get() + " vrf " +  bgvrf2 + "\n")
                        elif AFIvar.get() == 3:
                            remote_conn.send("address-f vpnv4 " + SAFIopt.get() + " \n")
                        elif AFIvar.get() == 4:
                            if "(" not in bgpproc.get():
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " \n")
                            else:
                                remote_conn.send("address-f ipv6 " + SAFIopt.get() + " vrf " +  bgvrf2 + "\n")
                        else:
                            remote_conn.send("address-f vpnv6 " + SAFIopt.get() + " \n")


                        if "(" not in bgpredisttoprocnum.get():
                            cmd = redistcmd
                        else:
                            cmd = redistospfvrfcmd
                        if bgpredistFilter.get() != "" and bgpredistFilter.get() != "r-map":
                            cmd = cmd + " route-map " + bgpredistFilter.get()
                        else:
                            pass
                        if bgpredistMetric.get() != "" and bgpredistMetric.get() != "Metric":
                            cmd = cmd + " metric " + bgpredistMetric.get()
                        else:
                            pass
                        if bgpredistTag.get() != "" and bgpredistTag.get() != "Tag":
                            cmd = cmd + " tag " + bgpredistTag.get()
                        else:
                            pass
                        remote_conn.send("no " + cmd + "\n")
                        sleep(0.2)
                        if "(" in bgpproc.get() and (AFIvar.get() == 2 or AFIvar.get() == 4):
                            sleep(0.2)
                            remote_conn.send("exit \n")
                        else:
                            pass
                        tkMessageBox.showinfo('BGP redistribution', 'Unlearned ' + getBGPoptredist.get() + '.', parent=window)
            sleep(0.2)
            remote_conn.send("exit \n")
            sleep(0.2)
            remote_conn.send("exit \n")            
        btn = Button(BGPframe, text="Learn", bg="orange", command=bgpredistribute)
        btn.grid(column=5, row=10)








        

        basicVRFframe=LabelFrame(window,text=" Create VRF ",font=('verdana', 8, 'bold'),padx=10,pady=2,width=100,height=100)
        basicVRFframe.grid(row=4,column=0, sticky=("nsew"))
        lbl = Label(basicVRFframe, text="VRF name:")
        lbl.grid(column=0, row=1)
        getVRF = Entry(basicVRFframe,width=15)
        getVRF.grid(column=1, row=1, padx=3)

        lbl = Label(basicVRFframe, text="RD:").grid(column=0, row=2)
        getVRFrd = Entry(basicVRFframe, bg='white', width=15, fg='grey')
        getVRFrd.grid(column=1, row=2, pady=4)
        getVRFrd.insert(0, "eg. 100:200")
        def handle_focus_in(_):
            if getVRFrd.cget('fg') != 'black':
                getVRFrd.delete(0, END)
                getVRFrd.config(fg='black')
        def handle_focus_out(_):
            if getVRFrd.get() == "":
                getVRFrd.delete(0, END)
                getVRFrd.config(fg='grey')
                getVRFrd.insert(0, "eg. 100:200")
        getVRFrd.bind("<FocusOut>", handle_focus_out)
        getVRFrd.bind("<FocusIn>", handle_focus_in)

        OPTIONS = [
        "Import",
        "Export",
        "Both",
        ]
        getVRFrtargetdir = StringVar(basicVRFframe)
        getVRFrtargetdir.set(OPTIONS[0])    # default value
        dropbox1 = OptionMenu(basicVRFframe, getVRFrtargetdir, *OPTIONS)   
        dropbox1.place(x=167, y=19)

        lbl = Label(basicVRFframe, text="RT:").place(x=257, y=25)
        
        getVRFrtarget = Entry(basicVRFframe, bg='white', width=15, fg='grey')
        getVRFrtarget.place(x=285, y=25)
        getVRFrtarget.insert(0, "eg. 100:200")
        def handle_focus_in(_):
            if getVRFrtarget.cget('fg') != 'black':
                getVRFrtarget.delete(0, END)
                getVRFrtarget.config(fg='black')
        def handle_focus_out(_):
            if getVRFrtarget.get() == "":
                getVRFrtarget.delete(0, END)
                getVRFrtarget.config(fg='grey')
                getVRFrtarget.insert(0, "eg. 100:200")    
        getVRFrtarget.bind("<FocusOut>", handle_focus_out)
        getVRFrtarget.bind("<FocusIn>", handle_focus_in)

        
        def createvrf():
            if chk_state_neg.get() == False:
                if getVRF.get() == '' :
                    tkMessageBox.showinfo('Error', 'Please enter a VRF name.', parent=window)
                    return
                elif getVRF.get() != '' and (getVRFrd.get() == '' or getVRFrd.get() == 'eg. 100:200') and (getVRFrtarget.get() == ''\
                     or getVRFrtarget.get() == 'eg. 100:200'):
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("ip vrf " + getVRF.get() + "\n")
                    tkMessageBox.showinfo('VRF', 'VRF created.', parent=window)
                elif getVRF.get() != '' and (getVRFrd.get() != '' or getVRFrd.get() != 'eg. 100:200') and (getVRFrtarget.get() == ''\
                     or getVRFrtarget.get() == 'eg. 100:200'):
                    if ":" not in getVRFrd.get():
                        tkMessageBox.showinfo('Error', 'Please enter in correct format with colon (e.g. 100:200).', parent=window)
                        return
                    else:
                        pass
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("ip vrf " + getVRF.get() + "\n")
                    sleep(0.5)                    
                    remote_conn.send("rd " + getVRFrd.get() + "\n")
                    sleep(0.5)
                    tkMessageBox.showinfo('VRF' + getVRF.get(), 'Route distinguisher created.', parent=window)
                elif getVRF.get() != '' and (getVRFrd.get() == '' or getVRFrd.get() == 'eg. 100:200') and (getVRFrtarget.get() != '' \
                    or getVRFrtarget.get() != 'eg. 100:200'):
                    if ":" not in getVRFrtarget.get():
                        tkMessageBox.showinfo('Error', 'Please enter in correct format with colon (e.g. 100:200).', parent=window)
                        return
                    else:
                        pass
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("ip vrf " + getVRF.get() + "\n")
                    sleep(0.5)                    
                    remote_conn.send("route-target " + getVRFrtargetdir.get() + " " + getVRFrtarget.get() + "\n")
                    sleep(0.5)
                    tkMessageBox.showinfo('VRF' + getVRF.get(), 'Route target created.', parent=window)                        
                else:
                    if (":" not in getVRFrd.get()) or (":" not in getVRFrtarget.get()):
                        tkMessageBox.showinfo('Error', 'Please enter in correct format with colon (e.g. 100:200).', parent=window)
                        return
                    else:
                        pass
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("ip vrf " + getVRF.get() + "\n")
                    sleep(0.5)
                    remote_conn.send("rd " + getVRFrd.get() + "\n")
                    sleep(0.5)
                    remote_conn.send("route-target " + getVRFrtargetdir.get() + " " + getVRFrtarget.get() + "\n")
                    sleep(0.5)                        
                    tkMessageBox.showinfo('VRF' + getVRF.get(), 'Route distinguisher and route-target created.', parent=window)
            else:
                if getVRF.get() == '':
                    tkMessageBox.showinfo('Error', 'Please enter a VRF name.', parent=window)
                    return
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    #if getVRFrd.get() != '' and getVRFrtarget.get() != '':
                    if (getVRFrd.get() != '' or getVRFrd.get() != 'eg. 100:200') and (getVRFrtarget.get() != ''\
                     or getVRFrtarget.get() != 'eg. 100:200'):
                        remote_conn.send("ip vrf " + getVRF.get() + "\n")
                        sleep(0.5)                    
                        remote_conn.send("no rd " + getVRFrd.get() + "\n")
                        sleep(0.5)
                        remote_conn.send("no route-target " + getVRFrtargetdir.get() + " " + getVRFrtarget.get() + "\n")
                        sleep(0.5)
                        tkMessageBox.showinfo('VRF' + getVRF.get(), 'Route distinguisher and route target removed.', parent=window)
                    elif (getVRFrd.get() != '' or getVRFrd.get() != 'eg. 100:200') and (getVRFrtarget.get() == ''\
                     or getVRFrtarget.get() == 'eg. 100:200'):
                        remote_conn.send("ip vrf " + getVRF.get() + "\n")
                        sleep(0.5)                    
                        remote_conn.send("no rd " + getVRFrd.get() + "\n")
                        sleep(0.5)
                        tkMessageBox.showinfo('VRF' + getVRF.get(), 'Route distinguisher removed.', parent=window)
                    elif (getVRFrd.get() == '' or getVRFrd.get() == 'eg. 100:200') and (getVRFrtarget.get() != ''\
                     or getVRFrtarget.get() != 'eg. 100:200'):
                        remote_conn.send("ip vrf " + getVRF.get() + "\n")
                        sleep(0.5)                    
                        remote_conn.send("no route-target " + getVRFrtargetdir.get() + " " + getVRFrtarget.get() + "\n")
                        sleep(0.5)
                        tkMessageBox.showinfo('VRF' + getVRF.get(), 'Route target removed.', parent=window)
                    else:
                        remote_conn.send("no vrf " + getVRF.get() + "\n")
                        sleep(0.5)
                        tkMessageBox.showinfo('VRF' + getVRF.get(), 'VRF removed.', parent=window)
                        sleep(0.5)
                        remote_conn.send("exit \n")
                        return
            sleep(0.5)
            remote_conn.send("exit \n")
            sleep(0.5)
            remote_conn.send("exit \n")                                                
        btn = Button(basicVRFframe, text="Aplicar", bg="orange", command=createvrf)
        btn.place(x=385, y=10)
        








        showhelpframe=LabelFrame(window,text=" Help ",font=('verdana', 8, 'bold'),padx=10,pady=10,width=100,height=100)
        showhelpframe.grid(column=1, row=3, rowspan = 2, sticky=("nsew"))
        def routehelp():
            tkMessageBox.showinfo('Help', '===Route selection===\n If there exists multiple routes to a same destination network, the best route would be chosen based on: \
                                \n 1.Lowest Administrative Distance, AD (Connected route(0) > Static route(1) > E-BGP(20) > EIGRP(90) > OSPF(110) > ISIS(115) > RIP(120) > iBGP(200))\
                                  \n 2. Routing protocol Metrics (If a routing protocol is considered)\n 3.Longest prefix match (/30 > /29) - final determining factor \
                                \n\n===VRF===\n A router only has 1 routing table by default - the Global Routing Table. VRFs allow multiple routing tables to be created in addition to \
the Global Routing Table. Hence, they theoretically behave like a "Layer 3 VLAN". Route distinguishers (RD) and route targets (RT) are only used for MPBGP VPN \n\n===Redistribution===\n\
This is used to share routes (connected routes, static routes or routes from another routing protocol) to a routing protocol. You can share specific routes with the "route-map" option.', parent=window)
        btn = Button(showhelpframe, text="Help", bg="yellow", command=routehelp)
        btn.grid(column=1, row=1)



        def bgpusagehelp():
            res = '-- BGP Usage --\n ' +\
                  ' - enabling BGP with ANY AF besides "def_AF" will disable default ipv4-unicast AF\n' +\
                  ' - running any BGP device opt will enable "ip bgp-community new-format"\n' +\
                  ' - Negate: To delete a BGP process, specify def_AF w/o VRF. Else, only the AF specified will be deleted'
            tkMessageBox.showinfo('BGP usage help', res, parent=window)
        btn = Button(showhelpframe, text="BGP usage help", bg="yellow", command=bgpusagehelp)
        btn.grid(column=1, row=4)

        def ospflearnhelp():
            tkMessageBox.showinfo('How OSPF protocol functions', \
'Can segregate into "areas" with border routers.\n\n\
OSPF default Metric Calculation:\n\
 - Cumulative cost = Sum of all outgoing interfaces cost in route\n\
 - Best route = Route which has the lowest Cumulative cost', parent=window)
        btn = Button(showhelpframe, text="OSPF basics", bg="yellow", command=ospflearnhelp)
        btn.grid(column=1, row=5)
        
        def eigrplearnhelp():
            tkMessageBox.showinfo('How EIGRP protocol functions', \
'Extremely fast failover with "feasible successor" routes.\n\n\
EIGRP default Metric Calculation (K1+K3 only):\n Metric= 256*( Bandwidth +Sum of all Delay)\n\n\
K value reference:\n\
 - K1 == minimum BANDWIDTH of the route, kbps\n\
 - K2 == Route DELAY, in tens of microseconds\n\
 - K3 == LOAD\n\
 - K4 == minimum MTU of the route\n\
 - K5 == RELIABILITY (% of successful pkt xmission)\n\
 - K6 == Ext Attributes (Only in EIGRP Named Mode w/ Wide Metrics)\
', parent=window)
        btn = Button(showhelpframe, text="EIGRP basics", bg="yellow", command=eigrplearnhelp)
        btn.grid(column=1, row=6)

        def bgplearnhelp():
            tkMessageBox.showinfo('How BGP protocol functions', \
'Secure routing protocol required for AS routing over the internet.\n\
- unlike other routing protocols, it relies on a bestpath policy rather than fastest path metrics.\n\
- unlike other routing protocols, not only does it allow OUTBOUND route control but also INBOUND.\n\
- unlike other routing protocols, has maxhop of 1 by default.\n\
- There exists 2 types of BGP - eBGP (internet use) and iBGP (like any IGP)\n\
- BGP routes traffic based on Autonomous Systems (AS). There is Public (internet use) and Private AS (64512-65535).\n\
- anti-loop mechanism for iBGP is the full-mesh, for eBGP is AS-Path\n\
- BGP bestpath policy selection(for a particular prefix):  \n \
   - highest WEIGHT, else\n \
   - highest LOCAL_PREFERENCE, else\n \
   - Origin from (network cmd > redistributed), else\n \
   - shortest AS-PATH, else\n \
   - Origin type (IGP > EGP > ?), else\n \
   - lowest MED, else\n \
   - Prefer eBGP over iBGP neighbor, else\n \
   - lowest IGP metric to next-hop of pfx, else\n \
   - Multipath (if enabled, install it), else\n \
   - oldest path (eBGP only else skip), else\n \
   - lowest RID (or RR originator-ID) of pfx source, else\n \
   - shortest cluster-list (RR only else skip), else\n \
   - lowest BGP neighbor IP\n \
- BGP neighbors have to be manually established - it runs over TCP port 179.\n\
- Neighbor session can be via IPv4/IPv6, and advertise IPv4/IPv6 over ANY of those session types.\n\
- Other config commonly used together w/ BGP routing: \n\
   - Route-Maps (to manipulate bestpath policy) \n\
   - Prefix-Lists and ACLs (used together w/ Route-Maps) \n\
   - Community (eg. to tell a neighbor to do something) \n\
- In real-world scenarios: \n\
   - you either use a private AS and loan IP from an ISP or buy an AS and buy IP to register it in your AS\n\
   - carriers normally will only accespt /24 or larger subnet advertisements \n\
   - you form neighbors by PEERING or TRANSIT \n\
     - PEERING means you both share partial routes with each other (eg. by a route server in a DC) \n\
     - TRANSIT means you pay to learn the full global route table. You will need a powerful router. \n\
 ', parent=window)
        btn = Button(showhelpframe, text="BGP basics", bg="yellow", command=bgplearnhelp)
        btn.grid(column=1, row=7)



        
        
        showrteframe=LabelFrame(window,text=" Show/Clear routing config ",font=('verdana', 8, 'bold'),padx=10,width=100,height=100)
        showrteframe.grid(column=0, row=6, sticky=("nsew"))

        lbl = Label(showrteframe, text="")
        lbl.grid(column=0, row=0, padx=90)

        def option_changed_showrouteopt(*args):
            if showrouteopt.get() == "Show VRF":
                text = '[brief|detail <>|counters]'
                showopt.delete(0, END)
                showopt.config(fg='grey')
                showopt.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt.cget('fg') != 'black':
                        showopt.delete(0, END)
                        showopt.config(fg='black')
                def handle_focus_out(_):
                    if showopt.get() == "":
                        showopt.delete(0, END)
                        showopt.config(fg='grey')
                        showopt.insert(0, text)
                showopt.bind("<FocusOut>", handle_focus_out)
                showopt.bind("<FocusIn>", handle_focus_in)
            elif showrouteopt.get() == "Clear route(s)":
                text = '[vrf <>] * | x.x.x.x'
                showopt.delete(0, END)
                showopt.config(fg='grey')
                showopt.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt.cget('fg') != 'black':
                        showopt.delete(0, END)
                        showopt.config(fg='black')
                def handle_focus_out(_):
                    if showopt.get() == "":
                        showopt.delete(0, END)
                        showopt.config(fg='grey')
                        showopt.insert(0, text)
                showopt.bind("<FocusOut>", handle_focus_out)
                showopt.bind("<FocusIn>", handle_focus_in)
            elif showrouteopt.get() == "Active protocols":
                text = 'NoInputRequired'
                showopt.delete(0, END)
                showopt.config(fg='grey')
                showopt.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt.cget('fg') != 'black':
                        showopt.delete(0, END)
                        showopt.config(fg='black')
                def handle_focus_out(_):
                    if showopt.get() == "":
                        showopt.delete(0, END)
                        showopt.config(fg='grey')
                        showopt.insert(0, text)
                showopt.bind("<FocusOut>", handle_focus_out)
                showopt.bind("<FocusIn>", handle_focus_in)
            elif showrouteopt.get() == "Proto/VRF/specific routes:":
                text = '[vrf <A>] [proto <procID>] [IP [mask]]'
                showopt.delete(0, END)
                showopt.config(fg='grey')
                showopt.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt.cget('fg') != 'black':
                        showopt.delete(0, END)
                        showopt.config(fg='black')
                def handle_focus_out(_):
                    if showopt.get() == "":
                        showopt.delete(0, END)
                        showopt.config(fg='grey')
                        showopt.insert(0, text)
                showopt.bind("<FocusOut>", handle_focus_out)
                showopt.bind("<FocusIn>", handle_focus_in)
            elif showrouteopt.get() == "Protocol detail:":
                text = 'eg. eigrp, ospf 2'
                showopt.delete(0, END)
                showopt.config(fg='grey')
                showopt.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt.cget('fg') != 'black':
                        showopt.delete(0, END)
                        showopt.config(fg='black')
                def handle_focus_out(_):
                    if showopt.get() == "":
                        showopt.delete(0, END)
                        showopt.config(fg='grey')
                        showopt.insert(0, text)
                showopt.bind("<FocusOut>", handle_focus_out)
                showopt.bind("<FocusIn>", handle_focus_in)
            else:
                text = ''
                showopt.delete(0, END)
                showopt.config(fg='grey')
                showopt.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt.cget('fg') != 'black':
                        showopt.delete(0, END)
                        showopt.config(fg='black')
                def handle_focus_out(_):
                    if showopt.get() == "":
                        showopt.delete(0, END)
                        showopt.config(fg='grey')
                        showopt.insert(0, text)
                showopt.bind("<FocusOut>", handle_focus_out)
                showopt.bind("<FocusIn>", handle_focus_in)                

        OPTIONS = [
        "Active protocols",
        "Protocol detail:",
        "Active routes",
        "Static routes",
        "Proto/VRF/specific routes:",
        "Route summary",
        "Show VRF",
        "Clear route(s)"
        ]
        showrouteopt = StringVar(showrteframe)
        showrouteopt.set(OPTIONS[0])
        showrouteopt.trace("w", option_changed_showrouteopt)
        dropbox = OptionMenu(showrteframe, showrouteopt, *OPTIONS)   
        dropbox.place(x= 0,y=0)

        showopt = Entry(showrteframe, bg='white', width=33, fg='grey')
        showopt.grid(column=1, row=0)
        showopt.insert(0, "NoInputRequired")
        def handle_focus_in(_):
            showopt.delete(0, END)
            showopt.config(fg='black')
        def handle_focus_out(_):
            if showopt.get() == "":
                showopt.delete(0, END)
                showopt.config(fg='grey')
                showopt.insert(0, "NoInputRequired")    
        showopt.bind("<FocusOut>", handle_focus_out)
        showopt.bind("<FocusIn>", handle_focus_in) 
        
        def showroute():
            if showrouteopt.get() == "Active routes":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show ip route \n")
                sleep(0.5)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Active routes', output, parent=window)
            elif showrouteopt.get() == "Static routes":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show run | i route \n")
                sleep(0.5)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Static routes', output, parent=window)
            elif showrouteopt.get() == "Route summary":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show ip route summ \n")
                sleep(0.5)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Route summary', output, parent=window)
            elif showrouteopt.get() == "Active protocols":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show ip proto summ \n")
                sleep(0.5)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Active protocols', output, parent=window)
            elif showrouteopt.get() == "Protocol detail:":
                if showopt.get() == "" or showopt.get() == "eg. eigrp, ospf 2":
                    tkMessageBox.showinfo('Error', 'Please enter a routing protocol.', parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("show ip proto | s " + showopt.get() + " \n")
                    sleep(0.5)         
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 1024
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('Protocol detail', output, parent=window)
            elif showrouteopt.get() == "Show VRF":
                if showopt.get() == "" or showopt.get() == "[brief|detail <>|counters]":
                    printvrf = "show ip vrf \n"
                else:
                    printvrf = "show ip vrf " + showopt.get() + " \n"
                buff_size = 16384
                sleep(0.5)
                remote_conn.send(printvrf)
                sleep(0.5)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('VRF information', output, parent=window)
            elif showrouteopt.get() == "Clear route(s)":
                if showopt.get() == "" or showopt.get() == "[vrf <>] * | x.x.x.x":
                    remote_conn.send("clear ip route * \n")
                    sleep(0.5)
                    tkMessageBox.showinfo('Clear routes', 'All routes cleared.', parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("clear ip route " + showopt.get() + " \n")
                    sleep(0.5)         
                    tkMessageBox.showinfo('Clear routes', 'Route cleared.', parent=window)
            else:
                if showopt.get() == "" or showopt.get() == "[vrf <A>] [proto <procID>] [IP [mask]]":
                    cmd = "show ip route \n"
                else:
                    cmd = "show ip route " + showopt.get() + " \n"
                buff_size = 16384
                sleep(0.5)
                remote_conn.send(cmd)
                sleep(0.5)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Route protocol', output, parent=window)
        btn = Button(showrteframe, text="Show", bg="orange", command=showroute)
        btn.place(x=400, y=0)




        def option_changed_showprotopt(*args):
            if showprotopt.get() == "RIP":
                text = '[database | neigh [<>]]'
                showopt2.delete(0, END)
                showopt2.config(fg='grey')
                showopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt2.cget('fg') != 'black':
                        showopt2.delete(0, END)
                        showopt2.config(fg='black')
                def handle_focus_out(_):
                    if showopt2.get() == "":
                        showopt2.delete(0, END)
                        showopt2.config(fg='grey')
                        showopt2.insert(0, text)
                showopt2.bind("<FocusOut>", handle_focus_out)
                showopt2.bind("<FocusIn>", handle_focus_in) 
            elif showprotopt.get() == "EIGRP" or showprotopt.get() == "OSPF":
                text = '[database | neigh [<>] | interface]'
                showopt2.delete(0, END)
                showopt2.config(fg='grey')
                showopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt2.cget('fg') != 'black':
                        showopt2.delete(0, END)
                        showopt2.config(fg='black')
                def handle_focus_out(_):
                    if showopt2.get() == "":
                        showopt2.delete(0, END)
                        showopt2.config(fg='grey')
                        showopt2.insert(0, text)
                showopt2.bind("<FocusOut>", handle_focus_out)
                showopt2.bind("<FocusIn>", handle_focus_in)
            elif showprotopt.get() == "BGP":
                text = '[neigh [<>] | summary]'
                showopt2.delete(0, END)
                showopt2.config(fg='grey')
                showopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt2.cget('fg') != 'black':
                        showopt2.delete(0, END)
                        showopt2.config(fg='black')
                def handle_focus_out(_):
                    if showopt2.get() == "":
                        showopt2.delete(0, END)
                        showopt2.config(fg='grey')
                        showopt2.insert(0, text)
                showopt2.bind("<FocusOut>", handle_focus_out)
                showopt2.bind("<FocusIn>", handle_focus_in)
            elif showprotopt.get() == "EIGRP/OSPF reset":
                text = '<protocol_ID>'
                showopt2.delete(0, END)
                showopt2.config(fg='grey')
                showopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt2.cget('fg') != 'black':
                        showopt2.delete(0, END)
                        showopt2.config(fg='black')
                def handle_focus_out(_):
                    if showopt2.get() == "":
                        showopt2.delete(0, END)
                        showopt2.config(fg='grey')
                        showopt2.insert(0, text)
                showopt2.bind("<FocusOut>", handle_focus_out)
                showopt2.bind("<FocusIn>", handle_focus_in)
            elif showprotopt.get() == "BGP reset":
                text = '<protocol_ID> [soft]'
                showopt2.delete(0, END)
                showopt2.config(fg='grey')
                showopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt2.cget('fg') != 'black':
                        showopt2.delete(0, END)
                        showopt2.config(fg='black')
                def handle_focus_out(_):
                    if showopt2.get() == "":
                        showopt2.delete(0, END)
                        showopt2.config(fg='grey')
                        showopt2.insert(0, text)
                showopt2.bind("<FocusOut>", handle_focus_out)
                showopt2.bind("<FocusIn>", handle_focus_in)                
            else:
                text = ''
                showopt2.delete(0, END)
                showopt2.config(fg='grey')
                showopt2.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if showopt2.cget('fg') != 'black':
                        showopt2.delete(0, END)
                        showopt2.config(fg='black')
                def handle_focus_out(_):
                    if showopt2.get() == "":
                        showopt2.delete(0, END)
                        showopt2.config(fg='grey')
                        showopt2.insert(0, text)
                showopt2.bind("<FocusOut>", handle_focus_out)
                showopt2.bind("<FocusIn>", handle_focus_in)

                
        OPTIONS = [
        "RIP",
        "EIGRP",
        "OSPF",
        "EIGRP/OSPF reset",
        "BGP",
        "BGP adv(filtered) rtes:",
        "BGP adv(raw) rtes:",
        "BGP rcv(filtered) rtes:",
        "BGP rcv(raw) rtes:",
        "BGP dampen flap-stats",
        "BGP dampen paths",
        "BGP dampen params",
        "BGP reset" 
        ]
        showprotopt = StringVar(showrteframe)
        showprotopt.set(OPTIONS[0])
        showprotopt.trace("w", option_changed_showprotopt)
        dropbox = OptionMenu(showrteframe, showprotopt, *OPTIONS)   
        dropbox.place(x= 0,y= 30)

        showopt2 = Entry(showrteframe, bg='white', width=33, fg='grey')
        showopt2.grid(column=1, row=1, pady=13)
        showopt2.insert(0, "[database | neigh [<>]]")
        def handle_focus_in(_):
            showopt2.delete(0, END)
            showopt2.config(fg='black')
        def handle_focus_out(_):
            if showopt2.get() == "":
                showopt2.delete(0, END)
                showopt2.config(fg='grey')
                showopt2.insert(0, "[database | neigh [<>]]")    
        showopt2.bind("<FocusOut>", handle_focus_out)
        showopt2.bind("<FocusIn>", handle_focus_in)
        
        def showproto():
            if showprotopt.get() == "RIP":
                if showopt2.get() == "" or showopt2.get() == "[database | neigh [<>]]":
                    tkMessageBox.showinfo('Error', 'Please enter an option.', parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("show ip rip " + showopt2.get() + " \n")
                    sleep(0.5)         
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 1024
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('RIP', output, parent=window)
            elif showprotopt.get() == "EIGRP" or showprotopt.get() == "OSPF":
                if showopt2.get() == "" or showopt2.get() == "[database | neigh [<>] | interface]":
                    tkMessageBox.showinfo('Error', 'Please enter an option.', parent=window)
                else:
                    chosenproto = showprotopt.get()
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("show ip " + chosenproto + " " + showopt2.get() + " \n")
                    sleep(0.5)
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 1024
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo(chosenproto, output, parent=window)
            elif showprotopt.get() == "EIGRP/OSPF reset":
                sleep(0.5)
                remote_conn.send("clear ip " + chosenproto + " " + showopt2.get() + " \n")
                sleep(0.5)
                tkMessageBox.showinfo(chosenproto, "Protocol has been reset.", parent=window)                   
            elif showprotopt.get() == "BGP":
                if showopt2.get() == "" or showopt2.get() == "[neigh [<>] | summary]":
                    tkMessageBox.showinfo('Error', 'Please enter an option.', parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("show ip bgp " + showopt2.get() + " \n")
                    sleep(0.5)         
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 1024
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('BGP', output, parent=window)
            elif showprotopt.get() == "BGP Reset":
                remote_conn.send("clear ip bgp " + showopt2.get() + " \n")
                sleep(0.5)         
                tkMessageBox.showinfo('Clear BGP', 'BGP process has been reset.', parent=window)
            elif showprotopt.get() == "BGP adv(filtered) rtes:":
                if showopt2.get() == "":
                    tkMessageBox.showinfo("Error", "Please enter BGP neighbor's IP address to view (filtered) routes advertised to it.", parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("sh ip bgp neighbors " + showopt2.get() + " advertised-routes \n")
                    sleep(0.5)         
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 1024
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('BGP advertised (filtered) routes', output, parent=window)
            elif showprotopt.get() == "BGP adv(raw) rtes:":
                if showopt2.get() == "":
                    cmd = "sh ip bgp \n"
                else:
                    cmd = "sh ip bgp " + showopt2.get() + "\n"
                buff_size = 16384
                sleep(0.5)
                remote_conn.send(cmd)
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('BGP advertised (unfiltered) routes', output, parent=window)   
            elif showprotopt.get() == "BGP rcv(filtered) rtes:":
                if showopt2.get() == "":
                    tkMessageBox.showinfo("Error", "Please enter BGP neighbor's IP address to view (before filtering) routes advertised to it.", parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("sh ip bgp neighbors " + showopt2.get() + " routes \n")
                    sleep(0.5)         
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 1024
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('BGP advertised routes', output, parent=window)
            elif showprotopt.get() == "BGP rcv(raw) rtes:":
                if showopt2.get() == "":
                    tkMessageBox.showinfo("Error", "Please enter BGP neighbor's IP address to view routes received (before filtering) from it.", parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("sh ip bgp neighbors " + showopt2.get() + " received-routes \n")
                    sleep(0.5)         
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 1024
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('BGP received routes', output, parent=window)
            elif showprotopt.get() == "BGP dampen flap-stats":
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("sh ip bgp dampening flap-stat \n")
                    sleep(0.5)         
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 1024
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('BGP dampening', output, parent=window)
            elif showprotopt.get() == "BGP dampen paths":
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("sh ip bgp dampening dampened-p \n")
                    sleep(0.5)         
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 1024
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('BGP dampening', output, parent=window)
            else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("sh ip bgp dampening param \n")
                    sleep(0.5)         
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 1024
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('BGP dampening', output, parent=window)

        btn = Button(showrteframe, text="Show", bg="orange", command=showproto)
        btn.place(x=400, y=30)







    def switch():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("Switching Control")
        window.geometry('650x500')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)

        negframe=LabelFrame(window,text=" Negate ",font=('verdana', 8, 'bold'),padx=10,width=100,height=100)
        negframe.grid(column=1, row=0, sticky=("nsew"))

        chk_state_neg = BooleanVar()
        chk_state_neg.set(False)
        chk = Checkbutton(negframe, variable=chk_state_neg)
        chk.grid(column=2, row=1)

        VLANframe=LabelFrame(window,text=" VLAN ID (creates new ID if does not already exist) ",font=('verdana', 8, 'bold'),padx=160,pady=10,width=100,height=100)
        VLANframe.grid(column=0, row=0, sticky=("nsew"))


        createv = Entry(VLANframe, bg='white', width=37, fg='grey')
        createv.grid(column=1, row=1)
        createv.insert(0, "e.g. 1, 4094, 3-15")
        def handle_focus_in(_):
            if createv.cget('fg') != 'black':
                createv.delete(0, END)
                createv.config(fg='black')
        def handle_focus_out(_):
            if createv.get() == "":
                createv.delete(0, END)
                createv.config(fg='grey')
                createv.insert(0, "e.g. 1, 4094, 3-15")    
        createv.bind("<FocusOut>", handle_focus_out)
        createv.bind("<FocusIn>", handle_focus_in)
        def createvlan():
            if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                tkMessageBox.showinfo('Error', 'Please enter VLAN ID.', parent=window)
            else:
                if chk_state_neg.get() == False:
                    remote_conn.send("conf t\n")
                    sleep(0.2)
                    remote_conn.send("vlan " + createv.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('VLAN ' + createv.get(), 'VLAN has been created.', parent=window)
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.2)
                    remote_conn.send("no vlan " + createv.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('VLAN ' + createv.get(), 'VLAN has been removed.', parent=window)                
        btn = Button(VLANframe, text="Aplicar", bg="orange", command=createvlan)
        btn.grid(column=1, row=2)


        
        Switchframe=LabelFrame(window,text=" Switchport Configuration ",font=('verdana', 8, 'bold'),padx=10,width=100,height=100)
        Switchframe.grid(column=0, row=1, sticky=("nsew"))

        lbl = Label(Switchframe, text="Aplicar VLAN id to interface:").grid(column=0, row=3)
        getvlan = Entry(Switchframe, bg='white', width=38, fg='grey')
        getvlan.grid(column=1, row=3)
        getvlan.insert(0, "e.g. 20, 3-15 (only Aplicar range to TRUNKS)")
        def handle_focus_in(_):
            if getvlan.cget('fg') != 'black':
                getvlan.delete(0, END)
                getvlan.config(fg='black')
        def handle_focus_out(_):
            if getvlan.get() == "":
                getvlan.delete(0, END)
                getvlan.config(fg='grey')
                getvlan.insert(0, "e.g. 20, 3-15 (only Aplicar range to TRUNKS)")    
        getvlan.bind("<FocusOut>", handle_focus_out)
        getvlan.bind("<FocusIn>", handle_focus_in)
        
        getiface = Entry(Switchframe, bg='white', width=15, fg='grey')
        getiface.grid(column=2, row=3)
        getiface.insert(0, "e.g. Eth0/0")
        def handle_focus_in(_):
            if getiface.cget('fg') != 'black':
                getiface.delete(0, END)
                getiface.config(fg='black')
        def handle_focus_out(_):
            if getiface.get() == "":
                getiface.delete(0, END)
                getiface.config(fg='grey')
                getiface.insert(0, "e.g. Eth0/0")    
        getiface.bind("<FocusOut>", handle_focus_out)
        getiface.bind("<FocusIn>", handle_focus_in)
        
        OPTIONS = [
        "Mode",
        "Access",
        "Trunk"
        ]
        getportmode = StringVar(Switchframe)
        getportmode.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(Switchframe, getportmode, *OPTIONS)   
        dropbox.grid(column=3, row=3)
    
        def setvlan():
            if getportmode.get() == "Mode" or getvlan.get() == "" or getvlan.get() == "e.g. 20, 3-15 (only Aplicar range to TRUNKS)"\
            or getiface.get() == "" or getiface.get() == "e.g. Eth0/0":
                    tkMessageBox.showinfo('Error', 'Please enter VLAN ID, interface, and choose switchport mode.', parent=window)
            else:
                if chk_state_neg.get() == False:
                    if getportmode.get() == "Access":                    
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("int " + getiface.get() + "\n")
                        sleep(0.2)                       
                        remote_conn.send("switchport access vlan " + getvlan.get() + " \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n") 
                        res = "VLAN id has been set to Access for port: " + getiface.get()
                        tkMessageBox.showinfo('VLAN id' + createvlan.get(), res, parent=window)
                    elif getportmode.get() == "Trunk":
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("int " + getiface.get() + "\n")
                        sleep(0.2)                
                        remote_conn.send("switchport trunk allowed vlan " + getvlan.get() + " \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n") 
                        res = "VLAN id has been set to Trunk for port: " + getiface.get()
                        tkMessageBox.showinfo('VLAN id', res, parent=window)
                else:
                    if getportmode.get() == "Access":                    
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("int " + getiface.get() + "\n")
                        sleep(0.2)                
                        remote_conn.send("no switchport access vlan " + getvlan.get() + " \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n") 
                        res = "VLAN id has been removed from Access for port: " + getiface.get()
                        tkMessageBox.showinfo('VLAN id' + createvlan.get(), res, parent=window)
                    elif getportmode.get() == "Trunk":
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("int " + getiface.get() + "\n")
                        sleep(0.2)                
                        remote_conn.send("no switchport trunk allowed vlan " + getvlan.get() + " \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n") 
                        res = "VLAN id has been removed from Trunk for port: " + getiface.get()
                        tkMessageBox.showinfo('VLAN id', res, parent=window)                    
        btn = Button(Switchframe, text="Aplicar", bg="orange", command=setvlan)
        btn.grid(column=1, row=4)


        lbl = Label(Switchframe, text="Set switchport mode:").grid(column=0, row=5)
        getiface1 = Entry(Switchframe, bg='white', width=15, fg='grey')
        getiface1.grid(column=1, row=5)
        getiface1.insert(0, "e.g. Eth0/0")
        def handle_focus_in(_):
            if getiface1.cget('fg') != 'black':
                getiface1.delete(0, END)
                getiface1.config(fg='black')
        def handle_focus_out(_):
            if getiface1.get() == "":
                getiface1.delete(0, END)
                getiface1.config(fg='grey')
                getiface1.insert(0, "e.g. Eth0/0")    
        getiface1.bind("<FocusOut>", handle_focus_out)
        getiface1.bind("<FocusIn>", handle_focus_in)

        OPTIONS = [
        "Mode",
        "Access",
        "Trunk (enforced)",
        "Trunk (Auto)",
        "Trunk (Desirable)"
        ]
        gettrkmode = StringVar(Switchframe)
        gettrkmode.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(Switchframe, gettrkmode, *OPTIONS)   
        dropbox.place(y=51, x=335)            
        def settrunk():
            if gettrkmode.get() == "Mode" or getiface1.get() == "" or getiface1.get() == "e.g. Eth0/0":
                    tkMessageBox.showinfo('Error', 'Please enter interface and choose switchport mode.', parent=window)
            elif gettrkmode.get() == "Access":
                remote_conn.send("conf t\n")
                sleep(0.2)
                remote_conn.send("int " + getiface1.get() + "\n")
                sleep(0.2)
                remote_conn.send("switchport mo acc \n")
                sleep(0.2)            
                remote_conn.send("exit \n")
                sleep(0.2)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('Switchport Mode', 'Port set to Access mode', parent=window)    
            elif gettrkmode.get() == "Trunk (enforced)":
                remote_conn.send("conf t\n")
                sleep(0.2)
                remote_conn.send("int " + getiface1.get() + "\n")
                sleep(0.2)                
                remote_conn.send("switchport trunk encap d \n")
                sleep(0.2)
                remote_conn.send("switchport mo tr \n")
                sleep(0.2)            
                remote_conn.send("exit \n")
                sleep(0.2)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('Switchport Mode', 'Port set to enforced Trunking', parent=window)
            elif gettrkmode.get() == "Trunk (Auto)":        
                remote_conn.send("conf t\n")
                sleep(0.2)
                remote_conn.send("int " + getiface1.get() + "\n")
                sleep(0.2)
                remote_conn.send("switchport trunk encap d \n")
                sleep(0.2)
                remote_conn.send("switchport mo dyn auto \n")
                sleep(0.2)            
                remote_conn.send("exit \n")
                sleep(0.2)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('Switchport Mode', 'Port set to Dynamic Auto Trunking', parent=window)
            else:
                remote_conn.send("conf t\n")
                sleep(0.2)
                remote_conn.send("int " + getiface1.get() + "\n")
                sleep(0.2)
                remote_conn.send("switchport trunk encap d \n")
                sleep(0.2)
                remote_conn.send("switchport mo dyn des \n")
                sleep(0.2)            
                remote_conn.send("exit \n")
                sleep(0.2)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('Switchport Mode', 'Port set to Dynamic Desirable Trunking', parent=window)                                
        btn = Button(Switchframe, text="Aplicar", bg="orange", command=settrunk)
        btn.grid(column=1, row=6)






        STPframe=LabelFrame(window,text=" Spanning Tree Configuration ",font=('verdana', 8, 'bold'),padx=10,width=100,height=100)
        STPframe.grid(column=0, row=2, sticky=("nsew"))


        def option_changed_STPopt(*args):
            if STPopt.get() == "Enable STP":
                text = 'mst | pvst | rapid-pvst'
                STPinput.delete(0, END)
                STPinput.config(fg='grey')
                STPinput.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if STPinput.cget('fg') != 'black':
                        STPinput.delete(0, END)
                        STPinput.config(fg='black')
                def handle_focus_out(_):
                    if STPinput.get() == "":
                        STPinput.delete(0, END)
                        STPinput.config(fg='grey')
                        STPinput.insert(0, text)
                STPinput.bind("<FocusOut>", handle_focus_out)
                STPinput.bind("<FocusIn>", handle_focus_in)
            elif STPopt.get() == "STP fwd_time":
                text = '<4-30>'
                STPinput.delete(0, END)
                STPinput.config(fg='grey')
                STPinput.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if STPinput.cget('fg') != 'black':
                        STPinput.delete(0, END)
                        STPinput.config(fg='black')
                def handle_focus_out(_):
                    if STPinput.get() == "":
                        STPinput.delete(0, END)
                        STPinput.config(fg='grey')
                        STPinput.insert(0, text)
                STPinput.bind("<FocusOut>", handle_focus_out)
                STPinput.bind("<FocusIn>", handle_focus_in)
            elif STPopt.get() == "STP hello_time":
                text = '<1-10>'
                STPinput.delete(0, END)
                STPinput.config(fg='grey')
                STPinput.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if STPinput.cget('fg') != 'black':
                        STPinput.delete(0, END)
                        STPinput.config(fg='black')
                def handle_focus_out(_):
                    if STPinput.get() == "":
                        STPinput.delete(0, END)
                        STPinput.config(fg='grey')
                        STPinput.insert(0, text)
                STPinput.bind("<FocusOut>", handle_focus_out)
                STPinput.bind("<FocusIn>", handle_focus_in)
            elif STPopt.get() == "STP max_age":
                text = '<6-40>'
                STPinput.delete(0, END)
                STPinput.config(fg='grey')
                STPinput.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if STPinput.cget('fg') != 'black':
                        STPinput.delete(0, END)
                        STPinput.config(fg='black')
                def handle_focus_out(_):
                    if STPinput.get() == "":
                        STPinput.delete(0, END)
                        STPinput.config(fg='grey')
                        STPinput.insert(0, text)
                STPinput.bind("<FocusOut>", handle_focus_out)
                STPinput.bind("<FocusIn>", handle_focus_in)
            elif STPopt.get() == "STP priority":
                text = 'eg. 0, 4096, 12288.. 61440 (increments of 4096)'
                STPinput.delete(0, END)
                STPinput.config(fg='grey')
                STPinput.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if STPinput.cget('fg') != 'black':
                        STPinput.delete(0, END)
                        STPinput.config(fg='black')
                def handle_focus_out(_):
                    if STPinput.get() == "":
                        STPinput.delete(0, END)
                        STPinput.config(fg='grey')
                        STPinput.insert(0, text)
                STPinput.bind("<FocusOut>", handle_focus_out)
                STPinput.bind("<FocusIn>", handle_focus_in)
            elif STPopt.get() == "STP root":
                text = 'pri|sec [dia <2-7> [hello <1-10>]]'
                STPinput.delete(0, END)
                STPinput.config(fg='grey')
                STPinput.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if STPinput.cget('fg') != 'black':
                        STPinput.delete(0, END)
                        STPinput.config(fg='black')
                def handle_focus_out(_):
                    if STPinput.get() == "":
                        STPinput.delete(0, END)
                        STPinput.config(fg='grey')
                        STPinput.insert(0, text)
                STPinput.bind("<FocusOut>", handle_focus_out)
                STPinput.bind("<FocusIn>", handle_focus_in)                
            else:
                text = 'NoInputRequired'
                STPinput.delete(0, END)
                STPinput.config(fg='grey')
                STPinput.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if STPinput.cget('fg') != 'black':
                        STPinput.delete(0, END)
                        STPinput.config(fg='black')
                def handle_focus_out(_):
                    if STPinput.get() == "":
                        STPinput.delete(0, END)
                        STPinput.config(fg='grey')
                        STPinput.insert(0, text)
                STPinput.bind("<FocusOut>", handle_focus_out)
                STPinput.bind("<FocusIn>", handle_focus_in)                
            
        
        OPTIONS = [
        "Enable STP",
        "STP fwd_time",
        "STP hello_time",
        "STP max_age",
        "STP priority",
        "STP root",
        "STP logging"
        ]
        STPopt = StringVar(STPframe)
        STPopt.set(OPTIONS[0])    # default value
        STPopt.trace("w", option_changed_STPopt)
        dropbox = OptionMenu(STPframe, STPopt, *OPTIONS)   
        dropbox.place(x=0, y=0)


        STPinput = Entry(STPframe, bg='white', width=40, fg='grey')
        STPinput.place(x=142, y=7)
        STPinput.insert(0, "mst | pvst | rapid-pvst")
        def handle_focus_in(_):
            if STPinput.cget('fg') != 'black':
                STPinput.delete(0, END)
                STPinput.config(fg='black')
        def handle_focus_out(_):
            if STPinput.get() == "":
                STPinput.delete(0, END)
                STPinput.config(fg='grey')
                STPinput.insert(0, "mst | pvst | rapid-pvst")    
        STPinput.bind("<FocusOut>", handle_focus_out)
        STPinput.bind("<FocusIn>", handle_focus_in)
        
        def STPclick():
            if chk_state_neg.get() == False:
                if STPopt.get() == "Enable STP":
                    remote_conn.send("conf t\n")
                    sleep(0.2)
                    remote_conn.send("spanning-t mode " + STPinput.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Spanning Tree Configuration', 'STP enabled with selected mode.', parent=window) 
                elif STPopt.get() == "STP fwd_time":
                    if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                        tkMessageBox.showinfo('ERROR', 'Please enter a VLAN ID above.', parent=window)
                    elif STPinput.get() == "" or STPinput.get() == "<4-30>":
                        tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("spanning-t vlan " + createv.get() + " forward-t " + STPinput.get() + "\n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP forward-time interval configured.', parent=window)
                elif STPopt.get() == "STP hello_time":
                    if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                        tkMessageBox.showinfo('ERROR', 'Please enter a VLAN ID above.', parent=window)
                    elif STPinput.get() == "" or STPinput.get() == "<1-10>":
                        tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("spanning-t vlan " + createv.get() + " hello-t " + STPinput.get() + "\n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP hello-time interval configured.', parent=window)
                elif STPopt.get() == "STP max_age":
                    if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                        tkMessageBox.showinfo('ERROR', 'Please enter a VLAN ID above.', parent=window)
                    elif STPinput.get() == "" or STPinput.get() == "<6-40>":
                        tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("spanning-t vlan " + createv.get() + " max-age " + STPinput.get() + "\n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP max-age configured.', parent=window)
                elif STPopt.get() == "STP priority":
                    if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                        tkMessageBox.showinfo('ERROR', 'Please enter a VLAN ID above.', parent=window)
                    elif STPinput.get() == "" or STPinput.get() == "eg. 0, 4096, 12288.. 61440 (increments of 4096)":
                        tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("spanning-t vlan " + createv.get() + " priority " + STPinput.get() + "\n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP bridge priority configured.', parent=window)
                elif STPopt.get() == "STP root":
                    if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                        tkMessageBox.showinfo('ERROR', 'Please enter a VLAN ID above.', parent=window)
                    elif STPinput.get() == "" or STPinput.get() == "pri|sec [dia <2-7> [hello <1-10>]]":
                        tkMessageBox.showinfo('ERROR', 'Please enter required value(s).', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("spanning-t vlan " + createv.get() + " root " + STPinput.get() + "\n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP root bridge configured.', parent=window)
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.2)
                    remote_conn.send("spanning-t logging \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Spanning Tree Configuration', 'STP logging enabled.', parent=window)
            else:
                if STPopt.get() == "Enable STP":
                    if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                        cmd = "no spanning-t \n"
                        res = "Spanning tree disabled."
                    else:
                        cmd = "no spanning-t vlan " + createv.get() + "\n"
                        res = "Spanning tree disabled for VLAN " + createv.get() + "."
                    remote_conn.send("conf t\n")
                    sleep(0.2)
                    remote_conn.send(cmd)
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Spanning Tree Configuration', res, parent=window) 
                elif STPopt.get() == "STP fwd_time":
                    if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                        tkMessageBox.showinfo('ERROR', 'Please enter a VLAN ID above.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("no spanning-t vlan " + createv.get() + " forward-t \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP forward-time reset.', parent=window)
                elif STPopt.get() == "STP hello_time":
                    if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                        tkMessageBox.showinfo('ERROR', 'Please enter a VLAN ID above.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("no spanning-t vlan " + createv.get() + " hello-t \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP hello-time reset.', parent=window)
                elif STPopt.get() == "STP max_age":
                    if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                        tkMessageBox.showinfo('ERROR', 'Please enter a VLAN ID above.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("no spanning-t vlan " + createv.get() + " max-age \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP max-age reset.', parent=window)
                elif STPopt.get() == "STP priority":
                    if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                        tkMessageBox.showinfo('ERROR', 'Please enter a VLAN ID above.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("no spanning-t vlan " + createv.get() + " priority \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP bridge priority reset.', parent=window)
                elif STPopt.get() == "STP root":
                    if createv.get() == "" or createv.get() == "e.g. 1, 4094, 3-15":
                        tkMessageBox.showinfo('ERROR', 'Please enter a VLAN ID above.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("no spanning-t vlan " + createv.get() + " root \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP root bridge reset.', parent=window)
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.2)
                    remote_conn.send("no spanning-t logging \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Spanning Tree Configuration', 'STP logging disabled.', parent=window)                
        btn = Button(STPframe, text="Aplicar", bg="orange", command=STPclick)
        btn.place(x=400, y=0)





        def option_changed_STPfeatopt(*args):
            if STPfeatopt.get() == "Features":
                text = ''
                STPfeatinput.delete(0, END)
                STPfeatinput.config(fg='grey')
                STPfeatinput.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if STPfeatinput.cget('fg') != 'black':
                        STPfeatinput.delete(0, END)
                        STPfeatinput.config(fg='black')
                def handle_focus_out(_):
                    if STPfeatinput.get() == "":
                        STPfeatinput.delete(0, END)
                        STPfeatinput.config(fg='grey')
                        STPfeatinput.insert(0, text)
                STPfeatinput.bind("<FocusOut>", handle_focus_out)
                STPfeatinput.bind("<FocusIn>", handle_focus_in)
            elif STPfeatopt.get() == "STP portfast" or STPfeatopt.get() == "STP rootguard" or STPfeatopt.get() == "STP loopguard" or STPfeatopt.get() == "STP BPDUguard" or \
                 STPfeatopt.get() == "STP BPDUfilter":
                text = 'eg. e0/0'
                STPfeatinput.delete(0, END)
                STPfeatinput.config(fg='grey')
                STPfeatinput.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if STPfeatinput.cget('fg') != 'black':
                        STPfeatinput.delete(0, END)
                        STPfeatinput.config(fg='black')
                def handle_focus_out(_):
                    if STPfeatinput.get() == "":
                        STPfeatinput.delete(0, END)
                        STPfeatinput.config(fg='grey')
                        STPfeatinput.insert(0, text)
                STPfeatinput.bind("<FocusOut>", handle_focus_out)
                STPfeatinput.bind("<FocusIn>", handle_focus_in)
            else:
                text = 'NoInputRequired'        #backbonefast, uplinkfast, ECguard
                STPfeatinput.delete(0, END)
                STPfeatinput.config(fg='grey')
                STPfeatinput.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if STPfeatinput.cget('fg') != 'black':
                        STPfeatinput.delete(0, END)
                        STPfeatinput.config(fg='black')
                def handle_focus_out(_):
                    if STPfeatinput.get() == "":
                        STPfeatinput.delete(0, END)
                        STPfeatinput.config(fg='grey')
                        STPfeatinput.insert(0, text)
                STPfeatinput.bind("<FocusOut>", handle_focus_out)
                STPfeatinput.bind("<FocusIn>", handle_focus_in)                
        OPTIONS = [
        "Features",
        "STP portfast",
        "STP backbonefast",
        "STP uplinkfast",
        "STP rootguard",
        "STP loopguard",
        "STP BPDUguard",
        "STP BPDUfilter",
        "STP ECguard"
        ]
        STPfeatopt = StringVar(STPframe)
        STPfeatopt.set(OPTIONS[0])    # default value
        STPfeatopt.trace("w", option_changed_STPfeatopt)
        dropbox = OptionMenu(STPframe, STPfeatopt, *OPTIONS)   
        dropbox.place(x=0, y=30)
        
        STPfeatinput = Entry(STPframe, bg='white', width=40, fg='grey')
        STPfeatinput.place(x=142, y=37)
        STPfeatinput.insert(0, "")
        def handle_focus_in(_):
            if STPfeatinput.cget('fg') != 'black':
                STPfeatinput.delete(0, END)
                STPfeatinput.config(fg='black')
        def handle_focus_out(_):
            if STPfeatinput.get() == "":
                STPfeatinput.delete(0, END)
                STPfeatinput.config(fg='grey')
                STPfeatinput.insert(0, "")    
        STPfeatinput.bind("<FocusOut>", handle_focus_out)
        STPfeatinput.bind("<FocusIn>", handle_focus_in)
        
        def STPfeatclick():
            if STPfeatopt.get() == "Features":
                tkMessageBox.showinfo('ERROR', 'Please choose an option.', parent=window)
            else:
                if chk_state_neg.get() == False:
                    if STPfeatopt.get() == "STP portfast" or STPfeatopt.get() == "STP rootguard" or STPfeatopt.get() == "STP loopguard" or STPfeatopt.get() == "STP BPDUguard" or \
                       STPfeatopt.get() == "STP BPDUfilter":
                        if STPfeatinput.get() == "" or STPfeatinput.get() == "eg. e0/0":
                            tkMessageBox.showinfo('ERROR', 'Please enter an interface.', parent=window)
                        else:
                            if STPfeatopt.get() == "STP portfast":
                                cmd = "spanning-tree portfast \n"
                                res = "STP portfast enabled on interface."
                            elif STPfeatopt.get() == "STP rootguard":
                                cmd = "spanning-tree guard root \n"
                                res = "STP rootguard enabled on interface."
                            elif STPfeatopt.get() == "STP loopguard":
                                cmd = "spanning-tree guard loop \n"
                                res = "STP loopguard enabled on interface."
                            elif STPfeatopt.get() == "STP BPDUguard":
                                cmd = "spanning-tree BPDUguard en \n"
                                res = "STP BPDUguard enabled on interface."
                            else:
                                cmd = "spanning-tree BPDUfilter en \n"
                                res = "STP BPDUfilter enabled on interface."
                            remote_conn.send("conf t\n")
                            sleep(0.2)
                            remote_conn.send("int " + STPfeatinput.get() + "\n")
                            sleep(0.2)
                            remote_conn.send(cmd)
                            sleep(0.2)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('Spanning Tree Configuration', res, parent=window) 
                    elif STPopt.get() == "STP backbonefast":
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("spanning-t backbonefast \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP backbonefast enabled globally.', parent=window)
                    elif STPopt.get() == "STP uplinkfast":
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("spanning-t uplinkfast \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP uplinkfast enabled globally.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("spanning-t etherchannel guard misconfig \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP Etherchannel misconfiguration guard enabled globally.', parent=window)
                else:
                    if STPfeatopt.get() == "STP portfast" or STPfeatopt.get() == "STP rootguard" or STPfeatopt.get() == "STP loopguard" or STPfeatopt.get() == "STP BPDUguard" or \
                       STPfeatopt.get() == "STP BPDUfilter":
                        if STPfeatinput.get() == "" or STPfeatinput.get() == "eg. e0/0":
                            tkMessageBox.showinfo('ERROR', 'Please enter an interface.', parent=window)
                        else:
                            if STPfeatopt.get() == "STP portfast":
                                cmd = "spanning-tree portfast disable \n"
                                res = "STP portfast disabled on interface."
                            elif STPfeatopt.get() == "STP rootguard":
                                cmd = "no spanning-tree guard root \n"
                                res = "STP rootguard disabled on interface."
                            elif STPfeatopt.get() == "STP loopguard":
                                cmd = "no spanning-tree guard loop \n"
                                res = "STP loopguard disabled on interface."
                            elif STPfeatopt.get() == "STP BPDUguard":
                                cmd = "spanning-tree BPDUguard dis \n"
                                res = "STP BPDUguard disabled on interface."
                            else:
                                cmd = "spanning-tree BPDUfilter dis \n"
                                res = "STP BPDUfilter disabled on interface."
                            remote_conn.send("conf t\n")
                            sleep(0.2)
                            remote_conn.send("int " + STPfeatinput.get() + "\n")
                            sleep(0.2)
                            remote_conn.send(cmd)
                            sleep(0.2)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('Spanning Tree Configuration', res, parent=window) 
                    elif STPopt.get() == "STP backbonefast":
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("no spanning-t backbonefast \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP backbonefast disabled globally.', parent=window)
                    elif STPopt.get() == "STP uplinkfast":
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("no spanning-t uplinkfast \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP uplinkfast disabled globally.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.2)
                        remote_conn.send("no spanning-t etherchannel guard misconfig \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Spanning Tree Configuration', 'STP Etherchannel misconfiguration guard disabled globally.', parent=window)                    
        btn = Button(STPframe, text="Aplicar", bg="orange", command=STPfeatclick)
        btn.place(x=400, y=30)





        SwitchShowframe=LabelFrame(window,text=" Show/Clear VLAN & Switchport ",font=('verdana', 8, 'bold'),padx=10,width=100,height=100)
        SwitchShowframe.grid(column=0, row=3, sticky=("nsew"))

        def option_changed_showVLANopt(*args):
            if showVLANopt.get() == "VLAN (id)":
                text = '<1-4094>'
                shvlanid.delete(0, END)
                shvlanid.config(fg='grey')
                shvlanid.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if shvlanid.cget('fg') != 'black':
                        shvlanid.delete(0, END)
                        shvlanid.config(fg='black')
                def handle_focus_out(_):
                    if shvlanid.get() == "":
                        shvlanid.delete(0, END)
                        shvlanid.config(fg='grey')
                        shvlanid.insert(0, text)
                shvlanid.bind("<FocusOut>", handle_focus_out)
                shvlanid.bind("<FocusIn>", handle_focus_in)
            else:
                text = 'NoInputRequired'
                shvlanid.delete(0, END)
                shvlanid.config(fg='grey')
                shvlanid.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if shvlanid.cget('fg') != 'black':
                        shvlanid.delete(0, END)
                        shvlanid.config(fg='black')
                def handle_focus_out(_):
                    if shvlanid.get() == "":
                        shvlanid.delete(0, END)
                        shvlanid.config(fg='grey')
                        shvlanid.insert(0, text)
                shvlanid.bind("<FocusOut>", handle_focus_out)
                shvlanid.bind("<FocusIn>", handle_focus_in)                
                
        OPTIONS = [
        "VLAN (id)",
        "VLAN brief",
        "VLANs summary",
        "Private VLANs",
        "RSPAN VLANs"
        ]
        showVLANopt = StringVar(SwitchShowframe)
        showVLANopt.set(OPTIONS[0])    # default value
        showVLANopt.trace("w", option_changed_showVLANopt)
        dropbox = OptionMenu(SwitchShowframe, showVLANopt, *OPTIONS)   
        dropbox.grid(row=0, column=0)

        shvlanid = Entry(SwitchShowframe, bg='white', width=40, fg='grey')
        shvlanid.place(x=142, y=5)
        shvlanid.insert(0, "<1-4094>")
        def handle_focus_in(_):
            if shvlanid.cget('fg') != 'black':
                shvlanid.delete(0, END)
                shvlanid.config(fg='black')
        def handle_focus_out(_):
            if shvlanid.get() == "":
                shvlanid.delete(0, END)
                shvlanid.config(fg='grey')
                shvlanid.insert(0, "<1-4094>")    
        shvlanid.bind("<FocusOut>", handle_focus_out)
        shvlanid.bind("<FocusIn>", handle_focus_in)
        
        def showvlan():
            if showVLANopt.get() == "VLAN (id)":
                if shvlanid.get() == '' or shvlanid.get() == '<1-4094>':
                    tkMessageBox.showinfo('Error', 'Please enter a VLAN ID.', parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("show vlan id " + shvlanid.get() + "\n")
                    sleep(0.5)        
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 2048
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('VLAN info', output, parent=window)
            else:
                if showVLANopt.get() == "VLAN brief":
                    cmd = "show vlan br \n"
                elif showVLANopt.get() == "VLANs summary":
                    cmd = "show vlan summ \n"
                elif showVLANopt.get() == "Private VLANs":
                    cmd = "show vlan private-v \n"
                else:
                    cmd = "show vlan remote-span \n"
                        
                buff_size = 16384
                sleep(0.5)
                remote_conn.send(cmd)
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('VLAN info', output, parent=window)

        btn = Button(SwitchShowframe, text="Show", bg="orange", command=showvlan)
        btn.place(x=400, y=0)





        

        def option_changed_showportopt(*args):
            if showportopt.get() == "SwitchPort" or showportopt.get() == "DTP":
                text = 'eg. fa0/0'
                shport.delete(0, END)
                shport.config(fg='grey')
                shport.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if shport.cget('fg') != 'black':
                        shport.delete(0, END)
                        shport.config(fg='black')
                def handle_focus_out(_):
                    if shport.get() == "":
                        shport.delete(0, END)
                        shport.config(fg='grey')
                        shport.insert(0, text)
                shport.bind("<FocusOut>", handle_focus_out)
                shport.bind("<FocusIn>", handle_focus_in)
            elif showportopt.get() == "VTP":
                text = 'status | counters | password'
                shport.delete(0, END)
                shport.config(fg='grey')
                shport.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if shport.cget('fg') != 'black':
                        shport.delete(0, END)
                        shport.config(fg='black')
                def handle_focus_out(_):
                    if shport.get() == "":
                        shport.delete(0, END)
                        shport.config(fg='grey')
                        shport.insert(0, text)
                shport.bind("<FocusOut>", handle_focus_out)
                shport.bind("<FocusIn>", handle_focus_in)
            else:
                text = 'NoInputRequired'
                shport.delete(0, END)
                shport.config(fg='grey')
                shport.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if shport.cget('fg') != 'black':
                        shport.delete(0, END)
                        shport.config(fg='black')
                def handle_focus_out(_):
                    if shport.get() == "":
                        shport.delete(0, END)
                        shport.config(fg='grey')
                        shport.insert(0, text)
                shport.bind("<FocusOut>", handle_focus_out)
                shport.bind("<FocusIn>", handle_focus_in)                
                
        OPTIONS = [
        "SwitchPort",
        "Trunk",
        "DTP",
        "VTP"
        ]
        showportopt = StringVar(SwitchShowframe)
        showportopt.set(OPTIONS[0])    # default value
        showportopt.trace("w", option_changed_showportopt)
        dropbox = OptionMenu(SwitchShowframe, showportopt, *OPTIONS)   
        dropbox.grid(row=1, column=0)

        shport = Entry(SwitchShowframe, bg='white', width=40, fg='grey')
        shport.place(x=142, y=35)
        shport.insert(0, "eg. fa0/0")
        def handle_focus_in(_):
            if shport.cget('fg') != 'black':
                shport.delete(0, END)
                shport.config(fg='black')
        def handle_focus_out(_):
            if shport.get() == "":
                shport.delete(0, END)
                shport.config(fg='grey')
                shport.insert(0, "eg. fa0/0")    
        shport.bind("<FocusOut>", handle_focus_out)
        shport.bind("<FocusIn>", handle_focus_in)
        

        def showportdtpvtp():
            if showportopt.get() == "SwitchPort":
                if shport.get() == '' or shport.get() == 'eg. fa0/0':
                    tkMessageBox.showinfo('Error', 'Please enter an interface (eg. fa0/0).', parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("show interface " + shport.get() + " switchport \n")
                    sleep(0.5)        
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 2048
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('Switchport info', output, parent=window)
            elif showportopt.get() == "DTP":
                if shport.get() == '' or shport.get() == 'eg. fa0/0':
                    tkMessageBox.showinfo('Error', 'Please enter an interface (eg. fa0/0).', parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("show dtp interface " + shport.get() + " \n")
                    sleep(0.5)        
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 2048
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('DTP info', output, parent=window)
            elif showportopt.get() == "VTP":
                if shport.get() == '' or shport.get() == 'status | counters | password':
                    tkMessageBox.showinfo('Error', 'Please enter an option (eg. status).', parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("show vtp " + shport.get() + " \n")
                    sleep(0.5)        
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 2048
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('VTP info', output, parent=window)
            else:
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show int trunk \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Trunk info', output, parent=window)
        btn = Button(SwitchShowframe, text="Show", bg="orange", command=showportdtpvtp)
        btn.place(x=400, y=30)









        def option_changed_showSTPopt(*args):
            if showSTPopt.get() == "STP interface":
                text = 'eg. fa0/0, vlan 1'
                shstp.delete(0, END)
                shstp.config(fg='grey')
                shstp.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if shstp.cget('fg') != 'black':
                        shstp.delete(0, END)
                        shstp.config(fg='black')
                def handle_focus_out(_):
                    if shstp.get() == "":
                        shstp.delete(0, END)
                        shstp.config(fg='grey')
                        shstp.insert(0, text)
                shstp.bind("<FocusOut>", handle_focus_out)
                shstp.bind("<FocusIn>", handle_focus_in)
            elif showSTPopt.get() == "STP detail":
                text = 'eg. Ethernet0/0, FastEthernet0/0'
                shstp.delete(0, END)
                shstp.config(fg='grey')
                shstp.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if shstp.cget('fg') != 'black':
                        shstp.delete(0, END)
                        shstp.config(fg='black')
                def handle_focus_out(_):
                    if shstp.get() == "":
                        shstp.delete(0, END)
                        shstp.config(fg='grey')
                        shstp.insert(0, text)
                shstp.bind("<FocusOut>", handle_focus_out)
                shstp.bind("<FocusIn>", handle_focus_in)
            elif showSTPopt.get() == "STP root":
                text = 'eg. e0/0, vlan 1'
                shstp.delete(0, END)
                shstp.config(fg='grey')
                shstp.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if shstp.cget('fg') != 'black':
                        shstp.delete(0, END)
                        shstp.config(fg='black')
                def handle_focus_out(_):
                    if shstp.get() == "":
                        shstp.delete(0, END)
                        shstp.config(fg='grey')
                        shstp.insert(0, text)
                shstp.bind("<FocusOut>", handle_focus_out)
                shstp.bind("<FocusIn>", handle_focus_in)
            elif showSTPopt.get() == "MST":
                text = 'config | detail | int <e0/0>'
                shstp.delete(0, END)
                shstp.config(fg='grey')
                shstp.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if shstp.cget('fg') != 'black':
                        shstp.delete(0, END)
                        shstp.config(fg='black')
                def handle_focus_out(_):
                    if shstp.get() == "":
                        shstp.delete(0, END)
                        shstp.config(fg='grey')
                        shstp.insert(0, text)
                shstp.bind("<FocusOut>", handle_focus_out)
                shstp.bind("<FocusIn>", handle_focus_in)
            elif showSTPopt.get() == "STP summary":
                text = '[total]'
                shstp.delete(0, END)
                shstp.config(fg='grey')
                shstp.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if shstp.cget('fg') != 'black':
                        shstp.delete(0, END)
                        shstp.config(fg='black')
                def handle_focus_out(_):
                    if shstp.get() == "":
                        shstp.delete(0, END)
                        shstp.config(fg='grey')
                        shstp.insert(0, text)
                shstp.bind("<FocusOut>", handle_focus_out)
                shstp.bind("<FocusIn>", handle_focus_in)
            else:
                text = 'NoInputRequired'
                shstp.delete(0, END)
                shstp.config(fg='grey')
                shstp.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if shstp.cget('fg') != 'black':
                        shstp.delete(0, END)
                        shstp.config(fg='black')
                def handle_focus_out(_):
                    if shstp.get() == "":
                        shstp.delete(0, END)
                        shstp.config(fg='grey')
                        shstp.insert(0, text)
                shstp.bind("<FocusOut>", handle_focus_out)
                shstp.bind("<FocusIn>", handle_focus_in)                
                
        OPTIONS = [
        "STP summary",
        "STP interface",
        "STP detail",
        "STP root",
        "STP inconsistency",
        "MST"
        ]
        showSTPopt = StringVar(SwitchShowframe)
        showSTPopt.set(OPTIONS[0])    # default value
        showSTPopt.trace("w", option_changed_showSTPopt)
        dropbox = OptionMenu(SwitchShowframe, showSTPopt, *OPTIONS)   
        dropbox.grid(row=2, column=0)

        shstp = Entry(SwitchShowframe, bg='white', width=40, fg='grey')
        shstp.place(x=142, y=65)
        shstp.insert(0, "NoInputRequired")
        def handle_focus_in(_):
            if shstp.cget('fg') != 'black':
                shstp.delete(0, END)
                shstp.config(fg='black')
        def handle_focus_out(_):
            if shstp.get() == "":
                shstp.delete(0, END)
                shstp.config(fg='grey')
                shstp.insert(0, "NoInputRequired")    
        shstp.bind("<FocusOut>", handle_focus_out)
        shstp.bind("<FocusIn>", handle_focus_in)
        

        def showSTP():
            if showSTPopt.get() == "STP interface":
                if shstp.get() == '' or shstp.get() == 'eg. fa0/0, vlan 1':
                    tkMessageBox.showinfo('Error', 'Please enter an interface or VLAN interface (eg. fa0/0, vlan 1).', parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("sh spanning-tree interface " + shstp.get() + " \n")
                    sleep(0.5)        
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 2048
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('Spanning Tree Info', output, parent=window)
            elif showSTPopt.get() == "STP detail":
                if shstp.get() == '' or shstp.get() == 'eg. Ethernet0/0, FastEthernet0/0':
                    tkMessageBox.showinfo('Error', 'Please enter an interface (eg. Ethernet0/0, FastEthernet0/0).', parent=window)
                else:
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("show spanning-tree detail | s " + shstp.get() + " \n")
                    sleep(0.5)        
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 2048
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('Spanning Tree info', output, parent=window)
            elif showSTPopt.get() == "STP root":
                if shstp.get() == '' or shstp.get() == 'eg. e0/0, vlan 1':
                    tkMessageBox.showinfo('Error', 'Please enter an interface or VLAN interface (eg. fa0/0, vlan 1).', parent=window)
                else:
                    if "vl" not in shport.get():
                        cmd = "show spanning-tree int " + shstp.get() + " \n"
                    else:
                        cmd = "show spanning-tree vlan " + shstp.get() + " \n"
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send(cmd)
                    sleep(0.5)        
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 2048
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    tkMessageBox.showinfo('Spanning Tree info', output, parent=window)
            else:
                if showSTPopt.get() == "STP summary" and (shstp.get() == "" or shstp.get() == "[total]"):
                    cmd = "show spanning-tree summary " + shstp.get() + " \n"
                elif showportopt.get() == "STP summary" and (shstp.get() != "" and shstp.get() != "[total]"):
                    cmd = "show spanning-tree summary " + shstp.get() + " total \n"
                else:
                    cmd = "show spanning-tree inconsisten \n"
                buff_size = 16384
                sleep(0.5)
                remote_conn.send(cmd)
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Spanning Tree info', output, parent=window)
        btn = Button(SwitchShowframe, text="Show", bg="orange", command=showSTP)
        btn.place(x=400, y=60)




        






        
    def DHCP():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("DHCP Control")
        window.geometry('550x350')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)

        negframe=LabelFrame(window,text=" Negate ",font=('verdana', 8, 'bold'),padx=17,pady=0,width=100,height=100)
        negframe.grid(row=0,column=1)
        chk_state_neg = BooleanVar()
        chk_state_neg.set(False)
        chk = Checkbutton(negframe, variable=chk_state_neg)
        chk.grid(column=3, row=1)


        dhcpframe=LabelFrame(window,text=" Configure DHCP Server ",font=('verdana', 8, 'bold'),padx=17,pady=0,width=100,height=100)
        dhcpframe.grid(row=0,column=0, sticky=("nsew"))
        
        lbl = Label(dhcpframe, text="Create DHCP pool name:").grid(column=0, row=2)                
        poolname = Entry(dhcpframe, width=17)
        poolname.grid(column=1, row=2)        

        lbl = Label(dhcpframe, text="DHCP pool subnet & mask:").grid(column=0, row=3)
        leasesubnet = Entry(dhcpframe, bg='white', width=17, fg='grey')
        leasesubnet.grid(column=1, row=3)
        leasesubnet.insert(0, "e.g. 192.168.1.0")
        def handle_focus_in(_):
            if leasesubnet.cget('fg') != 'black':
                leasesubnet.delete(0, END)
                leasesubnet.config(fg='black')
        def handle_focus_out(_):
            if leasesubnet.get() == "":
                leasesubnet.delete(0, END)
                leasesubnet.config(fg='grey')
                leasesubnet.insert(0, "e.g. 192.168.1.0")    
        leasesubnet.bind("<FocusOut>", handle_focus_out)
        leasesubnet.bind("<FocusIn>", handle_focus_in)

        leasemask = Entry(dhcpframe, bg='white', width=17, fg='grey')
        leasemask.grid(column=2, row=3)
        leasemask.insert(0, "e.g. 255.255.255.0")
        def handle_focus_in(_):
            if leasemask.cget('fg') != 'black':
                leasemask.delete(0, END)
                leasemask.config(fg='black')
        def handle_focus_out(_):
            if leasemask.get() == "":
                leasemask.delete(0, END)
                leasemask.config(fg='grey')
                leasemask.insert(0, "e.g. 255.255.255.0")    
        leasemask.bind("<FocusOut>", handle_focus_out)
        leasemask.bind("<FocusIn>", handle_focus_in)



        lbl = Label(dhcpframe, text="DHCP pool default gw & DNS:").grid(column=0, row=4)        
        defaultgateway = Entry(dhcpframe, bg='white', width=17, fg='grey')
        defaultgateway.grid(column=1, row=4)
        defaultgateway.insert(0, "e.g. 192.168.1.254")
        def handle_focus_in(_):
            if defaultgateway.cget('fg') != 'black':
                defaultgateway.delete(0, END)
                defaultgateway.config(fg='black')
        def handle_focus_out(_):
            if defaultgateway.get() == "":
                defaultgateway.delete(0, END)
                defaultgateway.config(fg='grey')
                defaultgateway.insert(0, "e.g. 192.168.1.254")    
        defaultgateway.bind("<FocusOut>", handle_focus_out)
        defaultgateway.bind("<FocusIn>", handle_focus_in)
        
        dnsServers = Entry(dhcpframe, bg='white', width=22, fg='grey')
        dnsServers.grid(column=2, row=4)
        dnsServers.insert(0, "e.g. 8.8.8.8 182.23.148.33")
        def handle_focus_in(_):
            if dnsServers.cget('fg') != 'black':
                dnsServers.delete(0, END)
                dnsServers.config(fg='black')
        def handle_focus_out(_):
            if dnsServers.get() == "":
                dnsServers.delete(0, END)
                dnsServers.config(fg='grey')
                dnsServers.insert(0, "e.g. 8.8.8.8 182.23.148.33")    
        dnsServers.bind("<FocusOut>", handle_focus_out)
        dnsServers.bind("<FocusIn>", handle_focus_in)


        lbl = Label(dhcpframe, text="DHCP IP lease time:").grid(column=0, row=5)
        leasetime = Entry(dhcpframe, bg='white', width=17, fg='grey')
        leasetime.grid(column=1, row=5)
        leasetime.insert(0, "e.g. 2 5 == 2 days 5 hrs")
        def handle_focus_in(_):
            if leasetime.cget('fg') != 'black':
                leasetime.delete(0, END)
                leasetime.config(fg='black')
        def handle_focus_out(_):
            if leasetime.get() == "":
                leasetime.delete(0, END)
                leasetime.config(fg='grey')
                leasetime.insert(0, "e.g. 2 5 == 2 days 5 hrs")    
        leasetime.bind("<FocusOut>", handle_focus_out)
        leasetime.bind("<FocusIn>", handle_focus_in)


        
        def dhcpserverlease():
            if chk_state_neg.get() == False:
                if poolname.get() == "" or leasesubnet.get() == "" or leasesubnet.get() == "e.g. 192.168.1.0" or leasemask.get() == "" or\
                    leasemask.get() == "e.g. 255.255.255.0":
                    tkMessageBox.showinfo('Error', 'Minimal requirement is to enter a Pool Name, Lease Subnet and Lease Subnet Mask.', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.2)
                    remote_conn.send("ip dhcp pool " + poolname.get() + " \n")
                    sleep(0.2)
                    remote_conn.send("network " + leasesubnet.get() + " " + leasemask.get() + " \n")
                    sleep(0.2)
                    if defaultgateway.get() != "" and defaultgateway.get() != "e.g. 192.168.1.254":
                        remote_conn.send("default-router " + defaultgateway.get() + " \n")
                        sleep(0.2)
                    else:
                        pass
                    sleep(0.2)
                    if leasetime.get() != "" and leasetime.get() != "e.g. 2 5 == 2 days 5 hrs":
                        remote_conn.send("lease " + leasetime.get() + " \n")
                        sleep(0.2)
                    else:
                        pass
                    sleep(0.2)
                    if dnsServers.get() != "" and dnsServers.get() != "e.g. 8.8.8.8 182.23.148.33":
                        remote_conn.send("dns-server " + dnsServers.get() + " \n")
                        sleep(0.2)
                    else:
                        pass
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    res = "DHCP range has been leased."
                    tkMessageBox.showinfo('DHCP', res, parent=window)
            else:
                remote_conn.send("conf t \n")
                sleep(0.2)
                if poolname.get() != "" and (leasesubnet.get() != "" and leasesubnet.get() != "e.g. 192.168.1.0")\
                and (leasemask.get() != "" or leasemask.get() != "e.g. 255.255.255.0"):
                    remote_conn.send("ip dhcp pool " + poolname.get() + " \n")
                    sleep(0.2)
                    remote_conn.send("no network " + leasesubnet.get() + " " + leasemask.get() + " \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    tkMessageBox.showinfo('DHCP', 'Network removed', parent=window)                     
                elif poolname.get() != "" and (defaultgateway.get() != "" and defaultgateway.get() != "e.g. 192.168.1.254"):
                    remote_conn.send("ip dhcp pool " + poolname.get() + " \n")
                    sleep(0.2)                    
                    remote_conn.send("no default-router " + defaultgateway.get() + " \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    tkMessageBox.showinfo('DHCP', 'Default router configured.', parent=window)                      
                elif poolname.get() != "" and (leasetime.get() != "" and leasetime.get() != "e.g. 2 5 == 2 days 5 hrs"):
                    remote_conn.send("ip dhcp pool " + poolname.get() + " \n")
                    sleep(0.2)
                    remote_conn.send("no lease " + leasetime.get() + " \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    tkMessageBox.showinfo('DHCP', 'Lease time configured.', parent=window)                     
                elif poolname.get() != "" and (dnsServers.get() != "" and dnsServers.get() != "e.g. 8.8.8.8 182.23.148.33"):
                    remote_conn.send("ip dhcp pool " + poolname.get() + " \n")
                    sleep(0.2)                    
                    remote_conn.send("no dns-server " + dnsServers.get() + " \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    tkMessageBox.showinfo('DHCP', 'DNS servers configured for pool.', parent=window)
                elif poolname.get() != "" and (dnsServers.get() != "" and dnsServers.get() != "e.g. 8.8.8.8 182.23.148.33") and \
                (leasesubnet.get() != "" and leasesubnet.get() != "e.g. 192.168.1.0") and (defaultgateway.get() != "" and \
                defaultgateway.get() != "e.g. 192.168.1.254") and (leasetime.get() != "" and leasetime.get() != "e.g. 2 5 == 2 days 5 hrs"):
                    remote_conn.send("no ip dhcp pool " + poolname.get() + " \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    tkMessageBox.showinfo('DHCP', 'DHCP pool ' + poolname.get() + ' deleted.', parent=window)
                else:
                    tkMessageBox.showinfo('Error', 'To negate, please fill up required fields: Poolname + network/default-router/lease time/DNS.\
                                                    Or, just enter poolname to delete.', parent=window)                    
        btn = Button(dhcpframe, text="Aplicar DHCP server", bg="orange", command=dhcpserverlease)
        btn.grid(column=1, row=6)


        blankdivider0 = Label(window, text=" ").grid(column=0, row=7)

        lbl1 = Label(dhcpframe, text="Set DHCP excluded:").grid(column=0, row=8)
        leaseexcludefrom = Entry(dhcpframe,width=15)
        leaseexcludefrom.grid(column=1, row=8)
        leaseexcludeto = Entry(dhcpframe,width=15)
        leaseexcludeto.grid(column=2, row=8)
        def dhcpserverexc():
            if chk_state_neg.get() == False:            
                remote_conn.send("conf t \n")
                sleep(0.2)             
                remote_conn.send("ip dhcp excluded-addr " + leaseexcludefrom.get() + " " + leaseexcludeto.get() + " \n")
                sleep(0.2)               
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('DHCP excluded', 'DCHP range has been excluded from leasing to clients.', parent=window)
            else:
                remote_conn.send("conf t \n")
                sleep(0.2)             
                remote_conn.send("no ip dhcp excluded-addr " + leaseexcludefrom.get() + " " + leaseexcludeto.get() + " \n")
                sleep(0.2)               
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('DHCP excluded', 'DCHP excluded range has been removed.', parent=window)                
        btn = Button(dhcpframe, text="Aplicar excluded", bg="orange", command=dhcpserverexc)
        btn.grid(column=1, row=9)

        blankdivider1 = Label(dhcpframe, text=" ").grid(column=0, row=10)

        showdhcpframe=LabelFrame(window,text=" Show DHCP config ",font=('verdana', 8, 'bold'),padx=17,pady=0,width=100,height=50)
        showdhcpframe.grid(row=1,column=0, sticky=("nsew"))



        OPTIONS = [
        "Config",
        "Server info",
        "Bindings",
        "Clear all bindings"
        ]
        shDHCPopt = StringVar(showdhcpframe)
        shDHCPopt.set(OPTIONS[0])    # default value
#        shDHCPopt.trace("w", option_changed_shDHCPopt)
        dropbox = OptionMenu(showdhcpframe, shDHCPopt, *OPTIONS)   
        dropbox.place(x=0, y=0)


        def cleardhcp():
            if shDHCPopt.get() == "Config":
                cmd = "show run | s dhcp \n"
            elif shDHCPopt.get() == "Server info":
                cmd = "show dhcp server \n"
            elif shDHCPopt.get() == "Bindings":
                cmd = "show ip dhcp binding \n"
            else:
                cmd = "clear ip dhcp binding * \n"

            buff_size = 65535
            sleep(0.5)
            remote_conn.send(cmd)
            sleep(1)
            while not remote_conn.recv_ready():
                remote_conn.recv(0)
                buff_size += 1024
                sleep(0.5)
            output = remote_conn.recv(buff_size).decode("utf-8")
            sleep(0.2)
            tkMessageBox.showinfo('DHCP', output, parent=window)
        btn = Button(showdhcpframe, text="Show", bg="orange", command=cleardhcp)
        btn.place(x=300, y=0)

  




    def ACL():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("ACL Control")
        window.geometry('560x640')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)


        negframe=LabelFrame(window,text=" Negate ",font=('verdana', 8, 'bold'),padx=17,pady=0,width=100,height=100)
        negframe.grid(row=0,column=1)
        chk_state_neg = BooleanVar()
        chk_state_neg.set(False)
        chk = Checkbutton(negframe, variable=chk_state_neg)
        chk.grid(column=5, row=2)


        aclframe=LabelFrame(window,text=" Create ACL ",font=('verdana', 8, 'bold'),padx=17,pady=0,width=100,height=100)
        aclframe.grid(row=0,column=0, sticky=("nsew"))
        
        lbl = Label(aclframe, text="Standard ACL: ")    
        lbl.grid(column=0, row=2)
        aclnumber = Entry(aclframe, bg='white', width=17, fg='grey')
        aclnumber.grid(column=1, row=2)
        aclnumber.insert(0, "1-99, or 1300-1999")
        def handle_focus_in(_):
            if aclnumber.cget('fg') != 'black':
                aclnumber.delete(0, END)
                aclnumber.config(fg='black')
        def handle_focus_out(_):
            if aclnumber.get() == "":
                aclnumber.delete(0, END)
                aclnumber.config(fg='grey')
                aclnumber.insert(0, "1-99, or 1300-1999")    
        aclnumber.bind("<FocusOut>", handle_focus_out)
        aclnumber.bind("<FocusIn>", handle_focus_in)
        
        lbl1 = Label(aclframe, text="Source IP & mask: ")    
        lbl1.grid(column=0, row=3)
        aclip = Entry(aclframe, bg='white', width=15, fg='grey')
        aclip.grid(column=1, row=3)
        aclip.insert(0, "eg. 192.168.1.0")
        def handle_focus_in(_):
            if aclip.cget('fg') != 'black':
                aclip.delete(0, END)
                aclip.config(fg='black')
        def handle_focus_out(_):
            if aclip.get() == "":
                aclip.delete(0, END)
                aclip.config(fg='grey')
                aclip.insert(0, "eg. 192.168.1.0")    
        aclip.bind("<FocusOut>", handle_focus_out)
        aclip.bind("<FocusIn>", handle_focus_in)
        
        aclmask = Entry(aclframe, bg='white', width=15, fg='grey')
        aclmask.grid(column=2, row=3)
        aclmask.insert(0, "eg. 0.0.0.255")
        def handle_focus_in(_):
            if aclmask.cget('fg') != 'black':
                aclmask.delete(0, END)
                aclmask.config(fg='black')
        def handle_focus_out(_):
            if aclmask.get() == "":
                aclmask.delete(0, END)
                aclmask.config(fg='grey')
                aclmask.insert(0, "eg. 0.0.0.255")    
        aclmask.bind("<FocusOut>", handle_focus_out)
        aclmask.bind("<FocusIn>", handle_focus_in)
        
        OPTIONS = [
        "Allow",
        "Block"
        ]
        permitoptn1 = StringVar(aclframe)
        permitoptn1.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(aclframe, permitoptn1, *OPTIONS)   
        dropbox.grid(column=3, row=3)        


        chk_state_logacl = BooleanVar()
        chk_state_logacl.set(False)
        chk1 = Checkbutton(aclframe, text='Log', variable=chk_state_logacl)
        chk1.grid(column=3, row=0)      



        def stdaclclicked():
            if chk_state_neg.get() == True:
                remote_conn.send("conf t\n")
                sleep(0.5)
                remote_conn.send("no access-list " + aclnumber.get() + "\n")
                sleep(0.5)
                remote_conn.send("exit \n")
                res = "ACL " + aclnumber.get() + " removed. (Hint: there may be multiple sequences (rules) per ACL)"
                tkMessageBox.showinfo('ACL', res, parent=window)
            else:
                if (permitoptn1.get() == "Allow") and (chk_state_logacl.get() == True):
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + aclnumber.get() + " permit " + aclip.get() + " " + aclmask.get() + " log \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "Standard ACL " + aclnumber.get() + " created to permit IP " + aclip.get() + " & mask " + aclmask.get() + ". Logged."
                    tkMessageBox.showinfo('ACL', res, parent=window)
                elif (permitoptn1.get() == "Allow") and (chk_state_logacl.get() == False):
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + aclnumber.get() + " permit " + aclip.get() + " " + aclmask.get() + "\n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "Standard ACL " + aclnumber.get() + " created to permit IP " + aclip.get() + " & mask " + aclmask.get() + "."
                    tkMessageBox.showinfo('ACL', res, parent=window)
                elif (permitoptn1.get() == "Block") and (chk_state_logacl.get() == True):
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + aclnumber.get() + " deny " + aclip.get() + " " + aclmask.get() + "log \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "Standard ACL " + aclnumber.get() + " created to deny IP " + aclip.get() + " & mask " + aclmask.get() + ". Logged."
                    tkMessageBox.showinfo('ACL', res, parent=window)                    
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + aclnumber.get() + " deny " + aclip.get() + " " + aclmask.get() + "\n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "Standard ACL " + aclnumber.get() + " created to deny IP " + aclip.get() + " & mask " + aclmask.get() + "."
                    tkMessageBox.showinfo('ACL', res, parent=window)                    
        btn = Button(aclframe, text="Create Std ACL", bg="orange", command=stdaclclicked)
        btn.grid(column=2, row=2)


        
        lbl3 = Label(aclframe, text="Extended ACL: ")    
        lbl3.grid(column=0, row=5)
        extaclnumber = Entry(aclframe, bg='white', width=17, fg='grey')
        extaclnumber.grid(column=1, row=5)
        extaclnumber.insert(0, "100-199, 2000-2699")
        def handle_focus_in(_):
            if extaclnumber.cget('fg') != 'black':
                extaclnumber.delete(0, END)
                extaclnumber.config(fg='black')
        def handle_focus_out(_):
            if extaclnumber.get() == "":
                extaclnumber.delete(0, END)
                extaclnumber.config(fg='grey')
                extaclnumber.insert(0, "100-199, 2000-2699")    
        extaclnumber.bind("<FocusOut>", handle_focus_out)
        extaclnumber.bind("<FocusIn>", handle_focus_in)
        
        lbl3 = Label(aclframe, text="Protocol: ")    
        lbl3.grid(column=0, row=6)
        extaclport = Entry(aclframe, bg='white', width=17, fg='grey')
        extaclport.grid(column=1, row=6)
        extaclport.insert(0, "tcp/udp/ip/<no.>")
        def handle_focus_in(_):
            if extaclport.cget('fg') != 'black':
                extaclport.delete(0, END)
                extaclport.config(fg='black')
        def handle_focus_out(_):
            if extaclport.get() == "":
                extaclport.delete(0, END)
                extaclport.config(fg='grey')
                extaclport.insert(0, "tcp/udp/ip/<no.>")    
        extaclport.bind("<FocusOut>", handle_focus_out)
        extaclport.bind("<FocusIn>", handle_focus_in)
        
        lbl4 = Label(aclframe, text="Source IP & mask: ")    
        lbl4.grid(column=0, row=7)
        extaclsrcip = Entry(aclframe, bg='white', width=15, fg='grey')
        extaclsrcip.grid(column=1, row=7)
        extaclsrcip.insert(0, "eg 192.168.1.1")
        def handle_focus_in(_):
            if extaclsrcip.cget('fg') != 'black':
                extaclsrcip.delete(0, END)
                extaclsrcip.config(fg='black')
        def handle_focus_out(_):
            if extaclsrcip.get() == "":
                extaclsrcip.delete(0, END)
                extaclsrcip.config(fg='grey')
                extaclsrcip.insert(0, "eg 192.168.1.1")    
        extaclsrcip.bind("<FocusOut>", handle_focus_out)
        extaclsrcip.bind("<FocusIn>", handle_focus_in)        
        extaclsrcmask = Entry(aclframe, bg='white', width=15, fg='grey')
        extaclsrcmask.grid(column=2, row=7)
        extaclsrcmask.insert(0, "eg. 0.0.0.0")
        def handle_focus_in(_):
            if extaclsrcmask.cget('fg') != 'black':
                extaclsrcmask.delete(0, END)
                extaclsrcmask.config(fg='black')
        def handle_focus_out(_):
            if extaclsrcmask.get() == "":
                extaclsrcmask.delete(0, END)
                extaclsrcmask.config(fg='grey')
                extaclsrcmask.insert(0, "eg. 0.0.0.0")    
        extaclsrcmask.bind("<FocusOut>", handle_focus_out)
        extaclsrcmask.bind("<FocusIn>", handle_focus_in)
        
        lbl4 = Label(aclframe, text="Destination IP & mask: ")    
        lbl4.grid(column=0, row=8)
        extacldstip = Entry(aclframe, bg='white', width=15, fg='grey')
        extacldstip.grid(column=1, row=8)
        extacldstip.insert(0, "eg. 192.168.2.0")
        def handle_focus_in(_):
            if extacldstip.cget('fg') != 'black':
                extacldstip.delete(0, END)
                extacldstip.config(fg='black')
        def handle_focus_out(_):
            if extacldstip.get() == "":
                extacldstip.delete(0, END)
                extacldstip.config(fg='grey')
                extacldstip.insert(0, "eg. 192.168.2.0")    
        extacldstip.bind("<FocusOut>", handle_focus_out)
        extacldstip.bind("<FocusIn>", handle_focus_in)        
        extacldstmask = Entry(aclframe, bg='white', width=15, fg='grey')
        extacldstmask.grid(column=2, row=8)
        extacldstmask.insert(0, "eg. 0.0.0.255")
        def handle_focus_in(_):
            if extacldstmask.cget('fg') != 'black':
                extacldstmask.delete(0, END)
                extacldstmask.config(fg='black')
        def handle_focus_out(_):
            if extacldstmask.get() == "":
                extacldstmask.delete(0, END)
                extacldstmask.config(fg='grey')
                extacldstmask.insert(0, "eg. 0.0.0.255")    
        extacldstmask.bind("<FocusOut>", handle_focus_out)
        extacldstmask.bind("<FocusIn>", handle_focus_in)
        

        OPTIONS = [
        "Allow",
        "Block"
        ]
        permitoptn2 = StringVar(aclframe)
        permitoptn2.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(aclframe, permitoptn2, *OPTIONS)   
        dropbox.grid(column=3, row=8)
        
        def extaclclicked():
            if chk_state_neg.get() == True:
                remote_conn.send("conf t\n")
                sleep(0.5)
                remote_conn.send("no access-list " + extaclnumber.get() + "\n")
                sleep(0.5)
                remote_conn.send("exit \n")
                res = "ACL " + extaclnumber.get() + " removed. (Hint: there may be multiple sequences (rules) per ACL)"
                tkMessageBox.showinfo('ACL', res, parent=window)
            else:
                if (permitoptn2.get() == "Allow") and (chk_state_logacl.get() == True):
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + extaclnumber.get() + " permit " + extaclport.get() + " " + extaclsrcip.get() + " " + extaclsrcmask.get()
                                           + " " + extacldstip.get() + " " + extacldstmask.get() + " log \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "Extended ACL " + extaclnumber.get() + " created to permit. Logged."
                    tkMessageBox.showinfo('ACL', res, parent=window)
                elif (permitoptn2.get() == "Allow") and (chk_state_logacl.get() == False):
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + extaclnumber.get() + " permit " + extaclport.get() + " " + extaclsrcip.get() + " " + extaclsrcmask.get()
                                           + " " + extacldstip.get() + " " + extacldstmask.get() + "\n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "Extended ACL " + extaclnumber.get() + " created to permit."
                    tkMessageBox.showinfo('ACL', res, parent=window)
                elif (permitoptn2.get() == "Block") and (chk_state_logacl.get() == True):
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + extaclnumber.get() + " deny " + extaclport.get() + " " + extaclsrcip.get() + " " + extaclsrcmask.get()
                                           + " " + extacldstip.get() + " " + extacldstmask.get() + " log \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "Extended ACL " + extaclnumber.get() + " created to deny. Logged."
                    tkMessageBox.showinfo('ACL', res, parent=window)                    
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + extaclnumber.get() + " deny " + extaclport.get() + " " + extaclsrcip.get() + " " + extaclsrcmask.get()
                                           + " " + extacldstip.get() + " " + extacldstmask.get() + "\n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "Extended ACL " + extaclnumber.get() + " created to deny."
                    tkMessageBox.showinfo('ACL', res, parent=window)            
        btn = Button(aclframe, text="Create Ext ACL", bg="orange", command=extaclclicked)
        btn.grid(column=2, row=5)


        lbl3 = Label(aclframe, text="MAC ACL: ")    
        lbl3.grid(column=0, row=10)
        macaclnumber = Entry(aclframe, bg='white', width=15, fg='grey')
        macaclnumber.grid(column=1, row=10)
        macaclnumber.insert(0, "700-799")
        def handle_focus_in(_):
            if macaclnumber.cget('fg') != 'black':
                macaclnumber.delete(0, END)
                macaclnumber.config(fg='black')
        def handle_focus_out(_):
            if macaclnumber.get() == "":
                macaclnumber.delete(0, END)
                macaclnumber.config(fg='grey')
                macaclnumber.insert(0, "700-799")    
        macaclnumber.bind("<FocusOut>", handle_focus_out)
        macaclnumber.bind("<FocusIn>", handle_focus_in)

        
        lbl4 = Label(aclframe, text="Address & mask: ")    
        lbl4.grid(column=0, row=11)
        macacladdr = Entry(aclframe, bg='white', width=15, fg='grey')
        macacladdr.grid(column=1, row=11)
        macacladdr.insert(0, "eg. aaaa.bbbb.cccc")
        def handle_focus_in(_):
            if macacladdr.cget('fg') != 'black':
                macacladdr.delete(0, END)
                macacladdr.config(fg='black')
        def handle_focus_out(_):
            if macacladdr.get() == "":
                macacladdr.delete(0, END)
                macacladdr.config(fg='grey')
                macacladdr.insert(0, "eg. aaaa.bbbb.cccc")    
        macacladdr.bind("<FocusOut>", handle_focus_out)
        macacladdr.bind("<FocusIn>", handle_focus_in)
        

        macaclmask = Entry(aclframe, bg='white', width=15, fg='grey')
        macaclmask.grid(column=2, row=11)
        macaclmask.insert(0, "eg. 0000.0011.1111")
        def handle_focus_in(_):
            if macaclmask.cget('fg') != 'black':
                macaclmask.delete(0, END)
                macaclmask.config(fg='black')
        def handle_focus_out(_):
            if macaclmask.get() == "":
                macaclmask.delete(0, END)
                macaclmask.config(fg='grey')
                macaclmask.insert(0, "eg. 0000.0011.1111")    
        macaclmask.bind("<FocusOut>", handle_focus_out)
        macaclmask.bind("<FocusIn>", handle_focus_in)


        
        OPTIONS = [
        "Allow",
        "Block"
        ]
        permitoptn3 = StringVar(aclframe)
        permitoptn3.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(aclframe, permitoptn3, *OPTIONS)   
        dropbox.grid(column=3, row=11)        
        def macaclclicked():
            if chk_state_neg.get() == True:
                remote_conn.send("conf t\n")
                sleep(0.5)
                remote_conn.send("no access-list " + macaclnumber.get() + "\n")
                sleep(0.5)
                remote_conn.send("exit \n")
                res = "ACL " + macaclnumber.get() + " removed. (Hint: there may be multiple sequences (rules) per ACL)"
                tkMessageBox.showinfo('ACL', res, parent=window)
            else:
                if (permitoptn3.get() == "Allow") and (chk_state_logacl.get() == True):
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + macaclnumber.get() + " permit " + macacladdr.get() + " " + macaclmask.get() + " log \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "MAC ACL " + macaclnumber.get() + " created to permit address " + macacladdr.get() + " & mask " + macaclmask.get() + ". Logged."
                    tkMessageBox.showinfo('ACL', res, parent=window)
                elif (permitoptn3.get() == "Allow") and (chk_state_logacl.get() == False):
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + macaclnumber.get() + " permit " + macacladdr.get() + " " + macaclmask.get() + "\n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "MAC ACL " + macaclnumber.get() + " created to permit address " + macacladdr.get() + " & mask " + macaclmask.get() + "."
                    tkMessageBox.showinfo('ACL', res, parent=window)
                elif (permitoptn3.get() == "Block") and (chk_state_logacl.get() == True):
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + macaclnumber.get() + " deny " + macacladdr.get() + " " + macaclmask.get() + "log \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "MAC ACL " + macaclnumber.get() + " created to deny address " + macacladdr.get() + " & mask " + macaclmask.get() + ". Logged."
                    tkMessageBox.showinfo('ACL', res, parent=window)                    
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("access-list " + macaclnumber.get() + " deny " + macacladdr.get() + " " + macaclmask.get() + "\n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "MAC ACL " + macaclnumber.get() + " created to deny address " + macacladdr.get() + " & mask " + macaclmask.get() + "."
                    tkMessageBox.showinfo('ACL', res, parent=window)                    
        btn = Button(aclframe, text="Create MAC ACL", bg="orange", command=macaclclicked)
        btn.grid(column=2, row=10)








        setaclframe=LabelFrame(window,text=" Aplicar ACL to interface or VTY ",font=('verdana', 8, 'bold'),padx=70,pady=5,width=100,height=100)
        setaclframe.grid(row=1,column=0, sticky=("nsew"))

        getiface = Entry(setaclframe, bg='white', width=15, fg='grey')
        getiface.grid(column=1, row=13)
        getiface.insert(0, "eg. fa0/0, vty 0")
        def handle_focus_in(_):
            if getiface.cget('fg') != 'black':
                getiface.delete(0, END)
                getiface.config(fg='black')
        def handle_focus_out(_):
            if getiface.get() == "":
                getiface.delete(0, END)
                getiface.config(fg='grey')
                getiface.insert(0, "eg. fa0/0, vty 0")    
        getiface.bind("<FocusOut>", handle_focus_out)
        getiface.bind("<FocusIn>", handle_focus_in)
        
        getsetacl = Entry(setaclframe, bg='white', width=15, fg='grey')
        getsetacl.grid(column=2, row=13)
        getsetacl.insert(0, "eg. MyACL")
        def handle_focus_in(_):
            if getsetacl.cget('fg') != 'black':
                getsetacl.delete(0, END)
                getsetacl.config(fg='black')
        def handle_focus_out(_):
            if getsetacl.get() == "":
                getsetacl.delete(0, END)
                getsetacl.config(fg='grey')
                getsetacl.insert(0, "eg. MyACL")    
        getsetacl.bind("<FocusOut>", handle_focus_out)
        getsetacl.bind("<FocusIn>", handle_focus_in)


        OPTIONS = [
        "in ",
        "out"
        ]
        getdir = StringVar(setaclframe)
        getdir.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(setaclframe, getdir, *OPTIONS)   
        dropbox.grid(column=3, row=13)    
        def setaclclick():
            if getiface.get() == '' or getiface.get() == 'eg. fa0/0, vty 0':
                tkMessageBox.showinfo('Error', 'Please enter a line or an interface.', parent=window)
            else:
                if 'vty' in getiface.get():
                    interfacetype = "line "
                    accesscmd = "access-class "
                else:
                    interfacetype = "int "
                    accesscmd = "ip access-group "
                remote_conn.send("conf t\n")
                sleep(0.5)
                remote_conn.send(interfacetype + getiface.get() + "\n")
                sleep(0.5)
                if chk_state_neg.get() == False:            
                    remote_conn.send(accesscmd + getsetacl.get() + " " + getdir.get() + "\n")
                    res = "ACL " + getsetacl.get() + " has been applied to " + getiface.get()
                    tkMessageBox.showinfo('ACL', res, parent=window)
                else:
                    remote_conn.send("no " + accesscmd + getsetacl.get() + " " + getdir.get() + "\n")
                    res = "ACL " + getsetacl.get() + " has been removed from " + getiface.get()
                    tkMessageBox.showinfo('ACL', res, parent=window)
                sleep(0.5)
                remote_conn.send("exit \n")
                sleep(0.5)
                remote_conn.send("exit \n")
        btn = Button(setaclframe, text="Aplicar ACL", bg="orange", command=setaclclick)
        btn.grid(column=3, row=15)

        def showaclintconf():
            if getiface.get() == '' or getiface.get() == 'eg. fa0/0, vty 0':
                tkMessageBox.showinfo('Error', 'Please enter a line or an interface.', parent=window)
            else:
                if 'vty' in getiface.get():
                    shcmd = "sh run | i " + getiface.get() + " | access-class \n"
                else:
                    shcmd = "sh ip int " + getiface.get() + " | i access list \n"
                buff_size = 16384
                sleep(0.5)
                remote_conn.send(shcmd)
                sleep(2)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Current ACL configuration', output, parent=window) 
        btn = Button(setaclframe, text="Show applied ACLs", bg="orange", command=showaclintconf)
        btn.grid(column=1, row=15, pady=5)


   




        pfxlistrtemapframe=LabelFrame(window,text=" Create Prefix List / Route-Map ",font=('verdana', 8, 'bold'),padx=10,pady=5,width=100,height=100)
        pfxlistrtemapframe.grid(row=2,column=0, sticky=("nsew"))


        PLRMvar = IntVar()
        PLRMvar.set(1)
        R1 = Radiobutton(pfxlistrtemapframe, text="PfxList", variable=PLRMvar, value=1)
        R1.grid(column=0, row=0)
        R2 = Radiobutton(pfxlistrtemapframe, text="Rte-Map", variable=PLRMvar, value=2)
        R2.grid(column=1, row=0)


        listname = Entry(pfxlistrtemapframe, bg='white', width=15, fg='grey')
        listname.grid(column=0, row=1)
        listname.insert(0, "ListName")
        def handle_focus_in(_):
            if listname.cget('fg') != 'black':
                listname.delete(0, END)
                listname.config(fg='black')
        def handle_focus_out(_):
            if listname.get() == "":
                listname.delete(0, END)
                listname.config(fg='grey')
                listname.insert(0, "ListName")
        listname.bind("<FocusOut>", handle_focus_out)
        listname.bind("<FocusIn>", handle_focus_in)

        listseq = Entry(pfxlistrtemapframe, bg='white', width=7, fg='grey')
        listseq.grid(column=1, row=1)
        listseq.insert(0, "seq no.")
        def handle_focus_in(_):
            if listseq.cget('fg') != 'black':
                listseq.delete(0, END)
                listseq.config(fg='black')
        def handle_focus_out(_):
            if listseq.get() == "":
                listseq.delete(0, END)
                listseq.config(fg='grey')
                listseq.insert(0, "seq no.")
        listseq.bind("<FocusOut>", handle_focus_out)
        listseq.bind("<FocusIn>", handle_focus_in)

        lbl = Label(pfxlistrtemapframe, text="PrefixList: ")    
        lbl.grid(column=0, row=3)
        
        listnetandmask = Entry(pfxlistrtemapframe, bg='white', width=21, fg='grey')
        listnetandmask.grid(column=1, row=3)        
        listnetandmask.insert(0, "eg. 1.1.1.0/24 le 24 ge 30")
        def handle_focus_in(_):
            if listnetandmask.cget('fg') != 'black':
                listnetandmask.delete(0, END)
                listnetandmask.config(fg='black')
        def handle_focus_out(_):
            if listnetandmask.get() == "":
                listnetandmask.delete(0, END)
                listnetandmask.config(fg='grey')
                listnetandmask.insert(0, "eg. 1.1.1.0/24 le 24 ge 30")
        listnetandmask.bind("<FocusOut>", handle_focus_out)
        listnetandmask.bind("<FocusIn>", handle_focus_in)        

        lbl = Label(pfxlistrtemapframe, text="Route-map: ")    
        lbl.grid(column=0, row=4)

        OPTIONS = [
        "Match",
        "Set"
        ]
        rtemapopt = StringVar(window)
        rtemapopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(pfxlistrtemapframe, rtemapopt, *OPTIONS)   
        dropbox.grid(column=1, row=4)

        OPTIONS = [
        "ACL",
        "v6ACL",
        "ACL(nexthop)",
        "v6ACL(nexthop)",
        "interface",
        "tag",
        "local-pref",
        "metric",
        "community",
        "as-path",
        "*weight",        
        "*origin",
        "*dampening",
        "*vrf"
        ]
        rtemapopt2 = StringVar(window)
        rtemapopt2.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(pfxlistrtemapframe, rtemapopt2, *OPTIONS)   
        dropbox.grid(column=2, row=4)

        rtemapval = Entry(pfxlistrtemapframe, width=10)
        rtemapval.grid(column=3, row=4)   

        OPTIONS = [
        "Permit",
        "Deny"
        ]
        permpfxrtedropopt = StringVar(window)
        permpfxrtedropopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(pfxlistrtemapframe, permpfxrtedropopt, *OPTIONS)   
        dropbox.grid(column=3, row=0)

        def setpfxrteconf():
            remote_conn.send("conf t \n")
            sleep(0.5)
            if chk_state_neg.get() == False:
                if PLRMvar == 1:
                    if listname.get() == "" or listname.get() == "eg. MyACL" or listseq.get() == "" or listseq.get() == "seq no.":
                        tkMessageBox.showinfo('ERROR', 'Error - please enter both the list name AND the sequence number.', parent=window)
                    elif (listnetandmask.get() != "" and listnetandmask.get() != "eg. 1.1.1.0/24 le 24 ge 30"):
                        remote_conn.send("ip prefix-l " + listname.get() + " " + listseq.get() + " \n")
                        sleep(1)
                        output = remote_conn.recv(2048).decode("utf-8")
                        if ('Insertion failed' in output):
                            tkMessageBox.showinfo('Error', output, parent=window)
                        else:
                            tkMessageBox.showinfo('Prefix List', 'List created.', parent=window)
                    else:
                        tkMessageBox.showinfo('ERROR', 'Please enter required input values to create a Prefix List.', parent=window)
                else:
                    if listname.get() == "" or listname.get() == "eg. MyACL" or listseq.get() == "" or listseq.get() == "seq no.":
                        tkMessageBox.showinfo('ERROR', 'Error - please enter both the list name AND the sequence number.', parent=window)
                    elif rtemapval.get() == "":
                        remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                        sleep(0.2)
                        tkMessageBox.showinfo('Route-Map', 'Route-Map (+ sequence) created.', parent=window)
                    else:
                        remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                        sleep(0.2)
                        if rtemapopt.get() == "Match":
                            if (rtemapopt2.get() == "*weight" or rtemapopt2.get() == "*origin" or rtemapopt2.get() == "*dampening" or rtemapopt2.get() == "*vrf"):
                                tkMessageBox.showinfo('ERROR', 'These values can ONLY be Set, not Matched: weight, origin, dampening, vrf.', parent=window)
                            elif rtemapopt2.get() == "ACL":
                                remote_conn.send("match ip address " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'ACL match clause created.', parent=window)
                            elif rtemapopt2.get() == "v6ACL":
                                remote_conn.send("match ipv6 address " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'IPv6 ACL match clause created.', parent=window)
                            elif rtemapopt2.get() == "ACL(nexthop)":
                                remote_conn.send("match ip next-hop " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'IP nexthop ACL match clause created.', parent=window)
                            elif rtemapopt2.get() == "v6ACL(nexthop)":
                                remote_conn.send("match ipv6 next-hop " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'IPv6 nexthop ACL match clause created.', parent=window)
                            else:
                                remote_conn.send("match " + rtemapopt2.get() + " " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'Match clause created.', parent=window)
                        else:
                            if rtemapopt2.get() == "ACL":
                                remote_conn.send("set ip address " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'ACL set clause created.', parent=window)
                            elif rtemapopt2.get() == "v6ACL":
                                remote_conn.send("set ipv6 address " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'IPv6 ACL set clause created.', parent=window)
                            elif rtemapopt2.get() == "ACL(nexthop)":
                                remote_conn.send("set ip next-hop " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'IP nexthop ACL set clause created.', parent=window)
                            elif rtemapopt2.get() == "v6ACL(nexthop)":
                                remote_conn.send("set ipv6 next-hop " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'IPv6 nexthop ACL set clause created.', parent=window)
                            elif rtemapopt2.get() == "*weight" or rtemapopt2.get() == "*origin" or rtemapopt2.get() == "*dampening" or rtemapopt2.get() == "*vrf":
                                rtemapoptnew = str(rtemapopt2.get())[1:]
                                remote_conn.send("set " + rtemapoptnew + " " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', rtemapoptnew + ' set clause created.', parent=window)
                            else:
                                remote_conn.send("set " + rtemapopt2.get() + " " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', rtemapopt2.get() + ' set clause created.', parent=window)
            else:
                if PLRMvar == 1:
                    if listname.get() == "" or listname.get() == "eg. MyACL":
                        tkMessageBox.showinfo('ERROR', 'Error - please enter both the list name.', parent=window)
                    elif (listseq.get() == "" or listseq.get() == "seq no.") and (listnetandmask.get() == "" or listnetandmask.get()\
                            == "eg. 1.1.1.0/24 le 24 ge 30"):
                        remote_conn.send("no ip prefix-l " + listname.get() + " \n")
                        sleep(0.2)
                        tkMessageBox.showinfo('Prefix List', 'Prefix List removed.', parent=window)
                    elif (listseq.get() != "" or listseq.get() != "seq no.") and (listnetandmask.get() != "" or listnetandmask.get()\
                            != "eg. 1.1.1.0/24 le 24 ge 30"):
                        remote_conn.send("no ip prefix-l " + listname.get() + " seq " + listseq.get() + " " + permpfxrtedropopt.get() + " " + \
                                         listnetandmask.get() + " \n")
                        sleep(0.2)
                        tkMessageBox.showinfo('Prefix List', 'Prefix List sequence removed.', parent=window)
                    else:
                        tkMessageBox.showinfo('ERROR', 'Please enter required input values to remove a Prefix List or a sequence within a Prefix List.', parent=window)
                else:
                    if listname.get() == "" or listname.get() == "eg. MyACL":
                        tkMessageBox.showinfo('ERROR', 'Error - please enter both the list name.', parent=window)
                    elif (listseq.get() == "" or listseq.get() == "seq no.") and rtemapval.get() == "":
                        remote_conn.send("no route-m " + listname.get() + " \n")
                        sleep(0.2)
                        tkMessageBox.showinfo('Route-Map', 'Route-Map removed.', parent=window)
                    elif (listseq.get() != "" or listseq.get() != "seq no.") and rtemapval.get() == "":
                        remote_conn.send("no route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                        sleep(0.2)
                        tkMessageBox.showinfo('Route-Map', 'Route-Map sequence removed.', parent=window)
                    elif (listseq.get() != "" or listseq.get() != "seq no.") and rtemapval.get() != "":
                        if rtemapopt.get() == "Match":
                            if (rtemapopt2.get() == "*weight" or rtemapopt2.get() == "*origin" or rtemapopt2.get() == "*dampening" or rtemapopt2.get() == "*vrf"):
                                tkMessageBox.showinfo('ERROR', 'These values can ONLY be Set, not Matched: weight, origin, dampening, vrf.', parent=window)
                            elif rtemapopt2.get() == "ACL":
                                remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                                sleep(0.2)
                                remote_conn.send("no match ip address " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'ACL match clause removed.', parent=window)
                            elif rtemapopt2.get() == "v6ACL":
                                remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                                sleep(0.2)
                                remote_conn.send("no match ipv6 address " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'IPv6 ACL match clause removed.', parent=window)
                            elif rtemapopt2.get() == "ACL(nexthop)":
                                remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                                sleep(0.2)
                                remote_conn.send("no match ip next-hop " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'ACL nexthop match clause removed.', parent=window)
                            elif rtemapopt2.get() == "v6ACL(nexthop)":
                                remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                                sleep(0.2)
                                remote_conn.send("no match ipv6 next-hop " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'IPv6 ACL nexthop match clause removed.', parent=window)
                            else:
                                remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                                sleep(0.2)
                                remote_conn.send("no match " + rtemapopt2.get() + " " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', rtemapopt2.get() + ' match clause removed.', parent=window)
                        else:
                            if rtemapopt2.get() == "ACL":
                                remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                                sleep(0.2)
                                remote_conn.send("no set ip address " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'ACL set clause removed.', parent=window)
                            elif rtemapopt2.get() == "v6ACL":
                                remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                                sleep(0.2)
                                remote_conn.send("no set ipv6 address " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'IPv6 ACL set clause removed.', parent=window)
                            elif rtemapopt2.get() == "ACL(nexthop)":
                                remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                                sleep(0.2)
                                remote_conn.send("no set ip next-hop " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'ACL nexthop set clause removed.', parent=window)
                            elif rtemapopt2.get() == "v6ACL(nexthop)":
                                remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                                sleep(0.2)
                                remote_conn.send("no set ipv6 next-hop " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', 'IPv6 ACL nexthop set clause removed.', parent=window)
                            elif rtemapopt2.get() == "*weight" or rtemapopt2.get() == "*origin" or rtemapopt2.get() == "*dampening" or rtemapopt2.get() == "*vrf":
                                rtemapoptnew = str(rtemapopt2.get())[1:]
                                remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                                sleep(0.2)
                                remote_conn.send("no set " + rtemapoptnew + " " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', rtemapoptnew + ' set clause removed.', parent=window)
                            else:
                                remote_conn.send("route-m " + listname.get() + " " + permpfxrtedropopt.get() + " " + listseq.get() + " \n")
                                sleep(0.2)
                                remote_conn.send("no set " + rtemapopt2.get() + " " + rtemapval.get() + " \n")
                                sleep(0.2)
                                tkMessageBox.showinfo('Route-Map', rtemapopt2.get() + ' set clause removed.', parent=window)
                    else:
                        tkMessageBox.showinfo('ERROR', 'Please enter required input values to remove a Route-Map, a sequence within a Route-map or \
a match/set clause within a Route-Map sequence.', parent=window)
            sleep(0.2)
            remote_conn.send("exit \n")
            sleep(0.2)
            remote_conn.send("exit \n")
        btn = Button(pfxlistrtemapframe, text="Aplicar", bg="orange", command=setpfxrteconf)
        btn.grid(column=2, row=0)







        
        speciallistframe=LabelFrame(window,text=" Create Other List ",font=('verdana', 8, 'bold'),padx=10,pady=5,width=100,height=100)
        speciallistframe.grid(row=3,column=0, sticky=("nsew"))

        OPTIONS = [
        "AS-Path ACL",
        "Community-List"
        ]
        speciallistopt = StringVar(window)
        speciallistopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(speciallistframe, speciallistopt, *OPTIONS)   
        dropbox.grid(column=0, row=0)

        speciallistnum = Entry(speciallistframe, bg='white', width=8, fg='grey')
        speciallistnum.grid(column=1, row=0)
        speciallistnum.insert(0, "ListNo.")
        def handle_focus_in(_):
            if speciallistnum.cget('fg') != 'black':
                speciallistnum.delete(0, END)
                speciallistnum.config(fg='black')
        def handle_focus_out(_):
            if speciallistnum.get() == "":
                speciallistnum.delete(0, END)
                speciallistnum.config(fg='grey')
                speciallistnum.insert(0, "ListNo.")
        speciallistnum.bind("<FocusOut>", handle_focus_out)
        speciallistnum.bind("<FocusIn>", handle_focus_in)

        speciallistval = Entry(speciallistframe, bg='white', width=40, fg='grey')
        speciallistval.grid(column=0, row=1, columnspan=2)
        speciallistval.insert(0, "Regex for AS-ACL, <eg. 10:20> for comm list")
        def handle_focus_in(_):
            if speciallistval.cget('fg') != 'black':
                speciallistval.delete(0, END)
                speciallistval.config(fg='black')
        def handle_focus_out(_):
            if speciallistval.get() == "":
                speciallistval.delete(0, END)
                speciallistval.config(fg='grey')
                speciallistval.insert(0, "Regex for AS-ACL, <eg. 10:20> for comm list")
        speciallistval.bind("<FocusOut>", handle_focus_out)
        speciallistval.bind("<FocusIn>", handle_focus_in)

        OPTIONS = [
        "Allow",
        "Block"
        ]
        speciallistdropopt = StringVar(window)
        speciallistdropopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(speciallistframe, speciallistdropopt, *OPTIONS)   
        dropbox.grid(column=4, row=0)

        def setspeciallistconf():
            if speciallistnum.get() == "" or speciallistnum.get() == "ListNo." or speciallistval.get() == "" or \
               speciallistval.get() == "Regex for AS-ACL, <10:20> for comm list":
                tkMessageBox.showinfo('ERROR', 'Error - please enter both the list number AND the value.', parent=window)
            elif shpfxrtedropopt == "AS-Path ACL":
                remote_conn.send("ip as-path access-l " + speciallistnum.get() + " " + speciallistdropopt.get() + " " + speciallistval.get() + " \n")
                sleep(0.5)
                tkMessageBox.showinfo('AS-Path ACL', 'List created.', parent=window)
            else:
                remote_conn.send("ip community-l " + speciallistnum.get() + " " + speciallistdropopt.get() + " " + speciallistval.get() + " \n")
                sleep(0.5)
                tkMessageBox.showinfo('Community List', 'List created.', parent=window)
        btn = Button(speciallistframe, text="Aplicar", bg="orange", command=setspeciallistconf)
        btn.grid(column=3, row=0)        








        showaclframe=LabelFrame(window,text=" Show Lists ",font=('verdana', 8, 'bold'),padx=20,pady=5,width=100,height=100)
        showaclframe.grid(row=4,column=0, sticky=("nsew"))

        OPTIONS = [
        "ACLs",
        "Prefix Lists",
        "Route-Maps",
        "AS-Path ACLs",
        "Community-Lists"
        ]
        shacldropopt = StringVar(window)
        shacldropopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(showaclframe, shacldropopt, *OPTIONS)   
        dropbox.grid(column=0, row=1)
        getaclshow = Entry(showaclframe, bg='white', width=15, fg='grey')
        getaclshow.grid(column=1, row=1)
        getaclshow.insert(0, "eg. MyACL, 5")
        def handle_focus_in(_):
            if getaclshow.cget('fg') != 'black':
                getaclshow.delete(0, END)
                getaclshow.config(fg='black')
        def handle_focus_out(_):
            if getaclshow.get() == "":
                getaclshow.delete(0, END)
                getaclshow.config(fg='grey')
                getaclshow.insert(0, "eg. MyACL, 5")    
        getaclshow.bind("<FocusOut>", handle_focus_out)
        getaclshow.bind("<FocusIn>", handle_focus_in)
        
        def showaclconf():
            if shacldropopt == "ACLs":            
                cmd = "sh ip access-l "
            elif shacldropopt == "Prefix Lists":
                cmd = "sh ip prefix-l "
            elif shacldropopt == "Route-Maps":
                cmd = "sh route-m "
            elif shacldropopt == "AS-Path ACLs":
                cmd = "sh ip as-path-acc "
            else:
                cmd = "sh ip community-l "

            if getaclshow.get() != "" or getaclshow.get() != "eg. MyACL, 5":
                cmd = cmd + getaclshow.get()
            else:
                pass
            buff_size = 16384
            sleep(0.5)
            remote_conn.send(cmd + " \n")
            sleep(0.5)
            while not remote_conn.recv_ready():
                remote_conn.recv(0)
                buff_size += 4096
                sleep(0.5)
            output = remote_conn.recv(buff_size).decode("utf-8")
            tkMessageBox.showinfo('Existing List', output, parent=window)
        btn = Button(showaclframe, text="Show List", bg="orange", command=showaclconf)
        btn.grid(column=2, row=1, pady=5)


        aclhelpframe=LabelFrame(window,text=" Help ",font=('verdana', 8, 'bold'),padx=10,pady=2,width=100,height=100)
        aclhelpframe.grid(row=3,column=1, rowspan=2, sticky=("nsew"))
        def aclhelp():
            res = "MAC ACLs don't work against IPv4 or IPv6 traffic directly. It actually is used to block the ARP reply/response (only within a VLAN)" +\
            " else use VACLs instead. \n\n" + "ACL logging behavior: After a period of inactivity longer than 5 mins, the first packet to match ACE will" +\
            " trigger a syslog message. All other messages after this will be triggered in a summary syslog message after another 5 mins. The command " +\
            "(ip access-list log-update threshold <n>) is used to generate a syslog message when <n> packets logged without waiting for the 5 min interval"\
            + "\n\n Regex for AS Path ACLS\n ^ = Beginning of string\n _ = Any whitespace\n ( ),[ ] = group items\n * = 0 or more of previous obj\n"\
            + "+ = 1 or more of previous obj\n . = matches any single char (eg 0.0 matches 020,030) \n ? = match any occurence of pattern (eg ba?b matches bb, bab)"\
            "\n$ = match last character of previous obj\n EXAMPLES:\n .* == anything, ^$ == local originated routes, ^100_ == learned from AS100, "\
            + "_100$ == originated in AS100, _100_  == any instance from AS100, ^[0-9]+$ == directly connected AS"
            tkMessageBox.showinfo('ACL Help', res, parent=window)
        btn = Button(aclhelpframe, text="ACL", bg="yellow", command=aclhelp)
        btn.grid(row=1,column=1)

        def pfxlisthelp():
            res = "\
TO ADD: \n\
  - MUST input <ListName> + <Seq number> + <Network+Mask[ge le]> \n \
  - make sure Mask < ge value <= le value \n\n \
TO NEGATE: \n\
  - if input <ListName> + <Seq number> == Deletes specific sequence of PrefixList \n \
  - if input <ListName> == Deletes PrefixList"
            tkMessageBox.showinfo('Prefix List Help', res, parent=window)
        btn = Button(aclhelpframe, text="PfxList", bg="yellow", command=pfxlisthelp)
        btn.grid(row=2,column=1)

        def rtemaphelp():
            res = "MATCH clause cannot be set with * attributes (eg. *weight)\n\n\
TO ADD: \n\
  - MUST minimally input <ListName> + <Seq number> \n \
TO NEGATE: \n\
  - if input <ListName> + <Seq number> + <Match/Set clause> == Deletes specific Match/Set clause \n \
  - if input <ListName> + <Seq number> == Deletes specific sequence of Route-Map \n \
  - if input <ListName> == Deletes Route-Map "

            tkMessageBox.showinfo('Route Map Help', res, parent=window)
        btn = Button(aclhelpframe, text="Rte-Map", bg="yellow", command=rtemaphelp)
        btn.grid(row=3,column=1)


    def NAT():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("NAT Control")
        window.geometry('520x300')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)
        

        negframe=LabelFrame(window,text=" Negate ",font=('verdana', 8, 'bold'),padx=5,pady=5,width=100,height=100)
        negframe.grid(row=0,column=1)
        
        chk_state_neg = BooleanVar()
        chk_state_neg.set(False)
        chk = Checkbutton(negframe, variable=chk_state_neg)
        chk.grid(column=0, row=0)




    

        natframe=LabelFrame(window,text=" NAT ",font=('verdana', 8, 'bold'),padx=5,pady=5,width=100,height=100)
        natframe.grid(row=0,column=0, sticky=("nsew"))

        chk_state_overload = BooleanVar()
        chk_state_overload.set(False)
        chk = Checkbutton(natframe, text='Overload', variable=chk_state_overload)
        chk.grid(column=0, row=3)


        lbl = Label(natframe, text="ACL for NAT source:")
        lbl.grid(column=0, row=1)
        getacl = Entry(natframe,width=15)
        getacl.grid(column=1, row=1)
        lbl = Label(natframe, text="Interface to NAT toward:")
        lbl.grid(column=0, row=2)        
        getinterface = Entry(natframe,width=15)
        getinterface.grid(column=1, row=2)
        
        def natclicked():
            if chk_state_neg.get() == True:                
                remote_conn.send("conf t\n")
                sleep(0.5)
                remote_conn.send("no ip nat inside source list " + getacl.get() + " interface " + getinterface.get() + "\n")
                sleep(0.5)
                remote_conn.send("exit \n")
                res = "NAT removed."
                tkMessageBox.showinfo('NAT', res, parent=window)
            else:
                if chk_state_overload.get() == True:
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("ip nat inside source list " + getacl.get() + " interface " + getinterface.get() + " overload " + "\n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "NAT added. Ensure ACL " + getacl.get() + " is created or will not work."
                    tkMessageBox.showinfo('NAT', res, parent=window)
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("ip nat inside source list " + getacl.get() + " interface " + getinterface.get() + "\n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "NAT added. Ensure ACL " + getacl.get() + " is created or will not work."
                    tkMessageBox.showinfo('NAT', res, parent=window)                    
        btn = Button(natframe, text="Aplicar", bg="orange", command=natclicked)
        btn.grid(column=1, row=3)


        portfwdframe=LabelFrame(window,text=" Port Forward ",font=('verdana', 8, 'bold'),padx=5,pady=5,width=100,height=100)
        portfwdframe.grid(row=1,column=0, sticky=("nsew"))
        
        chk_state_extendable = BooleanVar()
        chk_state_extendable.set(False)
        chk = Checkbutton(portfwdframe, text='Extendable', variable=chk_state_extendable)
        chk.grid(column=0, row=8)
        
        lbl = Label(portfwdframe, text="(leave proto and port(s) empty for 1-TO-1 map)")    
        lbl.grid(column=0, row=4)
        lbl = Label(portfwdframe, text="Enter protocol for Portforward:")    
        lbl.grid(column=0, row=5)
        getproto = Entry(portfwdframe, bg='white', width=15, fg='grey')
        getproto.grid(column=1, row=5)
        getproto.insert(0, "eg. tcp, udp")
        def handle_focus_in(_):
            if getproto.cget('fg') != 'black':
                getproto.delete(0, END)
                getproto.config(fg='black')
        def handle_focus_out(_):
            if getproto.get() == "":
                getproto.delete(0, END)
                getproto.config(fg='grey')
                getproto.insert(0, "eg. tcp, udp")
        getproto.bind("<FocusOut>", handle_focus_out)
        getproto.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(portfwdframe, text="Enter Local IP & port to Portforward:")    
        lbl.grid(column=0, row=6)
        getlocip = Entry(portfwdframe, bg='white', width=15, fg='grey')
        getlocip.grid(column=1, row=6)
        getlocip.insert(0, "eg. 192.168.1.1")
        def handle_focus_in(_):
            if getlocip.cget('fg') != 'black':
                getlocip.delete(0, END)
                getlocip.config(fg='black')
        def handle_focus_out(_):
            if getlocip.get() == "":
                getlocip.delete(0, END)
                getlocip.config(fg='grey')
                getlocip.insert(0, "eg. 192.168.1.1")
        getlocip.bind("<FocusOut>", handle_focus_out)
        getlocip.bind("<FocusIn>", handle_focus_in)
        
        getlocport = Entry(portfwdframe, bg='white', width=8, fg='grey')
        getlocport.grid(column=2, row=6)
        getlocport.insert(0, "eg. 5000")
        def handle_focus_in(_):
            if getlocport.cget('fg') != 'black':
                getlocport.delete(0, END)
                getlocport.config(fg='black')
        def handle_focus_out(_):
            if getlocport.get() == "":
                getlocport.delete(0, END)
                getlocport.config(fg='grey')
                getlocport.insert(0, "eg. 5000")
        getlocport.bind("<FocusOut>", handle_focus_out)
        getlocport.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(portfwdframe, text="Enter Global IP & port to Portforward:")    
        lbl.grid(column=0, row=7)
        getgloip = Entry(portfwdframe, bg='white', width=15, fg='grey')
        getgloip.grid(column=1, row=7)
        getgloip.insert(0, "eg. 100.1.1.1")
        def handle_focus_in(_):
            if getgloip.cget('fg') != 'black':
                getgloip.delete(0, END)
                getgloip.config(fg='black')
        def handle_focus_out(_):
            if getgloip.get() == "":
                getgloip.delete(0, END)
                getgloip.config(fg='grey')
                getgloip.insert(0, "eg. 100.1.1.1")
        getgloip.bind("<FocusOut>", handle_focus_out)
        getgloip.bind("<FocusIn>", handle_focus_in)
        
        getgloport = Entry(portfwdframe, bg='white', width=8, fg='grey')
        getgloport.grid(column=2, row=7)        
        getgloport.insert(0, "eg. 80")
        def handle_focus_in(_):
            if getgloport.cget('fg') != 'black':
                getgloport.delete(0, END)
                getgloport.config(fg='black')
        def handle_focus_out(_):
            if getgloport.get() == "":
                getgloport.delete(0, END)
                getgloport.config(fg='grey')
                getgloport.insert(0, "eg. 80")
        getgloport.bind("<FocusOut>", handle_focus_out)
        getgloport.bind("<FocusIn>", handle_focus_in)
        
        def portforwardclicked():
            if chk_state_neg.get() == True:                
                remote_conn.send("conf t\n")
                sleep(0.5)
                remote_conn.send("no ip nat inside source static " + getproto.get() + " " + getlocip.get() + " " + getlocport.get() + " " + getgloip.get()
                                           + " " + getgloport.get() + "\n")
                sleep(0.5)
                remote_conn.send("exit \n")
                res = "Portforward removed."
                tkMessageBox.showinfo('NAT', res, parent=window)
            else:
                if chk_state_extendable.get() == True:
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("ip nat inside source static " + getproto.get() + " " + getlocip.get() + " " + getlocport.get() + " " + getgloip.get()
                                           + " " + getgloport.get() + " extendable" + "\n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "Portforward added. Extendable."
                    tkMessageBox.showinfo('NAT', res, parent=window)
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.5)
                    remote_conn.send("ip nat inside source static " + getproto.get() + " " + getlocip.get() + " " + getlocport.get() + " " + getgloip.get()
                                           + " " + getgloport.get() + "\n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    res = "Portforward added."
                    tkMessageBox.showinfo('NAT', res, parent=window)
                
        btn = Button(portfwdframe, text="Aplicar", bg="orange", command=portforwardclicked)
        btn.grid(column=1, row=8)

        shnatframe=LabelFrame(window,text=" Show Config ",font=('verdana', 8, 'bold'),padx=5,pady=5,width=100,height=100)
        shnatframe.grid(row=2,column=0, sticky=("nsew"))
        
        def shownatconf():
            buff_size = 65535
            sleep(0.5)
            remote_conn.send("show ip nat trans \n")
            sleep(2)
            while not remote_conn.recv_ready():
                remote_conn.recv(0)
                buff_size += 2048
                sleep(0.5)
            output = remote_conn.recv(buff_size).decode("utf-8")
            tkMessageBox.showinfo('NAT translations', output, parent=window)          
        btn = Button(shnatframe, text="Show NAT xlation", bg="orange", command=shownatconf)
        btn.grid(column=0, row=9)


        def clearnat():
            sleep(0.5)
            remote_conn.send("clear ip nat trans * \n")
            sleep(0.5)
            tkMessageBox.showinfo('NAT', 'All NAT translations has been cleared. All TCP connections will drop.', parent=window)
        btn = Button(shnatframe, text="Clear NAT xlation", bg="orange", command=clearnat)
        btn.grid(column=2, row=9, pady=4, padx=15)




    def monitoring():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("Network Monitoring and Logging")
        window.geometry('485x730')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)


        negframe=LabelFrame(window,text=" Negate ",font=('verdana', 8, 'bold'),padx=5,pady=5,width=100,height=100)
        negframe.grid(row=0,column=1)
        
        chk_state_neg = BooleanVar()
        chk_state_neg.set(False)
        chk = Checkbutton(negframe, variable=chk_state_neg)
        chk.grid(column=0, row=0)


        CDPLLDPframe=LabelFrame(window,text=" L2 Device monitoring (Negate only used for Optionals) ",font=('verdana', 8, 'bold'),padx=10,pady=5,width=100,height=100)
        CDPLLDPframe.grid(row=0,column=0, sticky=("nsew"))

        lbl = Label(CDPLLDPframe, text="CDP:").grid(column=0, row=0)
        OPTIONS = [
        "Choose",
        "Enable",
        "Disable"
        ]
        cdpopt = StringVar(CDPLLDPframe)
        cdpopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(CDPLLDPframe, cdpopt, *OPTIONS)   
        dropbox.grid(column=1, row=0, padx=3)
        getcdpiface = Entry(CDPLLDPframe, bg='white', width=15, fg='grey')
        getcdpiface.grid(column=2, row=0)
        getcdpiface.insert(0, "eg. fa0/0")
        def handle_focus_in(_):
            if getcdpiface.cget('fg') != 'black':
                getcdpiface.delete(0, END)
                getcdpiface.config(fg='black')
        def handle_focus_out(_):
            if getcdpiface.get() == "":
                getcdpiface.delete(0, END)
                getcdpiface.config(fg='grey')
                getcdpiface.insert(0, "eg. fa0/0")    
        getcdpiface.bind("<FocusOut>", handle_focus_out)
        getcdpiface.bind("<FocusIn>", handle_focus_in)



        lbl = Label(CDPLLDPframe, text="LLDP:").grid(column=0, row=2)
        OPTIONS = [
        "Choose",
        "Enable",
        "Disable"
        ]
        lldpopt = StringVar(CDPLLDPframe)
        lldpopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(CDPLLDPframe, lldpopt, *OPTIONS)   
        dropbox.grid(column=1, row=2, padx=3)        
        getlldpiface = Entry(CDPLLDPframe, bg='white', width=15, fg='grey')
        getlldpiface.grid(column=2, row=2)
        getlldpiface.insert(0, "eg. fa0/0")
        def handle_focus_in(_):
            if getlldpiface.cget('fg') != 'black':
                getlldpiface.delete(0, END)
                getlldpiface.config(fg='black')
        def handle_focus_out(_):
            if getlldpiface.get() == "":
                getlldpiface.delete(0, END)
                getlldpiface.config(fg='grey')
                getlldpiface.insert(0, "eg. fa0/0")    
        getlldpiface.bind("<FocusOut>", handle_focus_out)
        getlldpiface.bind("<FocusIn>", handle_focus_in)

        LLDPvar = IntVar()
        LLDPvar.set(1)
        R1 = Radiobutton(CDPLLDPframe, text="Both", variable=LLDPvar, value=1)
        R1.grid(column=3, row=2)
        R2 = Radiobutton(CDPLLDPframe, text="Xmit", variable=LLDPvar, value=2)
        R2.grid(column=4, row=2)
        R3 = Radiobutton(CDPLLDPframe, text="Rcv", variable=LLDPvar, value=3)
        R3.grid(column=5, row=2)




        OPTIONS = [
        "Optional",
        "CDP hello",
        "CDP hold",
        "LLDP hello",
        "LLDP hold"
        ]
        othercdplldpopt = StringVar(CDPLLDPframe)
        othercdplldpopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(CDPLLDPframe, othercdplldpopt, *OPTIONS)   
        dropbox.grid(column=1, row=3, padx=3)
        getcdplldpother = Entry(CDPLLDPframe, bg='white', width=15, fg='grey')
        getcdplldpother.grid(column=2, row=3)
        getcdplldpother.insert(0, "eg. 5")
        def handle_focus_in(_):
            if getcdplldpother.cget('fg') != 'black':
                getcdplldpother.delete(0, END)
                getcdplldpother.config(fg='black')
        def handle_focus_out(_):
            if getcdplldpother.get() == "":
                getcdplldpother.delete(0, END)
                getcdplldpother.config(fg='grey')
                getcdplldpother.insert(0, "eg. 5")    
        getcdplldpother.bind("<FocusOut>", handle_focus_out)
        getcdplldpother.bind("<FocusIn>", handle_focus_in)


        
        def cdplldp():
            if cdpopt.get() == "Choose":
                pass
            elif cdpopt.get() == "Enable":
                if (getcdpiface.get() != "" and getcdpiface.get() != "eg. fa0/0"):
                    remote_conn.send("conf t \n")
                    sleep(0.5)
                    remote_conn.send("cdp run \n")
                    sleep(0.5)                    
                    remote_conn.send("int " + getcdpiface.get() + " \n")
                    sleep(0.5)
                    remote_conn.send("cdp enable \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('L2 Device monitoring', 'CDP monitoring enabled', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.5)
                    remote_conn.send("cdp run \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('L2 Device monitoring', 'CDP monitoring enabled globally', parent=window)
            else:
                if (getcdpiface.get() != "" and getcdpiface.get() != "eg. fa0/0"):
                    remote_conn.send("conf t \n")
                    sleep(0.5)
                    remote_conn.send("int " + getcdpiface.get() + " \n")
                    sleep(0.5)
                    remote_conn.send("no cdp enable \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")                    
                    tkMessageBox.showinfo('L2 Device monitoring', 'CDP monitoring disabled', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.5)
                    remote_conn.send("no cdp run \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")                    
                    tkMessageBox.showinfo('L2 Device monitoring', 'CDP monitoring disabled globally', parent=window)

            
            if lldpopt.get() == "Choose":
                pass
            elif lldpopt.get() == "Enable":
                if (getlldpiface.get() != "" and getlldpiface.get() != "eg. fa0/0"):
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("lldp run \n")
                    sleep(0.3)                    
                    remote_conn.send("int " + getlldpiface.get() + " \n")
                    sleep(0.3)
                    if LLDPvar.get() == 1:
                        remote_conn.send("lldp receive \n")
                        sleep(0.3)
                        remote_conn.send("lldp transmit \n")
                        sleep(0.3)                                           
                        tkMessageBox.showinfo('L2 Device monitoring', 'LLDP monitoring enabled to transmit and receive.', parent=window)
                    elif LLDPvar.get() == 2:
                        remote_conn.send("lldp transmit \n")
                        sleep(0.3)                                          
                        tkMessageBox.showinfo('L2 Device monitoring', 'LLDP monitoring enabled to transmit only.', parent=window)
                    else:
                        remote_conn.send("lldp receive \n")
                        sleep(0.3)                                         
                        tkMessageBox.showinfo('L2 Device monitoring', 'LLDP monitoring enabled to receive only.', parent=window)
                    remote_conn.send("exit \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.5)
                    remote_conn.send("lldp run \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")                    
                    tkMessageBox.showinfo('L2 Device monitoring', 'LLDP monitoring enabled globally', parent=window)
                    
            else:
                if (getlldpiface.get() != "" and getlldpiface.get() != "eg. fa0/0"):
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("int " + getlldpiface.get() + " \n")
                    sleep(0.3)
                    if LLDPvar.get() == 1:
                        remote_conn.send("no lldp receive \n")
                        sleep(0.3)
                        remote_conn.send("no lldp transmit \n")
                        sleep(0.3)                                           
                        tkMessageBox.showinfo('L2 Device monitoring', 'LLDP monitoring - transmit and receive disabled.', parent=window)
                    elif LLDPvar.get() == 2:
                        remote_conn.send("no lldp transmit \n")
                        sleep(0.3)                                          
                        tkMessageBox.showinfo('L2 Device monitoring', 'LLDP monitoring - transmit disabled.', parent=window)
                    else:
                        remote_conn.send("no lldp receive \n")
                        sleep(0.3)                                         
                        tkMessageBox.showinfo('L2 Device monitoring', 'LLDP monitoring - receive disabled.', parent=window)
                    remote_conn.send("exit \n")
                    sleep(0.3)
                    remote_conn.send("exit \n") 
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.5)
                    remote_conn.send("no lldp run \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")                    
                    tkMessageBox.showinfo('L2 Device monitoring', 'LLDP monitoring disabled globally', parent=window)

            if othercdplldpopt.get() == "Optional":
                pass
            elif (getcdplldpother.get() == "" and getcdplldpother.get() == "eg. 5"):
                tkMessageBox.showinfo('Error', 'Please enter a value.', parent=window)
            else:
                if chk_state_neg.get() == False:
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    if othercdplldpopt.get() == "CDP hello":
                        remote_conn.send("cdp timer " + getcdplldpother.get() + " \n")
                        sleep(0.3)                                           
                        tkMessageBox.showinfo('L2 Device monitoring', 'CDP hello timer modified.', parent=window)
                    elif othercdplldpopt.get() == "CDP hold":
                        remote_conn.send("cdp hold " + getcdplldpother.get() + " \n")
                        sleep(0.3)                                          
                        tkMessageBox.showinfo('L2 Device monitoring', 'CDP hold timer modified.', parent=window)
                    elif othercdplldpopt.get() == "LLDP hello":
                        remote_conn.send("lldp timer " + getcdplldpother.get() + " \n")
                        sleep(0.3)                                         
                        tkMessageBox.showinfo('L2 Device monitoring', 'LLDP hello timer modified.', parent=window)
                    else:
                        remote_conn.send("lldp hold " + getcdplldpother.get() + " \n")
                        sleep(0.3)                                         
                        tkMessageBox.showinfo('L2 Device monitoring', 'LLDP hold timer modified.', parent=window)
                    remote_conn.send("exit \n")                        
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    if othercdplldpopt.get() == "CDP hello":
                        remote_conn.send("no cdp timer \n")
                        sleep(0.3)                                           
                        tkMessageBox.showinfo('L2 Device monitoring', 'CDP hello timer reset.', parent=window)
                    elif othercdplldpopt.get() == "CDP hold":
                        remote_conn.send("no cdp hold \n")
                        sleep(0.3)                                          
                        tkMessageBox.showinfo('L2 Device monitoring', 'CDP hold timer reset.', parent=window)
                    elif othercdplldpopt.get() == "LLDP hello":
                        remote_conn.send("no lldp timer \n")
                        sleep(0.3)                                         
                        tkMessageBox.showinfo('L2 Device monitoring', 'LLDP hello timer reset.', parent=window)
                    else:
                        remote_conn.send("no lldp hold \n")
                        sleep(0.3)                                         
                        tkMessageBox.showinfo('L2 Device monitoring', 'LLDP hold timer reset.', parent=window)
                    remote_conn.send("exit \n")                     
 
        btn = Button(CDPLLDPframe, text="Aplicar", bg="orange", command=cdplldp)
        btn.grid(column=5, row=0, rowspan=2)


        def CDPLLDPHelp():
            res = ""
            tkMessageBox.showinfo('CDP & LLDP Help', res, parent=window)
        btn = Button(CDPLLDPframe, text="Help", bg="yellow", command=CDPLLDPHelp)
        btn.grid(row=3,column=5)
        

            
        UDLDframe=LabelFrame(window,text=" L1/2 Link monitoring (Negate only used for Optionals) ",font=('verdana', 8, 'bold'),padx=10,pady=5,width=100,height=100)
        UDLDframe.grid(row=1,column=0, sticky=("nsew"))

        lbl = Label(UDLDframe, text="UDLD:").grid(column=0, row=0)
        OPTIONS = [
        "Choose",
        "Enable",
        "Disable"
        ]
        UDLDopt = StringVar(UDLDframe)
        UDLDopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(UDLDframe, UDLDopt, *OPTIONS)   
        dropbox.grid(column=1, row=0, padx=3)
        getudldiface = Entry(UDLDframe, bg='white', width=15, fg='grey')
        getudldiface.grid(column=2, row=0)
        getudldiface.insert(0, "eg. fa0/0")
        def handle_focus_in(_):
            if getudldiface.cget('fg') != 'black':
                getudldiface.delete(0, END)
                getudldiface.config(fg='black')
        def handle_focus_out(_):
            if getudldiface.get() == "":
                getudldiface.delete(0, END)
                getudldiface.config(fg='grey')
                getudldiface.insert(0, "eg. fa0/0")    
        getudldiface.bind("<FocusOut>", handle_focus_out)
        getudldiface.bind("<FocusIn>", handle_focus_in)

        chk_udld_aggr = BooleanVar()
        chk_udld_aggr.set(False)
        chk = Checkbutton(UDLDframe, text="Aggressive", variable=chk_udld_aggr)
        chk.grid(column=3, row=0)


        

        def option_changed_otherudldpopt(*args):
            if otherudldpopt.get() == "Hello":
                text = 'eg. 5'
                getudldother.delete(0, END)
                getudldother.config(fg='grey')
                getudldother.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if getudldother.cget('fg') != 'black':
                        getudldother.delete(0, END)
                        getudldother.config(fg='black')
                def handle_focus_out(_):
                    if getudldother.get() == "":
                        getudldother.delete(0, END)
                        getudldother.config(fg='grey')
                        getudldother.insert(0, text)
                getudldother.bind("<FocusOut>", handle_focus_out)
                getudldother.bind("<FocusIn>", handle_focus_in)
            elif otherudldpopt.get() == "Auto-recovery" or otherudldpopt.get() == "Recover all":
                text = 'No input required'
                getudldother.delete(0, END)
                getudldother.config(fg='grey')
                getudldother.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if getudldother.cget('fg') != 'black':
                        getudldother.delete(0, END)
                        getudldother.config(fg='black')
                def handle_focus_out(_):
                    if getudldother.get() == "":
                        getudldother.delete(0, END)
                        getudldother.config(fg='grey')
                        getudldother.insert(0, text)
                getudldother.bind("<FocusOut>", handle_focus_out)
                getudldother.bind("<FocusIn>", handle_focus_in)
            else:
                text = ''
                getudldother.delete(0, END)
                getudldother.config(fg='grey')
                getudldother.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if getudldother.cget('fg') != 'black':
                        getudldother.delete(0, END)
                        getudldother.config(fg='black')
                def handle_focus_out(_):
                    if getudldother.get() == "":
                        getudldother.delete(0, END)
                        getudldother.config(fg='grey')
                        getudldother.insert(0, text)
                getudldother.bind("<FocusOut>", handle_focus_out)
                getudldother.bind("<FocusIn>", handle_focus_in)   


        OPTIONS = [
        "Optional",
        "Hello",
        "Auto-recovery",
        "Recover all"
        ]
        otherudldpopt = StringVar(UDLDframe)
        otherudldpopt.set(OPTIONS[0])    # default value
        otherudldpopt.trace("w", option_changed_otherudldpopt)
        dropbox = OptionMenu(UDLDframe, otherudldpopt, *OPTIONS)   
        dropbox.grid(column=1, row=1, padx=3)
        getudldother = Entry(UDLDframe, bg='white', width=16, fg='grey')
        getudldother.grid(column=2, row=1)
        getudldother.insert(0, '')
        window.focus_set()
        def handle_focus_in(_):
            if getudldother.cget('fg') != 'black':
                getudldother.delete(0, END)
                getudldother.config(fg='black')
        def handle_focus_out(_):
            if getudldother.get() == "":
                getudldother.delete(0, END)
                getudldother.config(fg='grey')
                getudldother.insert(0, 'xxxx.xxxx.xxxx')    
        getudldother.bind("<FocusOut>", handle_focus_out)
        getudldother.bind("<FocusIn>", handle_focus_in)
             
            
        
        def udld():
            if UDLDopt.get() == "Choose":
                pass
            elif UDLDopt.get() == "Enable":
                if (getudldiface.get() != "" and getudldiface.get() != "eg. fa0/0"):
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("udld enable \n")
                    sleep(0.3)
                    remote_conn.send("int " + getudldiface.get() + " \n")
                    sleep(0.3)
                    if chk_udld_aggr.get() == False:
                        remote_conn.send("udld port \n")
                    else:
                        remote_conn.send("udld port aggressive \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('UDLD', 'UDLD monitoring enabled', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("udld enable \n")
                    tkMessageBox.showinfo('UDLD', 'UDLD globally enabled', parent=window)
                sleep(0.3)
                remote_conn.send("exit \n")
            else:
                if (getudldiface.get() != "" and getudldiface.get() != "eg. fa0/0"):
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("int " + getudldiface.get() + " \n")
                    sleep(0.3)
                    remote_conn.send("no udld port \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('UDLD', 'UDLD monitoring disabled', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("no udld enable \n")
                    tkMessageBox.showinfo('UDLD', 'UDLD globally disabled', parent=window)                        
                sleep(0.3)
                remote_conn.send("exit \n")


            if otherudldpopt.get() == "Optional":
                pass
            else:
                if chk_state_neg.get() == False:
                    if otherudldpopt.get() == "Hello":
                        if (getudldother.get() == "" and getudldother.get() == "eg. 5"):
                            tkMessageBox.showinfo('Error', 'Please enter a value.', parent=window)
                        else:
                            remote_conn.send("conf t \n")
                            sleep(0.3)
                            remote_conn.send("udld message time " + getudldother.get() + " \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('UDLD', 'UDLD hello timer modified.', parent=window)
                    elif otherudldpopt.get() == "Auto-recovery":
                        if (getudldother.get() == "" and getudldother.get() == "eg. 5"):
                            remote_conn.send("conf t \n")
                            sleep(0.3)
                            remote_conn.send("udld recovery \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('UDLD', 'UDLD will auto recover from UDLD-triggered disables (default 20sec).', parent=window)
                        else:
                            remote_conn.send("conf t \n")
                            sleep(0.3)                        
                            remote_conn.send("udld recovery " + getcdplldpother.get() + " \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('UDLD', 'UDLD will auto recover from UDLD-triggered disables after specified time.', parent=window)
                    else:
                        if (getudldother.get() == "" and getudldother.get() == "eg. 5"):
                            tkMessageBox.showinfo('Error', 'Please enter a value.', parent=window)
                        else:
                            remote_conn.send("udld reset \n")
                            sleep(0.3)                           
                            tkMessageBox.showinfo('UDLD', 'All UDLD-triggered interface disables has been recovered.', parent=window)                      
                else:
                    if otherudldpopt.get() == "Hello":
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("no udld message time \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('UDLD', 'UDLD hello timer reset.', parent=window)
                    elif otherudldpopt.get() == "Auto-recovery":
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("no udld recovery \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('UDLD', 'UDLD auto-recovery disabled.', parent=window)
                    else:
                        pass
        btn = Button(UDLDframe, text="Aplicar", bg="orange", command=udld)
        btn.grid(column=5, row=0)
        blanklbl = Label(UDLDframe, text="      ").grid(column=4, row=0)

        def UDLDHelp():
            res = ""
            tkMessageBox.showinfo('UDLD Help', res, parent=window)
        btn = Button(UDLDframe, text="Help", bg="yellow", command=UDLDHelp)
        btn.grid(row=1,column=5)



        

        BFDframe=LabelFrame(window,text=" L3 Link monitoring (Negate not used) ",font=('verdana', 8, 'bold'),padx=10,pady=5,width=100,height=100)
        BFDframe.grid(row=2,column=0, sticky=("nsew"))

        lbl = Label(BFDframe, text="BFD:").grid(column=0, row=0)
        OPTIONS = [
        "Choose",
        "Enable",
        "Disable"
        ]
        BFDopt = StringVar(BFDframe)
        BFDopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(BFDframe, BFDopt, *OPTIONS)   
        dropbox.grid(column=1, row=0, padx=3)
        getbfdiface = Entry(BFDframe, bg='white', width=8, fg='grey')
        getbfdiface.grid(column=2, row=0, padx=1)
        getbfdiface.insert(0, "eg. fa0/0")
        def handle_focus_in(_):
            if getbfdiface.cget('fg') != 'black':
                getbfdiface.delete(0, END)
                getbfdiface.config(fg='black')
        def handle_focus_out(_):
            if getbfdiface.get() == "":
                getbfdiface.delete(0, END)
                getbfdiface.config(fg='grey')
                getbfdiface.insert(0, "eg. fa0/0")    
        getbfdiface.bind("<FocusOut>", handle_focus_out)
        getbfdiface.bind("<FocusIn>", handle_focus_in)

        getbfdintv = Entry(BFDframe, bg='white', width=7, fg='grey')
        getbfdintv.grid(column=3, row=0, padx=1)
        getbfdintv.insert(0, "interval")
        def handle_focus_in(_):
            if getbfdintv.cget('fg') != 'black':
                getbfdintv.delete(0, END)
                getbfdintv.config(fg='black')
        def handle_focus_out(_):
            if getbfdintv.get() == "":
                getbfdintv.delete(0, END)
                getbfdintv.config(fg='grey')
                getbfdintv.insert(0, "interval")    
        getbfdintv.bind("<FocusOut>", handle_focus_out)
        getbfdintv.bind("<FocusIn>", handle_focus_in)
        
        getbfdrx = Entry(BFDframe, bg='white', width=7, fg='grey')
        getbfdrx.grid(column=4, row=0, padx=1)
        getbfdrx.insert(0, "min_rx")
        def handle_focus_in(_):
            if getbfdrx.cget('fg') != 'black':
                getbfdrx.delete(0, END)
                getbfdrx.config(fg='black')
        def handle_focus_out(_):
            if getbfdrx.get() == "":
                getbfdrx.delete(0, END)
                getbfdrx.config(fg='grey')
                getbfdrx.insert(0, "min_rx")    
        getbfdrx.bind("<FocusOut>", handle_focus_out)
        getbfdrx.bind("<FocusIn>", handle_focus_in)

        getbfdmult = Entry(BFDframe, bg='white', width=9, fg='grey')
        getbfdmult.grid(column=5, row=0, padx=1)
        getbfdmult.insert(0, "multiplier")
        def handle_focus_in(_):
            if getbfdmult.cget('fg') != 'black':
                getbfdmult.delete(0, END)
                getbfdmult.config(fg='black')
        def handle_focus_out(_):
            if getbfdmult.get() == "":
                getbfdmult.delete(0, END)
                getbfdmult.config(fg='grey')
                getbfdmult.insert(0, "multiplier")    
        getbfdmult.bind("<FocusOut>", handle_focus_out)
        getbfdmult.bind("<FocusIn>", handle_focus_in)



     


        def bfd():
            if BFDopt.get() == "Choose":
                pass
            elif BFDopt.get() == "Enable":
                if (getbfdiface.get() == "" or getbfdiface.get() == "eg. fa0/0") and (getbfdintv.get() == "" or getbfdintv.get() == "interval") and \
                   (getbfdrx.get() == "" or getbfdrx.get() == "min_rx") and (getbfdmult.get() == "" or getbfdmult.get() == "multiplier"):
                    tkMessageBox.showinfo('ERROR', 'Please enter all required information.', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("int " + getbfdiface.get() + " \n")
                    sleep(0.3)
                    remote_conn.send("bfd interval " + getbfdintv.get() + " min_rx " + getbfdrx.get() + " multiplier " + getbfdmult.get() + " \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")                    
                    tkMessageBox.showinfo('BFD', 'BFD monitoring enabled on interface. NOTE: Remember to also enable it for the desired routing protocol(s) (in Route page) to take effect.', parent=window)
            else:
                if (getudldiface.get() == "" or getudldiface.get() == "eg. fa0/0"):
                    tkMessageBox.showinfo('ERROR', 'Please enter an interface at least.', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("int " + getbfdiface.get() + " \n")
                    sleep(0.3)
                    remote_conn.send("no bfd interval \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('BFD', 'BFD monitoring disabled on interface', parent=window)

                    
        btn = Button(BFDframe, text="Aplicar", bg="orange", command=bfd)
        btn.grid(column=6, row=0, padx=6)

        def BFDHelp():
            res = ""
            tkMessageBox.showinfo('BFD Help', res, parent=window)
        btn = Button(BFDframe, text="Help", bg="yellow", command=BFDHelp)
        btn.grid(row=1,column=6)
        

        SNMPframe=LabelFrame(window,text=" SNMP ",font=('verdana', 8, 'bold'),padx=10,pady=5,width=100,height=100)
        SNMPframe.grid(row=3,column=0, sticky=("nsew"))
        
        lbl = Label(SNMPframe, text="SNMP:").grid(column=0, row=0)
        OPTIONS = [
        "Choose",
        "Community",
        "Contact"
        ]
        SNMPopt = StringVar(SNMPframe)
        SNMPopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(SNMPframe, SNMPopt, *OPTIONS)   
        dropbox.grid(column=1, row=0, padx=3)
        getsnmp = Entry(SNMPframe, bg='white', width=12, fg='grey')
        getsnmp.grid(column=2, row=0)
        getsnmp.insert(0, "eg. public ro")
        def handle_focus_in(_):
            if getsnmp.cget('fg') != 'black':
                getsnmp.delete(0, END)
                getsnmp.config(fg='black')
        def handle_focus_out(_):
            if getsnmp.get() == "":
                getsnmp.delete(0, END)
                getsnmp.config(fg='grey')
                getsnmp.insert(0, "eg. public ro")    
        getsnmp.bind("<FocusOut>", handle_focus_out)
        getsnmp.bind("<FocusIn>", handle_focus_in)

        def snmp():
            if SNMPopt.get() == "Choose":
                pass
            elif SNMPopt.get() == "Community":
                if chk_state_neg.get() == False:
                    if (getsnmp.get() == "" or getsnmp.get() == "eg. public"):
                        tkMessageBox.showinfo('ERROR', 'Please enter all required information.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("snmp-server community " + getsnmp.get() + " \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")                   
                        tkMessageBox.showinfo('SNMP', 'SNMP monitoring configured. NOTE: Remember to use the same community value on your SNMP manager.', parent=window)
                else:
                    if (getsnmp.get() == "" or getsnmp.get() == "eg. public"):
                        tkMessageBox.showinfo('ERROR', 'Please enter all required information.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("no snmp-server community " + getsnmp.get() + " \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")                   
                        tkMessageBox.showinfo('SNMP', 'SNMP community deleted.', parent=window)                    
            else:
                if chk_state_neg.get() == False:
                    if (getsnmp.get() == "" or getsnmp.get() == "eg. public"):
                        tkMessageBox.showinfo('ERROR', 'Please enter all required information.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("snmp-server contact " + getsnmp.get() + " \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")                   
                        tkMessageBox.showinfo('SNMP', 'SNMP contact configured.', parent=window)
                else:
                    if (getsnmp.get() == "" or getsnmp.get() == "eg. public"):
                        tkMessageBox.showinfo('ERROR', 'Please enter all required information.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("no snmp-server contact \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")                   
                        tkMessageBox.showinfo('SNMP', 'SNMP contact deleted.', parent=window) 
        btn = Button(SNMPframe, text="Aplicar", bg="orange", command=snmp)
        btn.place(x=340, y=0)





        NFframe=LabelFrame(window,text=" Netflow ",font=('verdana', 8, 'bold'),padx=10,pady=5,width=100,height=100)
        NFframe.grid(row=4,column=0, sticky=("nsew"))

        lbl = Label(NFframe, text="Monitor:").grid(column=0, row=3)
        OPTIONS = [
        "Choose",
        "Ingress",
        "Egress"
        ]
        NFopt = StringVar(NFframe)
        NFopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(NFframe, NFopt, *OPTIONS)   
        dropbox.grid(column=1, row=3, padx=3)
        getnfiface = Entry(NFframe, bg='white', width=12, fg='grey')
        getnfiface.grid(column=2, row=3)
        getnfiface.insert(0, "eg. fa0/0")
        def handle_focus_in(_):
            if getnfiface.cget('fg') != 'black':
                getnfiface.delete(0, END)
                getnfiface.config(fg='black')
        def handle_focus_out(_):
            if getnfiface.get() == "":
                getnfiface.delete(0, END)
                getnfiface.config(fg='grey')
                getnfiface.insert(0, "eg. fa0/0")    
        getnfiface.bind("<FocusOut>", handle_focus_out)
        getnfiface.bind("<FocusIn>", handle_focus_in)


        chk_top_talker = BooleanVar()
        chk_top_talker.set(False)
        chk = Checkbutton(NFframe, text="TopTalkers", variable=chk_top_talker)
        chk.grid(column=1, row=4)

        OPTIONS = [
        "Sort by",
        "Bytes",
        "Packets"
        ]
        NFSortopt = StringVar(NFframe)
        NFSortopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(NFframe, NFSortopt, *OPTIONS)   
        dropbox.grid(column=2, row=4, padx=3)
        
        getnfentries = Entry(NFframe, bg='white', width=15, fg='grey')
        getnfentries.grid(column=3, row=4)
        getnfentries.insert(0, "no. of entries")
        def handle_focus_in(_):
            if getnfentries.cget('fg') != 'black':
                getnfentries.delete(0, END)
                getnfentries.config(fg='black')
        def handle_focus_out(_):
            if getnfentries.get() == "":
                getnfentries.delete(0, END)
                getnfentries.config(fg='grey')
                getnfentries.insert(0, "no. of entries")    
        getnfentries.bind("<FocusOut>", handle_focus_out)
        getnfentries.bind("<FocusIn>", handle_focus_in)

        OPTIONS = [
        "Match",
        "Src addr",
        "Dst addr",
        "Src port",
        "Dst port",
        "Src AS",
        "Dst AS",
        "In flow",
        "Out flow",
        "ProtoUDP",
        "ProtoTCP",
        "ClassMap"
        ]
        NFMatchopt = StringVar(NFframe)
        NFMatchopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(NFframe, NFMatchopt, *OPTIONS)   
        dropbox.grid(column=2, row=5, padx=3)        
        getnfmatch = Entry(NFframe, bg='white', width=15, fg='grey')
        getnfmatch.grid(column=3, row=5)
        getnfmatch.insert(0, "eg IP addr")
        def handle_focus_in(_):
            if getnfmatch.cget('fg') != 'black':
                getnfmatch.delete(0, END)
                getnfmatch.config(fg='black')
        def handle_focus_out(_):
            if getnfmatch.get() == "":
                getnfmatch.delete(0, END)
                getnfmatch.config(fg='grey')
                getnfmatch.insert(0, "eg IP addr")    
        getnfmatch.bind("<FocusOut>", handle_focus_out)
        getnfmatch.bind("<FocusIn>", handle_focus_in)        

        
        def netflow():
            if NFopt.get() == "Choose":
                pass
            else:
                if chk_state_neg == False:
                    if (getnfiface.get() == "" or getnfiface.get() == "eg. fa0/0"):
                        tkMessageBox.showinfo('ERROR', 'Please enter all required information.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("int " + getnfiface.get() + " \n")
                        sleep(0.3)
                        remote_conn.send("ip flow " + NFopt.get() + " \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")                    
                        tkMessageBox.showinfo('Netflow', 'Netflow monitoring enabled on interface.', parent=window)
                else:
                    if (getnfiface.get() == "" or getnfiface.get() == "eg. fa0/0"):
                        tkMessageBox.showinfo('ERROR', 'Please enter an interface at least.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("int " + getnfiface.get() + " \n")
                        sleep(0.3)
                        remote_conn.send("no ip flow " + NFopt.get() + " \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        sleep(0.3)
                        remote_conn.send("exit \n") 
                        tkMessageBox.showinfo('Netflow', 'Netflow monitoring disabled on interface', parent=window)


            if chk_top_talker.get() == False:
                pass
            else:
                top = ""
                match = ""
                if chk_state_neg == False:
                    if NFSortopt.get() == "Sort by":
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("ip flow-top-t \n")
                        sleep(0.3)
                        if getnfentries.get() != "" or getnfentries.get() != "no. of entries":
                            remote_conn.send("top " + getnfentries.get() + " \n")
                            sleep(0.3)
                            top = 'Toptalker entries configured. '
                        else:
                            pass
                        if NFMatchopt.get() != "Match":
                            if NFMatchopt.get() == "Src addr":
                                remote_conn.send("match so addr " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Dst addr":
                                remote_conn.send("match dest addr " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Src port":
                                remote_conn.send("match so port " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Dst port":
                                remote_conn.send("match dest port " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Src AS":
                                remote_conn.send("match so AS " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Dst AS":
                                remote_conn.send("match dest AS " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "In flow":
                                remote_conn.send("match dir ing " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Out flow":
                                remote_conn.send("match dir eg " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "ProtoUDP":
                                remote_conn.send("match proto udp" + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "ProtoTCP":
                                remote_conn.send("match proto tcp" + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "ClassMap":
                                remote_conn.send("match class-m " + getnfentries.get() + " \n")
                            sleep(0.3)
                            match = 'Toptalker match configured. '
                        else:
                            pass    
                        remote_conn.send("exit \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Netflow', 'Toptalker enabled. ', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("ip flow-top-t \n")
                        sleep(0.3)
                        remote_conn.send("sort " + NFSortopt.get() + " \n")
                        sleep(0.3)
                        if getnfentries.get() != "" or getnfentries.get() != "no. of entries":
                            remote_conn.send("top " + getnfentries.get() + " \n")
                            sleep(0.3)
                            top = 'Toptalker entries configured. '
                        else:
                            pass
                        if NFMatchopt.get() != "Match":
                            if NFMatchopt.get() == "Src addr":
                                remote_conn.send("match so addr " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Dst addr":
                                remote_conn.send("match dest addr " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Src port":
                                remote_conn.send("match so port " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Dst port":
                                remote_conn.send("match dest port " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Src AS":
                                remote_conn.send("match so AS " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Dst AS":
                                remote_conn.send("match dest AS " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "In flow":
                                remote_conn.send("match dir ing " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Out flow":
                                remote_conn.send("match dir eg " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "ProtoUDP":
                                remote_conn.send("match proto udp" + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "ProtoTCP":
                                remote_conn.send("match proto tcp" + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "ClassMap":
                                remote_conn.send("match class-m " + getnfentries.get() + " \n")
                            sleep(0.3)
                            match = 'Toptalker match configured. '
                        else:
                            pass
                        remote_conn.send("exit \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Netflow', 'Toptalker enabled, results sorted. ' + top + match, parent=window)
                else:
                    if NFSortopt.get() == "Sort by":
                        if (getnfentries.get() == "" or getnfentries.get() == "no. of entries") and (getnfmatch.get() == "" or getnfmatch.get() == "eg IP addr"):
                            remote_conn.send("conf t \n")
                            sleep(0.3)
                            remote_conn.send("no ip flow-top-t \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('Netflow', 'Toptalker disabled.', parent=window)
                        else:
                            if getnfentries.get() != "" or getnfentries.get() != "no. of entries":
                                remote_conn.send("no top \n")
                                sleep(0.3)
                            else:
                                pass
                                if NFMatchopt.get() != "Match":
                                    if NFMatchopt.get() == "Src addr":
                                        remote_conn.send("no match so addr " + getnfentries.get() + " \n")
                                    if NFMatchopt.get() == "Dst addr":
                                        remote_conn.send("no match dest addr " + getnfentries.get() + " \n")
                                    if NFMatchopt.get() == "Src port":
                                        remote_conn.send("no match so port " + getnfentries.get() + " \n")
                                    if NFMatchopt.get() == "Dst port":
                                        remote_conn.send("no match dest port " + getnfentries.get() + " \n")
                                    if NFMatchopt.get() == "Src AS":
                                        remote_conn.send("no match so AS " + getnfentries.get() + " \n")
                                    if NFMatchopt.get() == "Dst AS":
                                        remote_conn.send("no match dest AS " + getnfentries.get() + " \n")
                                    if NFMatchopt.get() == "In flow":
                                        remote_conn.send("no match dir ing " + getnfentries.get() + " \n")
                                    if NFMatchopt.get() == "Out flow":
                                        remote_conn.send("no match dir eg " + getnfentries.get() + " \n")
                                    if NFMatchopt.get() == "ProtoUDP":
                                        remote_conn.send("no match proto udp" + getnfentries.get() + " \n")
                                    if NFMatchopt.get() == "ProtoTCP":
                                        remote_conn.send("no match proto tcp" + getnfentries.get() + " \n")
                                    if NFMatchopt.get() == "ClassMap":
                                        remote_conn.send("no match class-m " + getnfentries.get() + " \n")
                                    sleep(0.3)
                                    
                                else:
                                    pass
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("ip flow-top-t \n")
                        sleep(0.3)
                        remote_conn.send("no sort " + NFSortopt.get() + " \n")
                        sleep(0.3)
                        if getnfentries.get() != "" or getnfentries.get() != "no. of entries":
                            remote_conn.send("no top \n")
                            sleep(0.3)
                            top = 'Toptalker entries reset. '
                        else:
                            pass
                        if NFMatchopt.get() != "Match":
                            if NFMatchopt.get() == "Src addr":
                                remote_conn.send("no match so addr " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Dst addr":
                                remote_conn.send("no match dest addr " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Src port":
                                remote_conn.send("no match so port " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Dst port":
                                remote_conn.send("no match dest port " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Src AS":
                                remote_conn.send("no match so AS " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Dst AS":
                                remote_conn.send("no match dest AS " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "In flow":
                                remote_conn.send("no match dir ing " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "Out flow":
                                remote_conn.send("no match dir eg " + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "ProtoUDP":
                                remote_conn.send("no match proto udp" + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "ProtoTCP":
                                remote_conn.send("no match proto tcp" + getnfentries.get() + " \n")
                            if NFMatchopt.get() == "ClassMap":
                                remote_conn.send("no match class-m " + getnfentries.get() + " \n")
                            sleep(0.3)
                            match = 'Toptalker match deleted. '
                        else:
                            pass
                        remote_conn.send("exit \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Netflow', 'Toptalker enabled, results sorting reset. ' + top + match, parent=window)
        btn = Button(NFframe, text="Aplicar", bg="orange", command=netflow)
        btn.place(x=340, y=0)

        def NetFlowHelp():
            res = ""
            tkMessageBox.showinfo('NetFlow Help', res, parent=window)
        btn = Button(NFframe, text="Help", bg="yellow", command=NetFlowHelp)
        btn.place(x=340, y=65)






        Mirrorframe=LabelFrame(window,text=" Port Mirroring (for Switch only) ",font=('verdana', 8, 'bold'),padx=10,pady=5,width=100,height=100)
        Mirrorframe.grid(row=5,column=0, sticky=("nsew"))

        SPANvar = IntVar()
        SPANvar.set(1)
        R1 = Radiobutton(Mirrorframe, text="SPAN", variable=SPANvar, value=1)
        R1.place(x=10, y=0)        
        R2 = Radiobutton(Mirrorframe, text="RSPAN local", variable=SPANvar, value=2)
        R2.place(x=75, y=0)
        R3 = Radiobutton(Mirrorframe, text="RSPAN remote", variable=SPANvar, value=3)
        R3.place(x=170, y=0)


        lbl = Label(Mirrorframe, text="Session Src:").grid(column=0, row=1, padx=5)

        getSessID = Entry(Mirrorframe, bg='white', width=6, fg='grey')
        getSessID.grid(column=4, row=0, padx=15)
        getSessID.insert(0, "<1-60>")
        def handle_focus_in(_):
            if getSessID.cget('fg') != 'black':
                getSessID.delete(0, END)
                getSessID.config(fg='black')
        def handle_focus_out(_):
            if getSessID.get() == "":
                getSessID.delete(0, END)
                getSessID.config(fg='grey')
                getSessID.insert(0, "<1-60>")    
        getSessID.bind("<FocusOut>", handle_focus_out)
        getSessID.bind("<FocusIn>", handle_focus_in)
        
        getSessiface = Entry(Mirrorframe, bg='white', width=15, fg='grey')
        getSessiface.grid(column=1, row=1, padx=10)
        getSessiface.insert(0, "eg. fa0/0, VLAN 2")
        def handle_focus_in(_):
            if getSessiface.cget('fg') != 'black':
                getSessiface.delete(0, END)
                getSessiface.config(fg='black')
        def handle_focus_out(_):
            if getSessiface.get() == "":
                getSessiface.delete(0, END)
                getSessiface.config(fg='grey')
                getSessiface.insert(0, "eg. fa0/0, VLAN 2")    
        getSessiface.bind("<FocusOut>", handle_focus_out)
        getSessiface.bind("<FocusIn>", handle_focus_in)
        
        OPTIONS = [
        "RX",
        "TX",
        "Both"
        ]
        MirrDiropt = StringVar(Mirrorframe)
        MirrDiropt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(Mirrorframe, MirrDiropt, *OPTIONS)   
        dropbox.grid(column=3, row=1, padx=5, sticky = 'w')
        
        lbl = Label(Mirrorframe, text="Session Dst:").grid(column=0, row=2, padx=5)
        getSessdstiface = Entry(Mirrorframe, bg='white', width=15, fg='grey')
        getSessdstiface.grid(column=1, row=2, padx=10)
        getSessdstiface.insert(0, "eg. fa0/0, VLAN 2")
        def handle_focus_in(_):
            if getSessdstiface.cget('fg') != 'black':
                getSessdstiface.delete(0, END)
                getSessdstiface.config(fg='black')
        def handle_focus_out(_):
            if getSessdstiface.get() == "":
                getSessdstiface.delete(0, END)
                getSessdstiface.config(fg='grey')
                getSessdstiface.insert(0, "eg. fa0/0, VLAN 2")    
        getSessdstiface.bind("<FocusOut>", handle_focus_out)
        getSessdstiface.bind("<FocusIn>", handle_focus_in)

        chk_encap_replicate = BooleanVar()
        chk_encap_replicate.set(False)
        chk = Checkbutton(Mirrorframe, text="Encapsulation Replicate", variable=chk_encap_replicate)
        chk.grid(column=2, row=2, columnspan=4)


        lbl = Label(Mirrorframe, text="Optional Filter:").grid(column=0, row=3, padx=5, columnspan=2, sticky=("w"))
        getSessfilter = Entry(Mirrorframe, bg='white', width=15, fg='grey')
        getSessfilter.grid(column=1, row=3, padx=10, pady=2, sticky = 'w')
        getSessfilter.insert(0, "eg. VLAN 5 - 7")
        def handle_focus_in(_):
            if getSessfilter.cget('fg') != 'black':
                getSessfilter.delete(0, END)
                getSessfilter.config(fg='black')
        def handle_focus_out(_):
            if getSessfilter.get() == "":
                getSessfilter.delete(0, END)
                getSessfilter.config(fg='grey')
                getSessfilter.insert(0, "eg. VLAN 5 - 7")    
        getSessfilter.bind("<FocusOut>", handle_focus_out)
        getSessfilter.bind("<FocusIn>", handle_focus_in)

        OPTIONS = [
        "All",
        "Unicast",
        "Broadcast",
        "Multicast"
        ]
        Filteropt = StringVar(Mirrorframe)
        Filteropt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(Mirrorframe, Filteropt, *OPTIONS)   
        dropbox.grid(column=3, row=3, padx=5)


#        blanklbl = Label(Mirrorframe, text="").grid(column=0, row=3)



        def spanport():
            if (getSessID.get() == "" or getSessID.get() == "<1-60>"):
                tkMessageBox.showinfo('Error', 'Please enter session ID. ', parent=window)
            else:
                MirrDir = str(MirrDiropt.get())
                if ("VLAN" in getSessiface.get()) or ("vlan" in getSessiface.get()):
                    MirrDir = "RX"
                else:
                    pass
                if chk_state_neg == False:
                    if SPANvar.get() == 1:
                        if ("vlan" in getSessdstiface.get()) or ("VLAN" in getSessdstiface.get()):
                            tkMessageBox.showinfo('Error', 'Destination for SPAN can only be an interface, not a VLAN. ', parent=window)
                        else:
                            if (getSessiface.get() != "" and getSessiface.get() != "eg. fa0/0, VLAN 2"):
                                remote_conn.send("conf t \n")
                                sleep(0.3)
                                if ("VLAN" in getSessiface.get()) or ("vlan" in getSessiface.get()):
                                    remote_conn.send("monitor session " + getSessID.get() + " source " + getSessiface.get() + " " + MirrDir + " \n")
                                else:
                                    remote_conn.send("monitor session " + getSessID.get() + " source interface " + getSessiface.get() + " " + MirrDir + " \n")
                                sleep(0.3)
                                remote_conn.send("exit \n")
                                spansrccomment = "SPAN session - source configured. "
                            else:
                                spansrccomment = "SPAN session - no source configured. "

                            if (getSessdstiface.get() != "" and getSessdstiface.get() != "eg. fa0/0, VLAN 2"):
                                remote_conn.send("conf t \n")
                                sleep(0.3)
                                if chk_encap_replicate.get() == False:
                                    remote_conn.send("monitor session " + getSessID.get() + " destination interface " + getSessdstiface.get() + " \n")
                                else:
                                    remote_conn.send("monitor session " + getSessID.get() + " destination interface " + getSessdstiface.get() + " encap replicate \n")
                                sleep(0.3)
                                remote_conn.send("exit \n")
                                spandstcomment = "SPAN session - destination configured. "
                            else:
                                spandstcomment = "SPAN session - no destination configured. "
                    elif SPANvar.get() == 2:
                        if ("vlan" not in getSessdstiface.get()) or ("VLAN" not in getSessdstiface.get()):
                            tkMessageBox.showinfo('Error', 'Please enter a VLAN ID for the destination; remember to create it ("remote-span" VLAN type) in both the source\
AND destination device also. ', parent=window)
                        else: 
                            if (getSessiface.get() != "" and getSessiface.get() != "eg. fa0/0, VLAN 2"):
                                remote_conn.send("conf t \n")
                                sleep(0.3)
                                if ("VLAN" in getSessiface.get()) or ("vlan" in getSessiface.get()):
                                    remote_conn.send("monitor session " + getSessID.get() + " source " + getSessiface.get() + " " + MirrDir + " \n")
                                else:
                                    remote_conn.send("monitor session " + getSessID.get() + " source interface " + getSessiface.get() + " " + MirrDir + " \n")
                                sleep(0.3)
                                remote_conn.send("exit \n")
                                spansrccomment = "RSPAN local session - source configured. "
                            else:
                                spansrccomment = "RSPAN local session - no source configured. "
                            
                            if (getSessdstiface.get() != "" and getSessdstiface.get() != "eg. fa0/0, VLAN 2"):
                                remote_conn.send("conf t \n")
                                sleep(0.3)
                                remote_conn.send("monitor session " + getSessID.get() + " destination remote " + getSessdstiface.get() + " \n")
                                sleep(0.3)
                                remote_conn.send("exit \n")
                                spandstcomment = "RSPAN local session - destination configured. "
                            else:
                                spandstcomment = "RSPAN local session - no destination configured. "
                    else:
                        if ("vlan" not in getSessiface.get()) or ("VLAN" not in getSessiface.get()):
                            tkMessageBox.showinfo('Error', 'Please enter a VLAN ID for the source; remember to create it ("remote-span" VLAN type) in both the source AND\
destination device also. ', parent=window)
                        elif ("vlan" in getSessdstiface.get()) or ("VLAN" in getSessdstiface.get()):
                            tkMessageBox.showinfo('Error', 'Destination for the remote RSPAN can only be an interface, not a VLAN. ', parent=window)
                        else:
                            if (getSessiface.get() != "" and getSessiface.get() != "eg. fa0/0, VLAN 2"):
                                remote_conn.send("conf t \n")
                                sleep(0.3)
                                remote_conn.send("monitor session " + getSessID.get() + " source remote " + getSessiface.get() + " " + MirrDir + " \n")
                                sleep(0.3)
                                remote_conn.send("exit \n")
                                spansrccomment = "RSPAN remote session - source configured. "
                            else:
                                spansrccomment = "RSPAN remote session - no source configured. "
                            
                            if (getSessdstiface.get() != "" and getSessdstiface.get() != "eg. fa0/0, VLAN 2"):
                                remote_conn.send("conf t \n")
                                sleep(0.3)
                                if chk_encap_replicate.get() == False:
                                    remote_conn.send("monitor session " + getSessID.get() + " destination interface " + getSessdstiface.get() + " \n")
                                else:
                                    remote_conn.send("monitor session " + getSessID.get() + " destination interface " + getSessdstiface.get() + " encap replicate \n")
                                sleep(0.3)
                                remote_conn.send("exit \n")
                                spandstcomment = "RSPAN remote session - destination configured. "
                            else:
                                spandstcomment = "RSPAN remote session - no destination configured. "

                    if (getSessfilter.get() != "" and getSessfilter.get() != "eg. VLAN 5 - 7"):
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        if Filteropt.get() == "All":
                            remote_conn.send("monitor session " + getSessID.get() + " filter " + getSessfilter.get() + " \n")
                        else:
                            remote_conn.send("monitor session " + getSessID.get() + " filter " + getSessfilter.get() + " address-type " + Filteropt.get() + " \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        spanfiltercomment = "SPAN filter configured. "
                    else:
                        spanfiltercomment = "No SPAN filter configured. "
                            
                    tkMessageBox.showinfo('SPAN/RSPAN', spansrccomment + spandstcomment + spanfiltercomment, parent=window)

                else:
                    if (getSessiface.get() == "" or getSessiface.get() == "eg. fa0/0, VLAN 2") and (getSessdstiface.get() == "" or getSessdstiface.get() == "eg. fa0/0, VLAN 2")\
                        and (getSessfilter.get() == "" or getSessfilter.get() == "eg. VLAN 5 - 7"):
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("no monitor session " + getSessID.get() + " \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('SPAN/RSPAN', 'Session deleted.', parent=window)
                    else:
                        if SPANvar.get() == 1:
                            if ("vlan" in getSessdstiface.get()) or ("VLAN" in getSessdstiface.get()):
                                tkMessageBox.showinfo('Error', 'Destination for SPAN can only be an interface, not a VLAN. ', parent=window)
                            else:
                                if (getSessiface.get() != "" and getSessiface.get() != "eg. fa0/0, VLAN 2"):
                                    remote_conn.send("conf t \n")
                                    sleep(0.3)
                                    if ("VLAN" in getSessiface.get()) or ("vlan" in getSessiface.get()):
                                        remote_conn.send("no monitor session " + getSessID.get() + " source " + getSessiface.get() + " " + MirrDir + " \n")
                                    else:
                                        remote_conn.send("no monitor session " + getSessID.get() + " source interface " + getSessiface.get() + " " + MirrDir + " \n")
                                    sleep(0.3)
                                    remote_conn.send("exit \n")
                                    spancomment = "SPAN session - source deleted. "
                                else:
                                    pass

                                if (getSessdstiface.get() != "" and getSessdstiface.get() != "eg. fa0/0, VLAN 2"):
                                    remote_conn.send("conf t \n")
                                    sleep(0.3)
                                    remote_conn.send("no monitor session " + getSessID.get() + " destination interface " + getSessdstiface.get() + " \n")
                                    sleep(0.3)
                                    remote_conn.send("exit \n")
                                    spancomment = "SPAN session - destination deleted. "
                                else:
                                    spancomment = "SPAN session - no SPAN destination changes. "
                        elif SPANvar.get() == 2:
                            if ("vlan" not in getSessdstiface.get()) or ("VLAN" not in getSessdstiface.get()):
                                tkMessageBox.showinfo('Error', 'Please enter a VLAN ID for the destination; remember to create it ("remote-span" VLAN type) in both the source\
    AND destination device also. ', parent=window)
                            else: 
                                if (getSessiface.get() != "" and getSessiface.get() != "eg. fa0/0, VLAN 2"):
                                    remote_conn.send("conf t \n")
                                    sleep(0.3)
                                    if ("VLAN" in getSessiface.get()) or ("vlan" in getSessiface.get()):
                                        remote_conn.send("no monitor session " + getSessID.get() + " source " + getSessiface.get() + " " + MirrDir + " \n")
                                    else:
                                        remote_conn.send("no monitor session " + getSessID.get() + " source interface " + getSessiface.get() + " " + MirrDir + " \n")
                                    sleep(0.3)
                                    remote_conn.send("exit \n")
                                    spancomment = "RSPAN local session - source deleted. "
                                else:
                                    spancomment = "RSPAN local session - no RSPAN source changes. "
                                
                                if (getSessdstiface.get() != "" and getSessdstiface.get() != "eg. fa0/0, VLAN 2"):
                                    remote_conn.send("conf t \n")
                                    sleep(0.3)
                                    remote_conn.send("no monitor session " + getSessID.get() + " destination remote " + getSessdstiface.get() + " \n")
                                    sleep(0.3)
                                    remote_conn.send("exit \n")
                                    spancomment = "RSPAN local session - destination deleted. "
                                else:
                                    spancomment = "RSPAN local session - no RSPAN destination changes. "
                        else:
                            if ("vlan" not in getSessiface.get()) or ("VLAN" not in getSessiface.get()):
                                tkMessageBox.showinfo('Error', 'Please enter a VLAN ID for the source; remember to create it ("remote-span" VLAN type) in both the source AND\
    destination device also. ', parent=window)
                            else:
                                if ("vlan" in getSessdstiface.get()) or ("VLAN" in getSessdstiface.get()):
                                    tkMessageBox.showinfo('Error', 'Destination for SPAN can only be an interface, not a VLAN. ', parent=window)
                                else:
                                    if (getSessiface.get() != "" and getSessiface.get() != "eg. fa0/0, VLAN 2"):
                                        remote_conn.send("conf t \n")
                                        sleep(0.3)
                                        remote_conn.send("no monitor session " + getSessID.get() + " source remote " + getSessiface.get() + " " + MirrDir + " \n")
                                        sleep(0.3)
                                        remote_conn.send("exit \n")
                                        spancomment = "RSPAN remote session - source deleted. "
                                    else:
                                        spancomment = "RSPAN remote session - no RSPAN source changes. "
                                    
                                    if (getSessdstiface.get() != "" and getSessdstiface.get() != "eg. fa0/0, VLAN 2"):
                                        remote_conn.send("conf t \n")
                                        sleep(0.3)
                                        remote_conn.send("no monitor session " + getSessID.get() + " destination interface " + getSessdstiface.get() + " \n")
                                        sleep(0.3)
                                        remote_conn.send("exit \n")
                                        spancomment = "RSPAN remote session - destination deleted. "
                                    else:
                                        spancomment = "RSPAN remote session - no RSPAN destination changes. "

                        if (getSessfilter.get() != "" and getSessfilter.get() != "eg. VLAN 5 - 7"):
                            remote_conn.send("conf t \n")
                            sleep(0.3)
                            if Filteropt.get() == "All":
                                remote_conn.send("no monitor session " + getSessID.get() + " filter " + getSessfilter.get() + " \n")
                            else:
                                remote_conn.send("no monitor session " + getSessID.get() + " filter " + getSessfilter.get() + " address-type " + Filteropt.get() + " \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            spanfiltercomment = "SPAN filter deleted. "
                        else:
                            spanfiltercomment = "No SPAN filter changes. "
                            
                        tkMessageBox.showinfo('SPAN/RSPAN', spansrccomment + spandstcomment + spanfiltercomment, parent=window)

        btn = Button(Mirrorframe, text="Aplicar", bg="orange", command=spanport)
        btn.grid(column=5, row=0, padx=3)

        def MirrorHelp():
            res = " "
            tkMessageBox.showinfo('Port Mirroring (aka SPAN) Help', res, parent=window)
        btn = Button(Mirrorframe, text="Help", bg="yellow", command=MirrorHelp)
        btn.grid(row=3,column=5)





        
        Syslogframe=LabelFrame(window,text=" Syslog ",font=('verdana', 8, 'bold'),padx=10,pady=5,width=100,height=100)
        Syslogframe.grid(row=6,column=0, sticky=("nsew"))

        blanklbl = Label(Syslogframe, text="").grid(column=0, row=0, padx=75, pady=5)
        OPTIONS = [
        "Syslog server IP:",
        "Syslog source-int:",
        "Log msg level:"
        ]
        Slogopt = StringVar(Syslogframe)
        Slogopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(Syslogframe, Slogopt, *OPTIONS)   
        dropbox.place(x=3, y=0)        
        getSlog = Entry(Syslogframe, width=15)
        getSlog.grid(column=1, row=0, padx=20)

        def slog():
            if chk_state_neg == False:
                if getSlog.get() == "":
                    tkMessageBox.showinfo('Error', 'Please enter the required information.', parent=window)
                elif Slogopt.get() == "Syslog server IP:":
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("logging host " + getSlog.get() + " \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Syslog', 'Logs from this router will be sent to your specified IP address.', parent=window)
                elif Slogopt.get() == "Log msg level:":
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("logging trap " + getSlog.get() + " \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Syslog', 'Logs for your specified level will be sent to a Syslog server (if the Syslog server IP is configured).', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("int " + getSlog.get() + " \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Syslog', 'Logs from this router will be sent to a Syslog server sourced from the IP address of the configured interface.', parent=window)
            else:
                if Slogopt.get() == "Syslog server IP:":
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("no logging host \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Syslog', 'Syslog server removed.', parent=window)
                elif Slogopt.get() == "Log msg level:":
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("no logging trap \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Syslog', 'Logs level reset.', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("no logging source-int \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Syslog', 'Syslog source interface reset.', parent=window)
        btn = Button(Syslogframe, text="Aplicar", bg="orange", command=slog)
        btn.place(x=340, y=0)




        shmonitoringframe=LabelFrame(window,text=" Show/Clear config ",font=('verdana', 8, 'bold'),padx=5,pady=5,width=100,height=100)
        shmonitoringframe.grid(row=7,column=0, sticky=("nsew"))

        OPTIONS = [
        "CDP neighbors",
        "CDP interface stats",
        "LLDP neighbors",
        "LLDP interface stats",
        "LLDP timers",
        "LLDP traffic",        
        "SNMP traffic",
        "SNMP community",
        "BFD",
        "BFD neighbors",
        "BFD summary",
        "BFD drops",
        "NetFlow",
        "NetFlow Exporters",
        "NetFlow: TopTalker",
        "SPAN Session:",
        "Syslog stats",
        "Clear Syslog logs"
        ]
        NFShowopt = StringVar(shmonitoringframe)
        NFShowopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(shmonitoringframe, NFShowopt, *OPTIONS)   
        dropbox.grid(column=0, row=0, padx=3)        
        shmoninput = Entry(shmonitoringframe, bg='white', width=15, fg='grey')
        shmoninput.grid(column=1, row=0)
        def showmonclick():
            buff_size = 16384
            sleep(0.5)
            if NFShowopt.get() == "CDP neighbors":
                remote_conn.send("show cdp neigh \n")
            elif NFShowopt.get() == "CDP interface stats":
                remote_conn.send("show cdp interface \n")
            elif NFShowopt.get() == "LLDP neighbors":
                remote_conn.send("show lldp neigh \n")                                
            elif NFShowopt.get() == "LLDP interface stats":
                remote_conn.send("show lldp interface \n")
            elif NFShowopt.get() == "LLDP timers":
                remote_conn.send("show lldp timers \n")
            elif NFShowopt.get() == "LLDP traffic":
                remote_conn.send("show lldp traffic \n")                
            elif NFShowopt.get() == "SNMP traffic":
                remote_conn.send("show SNMP \n")
            elif NFShowopt.get() == "SNMP community":
                remote_conn.send("show SNMP community \n")                
            elif NFShowopt.get() == "BFD":
                remote_conn.send("show BFD all \n")
            elif NFShowopt.get() == "BFD neighbors":
                remote_conn.send("show BFD neigh \n")
            elif NFShowopt.get() == "BFD summary":
                remote_conn.send("show BFD summ \n")
            elif NFShowopt.get() == "BFD drops":
                remote_conn.send("show BFD drops \n")
            elif NFShowopt.get() == "NetFlow":
                remote_conn.send("show ip cache flow \n")
            elif NFShowopt.get() == "NetFlow Exporters":
                remote_conn.send("show flow exporter \n")                
            elif NFShowopt.get() == "NetFlow: TopTalker":
                remote_conn.send("show ip flow top-t \n")
            elif NFShowopt.get() == "SPAN Session:":
                remote_conn.send("show monitor session " + shmoninput.get() + " \n")                
            elif NFShowopt.get() == "Syslog stats":
                remote_conn.send("show logging \n")
            else:
                remote_conn.send("clear logging \n")
            sleep(0.5)
            while not remote_conn.recv_ready():
                remote_conn.recv(0)
                buff_size += 2048
                sleep(0.5)
            output = remote_conn.recv(buff_size).decode("utf-8")
            tkMessageBox.showinfo('Monitoring Statistics', output, parent=window)            
        btn = Button(shmonitoringframe, text="Show", bg="orange", command=showmonclick)
        btn.place(x=347, y=0)






    def admin():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("Administration")
        window.geometry('410x407')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)

        negframe=LabelFrame(window,text=" Negate ",font=('verdana', 8, 'bold'),padx=5,pady=5,width=100,height=100)
        negframe.grid(row=0,column=1)
        
        chk_state_neg = BooleanVar()
        chk_state_neg.set(False)
        chk = Checkbutton(negframe, variable=chk_state_neg)
        chk.grid(column=0, row=0)
        
        AdminFrame=LabelFrame(window,text=" Configure credential ",font=('verdana', 8, 'bold'),padx=5,pady=5,width=100,height=100)
        AdminFrame.grid(row=0,column=0, sticky=("nsew"))

        chk_RO_acct = BooleanVar()
        chk_RO_acct.set(False)
        chk = Checkbutton(AdminFrame, text="Read only", variable=chk_RO_acct)
        chk.grid(column=2, row=0)
        
        lbl = Label(AdminFrame, text="Username:").grid(column=0, row=0)
        getusername = Entry(AdminFrame,width=15)
        getusername.grid(column=1, row=0)
        lbl = Label(AdminFrame, text="Password:").grid(column=0, row=1)
        getpasswd = Entry(AdminFrame,width=15)
        getpasswd.grid(column=1, row=1)
##        lbl = Label(AdminFrame, text="Enable\nPassword:").grid(column=0, row=2)
##        getenpasswd = Entry(AdminFrame,width=15)
##        getenpasswd.grid(column=1, row=2)

        lbl = Label(AdminFrame, text="Enable\nPassword:").grid(column=0, row=2)
        getenpasswd = Entry(AdminFrame, bg='white', width=15, fg='grey')
        getenpasswd.grid(column=1, row=2)
        getenpasswd.insert(0, "==WARNING==")
        def handle_focus_in(_):
            if getenpasswd.cget('fg') != 'black':
                getenpasswd.delete(0, END)
                getenpasswd.config(fg='black')
        def handle_focus_out(_):
            if getenpasswd.get() == "":
                getenpasswd.delete(0, END)
                getenpasswd.config(fg='grey')
                getenpasswd.insert(0, "==WARNING==")
        getenpasswd.bind("<FocusOut>", handle_focus_out)
        getenpasswd.bind("<FocusIn>", handle_focus_in)

        def adduserpass():
            userN = "username " + getusername.get()
            passW = " secret " + getpasswd.get()
            cmd = userN + passW + "\n"
            cmd2 = "enable secret " + getenpasswd.get() + "\n"
            if chk_RO_acct.get() == True:
                cmd = userN + " privilege 2 " + passW + "\n"
            else:
                pass
            if chk_state_neg.get() == False:
                if getusername.get() != "" and getpasswd.get() != "":
                    remote_conn.send("conf t\n")
                    sleep(0.3)
                    remote_conn.send(cmd)
                    sleep(0.3)
                    if getenpasswd.get() != "" and getenpasswd.get() != "==WARNING==":
                        remote_conn.send(cmd2)
                        sleep(0.3)
                    else:
                        pass
                    tkMessageBox.showinfo('Login credential', 'Username and password has been configured.', parent=window)
                else:
                    tkMessageBox.showinfo('ERROR', 'Please enter both the username and password.', parent=window)

            else:
                if getusername.get() != "" and getpasswd.get() == "":
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("no " + userN + "\n")
                    sleep(0.3)
                    if getenpasswd.get() != "" and getenpasswd.get() != "==WARNING==":
                        remote_conn.send("no " + cmd2)
                        sleep(0.3)
                    else:
                        pass
                    tkMessageBox.showinfo('Login credential', 'User deleted.', parent=window)
                elif getpasswd.get() != "" and getusername.get() == "":
                    tkMessageBox.showinfo('ERROR', 'Please enter either username only, or both username and password to negate.', parent=window)
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.3)
                    remote_conn.send("no " + cmd)
                    if getenpasswd.get() != "":
                        remote_conn.send("no " + cmd2)
                    else:
                        pass
                    sleep(0.3)
                    tkMessageBox.showinfo('Login credential', 'Username and password deleted.', parent=window) 
            sleep(0.5)
            remote_conn.send("exit \n")
        btn = Button(AdminFrame, text="Aplicar", bg="orange", command=adduserpass)
        btn.grid(column=1, row=3)

        lbl = Label(AdminFrame, text="").grid(column=0, row=4)
        
        lbl = Label(AdminFrame, text="Add/Remove\n RO command:").grid(column=0, row=5)
        getpriv = Entry(AdminFrame, bg='white', width=15, fg='grey')
        getpriv.grid(column=1, row=5)
        getpriv.insert(0, "e.g. show run")
        def handle_focus_in(_):
            if getpriv.cget('fg') != 'black':
                getpriv.delete(0, END)
                getpriv.config(fg='black')
        def handle_focus_out(_):
            if getpriv.get() == "":
                getpriv.delete(0, END)
                getpriv.config(fg='grey')
                getpriv.insert(0, "e.g. show run")    
        getpriv.bind("<FocusOut>", handle_focus_out)
        getpriv.bind("<FocusIn>", handle_focus_in)

        def addpriv():
            if chk_state_neg.get() == False:
                if getpriv.get() == "":
                    tkMessageBox.showinfo('ERROR', 'Please enter command to add to Read-Only user.', parent=window)
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.3)
                    remote_conn.send("privilege exec level 2 " + getpriv.get() + "\n")
                    tkMessageBox.showinfo('Privilege level', 'Command added to RO users privilege.', parent=window)
            else:
                if getpriv.get() == "":
                    tkMessageBox.showinfo('ERROR', 'Please enter command to remove from Read-Only user.', parent=window)
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.3)
                    remote_conn.send("privilege exec level 9 " + getpriv.get() + "\n")
                    tkMessageBox.showinfo('Privilege level', 'Command removed from RO users privilege.', parent=window)
            sleep(0.3)
            remote_conn.send("exit \n")
        btn = Button(AdminFrame, text="Aplicar", bg="orange", command=addpriv)
        btn.grid(column=1, row=6)
        




        AdminFrame2=LabelFrame(window,text=" Other Admin Config ",font=('verdana', 8, 'bold'),padx=5,pady=5,width=100,height=100)
        AdminFrame2.grid(row=2,column=0, sticky=("nsew"))

        #lbl = Label(AdminFrame, text="Reload").grid(column=0, row=4)

        OPTIONS = [
        "in",        
        "at",
        "now"
        ]
        relodatetime = StringVar(AdminFrame2)
        relodatetime.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(AdminFrame2, relodatetime, *OPTIONS)   
        dropbox.grid(column=0, row=0)
        
        reloadmins = Entry(AdminFrame2, bg='white', width=25, fg='grey')
        reloadmins.grid(column=1, row=0)
        reloadmins.insert(0, "e.g. (in) 15, (at) 02:00 apr 21")
        def handle_focus_in(_):
            if reloadmins.cget('fg') != 'black':
                reloadmins.delete(0, END)
                reloadmins.config(fg='black')
        def handle_focus_out(_):
            if reloadmins.get() == "":
                reloadmins.delete(0, END)
                reloadmins.config(fg='grey')
                reloadmins.insert(0, "e.g. (in) 15, (at) 02:00 apr 21")    
        reloadmins.bind("<FocusOut>", handle_focus_out)
        reloadmins.bind("<FocusIn>", handle_focus_in)
        
        
        def relo():
            if chk_state_neg.get() == False:
                if relodatetime.get() == "in":
                    if reloadmins.get() == "" or reloadmins.get() == "e.g. (in) 15, (at) 02:00 apr 21":
                        tkMessageBox.showinfo('ERROR', 'Please enter a number of seconds till/when the reload command initiates.', parent=window)
                    else:
                        remote_conn.send("reload in " + reloadmins.get() + "\n")
                        sleep(0.3)
                        tkMessageBox.showinfo('Reload', 'This device will reload in ' + reloadmins.get() + ' minutes.', parent=window)
                elif relodatetime.get() == "at":
                    if reloadmins.get() == "" or reloadmins.get() == "e.g. (in) 15, (at) 02:00 apr 21":
                        tkMessageBox.showinfo('ERROR', 'Please enter a number of seconds till/when the reload command initiates.', parent=window)
                    else:
                        remote_conn.send("reload at " + reloadmins.get() + "\n")
                        sleep(0.3)
                        tkMessageBox.showinfo('Reload', 'This device will reload at ' + reloadmins.get() + '.', parent=window)
                else:
                    reloadconfirmation = "Proceed with reload"
                    buff_size = 16384
                    sleep(0.3)
                    remote_conn.send("reload \n")
                    sleep(0.3)
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 1024
                        sleep(0.3)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    if reloadconfirmation in output:
                        remote_conn.send("yes \n")
                    else:
                        pass
                    tkMessageBox.showinfo('Reload', 'Reload command sent.', parent=window)
            else:
                remote_conn.send("reload cancel \n")
                sleep(0.3)
                tkMessageBox.showinfo('Reload', 'Reload command canceled.', parent=window)
        btn = Button(AdminFrame2, text="Reload", bg="orange", command=relo)
        btn.grid(column=2, row=0, padx=3)


        OPTIONS = [
        "exec",        
        "login",
        "motd"
        ]
        banneropt = StringVar(AdminFrame2)
        banneropt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(AdminFrame2, banneropt, *OPTIONS)   
        dropbox.grid(column=0, row=2)

        bannerinput = Entry(AdminFrame2, width=25)
        bannerinput.grid(column=1, row=2, pady = 2)        
        
        def banner():
            if bannerinput.get() == "":
                tkMessageBox.showinfo('ERROR', 'Please enter banner text.', parent=window)
            else:
                remote_conn.send("conf t\n")
                sleep(0.3)                    
                remote_conn.send("banner " + reloadmins.get() + " " + bannerinput.get() + "\n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('Banner', 'Banner configured.', parent=window)
        btn = Button(AdminFrame2, text="Banner", bg="orange", command=banner)
        btn.grid(column=2, row=2, padx=2)        

        OPTIONS = [
        "DomainName",        
        "HostName",
        "NameServer",
        "Set Clock",
        "UpdateClock:SWtoHW",
        "UpdateClock:HWtoSW",
        "Set as NTP server",
        "NTP packet source",
        "use NTP server IP"
        ]
        dhnameopt = StringVar(AdminFrame2)
        dhnameopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(AdminFrame2, dhnameopt, *OPTIONS)   
        dropbox.grid(column=0, row=3)

        dhinput = Entry(AdminFrame2, width=25)
        dhinput.grid(column=1, row=3)
        
        def dhostname():
            if chk_state_neg() == False:
                if dhnameopt.get() == "DomainName":
                    if dhinput.get() == "":
                        tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.3)                    
                        remote_conn.send("ip domain name " + dhinput.get() + "\n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Configuration', 'Domain name configured.', parent=window)
                elif dhnameopt.get() == "HostName":
                    if dhinput.get() == "":
                        tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.3)                    
                        remote_conn.send("hostname " + dhinput.get() + "\n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Configuration', 'Host name configured.', parent=window)
                elif dhnameopt.get() == "NameServer":
                    if dhinput.get() == "":
                        tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.3)                    
                        remote_conn.send("ip name-server " + dhinput.get() + "\n")
                        sleep(0.3)
                        remote_conn.send("exit \n")                        
                        tkMessageBox.showinfo('Configuration', 'Name server configured.', parent=window)
                elif dhnameopt.get() == "Set Clock":
                    if dhinput.get() == "":
                        tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                    else:
                        remote_conn.send("clock set " + dhinput.get() + " \n")
                        sleep(0.3)
                        tkMessageBox.showinfo('Configuration', 'Clock time has been updated.', parent=window)                        
                elif dhnameopt.get() == "UpdateClock:SWtoHW":
                    remote_conn.send("clock update-calendar \n")
                    sleep(0.3)
                    tkMessageBox.showinfo('Configuration', 'Hardware clock updated from the Software clock.', parent=window)
                elif dhnameopt.get() == "UpdateClock:HWtoSW":
                    remote_conn.send("clock read-calendar \n")
                    sleep(0.3)                    
                    tkMessageBox.showinfo('Configuration', 'Software clock updated from the Hardware clock. (NOTE: Hardware clock runs even if the device is powered off or rebooted)', parent=window)                        
                elif dhnameopt.get() == "Set as NTP server":
                    remote_conn.send("conf t\n")
                    sleep(0.3)                    
                    remote_conn.send("ntp master " + dhinput.get() + "\n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Configuration', 'NTP master configured.', parent=window)
                elif dhnameopt.get() == "NTP packet source":
                    if dhinput.get() == "":
                        tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.3)                    
                        remote_conn.send("NTP source " + dhinput.get() + "\n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Configuration', 'NTP source configured.', parent=window)
                else:
                    if dhinput.get() == "":
                        tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.3)                    
                        remote_conn.send("NTP server " + dhinput.get() + "\n")
                        sleep(0.3)
                        remote_conn.send("exit \n")                        
                        tkMessageBox.showinfo('Configuration', 'Name server configured.', parent=window)
            else:
                if dhnameopt.get() == "DomainName":
                    remote_conn.send("conf t\n")
                    sleep(0.3)                    
                    remote_conn.send("no ip domain name \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Configuration', 'Domain name removed.', parent=window)
                elif dhnameopt.get() == "HostName":
                    remote_conn.send("conf t\n")
                    sleep(0.3)                    
                    remote_conn.send("no hostname \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Configuration', 'Host name removed.', parent=window)
                elif dhnameopt.get() == "NameServer":
                    if dhinput.get() == "":
                        tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.3)                    
                        remote_conn.send("no ip name-server " + dhinput.get() + "\n")
                        sleep(0.3)
                        remote_conn.send("exit \n")                        
                        tkMessageBox.showinfo('Configuration', 'Name server removed.', parent=window)
                elif dhnameopt.get() == "Set Clock":
                    tkMessageBox.showinfo('Configuration', 'Nothing to negate.', parent=window)                        
                elif dhnameopt.get() == "UpdateClock:SWtoHW":
                    tkMessageBox.showinfo('Configuration', 'Nothing to negate.', parent=window)
                elif dhnameopt.get() == "UpdateClock:HWtoSW":
                    tkMessageBox.showinfo('Configuration', 'Nothing to negate.', parent=window)
                elif dhnameopt.get() == "Set as NTP server":
                    remote_conn.send("conf t\n")
                    sleep(0.3)                    
                    remote_conn.send("no ntp master \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Configuration', 'Domain name configured.', parent=window)
                elif dhnameopt.get() == "NTP packet source":
                    remote_conn.send("conf t\n")
                    sleep(0.3)                    
                    remote_conn.send("no NTP source \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Configuration', 'Host name configured.', parent=window)
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.3)                    
                    remote_conn.send("no NTP server \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")                        
                    tkMessageBox.showinfo('Configuration', 'Name server configured.', parent=window)
        btn = Button(AdminFrame2, text="Aplicar", bg="orange", command=dhostname)
        btn.grid(column=2, row=3, padx=2) 
        
        
        AdminShowFrame=LabelFrame(window,text=" Show config ",font=('verdana', 8, 'bold'),padx=5,pady=5,width=100,height=68)
        AdminShowFrame.grid(row=3,column=0, sticky=("nsew"))

        OPTIONS = [
        "Scheduled reloads",
        "Users",
        "Domain Name",
        "Hostname",
        "Time (SW clock)",
        "Time (HW clock)",
        "NTP status",
        "NTP associations"
        ]
        showitem = StringVar(AdminShowFrame)
        showitem.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(AdminShowFrame, showitem, *OPTIONS)   
        dropbox.place(x=0, y=0)

      

        def shadmin():
            if showitem.get() == "Scheduled reloads":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show reload \n")
                sleep(3)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Reloads scheduled', output, parent=window)
            elif showitem.get() == "Users":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show run | i username \n")
                sleep(3)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('User accounts', output, parent=window)
            elif showitem.get() == "Domain Name":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show run | i domain name \n")
                sleep(3)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Domain Name', output, parent=window)
            elif showitem.get() == "Hostname":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show run | i hostname \n")
                sleep(3)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Hostname', output, parent=window)               
            elif showitem.get() == "Time (SW clock)":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show clock detail \n")
                sleep(3)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Time (SW clock)', output, parent=window)
            elif showitem.get() == "Time (HW clock)":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show calen \n")
                sleep(3)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Time (HW clock)', output, parent=window)
            elif showitem.get() == "NTP status":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show ntp status \n")
                sleep(3)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Network Time Protocol status', output, parent=window)
            else:
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show ntp assoc \n")
                sleep(3)         
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 1024
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Network Time Protocol associations', output, parent=window)
                
        btn = Button(AdminShowFrame, text="Show", bg="orange", command=shadmin)
        btn.place(x=280, y=5)        




    def authen():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("Authentication")
        window.geometry('550x300')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)
        print "add radius, tacacs"
        AAAframe=LabelFrame(window,text=" AAA ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        AAAframe.grid(row=0,column=0, sticky=("nsew"))
        
        eightzerotwoxframe=LabelFrame(window,text=" 802.1x ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        eightzerotwoxframe.grid(row=1,column=0, sticky=("nsew"))





    def HAvail():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("High Availability")
        window.geometry('550x352')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)

        negframe=LabelFrame(window,text=" Negate ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        negframe.grid(row=0,column=1)
        chk_state_neg = BooleanVar()
        chk_state_neg.set(False)
        chk1 = Checkbutton(negframe, variable=chk_state_neg)
        chk1.grid(column=1, row=0)

        LAGframe=LabelFrame(window,text=" Link Aggregation (LACP, PAGP, static Etherchannel) ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        LAGframe.grid(row=0,column=0, sticky=("nsew"))

        lbl = Label(LAGframe, text="Bundle ID:").grid(column=0, row=0)
        LAGgrp = Entry(LAGframe, width=6)
        LAGgrp.grid(column=1, row=0)
        
        lbl = Label(LAGframe, text="Applied ports:").grid(column=3, row=0)
        LAGports = Entry(LAGframe, bg='white', width=16, fg='grey')
        LAGports.grid(column=4, row=0, padx=2)
        LAGports.insert(0, "eg. +fa0/0+fa0/1..")
        def handle_focus_in(_):
            if LAGports.cget('fg') != 'black':
                LAGports.delete(0, END)
                LAGports.config(fg='black')
        def handle_focus_out(_):
            if LAGports.get() == "":
                LAGports.delete(0, END)
                LAGports.config(fg='grey')
                LAGports.insert(0, "eg. +fa0/0+fa0/1..")    
        LAGports.bind("<FocusOut>", handle_focus_out)
        LAGports.bind("<FocusIn>", handle_focus_in)
        
        
        lbl = Label(LAGframe, text="Bundle Type:").grid(column=0, row=1)
        OPTIONS = [
        "LACP",
        "PAGP",
        "Static"
        ]
        LAGtype = StringVar(LAGframe)
        LAGtype.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(LAGframe, LAGtype, *OPTIONS)   
        dropbox.grid(column=1, row=1)

        OPTIONS = [
        "Layer 2",
        "Layer 3"
        ]
        LAGlayer = StringVar(LAGframe)
        LAGlayer.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(LAGframe, LAGlayer, *OPTIONS)   
        dropbox.grid(column=3, row=1, padx=5)
        
        OPTIONS = [
        "Active",
        "Passive"
        ]
        LAGnegostate = StringVar(LAGframe)
        LAGnegostate.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(LAGframe, LAGnegostate, *OPTIONS)   
        dropbox.grid(column=4, row=1)


        
        
        lbl = Label(LAGframe, text="Optional:").grid(column=0, row=3)
        OPTIONS = [
        "LACP system-priority",
        "LACP port-priority",
        "PAGP port-priority",
        "PAGP learn-method"
        ]
        LAGotheropt = StringVar(LAGframe)
        LAGotheropt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(LAGframe, LAGotheropt, *OPTIONS)   
        dropbox.grid(column=1, row=3, columnspan=3)
 
        LAGother = Entry(LAGframe, bg='white', width=7, fg='grey')
        LAGother.grid(column=4, row=3, sticky='w')
        LAGother.insert(0, "value")
        def handle_focus_in(_):
            if LAGother.cget('fg') != 'black':
                LAGother.delete(0, END)
                LAGother.config(fg='black')
        def handle_focus_out(_):
            if LAGother.get() == "":
                LAGother.delete(0, END)
                LAGother.config(fg='grey')
                LAGother.insert(0, "value")    
        LAGother.bind("<FocusOut>", handle_focus_out)
        LAGother.bind("<FocusIn>", handle_focus_in)
        
        LAGother2 = Entry(LAGframe, bg='white', width=7, fg='grey')
        LAGother2.grid(column=4, row=3, sticky='e')        
        LAGother2.insert(0, "eg. fa0/0")
        def handle_focus_in(_):
            if LAGother2.cget('fg') != 'black':
                LAGother2.delete(0, END)
                LAGother2.config(fg='black')
        def handle_focus_out(_):
            if LAGother2.get() == "":
                LAGother2.delete(0, END)
                LAGother2.config(fg='grey')
                LAGother2.insert(0, "eg. fa0/0")    
        LAGother2.bind("<FocusOut>", handle_focus_out)
        LAGother2.bind("<FocusIn>", handle_focus_in)

        lbl = Label(LAGframe, text="Optional Load\n Balance method:").grid(column=0, row=4)        
        OPTIONS = [
        "src-mac",
        "dst-mac",
        "src-ip",
        "dst-ip",
        "src-dst-mac",
        "src-dst-ip"
        ]
        LAGtypeopt = StringVar(LAGframe)
        LAGtypeopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(LAGframe, LAGtypeopt, *OPTIONS)   
        dropbox.grid(column=1, row=4, columnspan=3)

        def LAG():
            if LAGports.get() != "":
                portlist = LAGports.get()
                ports = re.findall("[+]\w+\/\d+", portlist)
            else:
                pass

            LAGnegostate = LAGnegostate.get()
            if LAGtype.get() == "PAGP":
                if LAGnegostate == "Active":
                    LAGnegostate = "desirable"
                else:
                    LAGnegostate = "auto"
            elif LAGtype.get() == "Static":
                LAGnegostate = "on"
            else:
                pass
            
            if chk_state_neg.get() == False:
                if LAGgrp.get() == "" or (LAGports.get() == "" or LAGports.get() == "eg. +fa0/0+fa0/1.."):
                    tkMessageBox.showinfo('ERROR', 'Please enter both a bundle ID AND the ports/interfaces to be added to that bundle.', parent=window)
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.3)                    
                    remote_conn.send("int port-channel " + LAGgrp.get() + "\n")
                    sleep(0.3)
                    if LAGlayer.get() == "Layer 3":
                        remote_conn.send("no switchport \n")
                        sleep(0.3)
                    else:
                        pass
                    for p in ports:
                        remote_conn.send("int " + str(p[1:]) + "\n")
                        sleep(0.3)
                        remote_conn.send("channel-group " + LAGgrp.get() + " mode " + LAGnegostate + "\n")
                        sleep(0.3)
                    remote_conn.send("exit \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")                        
                    tkMessageBox.showinfo('LAG', 'LAG bundle created, and ports added to LAG bundle.', parent=window)
            else:
                if LAGgrp.get() == "":
                    tkMessageBox.showinfo('ERROR', 'Minimum information required is to enter a bundle ID (to be deleted).', parent=window)
                else:
                    if LAGports.get() == "" or LAGports.get() == "eg. +fa0/0+fa0/1..":
                        remote_conn.send("conf t\n")
                        sleep(0.3)                    
                        remote_conn.send("no int port-channel " + LAGgrp.get() + "\n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('LAG', 'LAG bundle deleted.', parent=window)
                    else:
                        for p in ports:
                            remote_conn.send("int " + str(p[1:]) + "\n")
                            sleep(0.3)
                            remote_conn.send("no channel-group " + LAGgrp.get() + "\n")
                            sleep(0.3)
                        remote_conn.send("exit \n")
                        sleep(0.3)
                        remote_conn.send("exit \n") 
                        tkMessageBox.showinfo('LAG', 'Port removed from LAG bundle.', parent=window)
        btn = Button(LAGframe, text="Aplicar", bg="orange", command=LAG)
        btn.grid(column=6, row=0, padx=7)
                    
        def LAGoptional():
            if LAGother.get() == "" or LAGother.get() == "value":
                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
            else:
                if chk_state_neg() == False:
                    if LAGotheropt.get() == "LACP system-priority":
                        remote_conn.send("conf t\n")
                        sleep(0.3)                    
                        remote_conn.send("lacp system-priority " + LAGother.get() + "\n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('LAG', 'LACP system-priority configured.', parent=window)
                    elif LAGotheropt.get() == "LACP port-priority":
                        if LAGother2.get() == "" or LAGother2.get() == "eg. fa0/0":
                            tkMessageBox.showinfo('ERROR', 'Please enter a port(interface).', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("interface " + LAGother2.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("lacp port-priority " + LAGother.get() + "\n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('LAG', 'LACP port-priority configured.', parent=window)
                    elif LAGotheropt.get() == "PAGP port-priority":
                        if LAGother2.get() == "" or LAGother2.get() == "eg. fa0/0":
                            tkMessageBox.showinfo('ERROR', 'Please enter a port(interface).', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("interface " + LAGother2.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("pagp port-priority " + LAGother.get() + "\n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('LAG', 'PAGP port-priority configured.', parent=window)                        
                    else:
                        if LAGother2.get() == "" or LAGother2.get() == "eg. fa0/0":
                            tkMessageBox.showinfo('ERROR', 'Please enter a port(interface).', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("interface " + LAGother2.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("pagp learn-method " + LAGother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('LAG', 'PAGP learn-method configured.', parent=window)
                else:
                    if LAGotheropt.get() == "LACP system-priority":
                        remote_conn.send("conf t\n")
                        sleep(0.3)                    
                        remote_conn.send("no lacp system-priority \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('LAG', 'LACP system-priority reset to default.', parent=window)
                    elif LAGotheropt.get() == "LACP port-priority":
                        if LAGother2.get() == "" or LAGother2.get() == "eg. fa0/0":
                            tkMessageBox.showinfo('ERROR', 'Please enter a port(interface).', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("interface " + LAGother2.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no lacp port-priority \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('LAG', 'LACP port-priority reset to default.', parent=window)
                    elif LAGotheropt.get() == "PAGP port-priority":
                        if LAGother2.get() == "" or LAGother2.get() == "eg. fa0/0":
                            tkMessageBox.showinfo('ERROR', 'Please enter a port(interface).', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("interface " + LAGother2.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no pagp port-priority \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('LAG', 'PAGP port-priority reset to default.', parent=window)                        
                    else:
                        if LAGother2.get() == "" or LAGother2.get() == "eg. fa0/0":
                            tkMessageBox.showinfo('ERROR', 'Please enter a port(interface).', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("interface " + LAGother2.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no pagp learn-method \n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('LAG', 'PAGP learn-method reset to default.', parent=window)
        btn = Button(LAGframe, text="Aplicar", bg="orange", command=LAGoptional)
        btn.grid(column=6, row=3)

        def LAGoptionalbalance():
            if chk_state_neg.get() == False:
                remote_conn.send("conf t\n")
                sleep(0.3)                    
                remote_conn.send("port-channel load-balance " + LAGtypeopt.get() + "\n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('LAG', 'LAG load-distribution method among the ports in the Etherchannel bundle configured.', parent=window)
            else:
                remote_conn.send("conf t\n")
                sleep(0.3)                    
                remote_conn.send("port-channel load-balance src-mac \n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('LAG', 'LAG load-distribution method among the ports in the Etherchannel bundle reset to default (src-mac).', parent=window) 
        btn = Button(LAGframe, text="Aplicar", bg="orange", command=LAGoptionalbalance)
        btn.grid(column=6, row=4)




        RGRframe=LabelFrame(window,text=" Router Gateway Redundancy (HSRP, VRRP) & Balancing (GLBP)",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        RGRframe.grid(row=1,column=0, sticky=("nsew"))

        lbl = Label(RGRframe, text="Protocol ID:").grid(column=0, row=0)
        RGRID = Entry(RGRframe, bg='white', width=24, fg='grey')
        RGRID.grid(column=1, row=0, padx=2)
        RGRID.insert(0, "v1: <0-255>, v2: <0-4095>")
        def handle_focus_in(_):
            if RGRID.cget('fg') != 'black':
                RGRID.delete(0, END)
                RGRID.config(fg='black')
        def handle_focus_out(_):
            if RGRID.get() == "":
                RGRID.delete(0, END)
                RGRID.config(fg='grey')
                RGRID.insert(0, "v1: <0-255>, v2: <0-4095>")    
        RGRID.bind("<FocusOut>", handle_focus_out)
        RGRID.bind("<FocusIn>", handle_focus_in)
       
        
        lbl = Label(RGRframe, text="Virtual IP:").grid(column=2, row=0)
        RGRvip = Entry(RGRframe, bg='white', width=10, fg='grey')
        RGRvip.grid(column=3, row=0, padx=2)
        RGRvip.insert(0, "x.x.x.x")
        def handle_focus_in(_):
            if RGRvip.cget('fg') != 'black':
                RGRvip.delete(0, END)
                RGRvip.config(fg='black')
        def handle_focus_out(_):
            if RGRvip.get() == "":
                RGRvip.delete(0, END)
                RGRvip.config(fg='grey')
                RGRvip.insert(0, "x.x.x.x")    
        RGRvip.bind("<FocusOut>", handle_focus_out)
        RGRvip.bind("<FocusIn>", handle_focus_in)


        lbl = Label(RGRframe, text="Protocol Type:").grid(column=0, row=1)
        OPTIONS = [
        "HSRP",
        "VRRP",
        "GLBP"
        ]
        RGRprotoopt = StringVar(RGRframe)
        RGRprotoopt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(RGRframe, RGRprotoopt, *OPTIONS)   
        dropbox.grid(column=1, row=1) 


        lbl = Label(RGRframe, text="Interface:").grid(column=2, row=1)
        RGRiface = Entry(RGRframe, bg='white', width=10, fg='grey')
        RGRiface.grid(column=3, row=1)
        RGRiface.insert(0, "eg. fa0/0")
        def handle_focus_in(_):
            if RGRiface.cget('fg') != 'black':
                RGRiface.delete(0, END)
                RGRiface.config(fg='black')
        def handle_focus_out(_):
            if RGRiface.get() == "":
                RGRiface.delete(0, END)
                RGRiface.config(fg='grey')
                RGRiface.insert(0, "eg. fa0/0")    
        RGRiface.bind("<FocusOut>", handle_focus_out)
        RGRiface.bind("<FocusIn>", handle_focus_in)


        lbl = Label(RGRframe, text="Optional:").grid(column=0, row=2)
        OPTIONS = [
        "Preempt",
        "Priority",
        "Track interface",
        "Version(HSRP)",
        "Timers",
        "Authentication",
        "Group name",
        "Follow group(HSRP)",
        "Weighting(GLBP)",
        "Weighting track(GLBP)",
        "Forwarder preempt(GLBP)",
        "Balance algorithm(GLBP)"
        ]
        RGRotheropt = StringVar(RGRframe)
        RGRotheropt.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(RGRframe, RGRotheropt, *OPTIONS)   
        dropbox.grid(column=1, row=2)



        def RGR():
            proto = RGRprotoopt.get()
            if RGRprotoopt.get() == "HSRP":
                proto = "standby"
            else:
                pass
            if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                tkMessageBox.showinfo('ERROR', 'Please enter an interface and Protocol ID.', parent=window)
            else:
                if chk_state_neg.get() == False:
                    if (RGRvip.get() == "" or RGRvip.get() == "x.x.x.x"):
                        tkMessageBox.showinfo('ERROR', 'Please enter a VirtualIP to act as the gateway.', parent=window)
                    else:
                        remote_conn.send("conf t\n")
                        sleep(0.3)
                        remote_conn.send("int " + RGRiface.get() + "\n")
                        sleep(0.3)
                        remote_conn.send(proto + " " + RGRID.get() + " ip " + RGRvip.get() + "\n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Gateway Redundancy', proto + ' configured for interface ' + RGRiface.get() + '.', parent=window)
                else:
                    remote_conn.send("conf t\n")
                    sleep(0.3)
                    remote_conn.send("int " + RGRiface.get() + "\n")
                    sleep(0.3)
                    remote_conn.send("no " + proto + " " + RGRID.get() + " \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('Gateway Redundancy', proto + ' deleted.', parent=window)
        btn = Button(RGRframe, text="Aplicar", bg="orange", command=RGR)
        btn.grid(column=6, row=0)


        def RGRoptional():
            if RGRother.get() == "" or RGRother.get() == "value":
                tkMessageBox.showinfo('ERROR', 'Please enter a value.', parent=window)
            else:
                if chk_state_neg.get() == False:
                    if RGRotheropt == "Preempt":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send(proto + " " + RGRID.get() + " preempt \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Preempt configured.', parent=window)
                    elif RGRotheropt == "Priority":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send(proto + " " + RGRID.get() + " priority " + RGRother.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Priority configured.', parent=window)
                    elif RGRotheropt == "Track interface":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send(proto + " " + RGRID.get() + " track " + RGRother.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")                  
                            tkMessageBox.showinfo('Gateway Redundancy', 'Interface tracking (and priority decrementing) configured.', parent=window)
                    elif RGRotheropt == "Version(HSRP)":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("standby Version " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)        
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Version configured.', parent=window)
                    elif RGRotheropt == "Timers":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send(proto + " " + RGRID.get() + " timers " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Timers configured.', parent=window)
                    elif RGRotheropt == "Authentication":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send(proto + " " + RGRID.get() + " authentication md5 key-string 0 " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Authentication configured.', parent=window)
                    elif RGRotheropt == "Group name":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send(proto + " " + RGRID.get() + " name " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Group name configured.', parent=window)
                    elif RGRotheropt == "Follow group(HSRP)":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send(proto + " " + RGRID.get() + " follow " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Configured to follow group name ' + RGRother.get() + '.', parent=window)
                    elif RGRotheropt == "Weighting(GLBP)":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("glbp " + RGRID.get() + " weighting " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)        
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'GLBP weighting configured.', parent=window)
                    elif RGRotheropt == "Weighting track(GLBP)":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("glbp " + RGRID.get() + " weighting track " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'GLBP weight tracking configured.', parent=window)
                    elif RGRotheropt == "Forwarder preempt(GLBP)":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("glbp " + RGRID.get() + " Forwarder preempt \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'GLBP forwarder preempt.', parent=window)
                    else:
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("glbp " + RGRID.get() + " load-balancing " + RGRother.get() + " \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('Gateway Redundancy', 'GLBP load-balancing algorithm configured.', parent=window)

                else:
                    if RGRotheropt == "Preempt":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no " + proto + " " + RGRID.get() + " preempt \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Preempt removed.', parent=window)
                    elif RGRotheropt == "Priority":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no " + proto + " " + RGRID.get() + " priority " + RGRother.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Priority deleted.', parent=window)
                    elif RGRotheropt == "Track interface":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no " + proto + " " + RGRID.get() + " track " + RGRother.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")                  
                            tkMessageBox.showinfo('Gateway Redundancy', 'Interface tracking deleted.', parent=window)
                    elif RGRotheropt == "Version(HSRP)":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no standby Version \n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)        
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Version reset to default (HSRPv1).', parent=window)
                    elif RGRotheropt == "Timers":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no " + proto + " " + RGRID.get() + " timers " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Timers removed.', parent=window)
                    elif RGRotheropt == "Authentication":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no " + proto + " " + RGRID.get() + " authentication md5 key-string 0 " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Authentication deleted.', parent=window)
                    elif RGRotheropt == "Group name":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no " + proto + " " + RGRID.get() + " name " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Group name deleted.', parent=window)
                    elif RGRotheropt == "Follow group(HSRP)":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no " + proto + " " + RGRID.get() + " follow " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'Follow group name deleted.', parent=window)
                    elif RGRotheropt == "Weighting(GLBP)":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no glbp weighting \n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)        
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'GLBP weighting reset.', parent=window)
                    elif RGRotheropt == "Weighting track(GLBP)":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no glbp " + RGRID.get() + " weighting track " + RGRother.get() + "\n")
                            sleep(0.3)  
                            remote_conn.send("exit \n")
                            sleep(0.3)                            
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'GLBP weight tracking reset.', parent=window)
                    elif RGRotheropt == "Forwarder preempt(GLBP)":
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("no glbp " + RGRID.get() + " Forwarder preempt \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")                            
                            tkMessageBox.showinfo('Gateway Redundancy', 'GLBP forwarder preempt disabled.', parent=window)
                    else:
                        if (RGRiface.get() == "" or RGRiface.get() == "eg. fa0/0") or (RGRID.get() == "" or RGRID.get() == "v1: <0-255>, v2: <0-4095>"):
                            tkMessageBox.showinfo('ERROR', 'Please also enter the Protocol ID and the interface it is enabled on.', parent=window)
                        else:
                            remote_conn.send("conf t\n")
                            sleep(0.3)
                            remote_conn.send("int " + RGRiface.get() + "\n")
                            sleep(0.3)
                            remote_conn.send("glbp " + RGRID.get() + " load-balancing \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            sleep(0.3)
                            remote_conn.send("exit \n")
                            tkMessageBox.showinfo('Gateway Redundancy', 'GLBP load-balancing algorithm reset to default (round robin).', parent=window)
        btn = Button(RGRframe, text="Aplicar", bg="orange", command=RGRoptional)
        btn.grid(column=6, row=2)






        ShowHAframe=LabelFrame(window,text=" Show/Clear Config ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        ShowHAframe.grid(row=3,column=0, sticky=("nsew"))
        
        OPTIONS = [
        "Etherchannel",
        "Etherchannel detail",
        "Etherchannel load-balance",
        "Etherchannel summary",
        "PAGP neighbor",
        "PAGP counters",
        "LACP neighbor",
        "LACP counters",
        "HSRP all",
        "HSRP brief",
        "HSRP neighbors",
        "VRRP",
        "VRRP brief",
        "GLBP",
        "GLBP brief"
        ]
        showHAitem = StringVar(ShowHAframe)
        showHAitem.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(ShowHAframe, showHAitem, *OPTIONS)   
        dropbox.grid(column=1, row=1)
        howHAinput = Entry(ShowHAframe,width=15)
        howHAinput.grid(column=2, row=1)
        def shHA():
            if showHAitem.get() == "Etherchannel":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh Etherchannel \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "Etherchannel detail":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh Etherchannel detail \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "Etherchannel load-balance":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh Etherchannel load-balance \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "Etherchannel summary":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh Etherchannel summary \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "PAGP neighbor":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh PAGP neighbor \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "PAGP counters":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh PAGP counters \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "LACP neighbor":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh LACP neighbor \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "LACP counters":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh LACP counters \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "HSRP brief":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh standby brief \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "HSRP all":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh standby all \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "HSRP neighbors":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh standby neigh \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "VRRP":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh vrrp \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "VRRP brief":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh vrrp brief \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)
            elif showHAitem.get() == "GLBP brief":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh glbp brief \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)                
            else:
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh glbp \n")
                sleep(0.5)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('High Availability', output, parent=window)   
        btn = Button(ShowHAframe, text="Show", bg="orange", command=shHA)
        btn.grid(column=3, row=1, padx=3)

        showHAhelpframe=LabelFrame(window,text=" Help ",font=('verdana', 8, 'bold'),padx=10,pady=10,width=100,height=100)
        showHAhelpframe.grid(column=1, row=1, rowspan = 2, sticky=("nsew"))

        def LAGhelp():
            tkMessageBox.showinfo('Help', '===LAG help===', parent=window)
        btn = Button(showHAhelpframe, text="LAG Help", bg="yellow", command=LAGhelp)
        btn.grid(column=0, row=0)

        def HSRPVRRPhelp():
            tkMessageBox.showinfo('Help', '===HSRPVRRP help===', parent=window)
        btn = Button(showHAhelpframe, text="HSRP/VRRP\n Help", bg="yellow", command=HSRPVRRPhelp)
        btn.grid(column=0, row=1)
        
        def GLBPhelp():
            tkMessageBox.showinfo('Help', '===GLBP help===', parent=window)
        btn = Button(showHAhelpframe, text="GLBP help", bg="yellow", command=GLBPhelp)
        btn.grid(column=0, row=2)

        
        
    def QoS():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("QoS Control")
        window.geometry('580x300')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)

        negframe=LabelFrame(window,text=" Negate ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        negframe.grid(row=0,column=1)
        chk_state_neg = BooleanVar()
        chk_state_neg.set(False)
        chk1 = Checkbutton(negframe, variable=chk_state_neg)
        chk1.grid(column=1, row=0)        

        basicqosframe=LabelFrame(window,text=" Basic QOS ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        basicqosframe.grid(row=0,column=0, sticky=("nsew"))        
        lbl = Label(basicqosframe, text="Interface:")
        lbl.grid(column=0, row=2)
        getiface = Entry(basicqosframe,width=15)
        getiface.grid(column=1, row=2)
        lbl = Label(basicqosframe, text="Basic rate limit (bits, burst, maxburst):")
        lbl.grid(column=0, row=3)
        getbits = Entry(basicqosframe,width=15)
        getbits.grid(column=1, row=3)
        getburst = Entry(basicqosframe,width=15)
        getburst.grid(column=2, row=3)
        getmaxburst = Entry(basicqosframe,width=15)
        getmaxburst.grid(column=3, row=3)
        def ratelimitclicked():
            if chk_state_neg.get() == False:
                remote_conn.send("conf t\n")
                sleep(0.5)
                remote_conn.send("int " + getiface.get() + "\n")
                sleep(0.5)
                remote_conn.send("rate-limit input " + getbits.get() + getburst.get() + getmaxburst.get() + " conform-action transmit exceed-action drop" + "\n")
                sleep(0.5)
                remote_conn.send("exit \n")
                sleep(0.5)
                remote_conn.send("exit \n")                
                res = "Rate Limit has been set to: " + (getbits.get()/1000000)
                tkMessageBox.showinfo('Rate Limit', res, parent=window)
            else:
                remote_conn.send("conf t\n")
                sleep(0.5)
                remote_conn.send("int " + getiface.get() + "\n")
                sleep(0.5)                
                remote_conn.send("no rate-limit input " + getbits.get() + getburst.get() + getmaxburst.get() + " conform-action transmit exceed-action drop" + "\n")
                sleep(0.5)
                remote_conn.send("exit \n")
                sleep(0.5)
                remote_conn.send("exit \n")
                res = "Rate Limit has been removed"
                tkMessageBox.showinfo('Rate Limit', res, parent=window)                
        btn = Button(basicqosframe, text="Aplicar", bg="orange", command=ratelimitclicked)
        btn.grid(column=1, row=4)


        
        Advancedqosframe=LabelFrame(window,text=" Advanced QOS (UNDER CONSTRUCTION) ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        Advancedqosframe.grid(row=1,column=0, sticky=("nsew"))
        
        lbl = Label(Advancedqosframe, text="Set CBWFQ:").grid(column=0, row=5)
        txt = Entry(Advancedqosframe,width=15)
        txt.grid(column=1, row=5)
        def CBWFQclicked():
            res = "CBWFQ id has been set to: " + txt.get()
            tkMessageBox.showinfo('CBWFQ', res, parent=window)
        btn = Button(Advancedqosframe, text="Aplicar", bg="orange", command=CBWFQclicked)
        btn.grid(column=1, row=6)

        blanklbl = Label(Advancedqosframe, text="").grid(column=1, row=7)
    
        lbl = Label(Advancedqosframe, text="Set LLQ (for VOIP):").grid(column=0, row=8)
        txt = Entry(Advancedqosframe,width=15)
        txt.grid(column=1, row=8)
        def LLQclicked():
            res = "LLQ has been set to: " + txt.get()
            tkMessageBox.showinfo('LLQ', res, parent=window)
        btn = Button(Advancedqosframe, text="Aplicar", bg="orange", command=LLQclicked)
        btn.grid(column=1, row=9)

        
    def security():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("IPSec & other crypto functions")
        window.geometry('560x720')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)

        negframe=LabelFrame(window,text=" Negate ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        negframe.grid(row=0,column=1)
        chk_state_neg = BooleanVar()
        chk_state_neg.set(False)
        chk1 = Checkbutton(negframe, variable=chk_state_neg)
        chk1.grid(column=0, row=0)

        
        ipsecframe=LabelFrame(window,text=" IPSEC (* == optional) ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        ipsecframe.grid(row=0,column=0, sticky=("nsew"))


        lbl = Label(ipsecframe, text="PHASE 1", font=('verdana', 7, 'bold')).grid(column=0, row=0, pady=1)
        OPTIONS = [
        "Encryption",
        "3des",        
        "aes"
        ]
        ipsec_enc = StringVar(ipsecframe)
        ipsec_enc.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(ipsecframe, ipsec_enc, *OPTIONS)   
        dropbox.place(x=141, y=19)

        OPTIONS = [
        "Hash",
        "md5",        
        "sha256",
        "sha384",
        "sha512"
        ]
        ipsec_hash = StringVar(ipsecframe)
        ipsec_hash.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(ipsecframe, ipsec_hash, *OPTIONS)   
        dropbox.place(x=244, y=19)

        OPTIONS = [
        "DH Group",
        "5",
        "14",
        "19",
        "20",
        "21",
        "24"
        ]
        ipsec_dh = StringVar(ipsecframe)
        ipsec_dh.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(ipsecframe, ipsec_dh, *OPTIONS)   
        dropbox.place(x=317, y=19)
        
        blanklbl = Label(ipsecframe).grid(column=0, row=1, pady=5)

        lbl = Label(ipsecframe, text="PolicyID:").grid(column=0, row=1)
        PolicyID = Entry(ipsecframe, bg='white', width=9, fg='grey')
        PolicyID.grid(column=1, row=1)
        PolicyID.insert(0, "eg. 1")
        def handle_focus_in(_):
            if PolicyID.cget('fg') != 'black':
                PolicyID.delete(0, END)
                PolicyID.config(fg='black')
        def handle_focus_out(_):
            if PolicyID.get() == "":
                PolicyID.delete(0, END)
                PolicyID.config(fg='grey')
                PolicyID.insert(0, "eg. 1")    
        PolicyID.bind("<FocusOut>", handle_focus_out)
        PolicyID.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(ipsecframe, text="PSK:").grid(column=0, row=2)
        pskentry = Entry(ipsecframe, bg='white', width=9, fg='grey')
        pskentry.grid(column=1, row=2)
        pskentry.insert(0, "password")
        def handle_focus_in(_):
            if pskentry.cget('fg') != 'black':
                pskentry.delete(0, END)
                pskentry.config(fg='black')
        def handle_focus_out(_):
            if pskentry.get() == "":
                pskentry.delete(0, END)
                pskentry.config(fg='grey')
                pskentry.insert(0, "password")    
        pskentry.bind("<FocusOut>", handle_focus_out)
        pskentry.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(ipsecframe, text="Peer:").grid(column=2, row=2)
        PeerIDentry = Entry(ipsecframe, bg='white', width=22, fg='grey')
        PeerIDentry.grid(column=3, row=2, padx=2)
        PeerIDentry.insert(0, "eg. 0.0.0.0, MyPeerID")
        def handle_focus_in(_):
            if PeerIDentry.cget('fg') != 'black':
                PeerIDentry.delete(0, END)
                PeerIDentry.config(fg='black')
        def handle_focus_out(_):
            if PeerIDentry.get() == "":
                PeerIDentry.delete(0, END)
                PeerIDentry.config(fg='grey')
                PeerIDentry.insert(0, "eg. 0.0.0.0, MyPeerID")    
        PeerIDentry.bind("<FocusOut>", handle_focus_out)
        PeerIDentry.bind("<FocusIn>", handle_focus_in)

        lbl = Label(ipsecframe, text="*Life:").grid(column=4, row=2)
        lifep1 = Entry(ipsecframe, bg='white', width=9, fg='grey')
        lifep1.grid(column=5, row=2, sticky='w')
        lifep1.insert(0, "eg. 3600")
        def handle_focus_in(_):
            if lifep1.cget('fg') != 'black':
                lifep1.delete(0, END)
                lifep1.config(fg='black')
        def handle_focus_out(_):
            if lifep1.get() == "":
                lifep1.delete(0, END)
                lifep1.config(fg='grey')
                lifep1.insert(0, "eg. 3600")    
        lifep1.bind("<FocusOut>", handle_focus_out)
        lifep1.bind("<FocusIn>", handle_focus_in)
        
        def IPSECp1():
            if chk_state_neg.get() == False:
                if PolicyID.get() == "" or PolicyID.get() == "eg. 1" or pskentry.get() == "" or pskentry.get() == "password" or PeerIDentry.get() == "" or \
                   PeerIDentry.get() == "eg. 0.0.0.0, MyPeerID":
                    tkMessageBox.showinfo('Error', 'Please enter all required information.', parent=window)
                elif ipsec_enc.get() == "Encryption" or ipsec_hash.get() == "Hash" or ipsec_dh.get() == "DH Group":
                    tkMessageBox.showinfo('Error', 'Please choose Encryption, Hash snd DH Group option.', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.2)
                    remote_conn.send("crypto isakmp policy " + PolicyID.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("encr " + ipsec_enc.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("hash " + ipsec_hash.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("authentication pre-share \n")
                    sleep(0.2)
                    remote_conn.send("group " + ipsec_dh.get() + "\n")
                    sleep(0.2)
                    if lifep1.get() != "" and lifep1.get() != "eg. 3600":
                        remote_conn.send("lifetime " + lifep1.get() + "\n")
                        sleep(0.2)
                    else:
                        pass
                    remote_conn.send("crypto isakmp key " + pskentry.get() + " address " + PeerIDentry.get() + " \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('IPSEC Phase 1', 'Phase 1 ISAKMP policy has been configured.', parent=window)

            else:
                if PolicyID.get() == "" or PolicyID.get() == "eg. 1":
                    tkMessageBox.showinfo('Error', 'Please enter a PolicyID to delete it.', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.2)
                    remote_conn.send("no crypto isakmp policy " + PolicyID.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('IPSEC Phase 1', 'Phase 1 ISAKMP policy has been deleted.', parent=window)
        btn = Button(ipsecframe, text="Aplicar", bg="orange", command=IPSECp1)
        btn.place(x=417, y=19)
        


        
        lbl = Label(ipsecframe, text="PHASE 2", font=('verdana', 7, 'bold')).grid(column=0, row=3, pady=5)

        lbl = Label(ipsecframe, text="ProfileName:").grid(column=0, row=4)
        ipsecProfileName = Entry(ipsecframe, bg='white', width=9, fg='grey')
        ipsecProfileName.grid(column=1, row=4, padx=2)
        ipsecProfileName.insert(0, "eg. ipsec1")
        def handle_focus_in(_):
            if ipsecProfileName.cget('fg') != 'black':
                ipsecProfileName.delete(0, END)
                ipsecProfileName.config(fg='black')
        def handle_focus_out(_):
            if ipsecProfileName.get() == "":
                ipsecProfileName.delete(0, END)
                ipsecProfileName.config(fg='grey')
                ipsecProfileName.insert(0, "eg. ipsec1")    
        ipsecProfileName.bind("<FocusOut>", handle_focus_out)
        ipsecProfileName.bind("<FocusIn>", handle_focus_in)

        OPTIONS = [
        "Transform-Set",
        "ESP-AES 256",
        "esp-sha512-hmac",
        "ESP-AES-256-SHA-512",
        "ah-sha512-hmac"
        ]
        ipsec_transform_set = StringVar(ipsecframe)
        ipsec_transform_set.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(ipsecframe, ipsec_transform_set, *OPTIONS)   
        dropbox.place(x=141, y=92)

        OPTIONS = [
        "Mode",
        "Transport",        
        "Tunnel"
        ]
        ipsec_mode = StringVar(ipsecframe)
        ipsec_mode.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(ipsecframe, ipsec_mode, *OPTIONS)   
        dropbox.place(x=263, y=92)


        lbl = Label(ipsecframe, text="*Idle:").grid(column=0, row=5, pady=4)
        idlep2 = Entry(ipsecframe, bg='white', width=9, fg='grey')
        idlep2.grid(column=1, row=5)
        idlep2.insert(0, "eg. 3600")
        def handle_focus_in(_):
            if idlep2.cget('fg') != 'black':
                idlep2.delete(0, END)
                idlep2.config(fg='black')
        def handle_focus_out(_):
            if idlep2.get() == "":
                idlep2.delete(0, END)
                idlep2.config(fg='grey')
                idlep2.insert(0, "eg. 3600")    
        idlep2.bind("<FocusOut>", handle_focus_out)
        idlep2.bind("<FocusIn>", handle_focus_in)

        lbl = Label(ipsecframe, text="*PFS:").grid(column=2, row=5)
        PFSp2 = Entry(ipsecframe, bg='white', width=11, fg='grey')
        PFSp2.grid(column=3, row=5)
        PFSp2.insert(0, "eg. group14")
        def handle_focus_in(_):
            if PFSp2.cget('fg') != 'black':
                PFSp2.delete(0, END)
                PFSp2.config(fg='black')
        def handle_focus_out(_):
            if PFSp2.get() == "":
                PFSp2.delete(0, END)
                PFSp2.config(fg='grey')
                PFSp2.insert(0, "eg. group14")    
        PFSp2.bind("<FocusOut>", handle_focus_out)
        PFSp2.bind("<FocusIn>", handle_focus_in)

        lbl = Label(ipsecframe, text="*Life:").grid(column=4, row=5)
        lifep2 = Entry(ipsecframe, bg='white', width=19, fg='grey')
        lifep2.grid(column=5, row=5)
        lifep2.insert(0, "eg. 3600s, 3days, 3MB")
        def handle_focus_in(_):
            if lifep2.cget('fg') != 'black':
                lifep2.delete(0, END)
                lifep2.config(fg='black')
        def handle_focus_out(_):
            if lifep2.get() == "":
                lifep2.delete(0, END)
                lifep2.config(fg='grey')
                lifep2.insert(0, "eg. 3600s, 3days, 3MB")    
        lifep2.bind("<FocusOut>", handle_focus_out)
        lifep2.bind("<FocusIn>", handle_focus_in)

        def IPSECp2():
            if chk_state_neg.get() == False:
                if ipsecProfileName.get() == "" or ipsecProfileName.get():
                    tkMessageBox.showinfo('Error', 'Please enter an IPSEC Profile Name.', parent=window)
                elif ipsec_transform_set.get() == "Transform-Set" or ipsec_mode.get() == "Mode":
                    tkMessageBox.showinfo('Error', 'Please choose Transform-Set snd Mode.', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.2)
                    remote_conn.send("crypto ipsec transform-set " + ipsec_transform_set.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("mode " + ipsec_mode.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("crypto ipsec profile " + ipsecProfileName.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("set transform-set " + ipsec_transform_set.get() + "\n")
                    sleep(0.2)

                    if idlep2.get() != "" and idlep2.get() != "eg. 3600":
                        remote_conn.send("set security-assoc idle-time " + idlep2.get() + "\n")
                        res = 'Idle-time configured. '
                    else:
                        pass
                    if lifep2.get() != "" and lifep2.get() != "eg. 3600s, 3days, 3MB":
                        remote_conn.send("set security-assoc lifetime " + lifep2.get() + "\n")
                        res = res + 'Life-time configured. '
                    else:
                        pass
                    if PFSp2.get() != "" and PFSp2.get() != "eg. group14":
                        remote_conn.send("set pfs " + PFSp2.get() + "\n")
                        res = res + 'PFS configured. '
                    else:
                        pass
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('IPSEC Phase 2', 'Phase 2 IPSEC policy has been configured. ' + res, parent=window)

            else:
                if ipsecProfileName.get() == "" or ipsecProfileName.get() == "eg. 1":
                    tkMessageBox.showinfo('Error', 'Please enter a Profile Name.', parent=window)
                else:
                    remote_conn.send("conf t \n")
                    sleep(0.2)
                    if ipsec_transform_set.get() == "Transform-Set" and idlep2.get() == "" and idlep2.get() == "eg. 3600" and PFSp2.get() == "" and PFSp2.get() == "eg. group14" and \
                       lifep2.get() == "" and lifep2.get() == "eg. 3600s, 3days, 3MB":
                        remote_conn.send("no crypto ipsec profile " + ipsecProfileName.get() + "\n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('IPSEC Phase 2', 'Phase 2 IPSEC policy has been deleted.', parent=window)
                    else:
                        if ipsec_transform_set.get() != "Transform-Set":
                            remote_conn.send("no crypto ipsec transform-set \n")
                            res = 'Transform-Set deleted. '
                        else:
                            pass
                        if idlep2.get() != "" and idlep2.get() != "eg. 3600":
                            remote_conn.send("crypto ipsec profile " + ipsecProfileName.get() + "\n")
                            sleep(0.2)
                            remote_conn.send("no set security-assoc idle-time \n")
                            sleep(0.2)
                            remote_conn.send("exit \n")
                            res = res + 'Idle-time deleted. '
                        else:
                            pass
                        if lifep2.get() != "" and lifep2.get() != "eg. 3600s, 3days, 3MB":
                            remote_conn.send("crypto ipsec profile " + ipsecProfileName.get() + "\n")
                            sleep(0.2)
                            remote_conn.send("no set security-assoc lifetime \n")
                            sleep(0.2)
                            remote_conn.send("exit \n")
                            res = res + 'Life-time deleted. '
                        else:
                            pass
                        if PFSp2.get() != "" and PFSp2.get() != "eg. group14":
                            remote_conn.send("crypto ipsec profile " + ipsecProfileName.get() + "\n")
                            sleep(0.2)
                            remote_conn.send("no set pfs \n")
                            sleep(0.2)
                            remote_conn.send("exit \n")
                            res = res + 'PFS deleted. '
                        else:
                            pass
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('IPSEC Phase 2', res, parent=window)
        btn = Button(ipsecframe, text="Aplicar", bg="orange", command=IPSECp2)
        btn.place(x=417, y=92)

        





        dmvpnframe=LabelFrame(window,text=" DMVPN (* == optional, ** == spoke only) ",font=('verdana', 8, 'bold'),padx=10,pady=15,width=100,height=100)
        dmvpnframe.grid(row=1,column=0, sticky=("nsew"))
        
        lbl = Label(dmvpnframe, text="Interface:").grid(column=0, row=0)
        dmvpntuniface = Entry(dmvpnframe,bg='white', width=8, fg='grey')
        dmvpntuniface.place(x=56, y=0)
        dmvpntuniface.insert(0, "eg. tun0")
        def handle_focus_in(_):
            if dmvpntuniface.cget('fg') != 'black':
                dmvpntuniface.delete(0, END)
                dmvpntuniface.config(fg='black')
        def handle_focus_out(_):
            if dmvpntuniface.get() == "":
                dmvpntuniface.delete(0, END)
                dmvpntuniface.config(fg='grey')
                dmvpntuniface.insert(0, "eg. tun0")    
        dmvpntuniface.bind("<FocusOut>", handle_focus_out)
        dmvpntuniface.bind("<FocusIn>", handle_focus_in)

        chk_dyn_mcast = BooleanVar()
        chk_dyn_mcast.set(True)
        chk1 = Checkbutton(dmvpnframe, text="Dynamic Multicast", variable=chk_dyn_mcast)
        chk1.place(x=120, y=0)

        lbl = Label(dmvpnframe, text="Map:").grid(column=0, row=1)
        dmvpnmap = Entry(dmvpnframe,bg='white', width=31, fg='grey')
        dmvpnmap.grid(column=1, row=1)
        dmvpnmap.insert(0, "<remote_tunIP> <remote_pubIP>")
        def handle_focus_in(_):
            if dmvpnmap.cget('fg') != 'black':
                dmvpnmap.delete(0, END)
                dmvpnmap.config(fg='black')
        def handle_focus_out(_):
            if dmvpnmap.get() == "":
                dmvpnmap.delete(0, END)
                dmvpnmap.config(fg='grey')
                dmvpnmap.insert(0, "<remote_tunIP> <remote_pubIP>")    
        dmvpnmap.bind("<FocusOut>", handle_focus_out)
        dmvpnmap.bind("<FocusIn>", handle_focus_in)

        lbl = Label(dmvpnframe, text="Mcast Map:").place(x=250, y=20)
        dmvpnmapmcast = Entry(dmvpnframe,bg='white', width=15, fg='grey')
        dmvpnmapmcast.place(x=320, y=20)
        dmvpnmapmcast.insert(0, "<remote_pubIP>")
        def handle_focus_in(_):
            if dmvpnmapmcast.cget('fg') != 'black':
                dmvpnmapmcast.delete(0, END)
                dmvpnmapmcast.config(fg='black')
        def handle_focus_out(_):
            if dmvpnmapmcast.get() == "":
                dmvpnmapmcast.delete(0, END)
                dmvpnmapmcast.config(fg='grey')
                dmvpnmapmcast.insert(0, "<remote_pubIP>")
        dmvpnmapmcast.bind("<FocusOut>", handle_focus_out)
        dmvpnmapmcast.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(dmvpnframe, text="**NHS:").grid(column=0, row=2)
        dmvpnNHS = Entry(dmvpnframe,bg='white', width=15, fg='grey')
        dmvpnNHS.place(x=56, y=43)
        dmvpnNHS.insert(0, "<remote_tunIP>")
        def handle_focus_in(_):
            if dmvpnNHS.cget('fg') != 'black':
                dmvpnNHS.delete(0, END)
                dmvpnNHS.config(fg='black')
        def handle_focus_out(_):
            if dmvpnNHS.get() == "":
                dmvpnNHS.delete(0, END)
                dmvpnNHS.config(fg='grey')
                dmvpnNHS.insert(0, "<remote_tunIP>")
        dmvpnNHS.bind("<FocusOut>", handle_focus_out)
        dmvpnNHS.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(dmvpnframe, text="*Hold:").grid(column=0, row=3)
        dmvpnHold = Entry(dmvpnframe,bg='white', width=7, fg='grey')
        dmvpnHold.place(x=56, y=63)
        dmvpnHold.insert(0, "eg. 10")
        def handle_focus_in(_):
            if dmvpnHold.cget('fg') != 'black':
                dmvpnHold.delete(0, END)
                dmvpnHold.config(fg='black')
        def handle_focus_out(_):
            if dmvpnHold.get() == "":
                dmvpnHold.delete(0, END)
                dmvpnHold.config(fg='grey')
                dmvpnHold.insert(0, "eg. 10")    
        dmvpnHold.bind("<FocusOut>", handle_focus_out)
        dmvpnHold.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(dmvpnframe, text="*Timeout:").place(x=110, y=63)
        dmvpnRegistrationTimeout = Entry(dmvpnframe,bg='white', width=7, fg='grey')
        dmvpnRegistrationTimeout.place(x=168, y=63)
        dmvpnRegistrationTimeout.insert(0, "eg. 10")
        def handle_focus_in(_):
            if dmvpnRegistrationTimeout.cget('fg') != 'black':
                dmvpnRegistrationTimeout.delete(0, END)
                dmvpnRegistrationTimeout.config(fg='black')
        def handle_focus_out(_):
            if dmvpnRegistrationTimeout.get() == "":
                dmvpnRegistrationTimeout.delete(0, END)
                dmvpnRegistrationTimeout.config(fg='grey')
                dmvpnRegistrationTimeout.insert(0, "eg. 10")    
        dmvpnRegistrationTimeout.bind("<FocusOut>", handle_focus_out)
        dmvpnRegistrationTimeout.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(dmvpnframe, text="*Net_ID:").place(x=220, y=63)
        dmvpnNetID = Entry(dmvpnframe,bg='white', width=5, fg='grey')
        dmvpnNetID.place(x=268, y=63)
        dmvpnNetID.insert(0, "eg. 1")
        def handle_focus_in(_):
            if dmvpnNetID.cget('fg') != 'black':
                dmvpnNetID.delete(0, END)
                dmvpnNetID.config(fg='black')
        def handle_focus_out(_):
            if dmvpnNetID.get() == "":
                dmvpnNetID.delete(0, END)
                dmvpnNetID.config(fg='grey')
                dmvpnNetID.insert(0, "eg. 1")    
        dmvpnNetID.bind("<FocusOut>", handle_focus_out)
        dmvpnNetID.bind("<FocusIn>", handle_focus_in)
        
        lbl = Label(dmvpnframe, text="*Auth:").place(x=324, y=63)
        dmvpnAuth = Entry(dmvpnframe,bg='white', width=9, fg='grey')
        dmvpnAuth.place(x=362, y=63)
        dmvpnAuth.insert(0, "Password")
        def handle_focus_in(_):
            if dmvpnAuth.cget('fg') != 'black':
                dmvpnAuth.delete(0, END)
                dmvpnAuth.config(fg='black')
        def handle_focus_out(_):
            if dmvpnAuth.get() == "":
                dmvpnAuth.delete(0, END)
                dmvpnAuth.config(fg='grey')
                dmvpnAuth.insert(0, "Password")    
        dmvpnAuth.bind("<FocusOut>", handle_focus_out)
        dmvpnAuth.bind("<FocusIn>", handle_focus_in)


        chk_shortcut = BooleanVar()
        chk_shortcut.set(True)
        chk1 = Checkbutton(dmvpnframe, text="*NHRP shortcut(all)", variable=chk_shortcut)
        chk1.grid(column=1, row=4)

        chk_redirect = BooleanVar()
        chk_redirect.set(True)
        chk1 = Checkbutton(dmvpnframe, text="*NHRP redirect(hub only)", variable=chk_redirect)
        chk1.grid(column=3, row=4)




        
        def dmvpnclick():
            if dmvpntuniface.get() == "" or dmvpntuniface.get() == "eg. tun0":
                tkMessageBox.showinfo('Error', 'Please enter a tunnel interface to Aplicar DMVPN configuration on.', parent=window)
            else:
                if chk_state_neg.get() == False:
                    res = ""
                    remote_conn.send("conf t \n")
                    sleep(0.2)
                    remote_conn.send("int tun " + dmvpntuniface.get() + "\n")
                    sleep(0.2)
                    if dmvpnmap.get() != "" and dmvpnmap.get() != "<remote_tunIP> <remote_pubIP>":
                        remote_conn.send("ip nhrp map " + dmvpnmap.get() + "\n")
                        sleep(0.2)
                    else:
                        pass
                    if chk_dyn_mcast.get() == False:
                        remote_conn.send("ip nhrp map multicast " + dmvpnmapmcast.get() + "\n")
                    else:
                        remote_conn.send("ip nhrp map multicast dynamic \n")
                    sleep(0.2)
                    if dmvpnNHS.get() != "" and dmvpnNHS.get() != "<remote_tunIP>":
                        remote_conn.send("ip nhrp nhs " + dmvpnNHS.get() + "\n")
                        sleep(0.2)
                        res = res + "NHS configured. "
                    else:
                        pass
                    if dmvpnHold.get() != "" and dmvpnHold.get() != "eg. 10":
                        remote_conn.send("ip nhrp holdtime " + dmvpnHold.get() + "\n")
                        sleep(0.2)
                        res = res + "NHRP holdtime configured. "
                    else:
                        pass
                    if dmvpnRegistrationTimeout.get() != "" and dmvpnRegistrationTimeout.get() != "eg. 10":
                        remote_conn.send("ip nhrp registration timeout " + dmvpnRegistrationTimeout.get() + "\n")
                        sleep(0.2)
                        res = res + "NHRP registration timeout configured. "
                    else:
                        pass
                    if dmvpnNetID.get() != "" and dmvpnNetID.get() != "eg. 1":
                        remote_conn.send("ip nhrp network-id " + dmvpnNetID.get() + "\n")
                        sleep(0.2)
                        res = res + "NHRP network-id configured. "
                    else:
                        pass
                    if dmvpnAuth.get() != "" and dmvpnAuth.get() != "Password":
                        remote_conn.send("ip nhrp authentication " + dmvpnAuth.get() + "\n")
                        sleep(0.2)
                        res = res + "NHRP authentication configured. "
                    else:
                        pass
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('DMVPN', 'DMVPN configured. ' + res, parent=window)
                else:
                    res = ""
                    remote_conn.send("conf t \n")
                    sleep(0.2)
                    remote_conn.send("int tun " + dmvpntuniface.get() + "\n")
                    sleep(0.2)
                    if dmvpnmap.get() != "" and dmvpnmap.get() != "<remote_tunIP> <remote_pubIP>":
                        remote_conn.send("no ip nhrp map " + dmvpnmap.get() + "\n")
                        sleep(0.2)
                    else:
                        pass
                    if chk_dyn_mcast.get() == False:
                        remote_conn.send("no ip nhrp map multicast " + dmvpnmapmcast.get() + "\n")
                    else:
                        remote_conn.send("no ip nhrp map multicast dynamic \n")
                    sleep(0.2)
                    if dmvpnNHS.get() != "" and dmvpnNHS.get() != "<remote_tunIP>":
                        remote_conn.send("no ip nhrp nhs " + dmvpnNHS.get() + "\n")
                        sleep(0.2)
                        res = res + "NHS deleted. "
                    else:
                        pass
                    if dmvpnHold.get() != "" and dmvpnHold.get() != "eg. 10":
                        remote_conn.send("no ip nhrp holdtime \n")
                        sleep(0.2)
                        res = res + "NHRP holdtime reset. "
                    else:
                        pass
                    if dmvpnRegistrationTimeout.get() != "" and dmvpnRegistrationTimeout.get() != "eg. 10":
                        remote_conn.send("no ip nhrp registration timeout \n")
                        sleep(0.2)
                        res = res + "NHRP registration timeout reset. "
                    else:
                        pass
                    if dmvpnNetID.get() != "" and dmvpnNetID.get() != "eg. 1":
                        remote_conn.send("no ip nhrp network-id \n")
                        sleep(0.2)
                        res = res + "NHRP network-id deleted. "
                    else:
                        pass
                    if dmvpnAuth.get() != "" and dmvpnAuth.get() != "Password":
                        remote_conn.send("no ip nhrp authentication \n")
                        sleep(0.2)
                        res = res + "NHRP authentication deleted. "
                    else:
                        pass
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('DMVPN', 'DMVPN configured. ' + res, parent=window)
        btn = Button(dmvpnframe, text="Aplicar", bg="orange", command=dmvpnclick)
        btn.place(x=417, y=0)
        

      







        KeyMGMTframe=LabelFrame(window,text=" Key Management ",font=('verdana', 8, 'bold'),padx=10,pady=15,width=100,height=100)
        KeyMGMTframe.grid(row=2,column=0, sticky=("nsew"))
        lbl = Label(KeyMGMTframe, text="Generate Key:").grid(column=0, row=0, pady=7)

        blanklbl = Label(KeyMGMTframe, text="").grid(column=9, row=9, padx=93)

        OPTIONS = [
        "Key Type",
        "RSA",
        "EC"
        ]
        keyaction = StringVar(KeyMGMTframe)
        keyaction.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(KeyMGMTframe, keyaction, *OPTIONS)   
        dropbox.place(x=100, y=0)

        OPTIONS = [
        "Modulus",
        "256(EC)",
        "384(EC)",
        "1028(RSA)",
        "2048(RSA)",
        "4096(RSA)"
        ]
        keymod = StringVar(KeyMGMTframe)
        keymod.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(KeyMGMTframe, keymod, *OPTIONS)   
        dropbox.place(x=195, y=0)

        def generatekey():
            if chk_state_neg.get() == False:
                remote_conn.send("conf t \n")
                sleep(0.2)
                if keyaction.get() == "RSA":
                    remote_conn.send("crypto key generate rsa modulus " + keymod.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("y \n")
                else:
                    remote_conn.send("crypto key ec keysize " + keymod.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("y \n")
                sleep(0.2)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('Key Import/Export', 'Crypto key.', parent=window)
        btn = Button(KeyMGMTframe, text="Aplicar", bg="orange", command=generatekey)
        btn.place(x=417, y=0)






        blanklbl = Label(KeyMGMTframe).grid(column=0, row=1)







        lbl = Label(KeyMGMTframe, text="Create KeyChain:").grid(column=0, row=2, pady=6)
        keychainname = Entry(KeyMGMTframe, bg='white', width=15, fg='grey')
        keychainname.grid(column=1, row=2) 
        keychainname.insert(0, "keychain_name")
        def handle_focus_in(_):
            if keychainname.cget('fg') != 'black':
                keychainname.delete(0, END)
                keychainname.config(fg='black')
        def handle_focus_out(_):
            if keychainname.get() == "":
                keychainname.delete(0, END)
                keychainname.config(fg='grey')
                keychainname.insert(0, "keychain_name")    
        keychainname.bind("<FocusOut>", handle_focus_out)
        keychainname.bind("<FocusIn>", handle_focus_in)


        keynumber = Entry(KeyMGMTframe, bg='white', width=8, fg='grey')
        keynumber.grid(column=2, row=2, padx=2)
        keynumber.insert(0, "key_no.")
        def handle_focus_in(_):
            if keynumber.cget('fg') != 'black':
                keynumber.delete(0, END)
                keynumber.config(fg='black')
        def handle_focus_out(_):
            if keynumber.get() == "":
                keynumber.delete(0, END)
                keynumber.config(fg='grey')
                keynumber.insert(0, "key_no.")    
        keynumber.bind("<FocusOut>", handle_focus_out)
        keynumber.bind("<FocusIn>", handle_focus_in)




        def option_changed_keychainoption(*args):
            if keychainoption.get() == "Key-string":
                text = 'Password'
                keyvalue.delete(0, END)
                keyvalue.config(fg='grey')
                keyvalue.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if keyvalue.cget('fg') != 'black':
                        keyvalue.delete(0, END)
                        keyvalue.config(fg='black')
                def handle_focus_out(_):
                    if keyvalue.get() == "":
                        keyvalue.delete(0, END)
                        keyvalue.config(fg='grey')
                        keyvalue.insert(0, text)
                keyvalue.bind("<FocusOut>", handle_focus_out)
                keyvalue.bind("<FocusIn>", handle_focus_in)
            else:
                text = 'eg. 00:00:00 Jun 13 2008 23:59:59 Sep 12 2008'
                keyvalue.delete(0, END)
                keyvalue.config(fg='grey')
                keyvalue.insert(0, text)
                window.focus_set()
                def handle_focus_in(_):
                    if keyvalue.cget('fg') != 'black':
                        keyvalue.delete(0, END)
                        keyvalue.config(fg='black')
                def handle_focus_out(_):
                    if keyvalue.get() == "":
                        keyvalue.delete(0, END)
                        keyvalue.config(fg='grey')
                        keyvalue.insert(0, text)
                keyvalue.bind("<FocusOut>", handle_focus_out)
                keyvalue.bind("<FocusIn>", handle_focus_in)                
        
        OPTIONS = [
        "Key-string",
        "Accept-Life",
        "Send-Life"
        ]
        keychainoption = StringVar(KeyMGMTframe)
        keychainoption.set(OPTIONS[0])    # default value
        keychainoption.trace("w", option_changed_keychainoption)
        dropbox = OptionMenu(KeyMGMTframe, keychainoption, *OPTIONS)   
        dropbox.place(x=90, y=84)
        keyvalue = Entry(KeyMGMTframe,bg='white', width=40, fg='grey')
        keyvalue.place(x=193, y=91)
        keyvalue.config(font=("TkDefaultFont", 8))
        keyvalue.insert(0, "Password")
        def handle_focus_in(_):
            if keyvalue.cget('fg') != 'black':
                keyvalue.delete(0, END)
                keyvalue.config(fg='black')
        def handle_focus_out(_):
            if keyvalue.get() == "":
                keyvalue.delete(0, END)
                keyvalue.config(fg='grey')
                keyvalue.insert(0, "Password")    
        keyvalue.bind("<FocusOut>", handle_focus_out)
        keyvalue.bind("<FocusIn>", handle_focus_in)


        def createkchain():
            if keychainname.get() == "" or keychainname.get() == "keychain_name":
                tkMessageBox.showinfo('Error', 'Please enter keychain name.', parent=window)
            else:
                res = ""
                if chk_state_neg.get() == False:
                    remote_conn.send("conf t \n")
                    sleep(0.2)
                    remote_conn.send("key chain" + keychainname.get() + "\n")
                    sleep(0.2)
                    remote_conn.send("key " + keynumber.get() + "\n")
                    sleep(0.2)
                    if keychainoption.get() == "Key-string":
                        cmd = "key-string " + keyvalue.get() + "\n"
                        res = "Crypto key-string configured. "
                    elif keychainoption.get() == "Accept-Life":
                        cmd = "accept-Life local " + keyvalue.get() + "\n"
                        res = "Crypto accept-Life configured. "
                    elif keychainoption.get() == "Send-Life":
                        cmd = "send-lifetime local " + keyvalue.get() + "\n"
                        res = "Crypto send-lifetime configured. "
                    else:
                        pass
                    remote_conn.send(cmd)
                    sleep(0.2)                
                    remote_conn.send("exit \n")
                    sleep(0.2)                
                    remote_conn.send("exit \n")
                    sleep(0.2)                
                    remote_conn.send("exit \n")
                else:
                    if (keynumber.get() == "" or keynumber.get() == "keynumber") and (keyvalue.get() == "" or keyvalue.get() == "eg. 00:00:00 Jun 13 2008 23:59:59 Sep 12 2008" or \
                                                                                      keyvalue.get() == "Password"):
                        remote_conn.send("conf t \n")
                        sleep(0.2)
                        remote_conn.send("no key chain" + keychainname.get() + "\n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Crypto key chain', 'Crypto keychain deleted.', parent=window)
                    elif (keynumber.get() != "" and keynumber.get() != "keynumber") and (keyvalue.get() == "" \
                                                                                or keyvalue.get() == "eg. 00:00:00 Jun 13 2008 23:59:59 Sep 12 2008" or keyvalue.get() == "Password"):
                        remote_conn.send("conf t \n")
                        sleep(0.2)
                        remote_conn.send("key chain" + keychainname.get() + "\n")
                        sleep(0.2)
                        remote_conn.send("no key " + keynumber.get() + "\n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Crypto key chain', 'Crypto keyID deleted from keychain.', parent=window)
                    else:
                        remote_conn.send("conf t \n")
                        sleep(0.2)
                        remote_conn.send("key chain" + keychainname.get() + "\n")
                        sleep(0.2)
                        remote_conn.send("key " + keynumber.get() + "\n")
                        sleep(0.2)
                        if keychainoption.get() == "Key-string":
                            cmd = "no key-string \n"
                            res = "Crypto key-string deleted. "
                        elif keychainoption.get() == "Accept-Life":
                            cmd = "no accept-Life \n"
                            res = "Crypto accept-lifetime removed. "
                        elif keychainoption.get() == "Send-Life":
                            cmd = "no send-lifetime \n"
                            res = "Crypto send-lifetime removed. "
                        else:
                            pass
                        remote_conn.send(cmd)
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Crypto key chain', 'Crypto keychain configured. ' + res, parent=window)
        btn = Button(KeyMGMTframe, text="Aplicar", bg="orange", command=createkchain)
        btn.place(x=417, y=60)





        

        hardeningframe=LabelFrame(window,text=" Hardening ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        hardeningframe.grid(row=3,column=0, sticky=("nsew"))
        lbl = Label(hardeningframe, text="Storm Control(L2):").grid(column=0, row=0)
        lbl = Label(hardeningframe, text="dhcp snooping(L3):").grid(column=0, row=1)        
        lbl = Label(hardeningframe, text="DAI(L3):").grid(column=0, row=2)        
        lbl = Label(hardeningframe, text="IPSG(L3):").grid(column=0, row=3)        
        lbl = Label(hardeningframe, text="URPF(L3):").grid(column=0, row=4)
        lbl = Label(hardeningframe, text="Stateful Firewall(L4):").grid(column=0, row=5) 




        showframe=LabelFrame(window,text=" Show Crypto ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        showframe.grid(row=6,column=0, sticky=("nsew"))

        OPTIONS = [
        "Listening ports",
        "Crypto RSA keys",
        "ISAKMP SA (Phase1)",
        "ISAKMP policy",
        "ISAKMP profile",
        "IPSEC SA (Phase2)",
        "IPSEC policy",
        "IPSEC profile",
        "IPSEC traffic",
        "IPSEC sessions",
        "DMVPN",
        "NHRP",
        "NHRP traffic",
        "Clear Dynamic NHRP"
        ]
        showcryptocmd = StringVar(showframe)
        showcryptocmd.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(showframe, showcryptocmd, *OPTIONS)   
        dropbox.grid(column=1, row=1)
        shcrypto = Entry(showframe,width=15)
        shcrypto.place(x=187, y=5)
        def shcryptoclicked():
            if showcryptocmd.get() == "IPSEC SA (Phase2)":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh crypto ipsec sa \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Crypto Phase2 SA', output, parent=window)
            elif showcryptocmd.get() == "IPSEC policy":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh crypto ipsec policy \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('IPSEC policy', output, parent=window) 
            elif showcryptocmd.get() == "IPSEC profile":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh crypto ipsec profile \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('IPSEC profile', output, parent=window) 
                
            elif showcryptocmd.get() == "IPSEC traffic":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh crypto engine connection active \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('IPSEC traffic', output, parent=window)                
            elif showcryptocmd.get() == "ISAKMP SA (Phase1)":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh crypto isakmp sa \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Crypto Phase1 SA', output, parent=window)
            elif showcryptocmd.get() == "ISAKMP policy":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh crypto ISAKMP policy \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Crypto ISAKMP policy', output, parent=window)
            elif showcryptocmd.get() == "ISAKMP profile":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh crypto ISAKMP profile \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Crypto ISAKMP profile', output, parent=window)
            elif showcryptocmd.get() == "IPSEC sessions":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh crypto session \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Crypto session status', output, parent=window)                
            elif showcryptocmd.get() == "Crypto RSA keys":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh crypto key mypubkey rsa \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('RSA keys', output, parent=window)                
            elif showcryptocmd.get() == "Listening ports":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh control-plane host open-ports \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Opened ports', output, parent=window)
            elif showcryptocmd.get() == "DMVPN":
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh dmvpn \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('DMVPN', output, parent=window)
            else:
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("sh ip nhrp \n")
                sleep(0.5)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('NHRP', output, parent=window)
        btn = Button(showframe, text="Show", bg="orange", command=shcryptoclicked)
        btn.place(x=417, y=0)

        
        helpframe=LabelFrame(window,text="Help",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
        helpframe.grid(row=3,column=1, sticky=("nsew"), rowspan=2)
        
        def helpipsec():
            res = '-- IPSEC --\n ' +\
                  ' EDIT.'
            tkMessageBox.showinfo('IPSEC help', res, parent=window)
        btn = Button(helpframe, text="IPSEC", bg="yellow", command=helpipsec)
        btn.grid(column=0, row=0)

        def helpdmvpn():
            res = '-- DMVPN --\n ' +\
                  ' EDIT.'
            tkMessageBox.showinfo('DMVPN help', res, parent=window)
        btn = Button(helpframe, text="DMVPN", bg="yellow", command=helpdmvpn)
        btn.grid(column=0, row=1)

        def helpkeychain():
            res = '-- KeyChain --\n ' +\
                  ' EDIT.'
            tkMessageBox.showinfo('DMVPN help', res, parent=window)
        btn = Button(helpframe, text="Key", bg="yellow", command=helpkeychain)
        btn.grid(column=0, row=2)



        

    def pbrsla():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("PBR/SLA tracking (UNDER CONSTRUCTION)")
        window.geometry('550x300')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)
        label1 = Label(window, text="UNDER CONSTRUCTION").grid(row=0,column=0) 
        
    def pfr():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("Performance Routing (UNDER CONSTRUCTION)")
        window.geometry('550x300')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)
        label1 = Label(window, text="UNDER CONSTRUCTION").grid(row=0,column=0) 

    def mpls():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("MPLS (UNDER CONSTRUCTION)")
        window.geometry('550x300')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)
        label1 = Label(window, text="UNDER CONSTRUCTION").grid(row=0,column=0) 

    def CLI():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("CLI manual command")
        window.geometry('350x200')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)

        CLIframe=LabelFrame(window,text=" Command Line ",font=('verdana', 8, 'bold'),padx=40,pady=6,width=100,height=100)
        CLIframe.grid(row=0,column=0)

        getCLIinput = Entry(CLIframe, width=40)
        getCLIinput.grid(column=0, row=0)

        def CLIclick():
            if getCLIinput.get() == "":
                tkMessageBox.showinfo('ERROR', 'Please enter command.', parent=window)
            else:
                cmd = getCLIinput.get()
                buff_size = 16384
                sleep(0.5)
                remote_conn.send(cmd + "\n")
                sleep(3)
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('CLI', output, parent=window) 
        btn = Button(CLIframe, text="Aplicar", bg="orange", command=CLIclick)
        btn.grid(column=1, row=0, padx=5)



        
    def EEM():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("Cisco Event Manager (UNDER CONSTRUCTION)")
        window.geometry('550x300')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)
        label1 = Label(window, text="UNDER CONSTRUCTION").grid(row=0,column=0)
        
    def debugg():
        window = Toplevel()
        window.attributes('-topmost', 'true')
        window.title("Debug")
        window.geometry('450x150')
        menu = Menu(window)
        new_item = Menu(menu, tearoff=0)


        debugframe=LabelFrame(window,text=" Debugger ",font=('verdana', 8, 'bold'),padx=40,pady=6,width=100,height=100)
        debugframe.grid(row=7,column=0)


        debugdividerlbl1 = Label(debugframe, text="").grid(row=0,column=0)   
        debugdividerlbl2 = Label(debugframe, text="").grid(row=1,column=0)    
        OPTIONS = [
        "ip packet detail",
        "ip mpacket",
        "ip ICMP",
        "ip IGMP",
        "ip routing ",
        "ip mrouting",
        "ip RIP",
        "ip EIGRP",
        "ip OSPF adj",
        "ip OSPF hello",    
        "ip OSPF events",
        "ip OSPF packet",
        "ip BGP events",
        "ip BGP ipv4 unicast",
        "ip BGP ipv4 multicast",
        "ip BGP ipv6 unicast",
        "ip BGP ipv6 multicast",
        "ip BGP vpnv4 unicast", 
        "ip BGP mpls",    
        "ip BGP all",    
        "ip DHCP server events",
        "ip NAT",
        "ARP",
        "NTP events",
        "NTP packets",    
        "SNMP packets",
        "crypto IPSEC",
        "crypto ISAKMP",
        "standby",
        "VRRP",
        "GLBP",
        "etherchannel",
        "spanning-tree all",
        "spanning-tree events",    
        "RADIUS",
        "TACACS",    
        "tunnel",
        "MPLS adj",
        "MPLS events",
        "MPLS packets",
        "MPLS traffic-eng tunnels events",
        "MPLS traffic-eng link-management events",
        "MPLS traffic-eng link-management igp-neigh",
        "MPLS traffic-eng traffic-eng path lookup",
        "VLAN encap",
        "VLAN packets",
        ]
        getdebug = StringVar(debugframe)
        getdebug.set(OPTIONS[0])    # default value
        dropbox = OptionMenu(debugframe, getdebug, *OPTIONS)   
        dropbox.place(x=45, y=3)
        
        debugpktacl = Label(debugframe, text="Optional ACL for 'ip packet':")    
        debugpktacl.grid(column=0, row=20)
        debugpktacltxt = Entry(debugframe,width=15)
        debugpktacltxt.grid(column=1, row=20)            
        def showdebug():
            if remote_conn.recv_ready():
                tkMessageBox.showinfo('Debug enabled', 'Debugging enabled. Syslog enabled locally. CTRL+C to stop.', parent=window)
                remote_conn.send("conf t \n")
                sleep(0.2)
                remote_conn.send("logging host" + localip + "\n")
                sleep(0.2)
                remote_conn.send("logging trap 7 \n")
                sleep(0.2)
                remote_conn.send("logging rate-limit all 15 \n")    #generate 15 msgs every sec
                sleep(0.2)            
                remote_conn.send("service timestamps debug datetime show-timezone localtime year \n")
                sleep(0.2)
                remote_conn.send("service timestamps log datetime show-timezone localtime year \n")
                sleep(0.2)            
                remote_conn.send("do debug" + getdebug.get() + " " + debugpktacltxt.get() + " \n")
                sleep(0.2)                        
                cmd = ['python simplesyslogserver.py']
                subprocess.call(cmd, stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell=True)
                sleep(1)            
                remote_conn.send("logging trap 6 \n")
                sleep(0.2)
                remote_conn.send("do no debug all \n")
                sleep(0.2)            
                remote_conn.send("exit \n")
                sleep(0.2)            
        btn = Button(debugframe, text="Debug", bg="orange", command=showdebug)
        btn.grid(column=2, row=20, padx=11) 





        
    new_item.add_command(label='Route', command=route)
    new_item.add_separator()
    new_item.add_command(label='Switch', command=switch)
    new_item.add_separator()
    new_item.add_command(label='DHCP', command=DHCP)
    new_item.add_separator()
    new_item.add_command(label='ACL', command=ACL)
    new_item.add_separator()
    new_item.add_command(label='NAT', command=NAT)
    new_item.add_separator()
    new_item.add_command(label='Monitoring', command=monitoring)
   

    
    administration.add_command(label='Administration', command=admin)
    administration.add_separator()
    administration.add_command(label='Authentication', command=authen)


    advanced.add_command(label='HA', command=HAvail)
    advanced.add_separator()
    advanced.add_command(label='QoS', command=QoS)
    advanced.add_separator()  
    advanced.add_command(label='Security', command=security)
    advanced.add_separator()  
    advanced.add_command(label='PBR/SLA', command=pbrsla)
    advanced.add_separator()
    advanced.add_command(label='PFR', command=pfr)
    advanced.add_separator()
    advanced.add_command(label='MPLS', command=mpls)
    

    cli.add_command(label='CLI', command=CLI)
    cli.add_command(label='EEM', command=EEM)

    debug.add_command(label='Debug', command=debugg)
        
    menu.add_cascade(label='Basic', menu=new_item)
    menu.add_cascade(label='Administration', menu=administration)
    menu.add_cascade(label='Advanced', menu=advanced)
    menu.add_cascade(label='CLI & EEM', menu=cli)
    menu.add_cascade(label='Debug', menu=debug) 
    window.config(menu=menu)




def defaultpage():


    
    Negateanyframe=LabelFrame(window,text=" Negar ",font=('verdana', 8, 'bold'),padx=30,pady=7,width=100,height=100)
    Negateanyframe.grid(row=0,column=1, pady=10)
    
    chk_state_neg = BooleanVar()
    chk_state_neg.set(False)
    chk1 = Checkbutton(Negateanyframe, variable=chk_state_neg)
    chk1.grid(column=0, row=0)


    bifacemain=LabelFrame(window,text=" Interfaz (requerida para *, opcional para **) ",font=('verdana', 8, 'bold'),padx=122,pady=10,width=100,height=100)
    bifacemain.grid(row=0,column=0, sticky=("nsew"))
    
    

    getiface = Entry(bifacemain, bg='white', width=37, fg='grey')
    getiface.grid(column=0, row=0)
    getiface.insert(0, "e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..")
    def handle_focus_in(_):
        if getiface.cget('fg') != 'black':
            getiface.delete(0, END)
            getiface.config(fg='black')
    def handle_focus_out(_):
        if getiface.get() == "":
            getiface.delete(0, END)
            getiface.config(fg='grey')
            getiface.insert(0, "e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..")    
    getiface.bind("<FocusOut>", handle_focus_out)
    getiface.bind("<FocusIn>", handle_focus_in)

    biface=LabelFrame(window,text=" Configuración de interfaz ",font=('verdana', 8, 'bold'),padx=17,pady=0,width=100,height=100)
    biface.grid(row=1,column=0, sticky=("nsew"))


    chk_state_sec = BooleanVar()
    chk_state_sec.set(False)
    chk = Checkbutton(biface, text='IP secundaria', variable=chk_state_sec)
    chk.grid(column=2, row=2)

    chk_state_nosh = BooleanVar()
    chk_state_nosh.set(True)
    chk1 = Checkbutton(biface, text='Habilitar', variable=chk_state_nosh)
    chk1.grid(column=3, row=2)




    lbl = Label(biface, text="Establecer IP y máscara de subred:")
    lbl.grid(column=0, row=3)
    ipaddr = Entry(biface, bg='white', width=17, fg='grey')
    ipaddr.grid(column=1, row=3)
    ipaddr.insert(0, "IP. 'del' para eliminar.")
    def handle_focus_in(_):
        if ipaddr.cget('fg') != 'black':
            ipaddr.delete(0, END)
            ipaddr.config(fg='black')
    def handle_focus_out(_):
        if ipaddr.get() == "":
            ipaddr.delete(0, END)
            ipaddr.config(fg='grey')
            ipaddr.insert(0, "IP. 'del' para eliminar.")    
    ipaddr.bind("<FocusOut>", handle_focus_out)
    ipaddr.bind("<FocusIn>", handle_focus_in) 
    
    ipmask = Entry(biface, bg='white', width=17, fg='grey')
    ipmask.grid(column=2, row=3)
    ipmask.insert(0, "Máscara de subred. 'del' para eliminar.")
    def handle_focus_in(_):
        if ipmask.cget('fg') != 'black':
            ipmask.delete(0, END)
            ipmask.config(fg='black')
    def handle_focus_out(_):
        if ipmask.get() == "":
            ipmask.delete(0, END)
            ipmask.config(fg='grey')
            ipmask.insert(0, "Máscara de subred. 'del' para eliminar.")    
    ipmask.bind("<FocusOut>", handle_focus_out)
    ipmask.bind("<FocusIn>", handle_focus_in)

    
    lbl = Label(biface, text="Establecer origen / destino del túnel:")
    lbl.grid(column=0, row=4, pady=4)
    tunsrc = Entry(biface, bg='white', width=17, fg='grey')
    tunsrc.grid(column=1, row=4)
    tunsrc.insert(0, "Src IP. 'del' para eliminar.")
    def handle_focus_in(_):
        if tunsrc.cget('fg') != 'black':
            tunsrc.delete(0, END)
            tunsrc.config(fg='black')
    def handle_focus_out(_):
        if tunsrc.get() == "":
            tunsrc.delete(0, END)
            tunsrc.config(fg='grey')
            tunsrc.insert(0, "Src IP. 'del' para eliminar.")    
    tunsrc.bind("<FocusOut>", handle_focus_out)
    tunsrc.bind("<FocusIn>", handle_focus_in)
    
    tundst = Entry(biface, bg='white', width=17, fg='grey')
    tundst.grid(column=2, row=4)
    tundst.insert(0, "Dst IP. 'del' para eliminar.")
    def handle_focus_in(_):
        if tundst.cget('fg') != 'black':
            tundst.delete(0, END)
            tundst.config(fg='black')
    def handle_focus_out(_):
        if tundst.get() == "":
            tundst.delete(0, END)
            tundst.config(fg='grey')
            tundst.insert(0, "Dst IP. 'del' para eliminar.")    
    tundst.bind("<FocusOut>", handle_focus_out)
    tundst.bind("<FocusIn>", handle_focus_in)

    
    OPTIONS = [
    "Modo",        
    "GRE",
    "GRE mpoint",
    "IPIP",
    "MPLS TE"
    ]
    tunmode = StringVar(biface)
    tunmode.set(OPTIONS[0])    # default value
    dropbox = OptionMenu(biface, tunmode, *OPTIONS)
    dropbox.place(x=410, y=50)

    def setinterfaceipclick():
        bridgetxt = ""
        ipaddrcmd = "ip address " + ipaddr.get() + " " + ipmask.get()
        
        if getiface.get() == "" or getiface.get() == "e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..":
            tkMessageBox.showinfo('Error', 'Elija una interfaz.')
        else:
            if ((ipaddr.get() != "" and ipaddr.get().encode("utf-8") != "IP. 'del' para eliminar.") and (ipmask.get() == "" or ipmask.get().encode("utf-8") == "Máscara de subred. 'del' para eliminar."))\
               or ((ipaddr.get() == "" or ipaddr.get().encode("utf-8") == "IP. 'del' para eliminar.") and (ipmask.get() != "" and ipmask.get().encode("utf-8") != "Máscara de subred. 'del' para eliminar.")):
                tkMessageBox.showinfo('Error', 'Ingrese tanto la IP como la máscara de subred para configurar la IP.')
            elif chk_state_neg.get() == False and (getiface.get()[:2] == "tu") and ((tunsrc.get() != "" and tunsrc.get() != "Src IP. 'del' para eliminar.") or\
                 (tundst.get() != "" and tundst.get().encode("utf-8") != "Dst IP. 'del' para eliminar.")) and tunmode.get().encode("utf-8") == 'Modo':
                tkMessageBox.showinfo('Error', 'Seleccione un modo de túnel antes de agregar IP de túnel.')
            elif chk_state_neg.get() == False and (ipaddr.get() == "del" or ipmask.get() == "del" or tunsrc.get() == "del" or tundst.get() == "del"):
                tkMessageBox.showinfo('Error', 'Seleccione Negar para especificar "del" para la eliminación de direcciones IP.')
            else:
                if chk_state_neg.get() == False:

##                    if "fa" in getiface.get() or "gi" in getiface.get() or "te" in getiface.get():
##                        remote_conn.send("sh ip int " + getiface.get() + " \n")
##                        sleep(0.5)
##                        output = remote_conn.recv(2048).decode("utf-8")
##                        sleep(0.5)
##                        stripp = output.strip()
##                        sleep(0.2)
##                        if 'Invalid input' in stripp:
##                            tkMessageBox.showinfo('Error', 'The interface ' + getiface.get() + ' does not exist... Aborting. If BVI, ensure the Bridge Group has been created first.')
##                            return
##                        else:
##                            pass
##                    elif "bvi" in getiface.get():
##                        remote_conn.send("sh ip int " + getiface.get() + " \n")
##                        sleep(0.5)
##                        output = remote_conn.recv(2048).decode("utf-8")
##                        sleep(0.5)
##                        stripp = output.strip()
##                        sleep(0.2)
##                        if 'Invalid input' in stripp:
##                            tkMessageBox.showinfo('Error', 'The interface ' + getiface.get() + ' does not exist... Aborting. If BVI, ensure the Bridge Group has been created first.')
##                            return
##                        else:
##                            pass


                    
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    
##                    if "bvi" in getiface.get():
##                        
##                        bridgegrpid = getiface.get().split("bvi",1)[1]
##                        remote_conn.send("bridge irb \n")
##                        sleep(0.3)
##                        remote_conn.send("bridge " + bridgegrpid + " protocol ieee \n")
##                        sleep(0.3)
##                        remote_conn.send("bridge " + bridgegrpid + " route ip \n")
##                        bridgetxt = "The Bridge Group ID has been automatically created if it does not already exist - IRB type, with spanning tree enabled and routing capability. "
##                    else:
##                        pass



                    
                    remote_conn.send("int " + getiface.get() + "\n")
                    sleep(0.3)

                    output = remote_conn.recv(2048).decode("utf-8")
                    sleep(1)
                    stripp = output.strip()
                    sleep(0.2)
                    if 'Invalid input' in stripp:
                        sleep(0.2)
                        remote_conn.send("exit \n")
                        tkMessageBox.showinfo('Error', 'La interfaz ' + getiface.get() + ' no existe ... Abortando. Si es BVI, asegúrese de que el Grupo Bridge se haya creado primero.')
                        return
                    else:
                        pass
                    
                    tuntxt = ""
                    if (getiface.get()[:2] == "tu") and ((tunsrc.get() != "" and tunsrc.get().encode("utf-8") != "Src IP. 'del' para eliminar.") or\
                                                         (tundst.get() != "" and tundst.get().encode("utf-8") != "Dst IP. 'del' para eliminar.")):
                       
                        if tunmode.get() == 'GRE':
                            gettunmode = "tun mo gre ip"
                        elif tunmode.get() == 'GRE mpoint':
                            gettunmode = "tun mo gre multi"
                        elif tunmode.get() == 'IPIP':
                            gettunmode = "tun mo ipip"
                        else:
                            gettunmode = "tun mo mpls traffic-e"
                        remote_conn.send(gettunmode + "\n")
                        sleep(0.3)
                        remote_conn.send("tun so " + tunsrc.get() + "\n")
                        sleep(0.3)                        
                        remote_conn.send("tun dest " + tundst.get() + "\n")
                        sleep(0.3)
                        tuntxt = "IP de túnel configurada: no olvide agregar una ruta para impulsar el tráfico a través de este túnel. "                           
                    else:
                        pass

##                    sectxt = ""
##                    if chk_state_sec.get() == True:
##                        ipaddrcmd = ipaddrcmd + " secondary"
##                        if (ipaddr.get() != "" and ipaddr.get() != "IP. 'del' para eliminar.") and (ipmask.get() != "" and \
##                            ipmask.get() != "Máscara de subred. 'del' para eliminar."):
##                            sectxt = "IP is secondary. "
##                    else:
##                        pass

                    IPtxt = ""
                    if (ipaddr.get() != "" and ipaddr.get().encode("utf-8") != "IP. 'del' para eliminar.") and (ipmask.get() != "" and \
                        ipmask.get().encode("utf-8") != "Máscara de subred. 'del' para eliminar."):
                        if chk_state_sec.get() == False:
                            remote_conn.send(ipaddrcmd + "\n")
                            sleep(0.3)
                            IPtxt = "IP configurado. "
                        else:
                            remote_conn.send(ipaddrcmd + " secondary \n")
                            sleep(0.3)
                            IPtxt = "IP secundaria configurada. "
                    else:
                        pass

                    Shutstatetxt = ""
                    if chk_state_nosh.get() == False:
                        sleep(0.3)
                        remote_conn.send("sh \n")
                        sleep(0.3)
                        Shutstatetxt = "La interfaz está deshabilitada. "
                    else:
                        sleep(0.3)
                        remote_conn.send("no sh \n")
                        sleep(0.3)
                        Shutstatetxt = "La interfaz está habilitada. "

                    sleep(0.2)    
                    remote_conn.send("exit \n")
                    sleep(0.2)
                    remote_conn.send("exit \n") 
                    tkMessageBox.showinfo('Configuración IP', IPtxt + Shutstatetxt + tuntxt + bridgetxt)


                else:
                    if (ipaddr.get() == "" or ipaddr.get().encode("utf-8") == "IP. 'del' para eliminar.") and (ipmask.get() == "" or ipmask.get().encode("utf-8") == "Máscara de subred. 'del' para eliminar.") \
                       and (tunsrc.get() == "" or tunsrc.get().encode("utf-8") == "Src IP. 'del' para eliminar.") and (tundst.get() == "" or tundst.get().encode("utf-8") == "Dst IP. 'del' para eliminar."):
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("no int " + getiface.get() + "\n")
                        sleep(0.3)
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        tkMessageBox.showinfo('Configuración IP', 'Interfaz eliminada.')
                    else:
                        remote_conn.send("sh ip int " + getiface.get() + " \n")
                        sleep(0.5)
                        output = remote_conn.recv(2048).decode("utf-8")
                        sleep(0.5)
                        stripp = output.strip()
                        sleep(0.2)
                        if 'Invalid input' in stripp:
                            tkMessageBox.showinfo('Error', 'La interfaz ' + getiface.get() + ' no existe ... Abortando.')
                            return
                        else:
                            pass
                        
                        remote_conn.send("conf t \n")
                        sleep(0.3)
                        remote_conn.send("int " + getiface.get() + "\n")
                        sleep(0.3)
                        tuntxt = ""
                        if (getiface.get()[:2] == "tu") and ((tunsrc.get() != "" and tunsrc.get().encode("utf-8") != "Src IP. 'del' para eliminar.") or\
                                                             (tundst.get() != "" and tundst.get().encode("utf-8") != "Dst IP. 'del' para eliminar.")):
                           
                            if tunsrc.get() == "del":
                                remote_conn.send("no tun so \n")
                                sleep(0.3)
                                tuntxt = tuntxt + "Se eliminó la IP de origen del túnel. "
                            else:
                                pass
                            if tundst.get() == "del":
                                remote_conn.send("no tun dest \n")
                                sleep(0.3)
                                tuntxt = tuntxt + "Se eliminó la IP de destino del túnel. "
                            else:
                                pass
                            
                        else:
                            pass

##                        sectxt = ""
##                        if chk_state_sec.get() == True:
##                            ipaddrcmd = ipaddrcmd + " secondary"
##                            sectxt = "IP removed was a secondary IP. "
##                        else:
##                            pass

                        IPtxt = ""
                        if ipaddr.get() == "del" and ipmask.get() == "del":
                            if chk_state_sec.get() == False:
                                remote_conn.send("no ip addr \n")
                                IPtxt = "Dirección IP eliminada. "
                            else:
                                remote_conn.send("no ip addr sec \n")
                                IPtxt = "Dirección IP secundaria eliminada. "
                        elif (ipaddr.get() != "" or ipaddr.get().encode("utf-8") != "IP. 'del' para eliminar.") and (ipmask.get() != "" or ipmask.get().encode("utf-8") != "Máscara de subred. 'del' para eliminar."):
                            tkMessageBox.showinfo('Error', 'Utilice la palabra clave "del" en los campos de máscara de subred y IP para eliminar la IP.')
                            sleep(0.2)   
                            remote_conn.send("exit \n")
                            sleep(0.2)   
                            remote_conn.send("exit \n")
                            return
                        else:
                            pass

##                        Shutstatetxt = ""
##                        if chk_state_nosh.get() == False:
##                            sleep(0.3)
##                            remote_conn.send("sh \n")
##                            sleep(0.3)
##                            Shutstatetxt = "Interface is disabled. "
##                        else:
##                            sleep(0.3)
##                            remote_conn.send("no sh \n")
##                            sleep(0.3)
##                            Shutstatetxt = "Interface is enabled. "
                        sleep(0.2)   
                        remote_conn.send("exit \n")
                        sleep(0.2)
                        remote_conn.send("exit \n") 
                        tkMessageBox.showinfo('Configuración IP', IPtxt + tuntxt)
            
    btn = Button(biface, text="*Aplicar", bg="orange", command=setinterfaceipclick)
    btn.grid(column=3, row=3)






    blankdivider = Label(biface, text="").grid(column=0, row=5)

    lbl = Label(biface, text="Velocidad y dúplex:").grid(column=0, row=6)
    OPTIONS = [
    "auto",        
    "10",        
    "100",
    "1000"
    ]
    spd = StringVar(biface)
    spd.set(OPTIONS[0])    # default value
    dropbox = OptionMenu(biface, spd, *OPTIONS)   
    dropbox.grid(column=1, row=6)        
    OPTIONS = [
    "auto",        
    "half",        
    "full"
    ]
    dup = StringVar(biface)
    dup.set(OPTIONS[0])    # default value
    dropbox = OptionMenu(biface, dup, *OPTIONS)   
    dropbox.grid(column=2, row=6)  



    def setspeedduplex():
        if getiface.get() == "" or getiface.get() == "e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..":
            tkMessageBox.showinfo('Error', 'Elija una interfaz.')
        elif ("lo" in getiface.get()) or ("Lo" in getiface.get()) or ("tu" in getiface.get()) or ("bvi" in getiface.get()) or ("BVI" in getiface.get()) or ("." in getiface.get()):
            tkMessageBox.showinfo('Error', 'Solo se puede configurar la velocidad y el dúplex para interfaces físicas.')
        elif ("fa" in getiface.get() or "Fa" in getiface.get()) and spd.get() == "1000":
            tkMessageBox.showinfo('Error', 'La velocidad para FastEthernet se puede configurar solo hasta 100 Mbps.')
        else:    
            remote_conn.send("conf t \n")
            sleep(0.5)
            remote_conn.send("int " + getiface.get() + "\n")
            sleep(0.5)
            output = remote_conn.recv(2048).decode("utf-8")
            sleep(1)
            stripp = output.strip()
            sleep(0.2)
            if 'Invalid input' in stripp:
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('Error', 'La interfaz ' + getiface.get() + ' no existe ... Abortando. Si es BVI, asegúrese de que el Grupo Bridge se haya creado primero.')
                return
            else:
                pass
            remote_conn.send("speed " + spd.get() + "\n")
            sleep(0.5)
            remote_conn.send("duplex " + dup.get() + "\n")
            sleep(0.5)        
            remote_conn.send("exit \n")
            sleep(0.5)
            remote_conn.send("exit \n")
            res = "Velocidad establecida en " + spd.get() + " y duplex " + dup.get() + " en " + getiface.get()
            tkMessageBox.showinfo('Velocidad y dúplex', res)
    btn = Button(biface, text="*Aplicar", bg="orange", command=setspeedduplex)
    btn.grid(column=3, row=6)        

    blankdivider = Label(biface, text="").grid(column=0, row=8)
    
    lbl = Label(biface, text="Otros ajustes:").grid(column=0, row=9)

    def option_changed_otheroptn(*args):
        if otheroptn.get() == "MAC address":
            text = 'xxxx.xxxx.xxxx'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in) 

        elif otheroptn.get() == "DHCP Client":
            text = 'No se requiere entrada'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        elif otheroptn.get() == "dot1q":
            text = '1-4094'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        elif otheroptn.get() == "VRF" or otheroptn.get() == "fVRF":
            text = 'eg. MyVRF'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        elif otheroptn.get() == "ARP timeout":
            text = '(secs)'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        elif otheroptn.get() == "IP MTU(L3)":
            text = 'eg. 1400'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        elif otheroptn.get() == "MTU(L2)":
            text = 'eg. 1500'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        elif otheroptn.get() == "TCP MSS(L4)":
            text = 'eg. 1360'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        elif otheroptn.get() == "VFR":
            text = 'No se requiere entrada'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        elif otheroptn.get() == "Add to bridge":
            text = '<bridge-grp no.>'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        elif otheroptn.get() == "tun key":
            text = 'eg. 1'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        elif otheroptn.get() == "keepalive":
            text = '<secs> [<retries>]'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        elif otheroptn.get() == "bandwidth":
            text = '<kilobits>'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)
        else:
            text = '<IPSec_prof_name>'
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if otherinput.cget('fg') != 'black':
                    otherinput.delete(0, END)
                    otherinput.config(fg='black')
            def handle_focus_out(_):
                if otherinput.get() == "":
                    otherinput.delete(0, END)
                    otherinput.config(fg='grey')
                    otherinput.insert(0, text)    
            otherinput.bind("<FocusOut>", handle_focus_out)
            otherinput.bind("<FocusIn>", handle_focus_in)            
            
    OPTIONS = [
    "MAC address",
    "DHCP Client",
    "dot1q",
    "VRF",
    "fVRF",
    "ARP timeout",
    "TCP MSS(L4)",
    "IP MTU(L3)",
    "MTU(L2)",
    "VFR",
    "Add to bridge",
    "tun key",
    "keepalive",
    "bandwidth",
    "IPSEC profile"
    ]
    otheroptn = StringVar(biface)
    otheroptn.set(OPTIONS[0])    # default value
    otheroptn.trace("w", option_changed_otheroptn)
    dropbox = OptionMenu(biface, otheroptn, *OPTIONS)   
    dropbox.place(x=192, y=150)
    otherinput = Entry(biface, bg='white', width=16, fg='grey')
    otherinput.grid(column=2, row=9)
    otherinput.insert(0, 'xxxx.xxxx.xxxx')
    window.focus_set()
    def handle_focus_in(_):
        if otherinput.cget('fg') != 'black':
            otherinput.delete(0, END)
            otherinput.config(fg='black')
    def handle_focus_out(_):
        if otherinput.get() == "":
            otherinput.delete(0, END)
            otherinput.config(fg='grey')
            otherinput.insert(0, 'xxxx.xxxx.xxxx')    
    otherinput.bind("<FocusOut>", handle_focus_out)
    otherinput.bind("<FocusIn>", handle_focus_in)
    
    def setotherconf():
        if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
            tkMessageBox.showinfo('Error', 'Elija una interfaz.')
        else:
            if chk_state_neg.get() == False:
                remote_conn.send("conf t \n")
                sleep(0.5)
                remote_conn.send("int " + getiface.get() + "\n")
                sleep(0.5)
                if otheroptn.get() == 'MAC address':
                    if otherinput.get() != "" and otherinput.get() != "xxxx.xxxx.xxxx":
                        remote_conn.send(otheroptn.get() + " " + otherinput.get() + "\n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Dirección MAC de la interfaz configurada.')
                    else:
                        tkMessageBox.showinfo('Error', 'Ingrese una dirección MAC para configurar en la interfaz.')
                elif otheroptn.get() == 'dot1q':
                    if "." not in getiface.get():
                        tkMessageBox.showinfo('Error', 'La encapsulación Dot1q solo se puede aplicar a una subinterfaz.')
                    elif otherinput.get() == "":
                        tkMessageBox.showinfo('Error', 'Ingrese una ID de VLAN para aplicar en la subinterfaz.')
                    else:
                        sleep(0.5)
                        remote_conn.send("encap dot1Q " + otherinput.get() + "\n")
                        sleep(0.5)
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Dot1q ha sido configurado.')
                elif otheroptn.get() == 'VRF':
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("show ip vrf " + otherinput.get() + "\n")
                    sleep(3)        
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 2048
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    if otherinput.get() == "":
                        tkMessageBox.showinfo('Error', 'Ingrese un VRF para aplicar en la interfaz.')
                    elif otherinput.get() not in output:
                        tkMessageBox.showinfo('Error', 'Cree primero el VRF antes de aplicarlo.')
                    else:
                        sleep(0.5)
                        remote_conn.send("ip vrf forwarding " + otherinput.get() + "\n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'VRF configurado (si ya se ha creado).')
                elif otheroptn.get() == 'fVRF':
                    buff_size = 16384
                    sleep(0.5)
                    remote_conn.send("show ip vrf " + otherinput.get() + "\n")
                    sleep(3)        
                    while not remote_conn.recv_ready():
                        remote_conn.recv(0)
                        buff_size += 2048
                        sleep(0.5)
                    output = remote_conn.recv(buff_size).decode("utf-8")
                    if 'tu' not in getiface.get():
                        tkMessageBox.showinfo('Error', 'fVRF solo se puede aplicar a interfaces de túnel.')
                    elif otherinput.get() == "":
                        tkMessageBox.showinfo('Error', 'Ingrese un VRF para aplicar en la interfaz.')
                    elif otherinput.get() not in output:
                        tkMessageBox.showinfo('Error', 'Cree primero el VRF antes de aplicarlo.')
                    else:
                        sleep(0.5)
                        remote_conn.send("tunnel vrf " + otherinput.get() + "\n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'VRF configurado (si ya se ha creado).')
                elif otheroptn.get() == 'DHCP Client':
                    sleep(0.5)
                    remote_conn.send("ip addr dhcp \n")
                    sleep(0.5)       
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Configurado como cliente DHCP. SE HA ELIMINADO CUALQUIER DIRECCIÓN IP EXISTENTE.')
                elif otheroptn.get() == 'IP MTU(L3)':
                    if otherinput.get() != "" and otherinput.get() != "eg. 1400" and (68 <= int(otherinput.get()) <= 1500):
                        sleep(0.5)
                        remote_conn.send("ip mtu " + otherinput.get() + "\n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Paquete de interfaz configurado MTU.')
                    else:
                        tkMessageBox.showinfo('Error', 'Ingrese un valor MTU (68-1500) para aplicar en la interfaz.')
                elif otheroptn.get() == 'MTU(L2)':
                    if otherinput.get() != "" and otherinput.get() != "eg. 1500" and (68 <= int(otherinput.get()) <= 1500):
                        sleep(0.5)
                        remote_conn.send("mtu " + otherinput.get() + "\n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Marco de interfaz configurado MTU.')
                    else:
                        tkMessageBox.showinfo('Error', 'Ingrese un valor MTU (1500-1530) para aplicar en la interfaz.')                    
                elif otheroptn.get() == 'TCP MSS(L4)':
                    if otherinput.get() != "" and otherinput.get() != "eg. 1360" and (500 <= int(otherinput.get()) <= 1460):
                        sleep(0.5)
                        remote_conn.send("ip tcp adjust-mss " + otherinput.get() + " \n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Configured MSS.')
                    else:
                        tkMessageBox.showinfo('Error', 'Ingrese un valor de MSS (500-1460) para aplicar en la interfaz.')
                elif otheroptn.get() == 'VFR':
                    sleep(0.5)
                    remote_conn.send("ip virtual-reassembly \n")
                    sleep(0.5)       
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Enabled IP Virtual Reassembly for fragmented packets.')
                elif otheroptn.get() == 'Add to bridge':
                    if otherinput.get() == "<bridge-grp no.>" or otherinput.get() == "":
                        tkMessageBox.showinfo('Error', 'Ingrese un número de grupo de puente.')
                    else:
                        sleep(0.5)
                        remote_conn.send("int " + getiface.get() + " \n")
                        sleep(0.5)
                        remote_conn.send("bridge-group " + otherinput.get() + "\n")
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', getiface.get() + ' se ha agregado al grupo puente ' + otherinput.get())
                elif otheroptn.get() == 'tun key':
                    if getiface.get()[:2] != 'tu': 
                        tkMessageBox.showinfo('Error', 'La clave de túnel solo se puede aplicar a interfaces de túnel (por ejemplo, tun0).')
                    elif otherinput.get() == "" or otherinput.get() == "eg. 1":
                        tkMessageBox.showinfo('Error', 'Ingrese un valor de clave de túnel para aplicar en la interfaz.')
                    else:
                        remote_conn.send("tun key " + otherinput.get() + "\n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Llave de túnel configurada.')                
                elif otheroptn.get() == 'keepalive':
                    if otherinput.get() == "" or otherinput.get() == "<secs> [<retries>]":
                        tkMessageBox.showinfo('Error', 'Ingrese un valor de keepalive para aplicar en la interfaz.')
                    elif getiface.get()[:2] != 'tu':
                        findfirstdigits = re.search(r'\d+', otherinput.get()).group()
                        sleep(0.2)
                        remote_conn.send("keepalive " + findfirstdigits + "\n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Interfaz keepalive configurada.')
                    else:
                        remote_conn.send("keepalive " + otherinput.get() + "\n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Interfaz de túnel keepalive configurada.')
                elif otheroptn.get() == 'bandwidth':
                    if otherinput.get() == "" or otherinput.get() == "<kilobits>":
                        tkMessageBox.showinfo('Error', 'Ingrese un valor de ancho de banda para aplicar en la interfaz.')
                    else:
                        remote_conn.send("bandwidth " + otherinput.get() + "\n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Ancho de banda de interfaz configurado.')
                elif otheroptn.get() == 'IPSEC profile':
                    if getiface.get()[:2] != 'tu':
                        tkMessageBox.showinfo('Error', 'Aplique el perfil IPSEC a una interfaz de túnel (por ejemplo, tun0).')
                    elif otherinput.get() == "" or otherinput.get() == "<IPSec_prof_name>":
                        tkMessageBox.showinfo('Error', 'Ingrese un perfil IPSEC para aplicar en la interfaz.')
                    else:                    
                        remote_conn.send("tunnel protection ipsec profile " + otherinput.get() + "\n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Perfil IPSEC de túnel configurado.')                    
                else:
                    remote_conn.send(otheroptn.get() + " " + otherinput.get() + "\n")
                    sleep(0.5)       
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Tiempo de espera ARP configurado.')
            else:
                remote_conn.send("conf t \n")
                sleep(0.5)
                remote_conn.send("int " + getiface.get() + "\n")            
                if otheroptn.get() == 'MAC address':
                    remote_conn.send("no mac \n")
                    sleep(0.5)
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Restablecimiento de la dirección MAC de la interfaz a BIA.')
                elif otheroptn.get() == 'dot1q':
                    if "." not in getiface.get():
                        tkMessageBox.showinfo('Error', 'Not a subinterface.')
                    else:
                        sleep(0.5)
                        remote_conn.send("no encap dot1Q \n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Dot1q eliminado.')
                elif otheroptn.get() == 'VRF':
                    sleep(0.5)
                    remote_conn.send("no ip vrf forwarding \n")
                    sleep(0.5)       
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', 'VRF eliminado.')
                elif otheroptn.get() == 'DHCP Client':
                    sleep(0.5)
                    remote_conn.send("no ip addr dhcp \n")
                    sleep(0.5)       
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Desconfigurado como cliente DHCP.')
                elif otheroptn.get() == 'IP MTU(L3)':
                    sleep(0.5)
                    remote_conn.send("no ip mtu \n")
                    sleep(0.5)       
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Paquete de interfaz MTU restablecido al máximo predeterminado (1500B).')
                elif otheroptn.get() == 'MTU(L2)':
                    sleep(0.5)
                    remote_conn.send("no mtu \n")
                    sleep(0.5)       
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Marco de interfaz MTU restablecido al máximo predeterminado (1500B).')                
                elif otheroptn.get() == 'TCP MSS(L4)':
                    sleep(0.5)
                    remote_conn.send("no ip tcp adjust-mss \n")
                    sleep(0.5)       
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Interfaz MSS restablecida al máximo predeterminado (1460B).')
                elif otheroptn.get() == 'VFR':
                    sleep(0.5)
                    remote_conn.send("no ip virtual-reassembly \n")
                    sleep(0.5)       
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Reensamblaje virtual de IP deshabilitado para paquetes fragmentados.')
                elif otheroptn.get() == 'Add to bridge':
                    sleep(0.5)
                    remote_conn.send("no bridge-group " + otherinput.get() + "\n")
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', getiface.get() + ' ha sido eliminado del grupo de puentes ' + otherinput.get())
                elif otheroptn.get() == 'tun key':
                    if getiface.get()[:2] != 'tu': 
                        tkMessageBox.showinfo('Error', 'No es una interfaz de túnel.')
                    else:
                        remote_conn.send("no tun key \n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Llave de túnel eliminado.')                
                elif otheroptn.get() == 'tun kpalive':
                    if getiface.get()[:2] != 'tu':
                        tkMessageBox.showinfo('Error', 'Not a tunnel interface.')
                    else:                    
                        remote_conn.send("no keepalive \n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Túnel keepalive eliminado.')
                elif otheroptn.get() == 'bandwidth':
                        sleep(0.5)
                        remote_conn.send("no bandwidth \n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Ancho de banda de la interfaz restablecido a los valores predeterminados..')
                elif otheroptn.get() == 'IPSEC profile':
                    if getiface.get()[:2] != 'tu':
                        tkMessageBox.showinfo('Error', 'Especifique una interfaz de túnel (por ejemplo, tun0).')
                    elif otherinput.get() == "":
                        tkMessageBox.showinfo('Error', 'Ingrese un perfil IPSEC para eliminarlo de la interfaz.')
                    else:                    
                        remote_conn.send("no tunnel protection ipsec profile " + otherinput.get() + "\n")
                        sleep(0.5)       
                        tkMessageBox.showinfo('Otras configuraciones de interfaz', 'Perfil IPSEC de túnel eliminado.') 
                else:
                    sleep(0.5)
                    remote_conn.send("no " + otheroptn.get() + " " + otherinput.get() + "\n")
                    sleep(0.5)       
                    tkMessageBox.showinfo('Otras configuraciones de interfaz', 'El tiempo de espera de ARP se ha restablecido al valor predeterminado (4 horas)')
            remote_conn.send("exit \n")
            sleep(0.5)
            remote_conn.send("exit \n")
    btn = Button(biface, text="*Aplicar", bg="orange", command=setotherconf)
    btn.grid(column=3, row=9)

   
        

    def helpotherconf():
        res = 'VFR (Virtual Fragmentation Reassembly) - Para' +\
              ' detectar y prevenir una variedad de ataques de fragmentos. \n\nDot1q - Una encapsulación utilizada para Trunking, Router on a Stick, etc..' +\
              ' Valores válidos: 1-4094. Configúrelo solo en subinterfaces. Cualquier paquete destinado a la dirección IP de la interfaz física (si hay alguno configurado)' +\
              ' será bloqueado..' +\
              '\n\nVRF - funciona como una VLAN de capa 3. DEBE crearse (en la pestaña Ruta) primero antes de que se pueda aplicar.\n\n' +\
              'IP secundaria - Puede configurar varias direcciones IP secundarias en una interfaz. Si no hay una IP primaria configurada, la IP secundaria será ' +\
              'permanecen inactivos y ocultos solo hasta que se haya configurado una IP principal.' +\
              '\n\nPara puentear los puertos del enrutador, \n 1. Crear un Bridge Group,\n 2. Crear interfaz bvi\n 3. Otros ajustes > "Add to bridge"'
        tkMessageBox.showinfo('Ayuda con otras configuraciones de interfaz', res)
    btn = Button(biface, text="Ayuda", bg="yellow", command=helpotherconf)
    btn.grid(column=4, row=9)

    
    blankdivider = Label(biface, text="").grid(column=0, row=11)







    deviceconfframe=LabelFrame(window,text=" Configuración y ajuste del dispositivo ",font=('verdana', 8, 'bold'),padx=10,pady=8,width=100,height=100)
    deviceconfframe.grid(row=4,column=0, sticky=("nsew"))

    label = Label(deviceconfframe, text="Crear una entrada ARP estática: ").grid(column=0, row=1)
    getarpip = Entry(deviceconfframe, bg='white', width=15, fg='grey')
    getarpip.grid(column=1, row=1)
    getarpip.insert(0, "IP address")
    def handle_focus_in(_):
        if getarpip.cget('fg') != 'black':
            getarpip.delete(0, END)
            getarpip.config(fg='black')
    def handle_focus_out(_):
        if getarpip.get() == "":
            getarpip.delete(0, END)
            getarpip.config(fg='grey')
            getarpip.insert(0, "IP address")    
    getarpip.bind("<FocusOut>", handle_focus_out)
    getarpip.bind("<FocusIn>", handle_focus_in)    
    getarpmac = Entry(deviceconfframe, bg='white', width=15, fg='grey')
    getarpmac.grid(column=2, row=1)
    getarpmac.insert(0, "MAC address")
    def handle_focus_in(_):
        if getarpmac.cget('fg') != 'black':
            getarpmac.delete(0, END)
            getarpmac.config(fg='black')
    def handle_focus_out(_):
        if getarpmac.get() == "":
            getarpmac.delete(0, END)
            getarpmac.config(fg='grey')
            getarpmac.insert(0, "MAC address")    
    getarpmac.bind("<FocusOut>", handle_focus_out)
    getarpmac.bind("<FocusIn>", handle_focus_in)
    def setarp():
        remote_conn.send("conf t \n")
        sleep(0.5)        
        if chk_state_neg.get() == False:
            remote_conn.send("arp " + getarpip.get() + " " + getarpmac.get() + " arpa \n")
            sleep(0.5)
            remote_conn.send("exit \n")
            sleep(0.5)
            tkMessageBox.showinfo('ARP', 'Static ARP has been configured.')
        else:
            remote_conn.send("no arp " + getarpip.get() + " " + getarpmac.get() + " arpa \n")
            sleep(0.5)
            remote_conn.send("exit \n")
            sleep(0.5)
            tkMessageBox.showinfo('ARP', 'Static ARP has been removed.')          
    btn = Button(deviceconfframe, text="Aplicar", font=('helvetica', 8), bg="orange", command=setarp)
    btn.grid(column=3, row=1, padx=13)

    label = Label(deviceconfframe, text="Crear una entrada MAC estática: ").grid(column=0, row=2)
    getstmac = Entry(deviceconfframe, bg='white', width=15, fg='grey')
    getstmac.grid(column=1, row=2)
    getstmac.insert(0, "MAC address")
    def handle_focus_in(_):
        if getstmac.cget('fg') != 'black':
            getstmac.delete(0, END)
            getstmac.config(fg='black')
    def handle_focus_out(_):
        if getstmac.get() == "":
            getstmac.delete(0, END)
            getstmac.config(fg='grey')
            getstmac.insert(0, "MAC address")    
    getstmac.bind("<FocusOut>", handle_focus_out)
    getstmac.bind("<FocusIn>", handle_focus_in)        
    getstvlan = Entry(deviceconfframe, bg='white', width=15, fg='grey')
    getstvlan.grid(column=2, row=2)
    getstvlan.insert(0, "VLAN opcional")
    def handle_focus_in(_):
        if getstvlan.cget('fg') != 'black':
            getstvlan.delete(0, END)
            getstvlan.config(fg='black')
    def handle_focus_out(_):
        if getstvlan.get() == "":
            getstvlan.delete(0, END)
            getstvlan.config(fg='grey')
            getstvlan.insert(0, "VLAN opcional")    
    getstvlan.bind("<FocusOut>", handle_focus_out)
    getstvlan.bind("<FocusIn>", handle_focus_in)
    def setmac():
        if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
            tkMessageBox.showinfo('Error', 'Elija una interfaz.')
        else:
            remote_conn.send("conf t \n")
            sleep(0.5)
            if chk_state_neg.get() == False:
                if getstvlan.get() == '' or getstvlan.get() == 'VLAN opcional':
                    remote_conn.send("mac-address-table static " + getstmac.get() + " interface " + getiface.get() + " \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    sleep(0.5)
                    tkMessageBox.showinfo('MAC', 'MAC estática configurada. Tráfico hacia ' + getstmac.get() + ' será reenviado a ' + getiface.get())
                else:
                    remote_conn.send("mac-address-table static " + getstmac.get() + " interface " + getiface.get() + " vlan " + getstvlan.get() + " \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    sleep(0.5)
                    tkMessageBox.showinfo('MAC', 'MAC estática configurada. Paquetes en VLAN ' + getstvlan.get() +  ' hacia el destino ' + getstmac.get() + \
                                          ' será reenviado a ' + getiface.get())
            else:
                if getstvlan.get() == '' or getstvlan.get() == 'VLAN opcional':
                    remote_conn.send("no mac-address-table static " + getstmac.get() + " interface " + getiface.get() + " \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    sleep(0.5)
                    tkMessageBox.showinfo('MAC', 'MAC estática eliminada.')
                else:
                    remote_conn.send("no mac-address-table static " + getstmac.get() + " interface " + getiface.get() + " vlan " + getstvlan.get() + " \n")
                    sleep(0.5)
                    remote_conn.send("exit \n")
                    sleep(0.5)
                    tkMessageBox.showinfo('MAC', 'MAC estática eliminada.')        
    btn = Button(deviceconfframe, text="*Aplicar", font=('helvetica', 8), bg="orange", command=setmac)
    btn.grid(column=3, row=2, padx=13, pady=2) 


    def option_changed_arpmacopt(*args):
        if arpmacopt.get() == "Borrar ARP (todo)" or arpmacopt.get() == "Borrar MAC (todo)":
            text = 'No se requiere entrada'
            getmacarp.delete(0, END)
            getmacarp.config(fg='grey')
            getmacarp.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getmacarp.cget('fg') != 'black':
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='black')
            def handle_focus_out(_):
                if getmacarp.get() == "":
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='grey')
                    getmacarp.insert(0, text)
            getmacarp.bind("<FocusOut>", handle_focus_out)
            getmacarp.bind("<FocusIn>", handle_focus_in) 

        elif arpmacopt.get() == "Borrar ARP (interfaz)" or arpmacopt.get() == "Borrar MAC (interfaz)":
            text = 'eg. fa0/0'
            getmacarp.delete(0, END)
            getmacarp.config(fg='grey')
            getmacarp.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getmacarp.cget('fg') != 'black':
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='black')
            def handle_focus_out(_):
                if getmacarp.get() == "":
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='grey')
                    getmacarp.insert(0, text)    
            getmacarp.bind("<FocusOut>", handle_focus_out)
            getmacarp.bind("<FocusIn>", handle_focus_in)
        elif arpmacopt.get() == "Borrar ARP (ip)":
            text = 'eg. 1.2.3.4'
            getmacarp.delete(0, END)
            getmacarp.config(fg='grey')
            getmacarp.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getmacarp.cget('fg') != 'black':
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='black')
            def handle_focus_out(_):
                if getmacarp.get() == "":
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='grey')
                    getmacarp.insert(0, text)    
            getmacarp.bind("<FocusOut>", handle_focus_out)
            getmacarp.bind("<FocusIn>", handle_focus_in)
        elif arpmacopt.get().encode("utf-8") == "Borrar MAC (dirección)":
            text = 'xxxx.xxxx.xxxx'
            getmacarp.delete(0, END)
            getmacarp.config(fg='grey')
            getmacarp.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getmacarp.cget('fg') != 'black':
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='black')
            def handle_focus_out(_):
                if getmacarp.get() == "":
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='grey')
                    getmacarp.insert(0, text)    
            getmacarp.bind("<FocusOut>", handle_focus_out)
            getmacarp.bind("<FocusIn>", handle_focus_in)
        elif arpmacopt.get() == "Borrar MAC (vlan)":
            text = '<1-4094>'
            getmacarp.delete(0, END)
            getmacarp.config(fg='grey')
            getmacarp.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getmacarp.cget('fg') != 'black':
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='black')
            def handle_focus_out(_):
                if getmacarp.get() == "":
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='grey')
                    getmacarp.insert(0, text)    
            getmacarp.bind("<FocusOut>", handle_focus_out)
            getmacarp.bind("<FocusIn>", handle_focus_in)
        else:
            text = 'eg. 300'
            getmacarp.delete(0, END)
            getmacarp.config(fg='grey')
            getmacarp.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getmacarp.cget('fg') != 'black':
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='black')
            def handle_focus_out(_):
                if getmacarp.get() == "":
                    getmacarp.delete(0, END)
                    getmacarp.config(fg='grey')
                    getmacarp.insert(0, text)    
            getmacarp.bind("<FocusOut>", handle_focus_out)
            getmacarp.bind("<FocusIn>", handle_focus_in)
            
    OPTIONS = [
    "Borrar ARP (todo)",
    "Borrar ARP (ip)",
    "Borrar ARP (interfaz)",
    "Borrar MAC (todo)",
    "Borrar MAC (dirección)",
    "Borrar MAC (vlan)",
    "Borrar MAC (interfaz)",
    "Establecer MAC aging"
    ]
    arpmacopt = StringVar(deviceconfframe)
    arpmacopt.set(OPTIONS[0])    # default value
    arpmacopt.trace("w", option_changed_arpmacopt)
    dropbox = OptionMenu(deviceconfframe, arpmacopt, *OPTIONS)
    dropbox.place(x=0, y=50)
    
    getmacarp = Entry(deviceconfframe, bg='white', width=20, fg='grey')
    getmacarp.grid(column=1, row=4, columnspan=2)
    getmacarp.insert(0, "No se requiere entrada")
    def handle_focus_in(_):
        if getmacarp.cget('fg') != 'black':
            getmacarp.delete(0, END)
            getmacarp.config(fg='black')
    def handle_focus_out(_):
        if getmacarp.get() == "":
            getmacarp.delete(0, END)
            getmacarp.config(fg='grey')
            getmacarp.insert(0, "No se requiere entrada")    
    getmacarp.bind("<FocusOut>", handle_focus_out)
    getmacarp.bind("<FocusIn>", handle_focus_in)


    def arpmacclearset():
        if arpmacopt.get() == "Borrar ARP (todo)":
            remote_conn.send("clear arp \n")
            sleep(0.5)
            tkMessageBox.showinfo('Tabla ARP', 'Se borraron todas las entradas de la tabla ARP.')
        elif arpmacopt.get() == "Borrar ARP (ip)":
            if getmacarp.get() != "" and ("." in getmacarp.get()):
                remote_conn.send("clear ip arp " + getmacarp.get() + "\n")
                sleep(0.5)
                tkMessageBox.showinfo('Tabla ARP', 'Las entradas de la tabla ARP se borraron con el atributo IP especificado.')
            else:
                tkMessageBox.showinfo('Error', 'Ingrese una dirección IP para borrar la entrada ARP asociada.')
        elif arpmacopt.get() == "Borrar ARP (interfaz)":
            if (("fa" in getmacarp.get()) or ("gi" in getmacarp.get()) or ("te" in getmacarp.get()) or \
            ("tun" in getmacarp.get()) or ("lo" in getmacarp.get())):
                sleep(0.5)
                remote_conn.send("clear arp " + getmacarp.get() + "\n")
                sleep(0.5)
                tkMessageBox.showinfo('Tabla ARP', 'Las entradas de la tabla ARP se borraron con el atributo de interfaz especificado.')
            else:
                tkMessageBox.showinfo('Error', 'Ingrese una interfaz (SOLO fa / gi / te / tun / lo / bvi) para borrar la entrada ARP asociada.')
        elif arpmacopt.get() == "Borrar MAC (todo)":
                remote_conn.send("clear mac-address-table \n")
                sleep(0.5)
                tkMessageBox.showinfo('Tabla MAC', 'Se borraron todas las entradas de la tabla de direcciones MAC.')
        elif arpmacopt.get() == "Borrar MAC (vlan)":
            if getmacarp.get() != "" and getmacarp.get().isdigit() == True:
                remote_conn.send("clear mac-address-table vlan " + getmacarp.get() + " \n")
                sleep(0.5)
                tkMessageBox.showinfo('Tabla MAC', 'Se borraron todas las entradas de la tabla de direcciones MAC para VLAN ' + getmacarp.get() + '.')
            else:
                tkMessageBox.showinfo('Error', 'Ingrese una ID de VLAN para borrar la entrada de dirección MAC asociada.')
        elif arpmacopt.get().encode("utf-8") == "Borrar MAC (dirección)":
            if getmacarp.get() != "" and ("." in getmacarp.get()):
                remote_conn.send("clear mac-address-table address " + getmacarp.get() + " \n")
                sleep(0.5)
                tkMessageBox.showinfo('Tabla MAC', 'Se borró la entrada de la tabla de direcciones MAC.')
            else:
                tkMessageBox.showinfo('Error', 'Ingrese una dirección MAC (XXXX.XXXX.XXXX) para borrar la entrada de dirección MAC asociada.')
        elif arpmacopt.get() == "Borrar MAC (interfaz)":
            if getmacarp.get() != "":
                remote_conn.send("clear mac-address-table int " + getmacarp.get() + " \n")
                sleep(0.5)
                tkMessageBox.showinfo('Tabla MAC', 'Se borraron las entradas de la tabla de direcciones MAC para la interfaz ' + getmacarp.get() + '.')
            else:
                tkMessageBox.showinfo('Error', 'Ingrese una interfaz (SOLO fa / gi / te / tun / lo / bvi) para borrar la entrada de la dirección MAC asociada.')
        else:
            if chk_state_neg.get() == False:
                if getmacarp.get() != "" and getmacarp.get().isdigit() == True and (getmacarp.get() <= 1000000):
                    remote_conn.send("mac-address-table aging " + getmacarp.get() + " \n")
                    tkMessageBox.showinfo('Tabla MAC', 'Se ha configurado el tiempo de caducidad de la tabla de direcciones MAC.')
                else:
                    tkMessageBox.showinfo('Error', 'Introduzca un tiempo de caducidad de la dirección MAC numérica válida.')
            else:
                remote_conn.send("no mac-address-table aging \n")
                sleep(0.5)
                tkMessageBox.showinfo('Tabla MAC', 'Se restableció el tiempo de caducidad de la tabla de direcciones MAC.')
    btn = Button(deviceconfframe, text="Aplicar", font=('helvetica', 8), bg="orange", command=arpmacclearset)
    btn.grid(column=3, row=4)




    def option_changed_TCPtune(*args):
        if TCPtuneopt.get() == "PMTUD":
            text = '[<2-20> (mins)]'
            getTCPtune.delete(0, END)
            getTCPtune.config(fg='grey')
            getTCPtune.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getTCPtune.cget('fg') != 'black':
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='black')
            def handle_focus_out(_):
                if getTCPtune.get() == "":
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='grey')
                    getTCPtune.insert(0, text)
            getTCPtune.bind("<FocusOut>", handle_focus_out)
            getTCPtune.bind("<FocusIn>", handle_focus_in)
        elif TCPtuneopt.get() == "TCP egress queue":
            text = 'eg. 5 (segments)'
            getTCPtune.delete(0, END)
            getTCPtune.config(fg='grey')
            getTCPtune.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getTCPtune.cget('fg') != 'black':
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='black')
            def handle_focus_out(_):
                if getTCPtune.get() == "":
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='grey')
                    getTCPtune.insert(0, text)
            getTCPtune.bind("<FocusOut>", handle_focus_out)
            getTCPtune.bind("<FocusIn>", handle_focus_in) 
        elif TCPtuneopt.get() == "SYNWAIT-time":
            text = 'eg. 30 (secs)'
            getTCPtune.delete(0, END)
            getTCPtune.config(fg='grey')
            getTCPtune.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getTCPtune.cget('fg') != 'black':
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='black')
            def handle_focus_out(_):
                if getTCPtune.get() == "":
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='grey')
                    getTCPtune.insert(0, text)
            getTCPtune.bind("<FocusOut>", handle_focus_out)
            getTCPtune.bind("<FocusIn>", handle_focus_in)
        elif TCPtuneopt.get() == "TCP window-size":
            text = 'eg. 65535'
            getTCPtune.delete(0, END)
            getTCPtune.config(fg='grey')
            getTCPtune.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getTCPtune.cget('fg') != 'black':
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='black')
            def handle_focus_out(_):
                if getTCPtune.get() == "":
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='grey')
                    getTCPtune.insert(0, text)
            getTCPtune.bind("<FocusOut>", handle_focus_out)
            getTCPtune.bind("<FocusIn>", handle_focus_in) 
        elif TCPtuneopt.get() == "Habilitar ECN" or TCPtuneopt.get() == "Habilitar Selective-ACK" or TCPtuneopt.get() == "Habilitar TCP timestamp":
            text = 'No se requiere entrada'
            getTCPtune.delete(0, END)
            getTCPtune.config(fg='grey')
            getTCPtune.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getTCPtune.cget('fg') != 'black':
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='black')
            def handle_focus_out(_):
                if getTCPtune.get() == "":
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='grey')
                    getTCPtune.insert(0, text)
            getTCPtune.bind("<FocusOut>", handle_focus_out)
            getTCPtune.bind("<FocusIn>", handle_focus_in)
        else:
            text = ''
            getTCPtune.delete(0, END)
            getTCPtune.config(fg='grey')
            getTCPtune.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if getTCPtune.cget('fg') != 'black':
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='black')
            def handle_focus_out(_):
                if getTCPtune.get() == "":
                    getTCPtune.delete(0, END)
                    getTCPtune.config(fg='grey')
                    getTCPtune.insert(0, text)
            getTCPtune.bind("<FocusOut>", handle_focus_out)
            getTCPtune.bind("<FocusIn>", handle_focus_in)
            
    OPTIONS = [
    "PMTUD",
    "TCP egress queue",
    "SYNWAIT-time",
    "TCP window-size",
    "Habilitar ECN",
    "Habilitar Selective-ACK",
    "Habilitar TCP timestamp"
    ]
    TCPtuneopt = StringVar(deviceconfframe)
    TCPtuneopt.set(OPTIONS[0])    # default value
    TCPtuneopt.trace("w", option_changed_TCPtune)
    dropbox = OptionMenu(deviceconfframe, TCPtuneopt, *OPTIONS)   
    dropbox.place(x=0, y=80)
    
    getTCPtune = Entry(deviceconfframe, width=20)
    getTCPtune.grid(column=1, row=5, pady=5, columnspan=2)
    getTCPtune.delete(0, END)
    getTCPtune.config(fg='grey')
    getTCPtune.insert(0, "[<2-20> (mins)]")
    window.focus_set()
    def handle_focus_in(_):
        if getTCPtune.cget('fg') != 'black':
            getTCPtune.delete(0, END)
            getTCPtune.config(fg='black')
    def handle_focus_out(_):
        if getTCPtune.get() == "":
            getTCPtune.delete(0, END)
            getTCPtune.config(fg='grey')
            getTCPtune.insert(0, "[<2-20> (mins)]")
    getTCPtune.bind("<FocusOut>", handle_focus_out)
    getTCPtune.bind("<FocusIn>", handle_focus_in)


    def TCPtune():
        if chk_state_neg.get() == False:
            if TCPtuneopt.get() == "PMTUD":
                remote_conn.send("conf t \n")
                sleep(0.3)
                if getTCPtune.get() != "" and getTCPtune.get() != "[<2-20> (mins)]":
                    remote_conn.send("ip tcp path-mtu-discovery age-timer " + getTCPtune.get() + "\n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('TCP', 'PMTUD configurado con recalibración MTU cada ' + getTCPtune.get() + ' minutos.')
                else:
                    remote_conn.send("ip tcp path-mtu-discovery \n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('TCP', 'PMTUD está configurado..')                 
            elif TCPtuneopt.get() == "TCP egress queue":
                if getTCPtune.get() != "" and getTCPtune.get() != "eg. 5 (segments)":
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("ip tcp queuemax " + getTCPtune.get() + "\n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('TCP', 'TCP egress queue está configurado..')
                else:
                    tkMessageBox.showinfo('Error', 'porfavor introduzca un valor.')                    
            elif TCPtuneopt.get() == "SYNWAIT-time":
                if getTCPtune.get() != "" and getTCPtune.get() != "eg. 30 (secs)":
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("ip tcp synwait-time " + getTCPtune.get() + "\n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('TCP', 'TCP SYNWAIT-time está configurado..')
                else:
                    tkMessageBox.showinfo('Error', 'porfavor introduzca un valor.') 
            elif TCPtuneopt.get() == "TCP window-size":
                if getTCPtune.get() != "" and getTCPtune.get() != "eg. 65535": 
                    remote_conn.send("conf t \n")
                    sleep(0.3)
                    remote_conn.send("ip tcp window-size " + getTCPtune.get() + "\n")
                    sleep(0.3)
                    remote_conn.send("exit \n")
                    tkMessageBox.showinfo('TCP', 'TCP window-size está configurado..')
                else:
                    tkMessageBox.showinfo('Error', 'porfavor introduzca un valor.') 
            elif TCPtuneopt.get() == "Habilitar ECN":
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("ip tcp ecn \n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('TCP', 'TCP Explicit Congestion Notification feature configured. NOTE: remote peer must also be ECN-enabled for this feature to work.')
            elif TCPtuneopt.get() == "Habilitar Selective-ACK":
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("ip tcp selective-ack \n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('TCP', 'TCP Selective-ACK(SACK) está configurado.')
            else:
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("ip tcp timestamp \n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('TCP', 'TCP timestamp está configurado..')
        else:
            if TCPtuneopt.get() == "PMTUD":
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("no ip tcp path-mtu-discovery \n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('TCP', 'TCP PMTUD desactivada.') 
            elif TCPtuneopt.get() == "TCP egress queue":
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("no ip tcp queuemax \n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('TCP', 'TCP egress-queue-max restablecen a los predeterminados.') 
            elif TCPtuneopt.get() == "SYNWAIT-time":
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("no ip tcp synwait-time \n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('TCP', 'TCP SYNWAIT-time restablecen a los predeterminados.') 
            elif TCPtuneopt.get() == "TCP window-size":
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("no ip tcp window-size \n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('TCP', 'TCP window-size restablecen a los predeterminados.') 
            elif TCPtuneopt.get() == "Habilitar ECN":
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("no ip tcp ECN \n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('TCP', 'TCP Explicit Congestion Notification desactivada.') 
            elif TCPtuneopt.get() == "Habilitar Selective-ACK":
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("no ip tcp Selective-ACK \n")
                sleep(0.3)
                remote_conn.send("exit \n")
                tkMessageBox.showinfo('TCP', 'TCP Selective-ACK desactivada.')
            else:
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("ip tcp timestamp \n")
                sleep(0.3)
                remote_conn.send("exit \n")                
            tkMessageBox.showinfo('TCP', 'TCP timestamp desactivada.')
    btn = Button(deviceconfframe, text="Aplicar", font=('helvetica', 8), bg="orange", command=TCPtune)
    btn.grid(column=3, row=5)


    

    lbl = Label(deviceconfframe, text="Bridge Group:").grid(column=0, row=6, pady=(15,0))
    createbridge = Entry(deviceconfframe, bg='white', width=15, fg='grey')
    createbridge.grid(column=1, row=6, sticky='w', pady=(15,0))
    createbridge.insert(0, "eg. 5")
    def handle_focus_in(_):
        if createbridge.cget('fg') != 'black':
            createbridge.delete(0, END)
            createbridge.config(fg='black')
    def handle_focus_out(_):
        if createbridge.get() == "":
            createbridge.delete(0, END)
            createbridge.config(fg='grey')
            createbridge.insert(0, "eg. 5")    
    createbridge.bind("<FocusOut>", handle_focus_out)
    createbridge.bind("<FocusIn>", handle_focus_in)  

    chk_MAClearn = BooleanVar()
    chk_MAClearn.set(True)
    chk = Checkbutton(deviceconfframe, text="Aprendizaje MAC", font=("TkDefaultFont", 8), variable=chk_MAClearn)
    chk.grid(column=1, row=6, sticky='e', columnspan=2, pady=(15,0))
    


    def option_changed_bridgefilter(*args):
        if bridgefilter.get() == "Opcional":
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        elif bridgefilter.get() == "Priority":
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        elif bridgefilter.get() == "Aging time":
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        elif bridgefilter.get() == "Forward time":
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        elif bridgefilter.get() == "Hello time":
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        elif bridgefilter.get() == "Max Age":
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        elif bridgefilter.get() == "MAC filter":
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        elif bridgefilter.get() == "Domain":
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        elif bridgefilter.get() == "SpanningTree":
            text = 'NoInputRequired'
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        elif bridgefilter.get() == "iface_PathCost":
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        elif bridgefilter.get() == "iface_Priority":
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        elif bridgefilter.get() == "In_MACACL":
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    otherinput.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
        else:
            text = ''
            bridgeopt.delete(0, END)
            bridgeopt.config(fg='grey')
            bridgeopt.insert(0, text)
            window.focus_set()
            def handle_focus_in(_):
                if bridgeopt.cget('fg') != 'black':
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='black')
            def handle_focus_out(_):
                if bridgeopt.get() == "":
                    bridgeopt.delete(0, END)
                    bridgeopt.config(fg='grey')
                    bridgeopt.insert(0, text)
            bridgeopt.bind("<FocusOut>", handle_focus_out)
            bridgeopt.bind("<FocusIn>", handle_focus_in)
            
            
    OPTIONS = [
    "Opcional",
    "Priority",
    "Aging time",
    "Forward time",
    "Hello time",
    "Max Age",
    "MAC filter",
    "Domain",
    "SpanningTree",
    "iface_PathCost",
    "iface_Priority",
    "In_MACACL",
    "Out_MACACL"
    ]
    bridgefilter = StringVar(deviceconfframe)
    bridgefilter.set(OPTIONS[0])    # default value
    bridgefilter.trace("w", option_changed_bridgefilter)
    dropbox = OptionMenu(deviceconfframe, bridgefilter, *OPTIONS)   
    dropbox.place(y=145, x=15)

    bridgeopt = Entry(deviceconfframe, width=15)
    bridgeopt.grid(column=1, row=7, sticky='w', pady=2)



    def createbridgeG():
        if createbridge.get() == "" or createbridge.get() == "eg. 5":
            tkMessageBox.showinfo('ERROR', 'Ingrese el número de grupo de puente.')
        else:
            if chk_state_neg.get() == False: 
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("bridge irb \n")
                sleep(0.3)
                remote_conn.send("bridge " + createbridge.get() + " protocol ieee \n")
                sleep(0.3)
                remote_conn.send("bridge " + createbridge.get() + " route ip \n")
                sleep(0.3)
                if chk_MAClearn.get() == False:
                    remote_conn.send("no bridge " + createbridge.get() + " acquire \n")
                    res = 'El aprendizaje de MAC está deshabilitado. '
                else:
                    remote_conn.send("bridge " + createbridge.get() + " acquire \n")
                    res = 'El aprendizaje de MAC está habilitado. '
                sleep(0.3)
                remote_conn.send("exit \n")
                sleep(0.3)
                tkMessageBox.showinfo('Configuración de puente', 'Se ha creado el puente. ' + res)
            else:
                remote_conn.send("conf t \n")
                sleep(0.3)
                remote_conn.send("no bridge " + createbridge.get() + " \n")
                sleep(0.3)
                remote_conn.send("exit \n")

    btn = Button(deviceconfframe, text="Aplicar", font=('helvetica', 8), bg="orange", command=createbridgeG)
    btn.grid(row=6, column=3, pady=(15,0)) 

    def bridgeGOpt():
        if createbridge.get() == "" or createbridge.get() == "eg. 5":
            tkMessageBox.showinfo('ERROR', 'Ingrese el número de grupo de puente.')
        elif bridgefilter.get() == "Opcional":
            tkMessageBox.showinfo('ERROR', 'Por favor, elija una opción.')
        else:
            if chk_state_neg.get() == False:
                remote_conn.send("conf t \n")
                sleep(0.3)
                if bridgefilter.get() == "Priority":
                    remote_conn.send("bridge " + createbridge.get() + " priority " + bridgeopt.get() + " \n")
                    res = 'Priority está configurado. '
                elif bridgefilter.get() == "Aging time":
                    remote_conn.send("bridge " + createbridge.get() + " aging-time " + bridgeopt.get() + " \n")
                    res = 'Aging time está configurado. '
                elif bridgefilter.get() == "Forward time":
                    remote_conn.send("bridge " + createbridge.get() + " forward-time " + bridgeopt.get() + " \n")
                    res = 'Forward time está configurado. '
                elif bridgefilter.get() == "Hello time":
                    remote_conn.send("bridge " + createbridge.get() + " hello-time " + bridgeopt.get() + " \n")
                    res = 'Hello time está configurado. '
                elif bridgefilter.get() == "Max Age":
                    remote_conn.send("bridge " + createbridge.get() + " max-age " + bridgeopt.get() + " \n")
                    res = 'Max Age está configurado. '
                elif bridgefilter.get() == "MAC filter":
                    remote_conn.send("bridge " + createbridge.get() + " address " + bridgeopt.get() + " \n")
                    res = 'MAC filter está configurado. '
                elif bridgefilter.get() == "Domain":
                    remote_conn.send("bridge " + createbridge.get() + " domain " + bridgeopt.get() + " \n")
                    res = 'Domain está configurado. '
                elif bridgefilter.get() == "SpanningTree":
                    if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                        tkMessageBox.showinfo('Error', 'Elija una interfaz.')
                    else:                    
                        remote_conn.send("bridge-group " + createbridge.get() + " span \n")
                        res = 'Spanning Tree está configurado. '
                elif bridgefilter.get() == "iface_PathCost":
                    if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                        tkMessageBox.showinfo('Error', 'Elija una interfaz.')
                    else:
                        remote_conn.send("bridge-group " + createbridge.get() + " path-cost " + bridgeopt.get() + " \n")
                        res = 'Interface Path Cost está configurado. '
                elif bridgefilter.get() == "iface_Priority":
                    if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                        tkMessageBox.showinfo('Error', 'Elija una interfaz.')
                    else:
                        remote_conn.send("bridge-group " + createbridge.get() + " priority " + bridgeopt.get() + " \n")
                        res = 'Interface Priority está configurado. '
                elif bridgefilter.get() == "In_MACACL":
                    if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                        tkMessageBox.showinfo('Error', 'Elija una interfaz.')
                    else: 
                        remote_conn.send("bridge " + createbridge.get() + " input-address-list " + bridgeopt.get() + " \n")
                        res = 'MACACL entrante está configurado (filtrado por las direcciones de origen MAC). '
                else:
                    if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                        tkMessageBox.showinfo('Error', 'Elija una interfaz.')
                    else: 
                        remote_conn.send("bridge " + createbridge.get() + " output-address-list " + bridgeopt.get() + " \n")
                        res = 'MACACL saliente está configurado (filtrado por las direcciones MAC de destino). '
                sleep(0.3)
                tkMessageBox.showinfo('Bridge config', res)
            else:
                remote_conn.send("conf t \n")
                sleep(0.3)
                if bridgefilter.get() == "Priority":
                    remote_conn.send("no bridge priority \n")
                    res = 'Priority se restablece. '
                elif bridgefilter.get() == "Aging time":
                    remote_conn.send("no bridge aging-time \n")
                    res = 'Aging time se restablece. '
                elif bridgefilter.get() == "Forward time":
                    remote_conn.send("no bridge forward-time \n")
                    res = 'Forward time se restablece. '
                elif bridgefilter.get() == "Hello time":
                    remote_conn.send("no bridge hello-time \n")
                    res = 'Hello time se restablece. '
                elif bridgefilter.get() == "Max Age":
                    remote_conn.send("no bridge max-age \n")
                    res = 'Max Age se restablece. '
                elif bridgefilter.get() == "MAC filter":
                    remote_conn.send("no bridge " + createbridge.get() + " address " + bridgeopt.get() + " \n")
                    res = 'MAC filter está eliminado. '
                elif bridgefilter.get() == "Domain":
                    remote_conn.send("no bridge " + createbridge.get() + " domain " + bridgeopt.get() + " \n")
                    res = 'Domain está eliminado. '
                elif bridgefilter.get() == "SpanningTree":
                    if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                        tkMessageBox.showinfo('Error', 'Elija una interfaz.')
                    else:                    
                        remote_conn.send("bridge-group " + createbridge.get() + " spanning-disabled \n")
                        res = 'Spanning Tree está deshabilitado. '
                elif bridgefilter.get() == "iface_PathCost":
                    if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                        tkMessageBox.showinfo('Error', 'Elija una interfaz.')
                    else:
                        remote_conn.send("no bridge-group " + createbridge.get() + " path-cost \n")
                        res = 'Interface Path Cost se restablece. '
                elif bridgefilter.get() == "iface_Priority":
                    if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                        tkMessageBox.showinfo('Error', 'Elija una interfaz.')
                    else:
                        remote_conn.send("no bridge-group " + createbridge.get() + " priority \n")
                        res = 'Interface Priority se restablece. '
                elif bridgefilter.get() == "In_MACACL":
                    if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                        tkMessageBox.showinfo('Error', 'Elija una interfaz.')
                    else: 
                        remote_conn.send("no bridge " + createbridge.get() + " input-address-list " + bridgeopt.get() + " \n")
                        res = 'MACACL entrante está deshabilitado. '
                else:
                    if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                        tkMessageBox.showinfo('Error', 'Elija una interfaz.')
                    else: 
                        remote_conn.send("no bridge " + createbridge.get() + " output-address-list " + bridgeopt.get() + " \n")
                        res = 'Se elimina la MACACL saliente. '
                sleep(0.3)
                tkMessageBox.showinfo('Configuración de puente', res)
                    
    btn = Button(deviceconfframe, text="Aplicar", font=('helvetica', 8), bg="orange", command=bridgeGOpt)
    btn.grid(row=7, column=3)






    
    showconfframe=LabelFrame(window,text=" Mostrar configuración ",font=('verdana', 8, 'bold'),padx=50,pady=8,width=100,height=100)
    showconfframe.grid(row=6,column=0, sticky=("nsew"))
    
    OPTIONS = [
    "Estadísticas de la interfaz",
    "Configuración de interfaz",
    "Estadísticas de la interfaz L3",
    "Resumen de interfaces"
    ]
    showintopt = StringVar(showconfframe)
    showintopt.set(OPTIONS[0])    # default value
    dropbox = OptionMenu(showconfframe, showintopt, *OPTIONS)   
    dropbox.place(x=0, y=0)

    
    def showintconf():
        if showintopt.get().encode("utf-8") == "Estadísticas de la interfaz":
            if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                tkMessageBox.showinfo('Error', 'Ingrese una interfaz de arriba primero.')
            else:
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show int " + getiface.get() + "\n")
                sleep(1)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Configuración de interfaz actual', output)
        elif showintopt.get().encode("utf-8") == "Configuración de interfaz":
            if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                tkMessageBox.showinfo('Error', 'Ingrese una interfaz de arriba primero.')
            else:
                rep = getiface.get()
                newrep = ""
                if ("fa" in rep) or ("f" in rep):
                    newrep = rep.replace('fa', 'FastEthernet')
                elif ("ga" in rep) or ("g" in rep):
                    newrep = rep.replace('ga', 'GigabitEthernet')
                elif "et" in rep:
                    newrep = rep.replace('et', 'Ethernet')
                else:
                    pass
                    
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show run | s " + newrep + "\n")
                sleep(1)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Configuración de interfaz actual', output)
        elif showintopt.get().encode("utf-8") == "Estadísticas de la interfaz L3":
            if getiface.get() == '' or getiface.get() == 'e.g. fa0/0, fa0/0.2, vlan1, tun0, bvi1, po1 ..':
                tkMessageBox.showinfo('Error', 'Ingrese una interfaz de arriba primero.')
            else:
                buff_size = 16384
                sleep(0.5)
                remote_conn.send("show ip int " + getiface.get() + "\n")
                sleep(1)        
                while not remote_conn.recv_ready():
                    remote_conn.recv(0)
                    buff_size += 2048
                    sleep(0.5)
                output = remote_conn.recv(buff_size).decode("utf-8")
                tkMessageBox.showinfo('Configuración de interfaz actual', output)
        else:
            buff_size = 16384
            sleep(0.5)
            remote_conn.send("show ip int b \n")
            sleep(1)
            while not remote_conn.recv_ready():
                remote_conn.recv(0)
                buff_size += 2048
                sleep(0.5)
            output = remote_conn.recv(buff_size).decode("utf-8")
            tkMessageBox.showinfo('Configuración de interfaz actual', output)        
    btn = Button(showconfframe, text="Mostrar", bg="orange", command=showintconf)
    btn.place(x=300, y=0)
    


    OPTIONS = [
    "Estado del hardware",
    "Estado del hardware (detalle)",
    "Información de hardware",
    "Estado del búfer",
    "Reloj",
    "Tiempo de actividad",
    "Versión",
    "CPU",
    "Memoria",
    "Dúplex / Velocidad (configurado)",
    "Dúplex / velocidad (efectivo)",
    "Conexiones TCP",
    "Estadísticas de TCP",
    "UDP",
    "Puertos de escucha",
    "Tabla ARP",
    "Tabla MAC",
    "MAC table (totals)",
    "Puente"
    ]
    showintopt2 = StringVar(showconfframe)
    showintopt2.set(OPTIONS[0])    # default value
    dropbox = OptionMenu(showconfframe, showintopt2, *OPTIONS)   
    dropbox.place(x=0, y=30)


    def showintconf2():
        if showintopt2.get().encode("utf-8") == "Tabla MAC":
            buff_size = 16384
            sleep(0.5)
            remote_conn.send("show mac address-t \n")
            sleep(1)        
            while not remote_conn.recv_ready():
                remote_conn.recv(0)
                buff_size += 2048
                sleep(0.5)
            output = remote_conn.recv(buff_size).decode("utf-8")
            tkMessageBox.showinfo('Configuración de interfaz actual', output)
        elif showintopt2.get().encode("utf-8") == "Tabla MAC (totales)":
            buff_size = 16384
            sleep(0.5)
            remote_conn.send("show mac address-t count \n")
            sleep(1)        
            while not remote_conn.recv_ready():
                remote_conn.recv(0)
                buff_size += 2048
                sleep(0.5)
            output = remote_conn.recv(buff_size).decode("utf-8")
            tkMessageBox.showinfo('Configuración de interfaz actual', output)
        elif showintopt2.get().encode("utf-8") == "Tabla ARP":
            buff_size = 16384
            sleep(0.5)
            remote_conn.send("show arp \n")
            sleep(1)        
            while not remote_conn.recv_ready():
                remote_conn.recv(0)
                buff_size += 2048
                sleep(0.5)
            output = remote_conn.recv(buff_size).decode("utf-8")
            tkMessageBox.showinfo('Configuración de interfaz actual', output)
        else:
            if showintopt2.get().encode("utf-8") == "Estado del hardware":
                cmd = "show env \n"
            elif showintopt2.get().encode("utf-8") == "Estado del hardware (detalle)":
                cmd = "show env all \n"                
            elif showintopt2.get().encode("utf-8") == "Información de hardware":
                cmd = "show inv \n"
            elif showintopt2.get().encode("utf-8") == "Estado del búfer":
                cmd = "show buff \n"
            elif showintopt2.get().encode("utf-8") == "Reloj":
                cmd = "show clock \n"
            elif showintopt2.get().encode("utf-8") == "Tiempo de actividad":
                cmd = "show ver | i uptime | returned | restarted \n"
            elif showintopt2.get().encode("utf-8") == "Versión":
                cmd = "show ver | s IOS \n"
            elif showintopt2.get() == "CPU":
                cmd = "show proc cpu hist \n"
            elif showintopt2.get().encode("utf-8") == "Memoria":
                cmd = "show proc mem \n"
            elif showintopt2.get().encode("utf-8") == "Dúplex / Velocidad (configurado)":
                cmd = "show run | i interface | duplex | speed \n"
            elif showintopt2.get().encode("utf-8") == "Dúplex / velocidad (efectivo)":
                cmd = "show int | i dup| up \n"                
            elif showintopt2.get().encode("utf-8") == "Conexiones TCP":
                cmd = "show tcp brief nume \n"
            elif showintopt2.get().encode("utf-8") == "Estadísticas de TCP":
                cmd = "show tcp stat \n"
            elif showintopt2.get().encode("utf-8") == "Puertos de escucha":
                cmd = "show control-plane host open-p \n"
            elif showintopt2.get().encode("utf-8") == "Puente":
                cmd = "show bridge \n"
            else:
                cmd = "show udp \n"
            buff_size = 16384
            sleep(0.5)
            remote_conn.send(cmd)
            sleep(1)
            while not remote_conn.recv_ready():
                remote_conn.recv(0)
                buff_size += 2048
                sleep(0.5)
            output = remote_conn.recv(buff_size).decode("utf-8")
            tkMessageBox.showinfo('Configuración de interfaz actual', output)      
    btn = Button(showconfframe, text="Mostrar", bg="orange", command=showintconf2)
    btn.place(x=300, y=30)



    
if __name__ == "__main__":


        main()
        window.withdraw()
        jumphostip = askstring("", "Ingrese la IP de Jumphost (si no la tiene, escriba 'n'):")
        ip = askstring("", "Ingrese la IP del host:")
        if jumphostip == "" or ip == "":
            window.destroy()
        elif 'n' in jumphostip or 'N' in jumphostip:
            login()
        else:
            loginjumphost()
        window.deiconify()
        defaultpage()
        window.mainloop()
            
        
