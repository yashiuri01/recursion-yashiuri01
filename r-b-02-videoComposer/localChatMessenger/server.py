import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/tmp/socket_file'
fake = Faker()

try:
  os.unlink(server_address)
except FileNotFoundError:
  pass

print('Starting up on {}'.format(server_address))

sock.bind(server_address)
sock.listen(1)

while True:
  connection, client_address = sock.accept()

  try:
    print('connection from ', client_address)

    while True:
      data = connection.recv(10)
      if data:
        data_str = data.decode('utf-8')
        print('Received ' + data_str)
        response = f"Processing {data_str} //"
        reply = f"Thank you for telling me your name! My name is {fake.name()}"
        connection.send(response.encode())
        connection.send(reply.encode())
      else:
        print('no data from', client_address)
        break

  finally:
    print("Closing current connection")
    connection.close()
