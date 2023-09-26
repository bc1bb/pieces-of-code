#!/usr/bin/env python3
# Tableau de pascal

def p1(l1: list):
    l2 = [1]
    n = len(l1)
    for k in range(1, n):
        l2.append(l1[k] + l1[k - 1])
    l2.append(1)
    return l2


def p2(n: int):
    l = [1]
    for i in range(n):
        print(p1(l))
        l = p1(l)

p2(10)
