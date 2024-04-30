s = (input())
def count_substrings(S):
    n = len(S)
    count = 0
    seen = set()
    for start in range(n):
        for end in range(start + 1, n + 1):
            substring = S[start:end]
            if substring not in seen:
                seen.add(substring)
                count += 1
    return count

print(count_substrings(s))  
        
        
        
    
        
        
