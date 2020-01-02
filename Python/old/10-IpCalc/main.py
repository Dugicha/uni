def dec_to_bin(integer):
	if (integer < 0): return 0
	quotent = integer
	output = ""

	while (True):
		remainder = quotent % 2
		output = str(remainder) + output

		if (quotent == remainder): break

		quotent = int((quotent - remainder) / 2)

	return output

def separate_bytes(arg):
	num = str(arg)
	octets = []
	for i in range(0, 25, 8):
		octets.append(num[i:i+8])
	ret = "{}.{}.{}.{}".format(*octets)
	return ret

def get_ip_binary(ip):
	parts = ip.split(".")
	octets = []
	for part in parts:
		octets.append(dec_to_bin(int(part)))
	return "{}.{}.{}.{}".format(*octets)

def get_subnet_mask_binary(cidr):
	ret = "1" * cidr
	for i in range(cidr, 32):
		ret += "0"
	return int(ret)

def get_subnet_mask_decimal(cidr):
	mask = str(get_subnet_mask_binary(cidr))
	octets = []
	for i in range(0, 25, 8):
		octets.append(int(mask[i:i+8], 2))
	return "{}.{}.{}.{}".format(*octets)
	
#WRONG, IP AND MASK DON'T HAVE THE SAME LENGTHS ALL THE TIME, DUMB METHOD
def get_subnet_id_binary(ip, mask):
	ret = ""
	for i in range(0, len(ip)):
		if (ip[i] == "."):
			ret += "."
		else:
			ret += str(int(ip[i]) * int(mask[i]))
	return ret

def get_subnet_id(ip, mask):
	octets = get_subnet_id_binary(ip, mask).split(".")
	parts = []
	for octet in octets:
		parts.append(str(int(octet, 2)))
	return ".".join(parts)

ip = input("Input ip address: ")
cidr = int(input("Input CIDR: "))
ipBinary = get_ip_binary(ip)
subnetMask = separate_bytes(get_subnet_mask_binary(cidr))
subnetId = get_subnet_id_binary(ipBinary, subnetMask)

print("IP Address (binary): {}".format(ipBinary))
print("Subnet Mask: {}".format(get_subnet_mask_decimal(cidr)))
print("Subnet Mask (binary): {}".format(subnetMask))
print("Subnet ID (Network Address): {}".format(get_subnet_id(ipBinary, subnetMask)))
