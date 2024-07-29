import scapy.all as scapy

def sniff_packets(interface,filter=None):
    scapy.sniff(iface=interface,storage=False,prn=process_packets,filter=None)
    
def process_packets(packets):
    if packets.haslayer(scapy.IP):
        ip_src=packets[scapy.IP].src
        ip_dst=packets[scapy.IP].dst
        protocol=packets[scapy.IP].pro
        print(f" ip packets: {ip_src} --> {ip_dst}  Protocol :{protocol}")
        
    if packets.haslayer(scapy.TCP):
        srd=packets[scapy.TCP].sport
        dst=packets[scapy.TCP].dport
         print(f" TCP packets: {ip_src} :{srd} --> {ip_dst}:{dst}")
        
    if packets.haslayer(scapy.UDP):
        Ssrd=packets[scapy.UDP].sport
        Ddst=packets[scapy.UDP].dport
         print(f" TCP packets: {ip_src} :{Ssrd} --> {ip_dst}:{Ddst}")     
         
    else:
        print(f" ip packets: {ip_src} --> {ip_dst}  Protocol :{protocol}")
         
         
def main():
    interface=input("enter the interface to scan")
    print("\n Starting packet sniffing......")
    sniff_packets(inteface,filter=None)
    
if __name__=="__main__":
    main()
