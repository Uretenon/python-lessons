lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(lst)
for item in lst:
    print(f'Привет, {item[item.rindex(" ")+1:].lower().capitalize()}!')
