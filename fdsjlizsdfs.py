def is_polindrom(my_str):
    '''время выполнения O(n)'''
    my_str = my_str.lower()  # убираем заглавные буквы
    n = len(my_str) // 2
    for i in range(n):  # проходим окошками по слову
        if my_str[i] != my_str[-(i + 1)]:  # создаём окошки и сравниваем буквы в них
            return False
    return True
