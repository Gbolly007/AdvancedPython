# Python version 3.8
from __future__ import print_function
import inspect
from inspect import signature
from tabulate import tabulate
import sys
import io
from contextlib import redirect_stdout
# Python 3.8

import math
import token
import keyword
import tokenize

glo_dict = {}


def elimdocstring(text):
    while True:
        if text.find('"""') == -1:
            break
        inline_start = text.find('"""')
        curr = text[inline_start + 5:]
        inline_end = curr.find('"""') + inline_start + 5
        if inline_end == -1:
            text = text[:inline_start]
        else:
            text = text[:inline_start] + text[inline_end + 5:]
    return text


def getwordstat(line, des, not_des=""):
    if line.find(des) == -1:
        return 0
    else:
        des_ind = line.find(des)
        ndes_ind = line.find(not_des)
        curr = line[des_ind + len(des) + 1:]
        if des_ind == ndes_ind:
            return getwordstat(curr, des, not_des)
        return getwordstat(curr, des, not_des) + 1


def removeinlines(text):
    while True:
        if text.find('#') == -1:
            break
        inline_start = text.find('#')
        curr = text[inline_start:]
        inline_end = curr.find('\n')
        if inline_end == -1:
            text = text[:inline_start]
        else:
            text = text[:inline_start] + text[inline_end + inline_start + 1:]
    return text


def exstrings(text):
    while True:
        if text.find('"') == -1:
            break
        string_start = text.find('"')
        curr = text[string_start + 1:]
        string_end = curr.find('"') + string_start + 1
        text = text[:string_start] + text[string_end + 1:]

    while True:
        if text.find("'") == -1:
            break
        string_start = text.find("'")
        curr = text[string_start + 1:]
        string_end = curr.find("'") + string_start + 1
        text = text[:string_start] + text[string_end + 1:]

    return text


def destring(text):
    text = elimdocstring(text)
    text = exstrings(text)
    text = removeinlines(text)

    return text


def methodless(text):
    while True:
        if text.find('def') == -1:
            break
        inline_start = text.find('def')
        curr = text[inline_start:]
        inline_end = curr.find('\n')
        if inline_end == -1:
            text = text[:inline_start]
        else:
            text = text[:inline_start] + text[inline_end + inline_start + 1:]
    return text


def num_assign(line):
    if line.find("=") == -1:
        return 0
    else:
        des_ind = line.find("=")
        curr = line[des_ind + len("=") + 1:]
        if line[des_ind - 1] == "!" or line[des_ind + 1] == "=":
            return num_assign(curr)
        return num_assign(curr) + 1


def getdocstringtotal(text):
    if text.find('"""') == -1:
        return 0
    beg = text[text.find('"""') + 5:]
    end = beg[:beg.find('"""')]
    lines = end.split("\n")
    return getdocstringtotal(beg[beg.find('"""') + 5:]) + len(lines) - 1


def inlinedocs_count(text):
    if text.find('#') == -1 or text.find('\n') == -1:
        return 0
    beg = text[text.find('#'):]
    return inlinedocs_count(beg[beg.find('\n') + 1:]) + 1


def totalnum_literal(text):
    count = 0
    cur_text = '%s' % text
    while True:
        if cur_text.find('"') == -1:
            break
        string_start = cur_text.find('"')
        curr = cur_text[string_start + 1:]
        string_end = curr.find('"') + string_start + 1
        cur_text = cur_text[string_end + 1:]
        count += 1

    cur_text = '%s' % text
    while True:
        if cur_text.find("'") == -1:
            break
        string_start = cur_text.find("'")
        curr = cur_text[string_start + 1:]
        string_end = curr.find("'") + string_start + 1
        cur_text = cur_text[string_end + 1:]
        count += 1

    cur_text = '%s' % text
    i = 0
    while i < len(cur_text):
        if cur_text[i].isdigit():
            while cur_text[i].isdigit():
                i += 1
            count += 1
        i += 1

    return count


def list_entity(list, by=" "):
    new_lines = []
    for line in list:
        if '"' in line or "'" in line:
            new_lines.append(line)
        else:
            new_lines += line.split(by)
    return new_lines


