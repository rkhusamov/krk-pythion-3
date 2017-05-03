# -*- coding: utf-8 -*-
# Домашнее задание. Лучше если каждая задачка будет оформлена в виде одного файла .py
# 2) min/max
# написать программу найти макс и мин элемент в массивее - сделать через цикл
# a=[1,7,13,-2,7 ....] #len (a)==10

a = [int(i) for i in input().split()]
#a = []
min = a[0]
max = a[0]
for i in range(1,len(a)):
    if a[i] > max:
        max = a[i]
    elif a[i] < min:
        min = a[i]
print(max, min)

