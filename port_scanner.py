import socket
    
def get_open_ports(target, port_range, verbose=None):
    open_ports = []
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start, end = port_range
    
    def port_scan(port):
        try:
            s.connect((target, port))
            return True
        except: 
            return False
    
    for i in range(start, (end+1)):
        port = i
        if port_scan(port):
            print(f"The port {port} is Open.")
            open_ports.append(port)
        else:
            print(f'The port {port} is Closed.')

    return(open_ports)