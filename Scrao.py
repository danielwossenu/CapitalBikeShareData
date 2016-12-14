def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            is_palindrome(s[1:-1])
        else:
            return False


print is_palindrome("abba")
print is_palindrome("abab")
