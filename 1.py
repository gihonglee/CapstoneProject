def feq_of_chars(s):
    d = {}
    for wrd in s.split():
        for char in wrd:
            if char in wrd:
                d[char] += 1
            else:
                d[char] = 1
        return d

feq_of_chars("gihong")
