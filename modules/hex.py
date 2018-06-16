#!/usr/bin python3.6


def bit_length(self):
    s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
    s = s.lstrip('-0b') # remove leading zeros and minus sign
    return s

# print(bit_length(50))

x = 36
y = ('Package Controle', 
    'Dayle Rees Color Schemes', 
    'Predawn', 
    'Bracket Highighter',
    'Side Enhancements', 
    'SublimeCodeIntel', 
    'SublimeLinter-pylint')

try:
    if x == 0:
        print("0 in Binary egal 0")
    else:
        print(x)

    print(y[2].upper())
    print(len(y), "\n")

    a = 0
    for i in y:
        a +=1
        print(a, i)

except (NameError, SyntaxError):
    print("Name du code")