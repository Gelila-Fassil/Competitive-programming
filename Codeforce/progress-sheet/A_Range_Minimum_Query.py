import sys
import math

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    t = int(input[idx]); idx += 1
    
    for _ in range(t):
        n = int(input[idx]); idx += 1
        arr = list(map(int, input[idx:idx+n])); idx += n
        LOG = math.floor(math.log2(n)) + 2
        st = [[0] * n for _ in range(LOG)]
        for i in range(n):
            st[0][i] = arr[i]
        for k in range(1, LOG):
            length = 1 << k  
            half = 1 << (k-1)  
            for i in range(n - length + 1):
                st[k][i] = min(st[k-1][i], st[k-1][i + half])
        q = int(input[idx]); idx += 1
        output = []
        for _ in range(q):
            i = int(input[idx]); j = int(input[idx+1]); idx += 2
            
            length = j - i + 1
            k = math.floor(math.log2(length))
            ans = min(st[k][i], st[k][j - (1 << k) + 1])
            output.append(ans)
        
        print('\n'.join(map(str, output)))

solve()