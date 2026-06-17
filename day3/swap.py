import sys

def solve():
    t_str = input("Enter number of test cases (t): ")
     out = []
     for case_num in range(1, t + 1):
        print(f"\n--- Test Case #{case_num} ---")
        n = int(input("  Enter number of items (n): "))
        A = [int(x) for x in input("  Enter the shelf array elements (separated by space): ").split()]
        unique_elements = set(A)
        U = len(unique_elements)
        target_transitions = U - 1
        initial_transitions = 0
        for i in range(n - 1):
            if A[i] != A[i+1]:
                initial_transitions += 1
            if initial_transitions == target_transitions:
            out.append("YES")
            print("  -> Already grouped correctly!")
            continue
        if initial_transitions - target_transitions > 4:
            out.append("NO")
            print("  -> Too many disjoint groups to fix with 1 swap.")
            continue
        block_types = []
        if n > 0:
            block_types.append(A[0])
            for i in range(1, n):
                if A[i] != A[i-1]:
                    block_types.append(A[i])
        type_counts = {}
        for b_type in block_types:
            type_counts[b_type] = type_counts.get(b_type, 0) +1
        candidates = []
        for i in range(n):
            if type_counts.get(A[i], 0) > 1:
                candidates.append(i)
        possible = False
        for i in candidates:
            for j in range(n):
                if A[i] == A[j]:
                    continue
                
             affected_pairs = set()
                for pos in (i, j):
                    if pos > 0:
                        affected_pairs.add((pos - 1, pos))
                    if pos < n - 1:
                        affected_pairs.add((pos, pos + 1))
                        
               old_mismatches = sum(1 for u, v in affected_pairs if A[u] != A[v]
              A[i], A[j] = A[j], A[i]

                new_mismatches = sum(1 for u, v in affected_pairs if A[u] != A[v])
       
                A[i], A[j] = A[j], A[i]

                if initial_transitions - old_mismatches + new_mismatches == target_transitions:
                    possible = True
                    break
            if possible:
                break
                
        result = "YES" if possible else "NO"
        out.append(result)
        print(f"  -> Can be fixed in at most one swap? {result}")
        
    print("\n=== Final Summary Output ===")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
