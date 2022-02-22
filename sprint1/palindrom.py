import string

def is_palindrome(line: str) -> bool:
    new_line = ''.join(i.lower() for i in line if i in string.ascii_letters)
    if new_line == new_line[::-1]:
        return True
    else:
        return False

print(is_palindrome(input().strip()))