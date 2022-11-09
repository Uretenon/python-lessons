def delABC(text):
    text_list = text.split()
    print(text_list)
    print(" ".join(list(filter(lambda word:  'абв' not in word, text_list))))


delABC("забвение зимбабве незабвен капалан абвис бавина")
