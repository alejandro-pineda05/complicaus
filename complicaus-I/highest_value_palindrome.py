
def highestValuePalindrome(s, n, k):
    nums = list(map(int, list(s)))
    changes = []
    for i in range(n // 2):
        left = nums[i]
        right = nums[n-1 - i]
        if left != right:
            changes.append(i)
    
    if k < len(changes):
        return "-1"

    k -= len(changes)
    for i in range(n // 2):
        if k >= 1 and i in changes:
            k += 1

        if k < 2:
            break
        
        if nums[i] != 9:
            nums[i] = 9
            k -= 1
        if nums[n-1 - i] != 9:
            nums[n-1 - i] = 9
            k -= 1
    
    for i in changes:
        left = nums[i]
        right = nums[n-1 - i]
        if left < right:
            nums[i] = right
        else:
            nums[n-1 - i] = left
    
    if n % 2 == 1 and k > 0:
        nums[n//2] = 9
        
    return "".join(list(map(str, nums)))
