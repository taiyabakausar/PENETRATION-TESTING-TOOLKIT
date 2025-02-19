from port_scanner import scan_ports
from brute_forcer import brute_force

def main():
    print("Welcome to the Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    choice = input("Select a module (1 or 2): ")

    if choice == '1':
        target = input("Enter the target IP address: ")
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        open_ports = scan_ports(target, start_port, end_port)
        print(f"Open ports: {open_ports}")

    elif choice == '2':
        url = input("Enter the target URL: ")
        username = input("Enter the username: ")
        password_list = input("Enter the path to the password list (comma-separated): ").split(',')
        password_list = [password.strip() for password in password_list]
        brute_force(url, username, password_list)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()