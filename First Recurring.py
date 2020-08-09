def first_recurring(str):
    counts = {}
    for char in str:
        if char in counts:
            return char
        counts[char] = 1
    return None


str = 'ABCAB'
print(first_recurring(str))
