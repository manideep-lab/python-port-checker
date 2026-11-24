import socket

def check_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)

        result = s.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} on {host} is OPEN")
        else:
            print(f"Port {port} on {host} is CLOSED or UNREACHABLE")

        s.close()

    except socket.gaierror:
        print("Invalid hostname!")
    except ValueError:
        print("Invalid port number!")
    except Exception as e:
        print("Error:", e)


host = input("Enter system IP address or hostname: ")

try:
    port = int(input("Enter port number: "))

    if 1 <= port <= 65535:
        check_port(host, port)
    else:
        print("Enter a valid port (1-65535).")

except ValueError:
    print("Please enter a valid number.")
  
