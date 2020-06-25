import math
lis = []
i = 0
while True:
    user_input = input('>>>')

    ui = user_input.split(' ')
    neg = ''
    for u in ui:
        if len(u) > 2:
            if '+' in u:
                v = u.split('+')

                if len(v) >= 2:
                    print('Invalid expression')
                    neg = 'ss'

            elif '-' in u:
                v = u.split('-')
                if len(v) >= 2:
                    print('Invalid expression')
                    neg = 'ss'
    try:
        mychar = ['/', '*', '%', '^', '=']
        bsop = ['+', '-']
        if (x in user_input for x in bsop) and not any(x in user_input for x in mychar) and len(neg) == 0:

            if '[' and ']' in user_input:
                ui = user_input.split(' ')
                ii = 0
                for u in ui:
                    if '[' in u:
                        gg = 'lis['+u[1]+']'
                        ui[ii] = gg
                    ii += 1
                user_inputs = ' '.join(map(str, ui))
                print(user_inputs)
                li = eval(str(user_inputs))
                print(str(i)+': ' + str(li))
                i += 1
                lis.append(li)
                print(lis)
            else:

                li = eval(user_input)
                print(str(i)+': ' + str(li))
                i += 1
                lis.append(li)
                print(lis)
    except:
        print('Invalid expression')
