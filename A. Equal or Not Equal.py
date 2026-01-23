import sys
def main():
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        s = input().strip()
        num_N = 0
        for c in s:
            if c == 'N':
                num_N += 1
            if num_N > 1:
                print("YES")
                break
        if num_N == 1:
            print("NO")
        elif num_N == 0:
            print("YES")
        

if __name__ == "__main__":
    main()
# 4
# EEE
# EN
# ENNEENE
# NENN
