# -*- coding: utf-8 -*-
# Домашнее задание. Лучше если каждая задачка будет оформлена в виде одного файла .py
# 6) Пользователь вводит строку. Напечатать словарь, ключами которого являются четные символы строки, а значениями нечетные. Если последнему ключу не хватает значения, не добавлять его в словарь.
s = input()
a = dict()
#a["1"]="q"
# a[s[1]] = s[2]
for i in range(0, len(s)-1, 2):
    a[s[i+1]] = s[i]

print(a)
