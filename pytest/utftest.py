# -*- coding: utf-8 -*-
def normalize(name):
    return name.capitalize()
L1=['ada','lisa']
L2=list(map(normalize,L1))
print(L2)
