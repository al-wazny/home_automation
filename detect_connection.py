from scapy.all import ARP, Ether, srp

ip = "192.168.2.33/24"

arp = ARP(pdst=ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0] #thanks to the specified subnet mask, all possible hosts within the network will receive the package and responde

for _, received_packages in result:
    print(received_packages.hwsrc) #print the mac address of all devices inside the network