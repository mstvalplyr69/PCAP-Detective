import scapy.all as scapy
import argparse

# Define the function for creating the packets
def create_tagged_packet(target_ip, target_port, packet_size, tag_text):
    """
    Create a UDP packet with a loud identifier and a specific length.
    """
    # Create an IP layer with the destination as the target IP
    ip = scapy.IP(dst=target_ip)
    
    # Create a UDP layer with custom ports
    udp = scapy.UDP(sport=12345, dport=target_port)
    
    # Create the payload with the tag text and pad it to the desired packet size
    payload = tag_text.ljust(packet_size, 'X')  # Pad with 'X' if needed
    packet = ip / udp / payload
    
    return packet

# Function to run the script and handle input/output
def run_pcap_detective():
    # Setup Argument Parser
    parser = argparse.ArgumentParser(description="PCAP Detective - Tag packets for analysis")
    parser.add_argument("hostloc", help="Specify LOCAL or REMOTE machine", choices=["LOCAL", "REMOTE"])
    parser.add_argument("target_ip", help="IP address of the target machine")
    parser.add_argument("target_port", type=int, help="Target port number")
    parser.add_argument("packet_size", type=int, help="Size of the packet in bytes")
    parser.add_argument("tag_text", help="Loud text to insert into packet payload")
    args = parser.parse_args()

    # Create tagged packet
    tagged_packet = create_tagged_packet(args.target_ip, args.target_port, args.packet_size, args.tag_text)
    
    # Display the packet in a readable format
    print(f"Created packet with target IP {args.target_ip}:")
    tagged_packet.show()

    # Optionally, send the packet
    scapy.send(tagged_packet)  # Uncomment to actually send the packet

# Call the function if the script is executed
if __name__ == "__main__":
    run_pcap_detective()

