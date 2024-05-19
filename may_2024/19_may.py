from typing import List

class Solution:
    def findClosest(self, n: int, k: int, arr: List[int]) -> int:
        l, r = 0, n - 1
        
        while l < r:
            m = l + (r - l) // 2
            if arr[m] == k:
                return arr[m]
            elif arr[m] < k:
                l = m + 1
            else:
                r = m
        
        # l is the position where arr[l] >= k or the end of the array
        if l > 0 and (arr[l] > k or arr[l] == k and l < n):
            l -= 1
        
        if l < n - 1 and abs(arr[l + 1] - k) < abs(arr[l] - k):
            return arr[l + 1]
        elif l < n - 1 and abs(arr[l + 1] - k) == abs(arr[l] - k):
            return arr[l + 1]
        
        return arr[l]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    n = 6
    k = 7
    arr = [1, 3, 5, 6, 8, 9]
    print(solution.findClosest(n, k, arr))  # Output: 6
    
    # Test case 2
    n = 6
    k = 10
    arr = [1, 3, 5, 6, 8, 9]
    print(solution.findClosest(n, k, arr))  # Output: 9
    
    # Test case 3
    n = 6
    k = 4
    arr = [1, 3, 5, 6, 8, 9]
    print(solution.findClosest(n, k, arr))  # Output: 3

    # Example from the problem statement
    # Test case 4
    n = 4
    k = 4
    arr = [1, 3, 6, 7]
    print(solution.findClosest(n, k, arr))  # Output: 3

    # Test case 5
    n = 7
    k = 4
    arr = [1, 2, 3, 5, 6, 8, 9]
    print(solution.findClosest(n, k, arr))  # Output: 5
