
import subprocess
import optparse
import re
print("started")
def input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="macchange to ")
    parse_object.add_option("-m","--macaddress",dest="macaddress",help="macc")
    return parse_object.parse_args()

def macc_change(interface,macaddress):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",macaddress])
    subprocess.call(["ifconfig",interface,"up"])

def control(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    newmac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if newmac:
        return newmac.group(0)
    else:
        return None
(user_input,argument)=input()
macc_change( user_input.interface,user_input.macaddress)
final=control(user_input.interface)
if final==user_input.macaddress:
    print("success")
    subprocess.check_output(["ifconfig"])
else:
    print("unsuccessful")