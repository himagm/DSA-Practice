def palindrome(my_str, start, end):    
    if start >= end:
        return True
    if my_str[start] != my_str[end]:
        return False
    return palindrome(my_str, start+1, end-1)

if __name__ == "__main__":

    test = "MnonM"
    n = len(test)
    res = palindrome(test, 0, n-1)
    print(res)

