class Solution:
    def search(self, arr, targetVal):
        low = 0
        high = len(arr) - 1
    
        while low <= high:
            mid = (low + high) // 2
    
            if arr[mid] == targetVal:
                return mid
    
            if arr[mid] < targetVal:
                low = mid + 1
            else:
                high = mid - 1
    
        return -1
    