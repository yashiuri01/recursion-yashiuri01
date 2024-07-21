import markdown
import sys


def main():
  sys.stdout.buffer.write(b"Please input markdown text\n")
  sys.stdout.flush()
  inputText = sys.stdin.readline().strip()

  html = markdown.markdown(inputText)
  print(html)


if __name__ == "__main__":
  main()