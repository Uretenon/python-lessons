def encodeRLE(text):

    encoding = ''
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + text[i]
        i += 1
    return encoding


def decodeRLE(text):

    decoding = ''
    i = 0
    while i < len(text):
        count = ""
        while text[i].isdigit():
            count = count + text[i]
            i += 1
        count = int(count)
        for j in range(count):
            decoding = decoding + text[i]
        j = 0
        i += 1
    return decoding


text = "aaaaabbcccddaaa, rrrrraaaavvvv"
k = encodeRLE(text)
print(k)
print(decodeRLE(k))
print(84 // 28 % 2 == 0)