import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

try:
  sock.connect(server_address)
except socket.error as err:
  print(err)
  sys.exit(1)

try:
  message = input('Enter your name: ')
  messageBytes = message.encode('utf-8')
  sock.sendall(messageBytes)
  sock.settimeout(30)

  try:
    while True:
      data = str(sock.recv(1048))
      if data:
        print('Server response: '+ data)
      else:
        break
  except(TimeoutError):
    print('Socket timeout, ending listening for server messages')
  except Exception as e:
    print(f"An error occurred: {e}")

finally:
  print('closing socket')
  sock.close()