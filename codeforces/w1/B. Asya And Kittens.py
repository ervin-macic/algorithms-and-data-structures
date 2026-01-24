import sys
def main():
    input = sys.stdin.readline
    n = int(input())
    
    ans = []
    R = [0] * (n+1)
    Rinv = [[] for _ in range(n+1)]
    def make_set(x):
        R[x] = x
        Rinv[x].append(x)
    
    def find_set(x):
        return R[x]

    def union(x, y):
        rx = find_set(x)
        ry = find_set(y)
        if rx == ry:
            return 
        else:
            if len(Rinv[rx]) < len(Rinv[ry]):
                for elem in Rinv[rx]:
                    R[elem] = ry 
                    Rinv[ry].append(elem)
                # Rinv[rx].clear() # maybe unnecessary
            else:
                for elem in Rinv[ry]:
                    R[elem] = rx
                    Rinv[rx].append(elem)
                # Rinv[ry].clear()
            # print(R)
            # print(Rinv)
            # print("--------------------")
    
    # Example: 
    for i in range(1, n+1):
        make_set(i)
    for _ in range(n-1):
        (a,b) = map(int, input().strip().split())
        union(a, b)
    for lst in Rinv:
        if len(lst) == n:
            ans = lst 
            break

    result = " ".join(map(str, ans))
    print(result)

if __name__ == "__main__":
    main()