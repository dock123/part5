"""
Домашнее задание:

1)
Функция принимает аргумент, проверяет тип. Если это не список или кортеж,
выводит значение типа. Если же кортеж или список, то нужно определить длину.
Если она больше 1, то вывести информацию о том, сколько разных типов данных
там содержится. («Список/кортеж состоит из None, int. str» и т.д.)
"""
types_arg=[]
def func(arg):
    if type(arg) is tuple or type(arg) is list:
        if len(arg)>1:
            for i in arg:
                types_arg.append(str(type(i)))
            return print("Это ",type(arg)," его длина=",len(arg),", он содержит типы: ",set(types_arg))
        else:
            return print("длина ", len(arg),"тип ", type(arg))
    else:
        return print("типы ",type(arg))


func([16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD'])