def num_param(text):
    begin_index = text.find('(')
    if begin_index == -1:
        return 0
    beg = text[begin_index + 1:]
    arg = beg[:beg.find(')') + 1]

    if arg == ')':
        count = 0
    else:
        count = 1

    open_n = 1
    close_n = 0
    while open_n != close_n:
        open_index = beg.find("(")
        close_index = beg.find(")")
        if open_index != -1 and open_index < close_index:
            open_n += 1
            beg = beg[open_index + 1:]
        else:
            close_n += 1
            beg = beg[close_index + 1:]

    if len(beg) == 0:
        return count

    close_index = text.find(beg)
    arg = text[begin_index:close_index]

    lines = arg.split(",")
    lines = list_entity(lines, by="(")
    lines = list_entity(lines, by=")")
    lines = list_entity(lines, by=" ")

    f = 0
    while f == 0:
        try:
            lines.remove('')
        except BaseException:
            f = 1

    n, i, j = len(lines), 0, 0
    operators = ['if', 'elif', 'else', 'try', 'for', 'with', 'return', 'def', 'import', 'except', '+', '-', '/', '*',
                 '==', '!=', 'and', 'not', '=', '>', '<', '<=', '>=', 'in']
    while i+j != n:
        if lines[i] in operators:
            lines.pop(i)
            j += 1
        else:
            i += 1

    return num_param(text[close_index + 1:]) + count + len(lines)


