def Palindrom (string: str) -> bool:
    right = len(string) - 1
    left = 0
    while right != left and right - left != 1:
        s1 = string[right]
        s2 = string[left]
        if not s1 == s2:
            return False
        right -= 1
        left += 1
    return True

print(Palindrom("лессооссел"))