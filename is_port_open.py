import socket
def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      print("{}, {}, True".format(ip, port))
   except:
      print("{}, {}, False".format(ip, port))

with open("serverlist.txt") as serverlist:
    for line in serverlist:
        ip, port = line.strip().split(",")
        isOpen(ip, port)