def stat_complexity(func):

    filecontent = ""

    filecontent = inspect.getsource(func)
    # print(filecontent)

    filename = 'myshell.py'
    f = open(filename, "w+")
    f.write(filecontent)
    f.close()
    s = open('myshell.py').readline
    counter = 0
    os.remove('myshell.py')
    l = []
    for i in tokenize.generate_tokens(s):
        if i.type == token.NAME and keyword.iskeyword(i.string):
            counter += 1
            l.append(i.string)

    print(counter)
    nt_dict = dict((i, l.count(i)) for i in l)
    src_code_without_strings = destring(filecontent)
    valoperator = 0
    genvaloperator = 0

    iif = nt_dict.get('if', 0)
    valoperator += iif
    genvaloperator += 1 if iif != 0 else 0

    eelif = nt_dict.get('elif', 0)
    valoperator += eelif
    genvaloperator += 1 if eelif != 0 else 0

    eelse = nt_dict.get('else', 0)
    valoperator += eelse
    genvaloperator += 1 if eelse != 0 else 0

    ttry = nt_dict.get('try', 0)
    valoperator += ttry
    genvaloperator += 1 if ttry != 0 else 0

    ffor = nt_dict.get('for', 0)
    valoperator += ffor
    genvaloperator += 1 if ffor != 0 else 0

    wwith = nt_dict.get('with', 0)
    valoperator += wwith
    genvaloperator += 1 if wwith != 0 else 0

    rreturn = nt_dict.get('return', 0)
    valoperator += rreturn
    genvaloperator += 1 if rreturn != 0 else 0

    ddef = nt_dict.get('def', 0)
    valoperator += ddef
    genvaloperator += 1 if ddef != 0 else 0

    iimport = nt_dict.get('import', 0)
    valoperator += iimport
    genvaloperator += 1 if iimport != 0 else 0

    ccalls = getwordstat(src_code_without_strings, "(")
    valoperator += ccalls
    genvaloperator += 1 if ccalls != 0 else 0

    pplus = getwordstat(src_code_without_strings, "+")
    mminus = getwordstat(src_code_without_strings, "-")
    ddivide = getwordstat(src_code_without_strings, "/")
    mmult = getwordstat(src_code_without_strings, "*")
    aarith = pplus + mminus + ddivide + mmult
    valoperator += aarith
    genvaloperator += 1 if pplus != 0 else 0
    genvaloperator += 1 if mminus != 0 else 0
    genvaloperator += 1 if ddivide != 0 else 0
    genvaloperator += 1 if mmult != 0 else 0

    eequal = getwordstat(src_code_without_strings, "==")
    nnegate = getwordstat(src_code_without_strings, "!=")
    aand = nt_dict.get('and', 0)
    nnot = nt_dict.get('not', 0)
    logic_n = eequal + nnegate + aand + nnot
    valoperator += logic_n
    genvaloperator += 1 if eequal != 0 else 0
    genvaloperator += 1 if nnegate != 0 else 0
    genvaloperator += 1 if aand != 0 else 0
    genvaloperator += 1 if nnot != 0 else 0

    aassign = num_assign(src_code_without_strings)
    valoperator += aassign
    genvaloperator += 1 if aassign != 0 else 0

    valoperand = 0
    genvaloperand = 0

    scr_code_without_inlines = removeinlines(filecontent)
    src_code_without_docstrings = elimdocstring(filecontent)
    docstr_n = getdocstringtotal(scr_code_without_inlines)
    valoperand += docstr_n
    genvaloperand += 1 if docstr_n != 0 else 0

    inlines_n = inlinedocs_count(filecontent)
    valoperand += inlines_n
    genvaloperand += 1 if inlines_n != 0 else 0

    literals_n = totalnum_literal(src_code_without_docstrings)
    valoperand += literals_n
    genvaloperand += 1 if literals_n != 0 else 0

    valoperand += ddef + aassign
    genvaloperand += 1 if ddef != 0 or aassign != 0 else 0

    scr_code_with_literals_and_wout_defs = methodless(
        removeinlines(src_code_without_docstrings))
    arg_n = num_param(scr_code_with_literals_and_wout_defs)
    valoperand += arg_n
    genvaloperand += 1 if arg_n != 0 else 0

    N = valoperator + valoperand

    L = genvaloperator * math.log(genvaloperator, 2) + \
        genvaloperand * math.log(genvaloperand, 2)

    V = N * math.log(genvaloperator + genvaloperand, 2)

    D = (genvaloperator / 2) * (valoperand / genvaloperand)

    E = D * V

    dicts = {}
    operatordict = {}
    operandict = {}
    programdict = {}
    operatordict['if'] = iif
    operatordict['elif'] = eelif
    operatordict['else'] = eelse
    operatordict['try'] = ttry
    operatordict['for'] = ffor
    operatordict['with'] = wwith
    operatordict['return'] = rreturn
    operatordict['def'] = ddef
    operatordict['import'] = iimport
    operatordict['calls'] = ccalls
    operatordict['arithmetic'] = aarith
    operatordict['logic'] = logic_n
    operatordict['assign'] = aassign
    operatordict['N1'] = valoperator
    operandict['docstrings'] = docstr_n
    operandict['inlinedocs'] = inlines_n

    operandict['literals'] = literals_n
    operandict['entities'] = ddef + aassign
    operandict['args'] = arg_n
    operandict['N2'] = valoperand
    programdict['vocabulary'] = genvaloperator + genvaloperand
    programdict['length'] = valoperator + valoperand
    programdict['calc_length'] = L
    programdict['volume'] = V
    programdict['difficulty'] = D
    programdict['effort'] = E
    dicts['operators'] = operatordict
    dicts['operands'] = operandict
    dicts['program'] = programdict
    glo_dict['Complexity'] = dicts
    return func


def stat_object(func):
    '''This method takes in a function as arguments
    passes to the function below which reads the content
    of the function argument and prints out the content
    '''
    def helper(*args, **kwargs):
        lines = inspect.getsource(func)
        sig = signature(func)
        f = io.StringIO()
        with redirect_stdout(f):
            str(func(*args, **kwargs))

        i = 0
        for line in lines.split('\n'):
            if 'print(' in line:
                i += 1
        i -= 1
        i = str(i)
        compl = '{print: ' + i + '}'
        dicts = {}
        dicts['Name'] = func.__name__
        dicts['Type'] = str(type(func))
        dicts['Sign'] = str(sig)
        dicts['Args'] = str({
            k: v.default
            for k, v in sig.parameters.items()
            if v.default is not inspect.Parameter.empty
        })
        dicts['Doc'] = inspect.getdoc(func)
        dicts['Complx'] = compl
        dicts['Source'] = lines
        dicts['Output'] = f.getvalue()
        glo_dict['Object'] = dicts
        print(glo_dict)

    return helper
