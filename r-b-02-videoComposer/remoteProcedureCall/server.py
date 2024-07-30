import json
import math
import os
import socket


def floor(x):
  return math.floor(x)


def nroot(n, x):
  return int(math.pow(x, 1 / n))


def reverse(s):
  return s[::-1]


def validAnagram(str1,str2):
  if len(str1) != len(str2):
    return False
  return str1 == str2[::-1]


def sort(strArr):
  strArr.sort()
  return strArr


def dispatch (method, params):
  if method == 'floor':
    return floor(*params)
  elif method == 'nroot':
    return nroot(*params)
  elif method == 'reverse':
    return reverse(*params)
  elif method == 'validAnagram':
    return validAnagram(*params)
  elif method == 'sort':
    return sort(*params)
  else:
    raise ValueError(f"Unknown method: {method}")


def startServer():
  sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
  server_address = '/tmp/socket_file'
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
        data = connection.recv(1024)
        if data:
          request = json.loads(data.decode('utf-8'))
          print('Received request ', request)
          method = request['method']
          params = request['params']
          request_id = request['id']

          result = dispatch(method, params)
          response = {
            "results": str(result),
            "result_type": "int",
            "id": request_id
          }
          connection.sendall(json.dumps(response).encode('utf-8'))
        else:
          print('no data from', client_address)
          break

    finally:
      print("Closing current connection")
      connection.close()

"""
def test():
  #print(floor(35.546))
  #print(nroot(2, 16))
  #print(reverse("hello"))
  #print(validAnagram("hello","llleh"))
  #print(sort([1,3,3,4,5,2,4]))
  #print(sort(["banana","apple","watermelon","orange"]))
  #print(dispatch("floor", [35.546]))
  #print(dispatch("nroot", [2, 16]))
  #print(dispatch("reverse", ["hello"]))
  #print(dispatch("validAnagram", ["hello", "llleh"]))
  #print(dispatch("sort", [[1, 3, 3, 4, 5, 2, 4]]))
  #print(dispatch("sort", [["banana", "apple", "watermelon", "orange"]]))
"""

if __name__ == "__main__":
  startServer()
  #test()