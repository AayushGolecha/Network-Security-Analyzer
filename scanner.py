import socket
import subprocess

def port_scan(target, ports):
    print(f"Scanning target: {target}")
    open_ports = []
    closed_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: Open")
                open_ports.append(port)
            else:
                print(f"Port {port}: Closed")
                closed_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()
        except socket.gaierror:
            print("Hostname could not be resolved. Exiting...")
            exit()
        except socket.error:
            print("Couldn't connect to server. Exiting...")
            exit()
    return open_ports, closed_ports

def vulnerability_scan(target):
    print(f"Scanning for vulnerabilities on target: {target}")
    # Here you can add more sophisticated vulnerability checks
    # For simplicity, let's just ping the target
    response = subprocess.run(['ping', '-c', '4', target], stdout=subprocess.PIPE)
    if response.returncode == 0:
        print("Target is reachable")
    else:
        print("Target is unreachable")

def main():
    target = input("Enter target IP address: ")
    # ports = [21, 22, 80, 443]  # Example list of ports to scan
    p=list(input("Enter the ports to scan: ").split(","))
    temp=map(int,p)
    ports = list(temp)

    open_ports, closed_ports = port_scan(target, ports)
    vulnerability_scan(target)

if __name__ == "__main__":
    main()
1