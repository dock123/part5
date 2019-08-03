"""
 Список [16, -17, 2, 78.7, False, False, {‘True’: True}, 555, 12, 23, 42, ‘DD’]
Функция, принимает на вход список
-выбирает из него все int и float
-составить из него новый список, отсортированный от наименьшего значения большему.
"""
#ver 0.1
new_list=[]

def func(arg):
    for i in arg:
        if type(i) is int or type(i) is float:
            new_list.append(i)
    new_list.sort()
    return print(new_list)
    pass

func([16, -17, 2, 78.7, False, False, {"True": True}, 555, 12, 23, 42, "DD"])




#ver 0.2

def func(arg):
    new_list=[i for i in arg if isinstance(i,(int,float))]
    new_list.sort()
    return new_list

print(func([16, -17, 2, 78.7, False, False, {"True": True}, 555, 12, 23, 42, "DD"]))