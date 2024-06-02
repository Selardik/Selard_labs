from collections import deque

def find_smallest_multiple_of_n(N):
    if N <= 0:
        return "No"
    
    q = deque()
    visited = set()
    
    q.append("1")
    
    while q:
        current = q.popleft()
        
        remainder = 0
        for c in current:
            remainder = (remainder * 10 + int(c)) % N
        
        if remainder == 0:
            return current
        
        if remainder not in visited:
            visited.add(remainder)
            q.append(current + "1")
    
    return "No"

def main():
    N = int(input("Введите число N: "))
    
    result = find_smallest_multiple_of_n(N)
    print(result)
    
    print("Дядькин Владислав Вениаминович РПИб-о23")

if __name__ == "__main__":
    main()
