def ip_to_bytes(ip_str):
    
    parts = [int(x) for x in ip_str.strip().split(".")]
    return bytes(parts)  #to_bytes can only be used to convert one elements each time.

def compute_checksum(pseudo_header, tcp_data):
    
    # zero out checksum
    tcp_zero_cksum = tcp_data[:16] + b'\x00\x00' + tcp_data[18:]

    # force to be even
    if len(tcp_zero_cksum) % 2 == 1:
        tcp_zero_cksum += b'\x00'

    # form about_to_check result
    data = pseudo_header + tcp_zero_cksum

    # sum
    total = 0
    for offset in range(0, len(data), 2):
        word = int.from_bytes(data[offset:offset + 2], "big")
        total += word
        total = (total & 0xffff) + (total >> 16)

    # this execute a mapping so they all fit into 16 bits.
    total = (total & 0xffff) + (total >> 16)

    # mask to 16 bits
    return (~total) & 0xffff

    # The checksum never needs the exact original sum. 
    # It only needs the sum modulo 0xFFFF (65535), and folding preserves that.

def validate_tcp_packet(addrs_filename, data_filename):

    # Read IP addresses file
    with open(addrs_filename, "r") as fp:
        line = fp.read().strip()
        src_ip_str, dest_ip_str = line.split()

    src_bytes = ip_to_bytes(src_ip_str)
    dest_bytes = ip_to_bytes(dest_ip_str)

    # Read raw TCP data file
    with open(data_filename, "rb") as fp:
        tcp_data = fp.read()
    tcp_length = len(tcp_data)

    orig_checksum = int.from_bytes(tcp_data[16:18], "big")

    # Source IP (4) + Dest IP (4) + Zero (1) + Protocol (1) + TCP Length (2)

    pseudo_header = src_bytes + dest_bytes + b'\x00' + b'\x06' + tcp_length.to_bytes(2, "big")

    calculated_checksum = compute_checksum(pseudo_header, tcp_data)
    return calculated_checksum == orig_checksum

def main():

    for i in range(10):
        addrs_file = f"tcp_data/tcp_addrs_{i}.txt"
        data_file = f"tcp_data/tcp_data_{i}.dat"

        if validate_tcp_packet(addrs_file, data_file):
            print("PASS")
        else:
            print("FAIL")

if __name__ == "__main__":
    main()