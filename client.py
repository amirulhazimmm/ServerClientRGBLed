import socket, sys, string

## To create Socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to connect")
    sys.exit();

print("[CLIENT]Socket Created")

## To declare the host and port
host = "localhost"
port = 25000

## Function to connect
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("[CLIENT]Hostname could not be resolved")
    sys.exit();

print("[CLIENT]IP Address: " + remote_ip)

s.connect((remote_ip, port))

print("[CLIENT]Socket Connected to " + host + " using IP " + remote_ip + "\n")

## Function to receive msg from server
rcvMsg = s.recv(4096)
rcvMsg = "<Server>" + rcvMsg.decode() + "\n"
print(rcvMsg)


## Function to send msg to server
message = input("<Client> ")

try:
    s.send(message.encode())
except socket.error:
    print("[CLIENT]Did not send successfully")
    sys.exit()

print("[CLIENT]Message Sent Successfully")


