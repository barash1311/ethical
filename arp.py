import scapy.all as scapy
import optparse
'''1.arp request
2.broadcast
3.responser
4. show'''
def userinp():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest="ip_address",help="add address")
    (user_input,argument)=parse_object.parse_args()
    if not user_input.ip_address:
        print("enter the ip address")
    return user_input
def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list)=scapy.srp(combined_packet,timeout=1)
    answered_list.summary()


user_ip_address=userinp()
scan_my_network(user_ip_address.ip_address)