import sys
def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    n = int(data[idx])
    idx +=1
    nums = list(map(int,data[idx:idx+n]))
    idx +=n
    