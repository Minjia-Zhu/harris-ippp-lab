def count(letter,l):
    count = 0
    for i in l:
        if i == letter:
            count += 1
    return count


def better_count(s,l):
    d = {}
    for letter in s:
        d[letter]=count(letter,l)
    return d
