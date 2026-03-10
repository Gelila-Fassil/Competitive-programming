import sys

def solve():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        a = input[idx:idx+n]
        idx += n
        b = input[idx:idx+n]
        idx += n
        
        # Map member ID to their position in the 22:00 list (b)
        pos_in_b = {member: i for i, member in enumerate(b)}
        
        # Find the length of the longest prefix of 'a' that maintains 
        # relative order in 'b'
        count = 0
        last_pos = -1
        
        for member in a:
            current_pos = pos_in_b[member]
            if current_pos > last_pos:
                count += 1
                last_pos = current_pos
            else:
                # Once the sequence is broken, no further members 
                # can be part of the "untouched" set
                break
        
        results.append(str(n - count))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()