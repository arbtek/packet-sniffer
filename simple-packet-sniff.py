from scapy.all import sniff

#sniff a packet and dump the content
#packet object and we're printing that to the terminal 
def packet_callback(packet):
    print(packet.show())

#main function 
#filter for tcp, udp, w/e inside sniff
#you can specify interface w/ iface
#only doing this for one packet (count=1)
def main():
    sniff(prn=packet_callback, count=1)

#hello world of scapy
#can do mitm, etc from this
if __name__ == '__main__':
    main()