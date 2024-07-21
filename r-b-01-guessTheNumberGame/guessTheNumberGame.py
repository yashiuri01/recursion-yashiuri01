import sys
import random
import time


def createRandomInt(arg1, arg2):
  return random.randint(arg1, arg2)

def checkUserAnswer(randInt):
  answer = 0
  i = 10

  while i > 0:
    print(f"You only have {i} answers left")
    sys.stdout.buffer.write(b"What is the random integer that is output?\n")
    sys.stdout.flush()
    answer = int(sys.stdin.buffer.readline())
    time.sleep(0.5)

    if (randInt == answer):
      print(f"Your answer is correct!")
      print(f"random integer is {randInt}!\n")
      sys.exit(0)
    else:
      i -= 1
      print(f"Your answer is incorrect.\n")

  if i < 0:
    print(f"You can no longer answer")
    print(f"random integer is {randInt}\n")
    sys.exit(1)


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print(f"ERROR: Please enter only 2 arguments")
    sys.exit(1)

  arg1 = int(sys.argv[1])
  arg2 = int(sys.argv[2])
  randInt = createRandomInt(arg1, arg2)

  checkUserAnswer(randInt)
