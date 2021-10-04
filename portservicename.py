import sys         # Disclaimer: This script is for educational purposes only.
import socket
import pyfiglet


def disp():
    print("\n"+"*"*65) 
    print(pyfiglet.figlet_format("          DcapPort"))
    print("*\t\t\tD_captainkenya\t\t\t\t*")
    print("*\t\t    Dcaptainkenya@gmail.com\t\t\t*")
    print("*\t      https://www.D-captainkenya.github.io\t\t*")
    print("*"*65)
    print("\nCheck Common Port Service Names")
    print("\n"+"-"*50)
    print("\tPort\t\tService")
    print("-"*50)
    input_port()

def usage():
    print("please specify a port numbers correctly!")
    print("\nUSAGE:")
    print("\tpython portservice.py XW XXXX XZ XYZ")
    print("EXAMPLE\n\t  Python portservice.py 80 21\n")
    sys.exit()

def input_port():
    try:
        # get port arguments
        n = len(sys.argv)
        if n < 1:
            usage()
        elif n > 1:
            portlis = [int(port) for port in sys.argv[1:]]
            port_name(portlis)
        else:
            usage()
            sys.exit()
    except ValueError:
        usage()
    except KeyboardInterrupt:
        print("\nKeyboard interrupted. \nExiting...")
        sys.exit()


def port_name(portlis):
    for p in portlis:
        try:
            print(f"\t{p} \t--> \t" f"{socket.getservbyport(p, 'tcp')}")
            try:
                print(f"\t{p} \t--> \t" f"{socket.getservbyport(p, 'udp')} (UDP)")
            except:
                pass
        except:
            try:
                print(f"\t{p} \t--> \t" f"{socket.getservbyport(p, 'udp')}")
            except:
                print(f"\t{p} \t-->  \tUNIDENTIFIED")
    print("\nRarely, ports have different names depending on the protocol using it.\nI did my best.")
    

if __name__ == "__main__":
    disp()