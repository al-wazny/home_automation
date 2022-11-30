from scapy.all import ARP, Ether, srp

ip = "192.168.2.0/24"

#create the package
arp = ARP(pdst=ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
package = ether/arp

#thanks to the specified subnet mask, all possible hosts within the network will receive the package and responde
result = srp(package, timeout=3, verbose=0)[0] 

for _, received_packages in result:
    #print the mac address of all devices inside the network
    print(received_packages.hwsrc) 