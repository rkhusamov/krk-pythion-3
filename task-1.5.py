# -*- coding: utf-8 -*-
# Домашнее задание. Лучше если каждая задачка будет оформлена в виде одного файла .py
# 5) Пользователь вводит число N. Создать массив размера N, который одинаково читается как слева направо, так и справа налево.
n = int(input())
a = [n // 2] * n
for i in range(len(a) // 2):
    a[i] , a[len(a) - i - 1] = i, i

print(a)
