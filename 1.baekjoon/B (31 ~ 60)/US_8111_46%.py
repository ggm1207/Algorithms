import sys

MIS = lambda : int(sys.stdin.readline())

onezeroList = []

base = [1]
i = 0
while(i <= 10):
  onezeroList += base
  nexts = []
  print(i)
  for bb in base:
    nexts.append(bb*10)
    nexts.append(bb*10 + 1)
  base = nexts
  i += 1
print(onezeroList[5:])
  


def fake(N):
  print('BRAK')

if __name__ == "__main__":
  T = MIS()
  for _ in range(T):
    N = MIS() # N <= 20000 (자연수)
    fake(N)