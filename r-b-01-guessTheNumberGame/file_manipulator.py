import sys
import re
import itertools


# inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成
def reverseInputToOutput(inputFile,outputFile):
  inputArr = readFile(inputFile)
  OutputArr = createOutputArray(inputArr,False)
  writeFile(outputFile,OutputArr)


# inputpath にあるファイルのコピーを作成し、outputpath として保存
def copyInputToOutput(inputFile,outputFile):
  inputArr = readFile(inputFile)
  OutputArr = createOutputArray(inputArr,True)
  writeFile(outputFile,OutputArr)


# inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製
def duplicateContentsInput(inputFile,n):
  inputArr = readFile(inputFile)
  OutputArr = []
  for i in range(n):
    OutputArr.append(createOutputArray(inputArr,True))

  OutputArr = list(itertools.chain.from_iterable(OutputArr))
  writeFile(inputFile,OutputArr)


# inputFile内の"needle"を"newstring"に置き換える
def replaceStringInputNeedle(inputFile):
  inputArr = readFile(inputFile)
  outputArr = [line.replace('needle', 'newstring') for line in inputArr]
  writeFile(inputFile, outputArr)


# ファイル読み込み処理
def readFile(path):
  try:
    with open(path,'r') as f:
      file = f.readlines()
    return file
  except Exception as e:
    print(f"ERROR: readFile: could not read file {path}: {e}")
    sys.exit(1)


# ファイル書き込み処理
def writeFile(path,contents):
  try:
    with open(path,'w') as f:
      f.write('\n'.join(contents))
    print(f"SUCCESS: writeFile: output file is {path}")
    sys.exit(0)
  except Exception as e:
    print(f"ERROR: writeFile: could not read file {path}: {e}")
    sys.exit(1)


# 出力する文字列を生成
def createOutputArray(inputArr,order):
  OutputArr = []
  if order:
    for inputWord in inputArr:
      if inputWord.strip() and inputWord != "\n":
        OutputArr.append(inputWord.strip())
  else:
    for inputWord in inputArr:
      if inputWord.strip() and inputWord != "\n":
        OutputArr.append(inputWord.strip()[::-1])
  return OutputArr


# メイン処理
if __name__ == "__main__":
  if len(sys.argv) != 4:
    print(f"ERROR: Please enter only 3 arguments")
    sys.exit(1)

  # 引数で処理を分岐するようにする
  f = sys.argv[1]
  inputFile = sys.argv[2]
  outputFile = sys.argv[3]

  if f == 'reverse':
    reverseInputToOutput(inputFile,outputFile)
  elif f == 'copy':
    copyInputToOutput(inputFile,outputFile)
  elif f == 'duplicate':
    sys.stdout.buffer.write(b"How many times to duplicate?\n")
    sys.stdout.flush()
    n = int(sys.stdin.buffer.readline())
    if isinstance(n,int) == False:
      print(f"ERROR: could not read option")
      sys.exit(1)
    duplicateContentsInput(inputFile,n)
  elif f == 'replace':
    replaceStringInputNeedle(inputFile)
  else:
    print(f"ERROR: command not found")
    sys.exit(1)
