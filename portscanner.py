import socket

def main():
    # Get the target IP address and port range from the user.
    target_ip = input("Enter the target IP address: ")
    port_range = input("Enter the port range (start-end): ")

    # Split the port range into two integers.
    start_port, end_port = port_range.split("-")

    # Convert the port numbers to integers.
    start_port = int(start_port)
    end_port = int(end_port)

    # Check if the target IP address is valid.
    try:
        socket.inet_aton(target_ip)
    except socket.error:
        print("Invalid IP address.")
        return

    # Check if the port range is valid.
    if start_port > end_port:
        print("Start port must be less than or equal to end port.")
        return

    # Start the port scan.
    print("Scanning...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        # Try to connect to the port.
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, port))

            # The port is open.
            open_ports.append(port)
        except socket.error:
            pass

    # Close the socket.
    sock.close()

    # Print the open ports.
    print("Open ports:", open_ports)

main()