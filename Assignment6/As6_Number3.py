# Python version 3.8
import sympy as sym
# list for storing results of operations
lis = []
# variables to store symbolic computation
a = sym.Symbol('a')
b = sym.Symbol('b')
c = sym.Symbol('c')
d = sym.Symbol('d')
e = sym.Symbol('e')
f = sym.Symbol('f')
g = sym.Symbol('g')
h = sym.Symbol('h')
i = sym.Symbol('i')
j = sym.Symbol('j')
k = sym.Symbol('k')
l = sym.Symbol('l')
m = sym.Symbol('m')
n = sym.Symbol('n')
o = sym.Symbol('o')
p = sym.Symbol('p')
q = sym.Symbol('q')
r = sym.Symbol('r')
s = sym.Symbol('s')
t = sym.Symbol('t')
u = sym.Symbol('u')
v = sym.Symbol('v')
w = sym.Symbol('w')
x = sym.Symbol('x')
y = sym.Symbol('y')
z = sym.Symbol('z')
# Loop to calculate
while True:
 # Variable to accept input from user
    user_input = input('>>>')
# Code block to check malformed input
    ui = user_input.split(' ')
    neg = ''
    for u in ui:
        if len(u) > 2:
            if '+' in u:
                v = u.split('+')
                kk = 0
                for c in v:
                    if len(c) == 0:
                        v.pop(kk)
                    kk += 1

                if len(v) >= 2:

                    print('err: invalid expression')
                    neg = 'ss'

            elif '-' in u:
                v = u.split('-')
                jj = 0
                for c in v:
                    if len(c) == 0:
                        v.pop(jj)
                    jj += 1
                if len(v) >= 2:

                    print('err: invalid expression')
                    neg = 'ss'
    try:
        # list to store disallowed operators that are not accepted for basic arithmetic operations
        mychar = ['/', '*', '%', '^', '=']
        # list to store disallowed operators that are not accepted for symbolic computation
        mychar_n = ['/', '%', '^', '=']
        bsop = ['+', '-']
        syms = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z', 'y', 'x']
# condition to check if user passed the value of an list and convert it
        if '[' and ']' in user_input:

            uis = user_input.split(' ')
            ii = 0
            for u in uis:
                if '[' in u:
                    g = int(u[1])

                    gg = lis[g]

                    ui[ii] = gg
                ii += 1

            user_input = ' '.join(map(str, ui))
# condition that handles symbolic computation
        if any(x in user_input for x in syms):
            if not any(x in user_input for x in mychar_n) and len(neg) == 0:

                if 'expand' in user_input:
                    user_input = user_input.replace('expand', '')

                    lis.append(sym.expand(user_input))
                    print(str(len(lis)-1)+': ' + str(sym.expand(user_input)))

                else:
                    li = eval(str(user_input))

                    lis.append(li)
                    print(str(len(lis)-1)+': ' + str(li))
# condition that handles basic arithmetic
        else:
            if (x in user_input for x in bsop) and not any(x in user_input for x in mychar) and len(neg) == 0:
                li = eval(user_input)
                lis.append(li)
                print(str(len(lis)-1)+': ' + str(li))

    except:
        print('err: invalid expression')
