import socket
from IPy import IP

def scan(ipaddress,port):
	try:
		sock=socket.socket()
		sock.settimeout(0.5)
		sock.connect((ipaddress, port))
		try:
			banner = get_banner(sock)
			print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
		except:
			print("[+]Open Port " + str(port))
	except:
		pass


def  get_banner(s):
	return s.recv(1024)


def scan_ports(ip):
	max_ports=int(input("How many ports: "))
	print("-----------Scanning----------")
	for ports in range(1, max_ports):
		scan(ip,ports)

ip=input("Give me the IP: ")
scan_ports(ip)

