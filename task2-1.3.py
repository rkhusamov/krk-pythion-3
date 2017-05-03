# -*- coding: utf-8 -*-
# Домашнее задание. Лучше если каждая задачка будет оформлена в виде одного файла .py
# 3) вывести первые 10 чисел Фибоначчи

n = int(input())
prev = 1
pprev = 1
for i in range(3,n+1):
    print(i,prev + pprev)
    pprev, prev = prev, pprev+prev
