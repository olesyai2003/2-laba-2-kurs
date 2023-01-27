# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    def f(func):
        def g(b, chars=' !?'):
            tmp = ''.join(map(lambda x: x if x not in chars else '-', func(b)))
            while '--' in tmp:
                tmp = tmp.replace('--', '-')
            return tmp

        return g

    @f
    def h(t):
        t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
             'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
             'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
             'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
        return ''.join(map(lambda x: t.get(x, x), a.lower()))

    print('Введите текст:')
    a = input()
    print(h(a, chars='?!:;,. '))


if __name__ == '__main__':
    main()