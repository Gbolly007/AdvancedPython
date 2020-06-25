# Python version 3.8
# list for storing results of operations
lis = []

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
                    kk += 1
                if len(v) >= 2:
                    print('err: invalid expression')
                    neg = 'ss'
    try:
        # list to store disallowed operators that are not accepted
        mychar = ['/', '*', '%', '^', '=']
        # list to store allowed operators that are not accepted
        bsop = ['+', '-']
        if (x in user_input for x in bsop) and not any(x in user_input for x in mychar) and len(neg) == 0:
            # condition to check if user passed the value of an list and convert it
            if '[' and ']' in user_input:
                ui = user_input.split(' ')
                ii = 0
                for u in ui:
                    if '[' in u:
                        gg = 'lis['+u[1]+']'
                        ui[ii] = gg
                    ii += 1
                user_inputs = ' '.join(map(str, ui))

                li = eval(str(user_inputs))
                lis.append(li)
                print(str(len(lis)-1)+': ' + str(li))

            else:

                li = eval(user_input)
                lis.append(li)
                print(str(len(lis)-1)+': ' + str(li))

    except:
        print('err: invalid expression')
