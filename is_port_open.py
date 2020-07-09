import socket
def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      print(ip + " " + str(port) + " " + "True")
   except:
      print(ip + " " + str(port) + " " + "False")

with open("serverlist.txt") as serverlist:
    for line in serverlist:
        ip, port = line.strip().split(",")
        isOpen(ip, port)

