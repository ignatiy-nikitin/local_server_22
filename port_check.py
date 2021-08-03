import socket


def is_port_busy(ip, port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, port))
      s.shutdown(2)
      return True
   except:
      return False
