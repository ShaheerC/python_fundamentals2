def letters(string):
    x = int(len(string))
    if x > 7:
        return False
    else:
        return True

print(letters('1234567'))
print(letters('12345678'))
print(letters('123456789'))