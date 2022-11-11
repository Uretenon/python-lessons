def processing(lst):
    i = 0
    lst_string = ""  # строчка на вывод
    while i < len(lst):
        indx = 0
        count = 0
        real_num = False
        for char in lst[i]:
            if char == ".":  # сначала проверяем на вещественные числа
                real_num = True
            elif char.isdigit():  # проверка на количество цифр в числе
                count += 1
                indx = lst[i].index(char)
        if any(num.isdigit() for num in lst[i]) and not real_num:  # если есть хоть какая-то цифра в элементе листа, и число целое
            if count == 1:  # если элемент - цифра, то прибавим 0 в листе
                lst[i] = lst[i][:indx] + '0' + lst[i][indx:]
            lst_string += f'"{lst[i]}" '  # добавим числовой элемент в строку на вывод
            lst.insert(i, '"')
            lst.insert(i + 2, '"')
            i += 2
        else:
            if lst[i] != '"':
                lst_string += f'{lst[i]} '
            i += 1
    print("\nНеобходимо его обработать - ✓\n", lst)
    print("Обособить каждое целое число кавычками - ✓\nВещественные не трогаем - ✓\nДополнить нулём до двух целочисленных разрядов - ✓\n", lst_string)


lst = ['в', '5', 'часов', '17.5', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print("Дано:",lst)
processing(lst)
