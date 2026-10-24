import sys
import json
import math


def ipv4_to_value(ipv4_addr):

    value = 0;
    for part in ipv4_addr.split("."):
        value = (value << 8)
        value = value + int(part)
    return value    


def get_subnet_mask_value(slash):


    piece = slash.split("/")
    len = int(piece[-1])
    mask = 0
    for i in range (len):
        mask = (mask << 1) | 1
    zeroes = 32 - len
    mask = mask << zeroes
    return mask

def ips_same_subnet(ip1, ip2, slash):
    
    val1 = ipv4_to_value(ip1)
    val2 = ipv4_to_value(ip2)
    mask = get_subnet_mask_value(slash)
    return (val1 & mask) == (val2 & mask)


def find_router_for_ip(routers, ip):
    """
    Searches the router dictionary to find which router serves the subnet
    containing the given IP address.
    """
    for router_ip in routers:
        info = routers[router_ip]
        slash = info["netmask"]
        if ips_same_subnet(router_ip, ip, slash):
            return router_ip
    return None



def dijkstras_shortest_path(routers, src_ip, dest_ip):
    
    # 1. Identify first and last routers.
    src_router = find_router_for_ip(routers, src_ip)
    dest_router = find_router_for_ip(routers, dest_ip)

    # 2. Handle same subnet.
    if not src_router or not dest_router or src_router == dest_router:
        return []

    # 3. Initialization
    to_visit = set(routers.keys())
    distance = {r: math.inf for r in routers}
    parent = {r: None for r in routers}

    distance[src_router] = 0

    # 4. Dijkstra's Loop
    while to_visit:
        # Import min dist node.
        current = min(to_visit, key=lambda node: distance[node])

        # Unreachable case.
        if distance[current] == math.inf:
            break

        to_visit.remove(current)

        # Algorithm finish
        if current == dest_router:
            break

        # Relax
        connections = routers[current].get("connections", {})
        for neighbor, conn_info in connections.items():
            if neighbor in to_visit:
                weight = conn_info.get("ad", 110)  # Default AD = 110
                alt = distance[current] + weight
                if alt < distance[neighbor]:
                    distance[neighbor] = alt
                    parent[neighbor] = current

    # 5. Path Reconstruction
    if distance[dest_router] == math.inf:
        return []

    path = []
    curr = dest_router
    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    path.reverse()
    return path


#------------------------------
# DO NOT MODIFY BELOW THIS LINE
#------------------------------
def read_routers(file_name):
    with open(file_name) as fp:
        data = fp.read()

    return json.loads(data)

def find_routes(routers, src_dest_pairs):
    for src_ip, dest_ip in src_dest_pairs:
        path = dijkstras_shortest_path(routers, src_ip, dest_ip)
        print(f"{src_ip:>15s} -> {dest_ip:<15s}  {repr(path)}")

def usage():
    print("usage: dijkstra.py infile.json", file=sys.stderr)

def main(argv):
    try:
        router_file_name = argv[1]
    except:
        usage()
        return 1

    json_data = read_routers(router_file_name)

    routers = json_data["routers"]
    routes = json_data["src-dest"]

    find_routes(routers, routes)

if __name__ == "__main__":
    sys.exit(main(sys.argv))