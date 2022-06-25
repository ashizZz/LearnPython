def is_palindrome(string):
    start_index = 0
    end_index = len(string) - 1
    while end_index >= start_index:
        if string[start_index] != string[end_index]:
            return False
        start_index += 1
        end_index -= 1
        return True
    value = input('Enter the string for palindrome:')
    ans = is_palindrome(value)
    if ans is True:
        return True
    else:
        return False


c = is_palindrome('madam')
print(c)
