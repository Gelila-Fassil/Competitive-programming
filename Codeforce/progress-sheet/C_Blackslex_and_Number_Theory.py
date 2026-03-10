import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = [int(x) for x in input_data[idx:idx+n]]
        idx += n
        
        a.sort()
        min_val = a[0]
        
        # Option 1: Make everything 0 (k = min_val)
        res1 = min_val
        
        # Option 2: Make everything min_val (k = smallest difference)
        res2 = 0
        if n > 1:
            # Smallest difference between any a[i] and a[0]
            res2 = a[1] - a[0]
            
        results.append(str(max(res1, res2)))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()