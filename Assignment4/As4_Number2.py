# Python 3.8
from __future__ import print_function
import math
import token
import keyword
import tokenize


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


def main():
    filecontent = ""
    try:
        while True:
            line = input()
            filecontent += "\n" + line
    except EOFError:
        pass

    filename = 'myshell.py'
    f = open(filename, "w+")
    f.write(filecontent)
    f.close()
    s = open('myshell.py').readline
    counter = 0

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
    print("[operators]")
    iif = nt_dict.get('if', 0)
    valoperator += iif
    genvaloperator += 1 if iif != 0 else 0
    print("if:", iif)
    eelif = nt_dict.get('elif', 0)
    valoperator += eelif
    genvaloperator += 1 if eelif != 0 else 0
    print("elif:", eelif)
    eelse = nt_dict.get('else', 0)
    valoperator += eelse
    genvaloperator += 1 if eelse != 0 else 0
    print("else:", eelse)
    ttry = nt_dict.get('try', 0)
    valoperator += ttry
    genvaloperator += 1 if ttry != 0 else 0
    print("try:", ttry)
    ffor = nt_dict.get('for', 0)
    valoperator += ffor
    genvaloperator += 1 if ffor != 0 else 0
    print("for:", ffor)
    wwith = nt_dict.get('with', 0)
    valoperator += wwith
    genvaloperator += 1 if wwith != 0 else 0
    print("with:", wwith)
    rreturn = nt_dict.get('return', 0)
    valoperator += rreturn
    genvaloperator += 1 if rreturn != 0 else 0
    print("return:", rreturn)
    ddef = nt_dict.get('def', 0)
    valoperator += ddef
    genvaloperator += 1 if ddef != 0 else 0
    print("def:", ddef)
    iimport = nt_dict.get('import', 0)
    valoperator += iimport
    genvaloperator += 1 if iimport != 0 else 0
    print("import:", iimport)
    ccalls = getwordstat(src_code_without_strings, "(")
    valoperator += ccalls
    genvaloperator += 1 if ccalls != 0 else 0
    print("calls:", ccalls - ddef)
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
    print("arithmetic:", aarith)
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
    print("logic:", logic_n)
    aassign = num_assign(src_code_without_strings)
    valoperator += aassign
    genvaloperator += 1 if aassign != 0 else 0
    print("assign:", aassign)
    print("N1:", valoperator)

    valoperand = 0
    genvaloperand = 0
    print("\n[operands]")
    scr_code_without_inlines = removeinlines(filecontent)
    src_code_without_docstrings = elimdocstring(filecontent)
    docstr_n = getdocstringtotal(scr_code_without_inlines)
    valoperand += docstr_n
    genvaloperand += 1 if docstr_n != 0 else 0
    print("docstrings:", docstr_n)
    inlines_n = inlinedocs_count(filecontent)
    valoperand += inlines_n
    genvaloperand += 1 if inlines_n != 0 else 0
    print("inlinedocs:", inlines_n)
    literals_n = totalnum_literal(src_code_without_docstrings)
    valoperand += literals_n
    genvaloperand += 1 if literals_n != 0 else 0
    print("literals:", literals_n)
    valoperand += ddef + aassign
    genvaloperand += 1 if ddef != 0 or aassign != 0 else 0
    print("entities:", ddef + aassign)
    scr_code_with_literals_and_wout_defs = methodless(
        removeinlines(src_code_without_docstrings))
    arg_n = num_param(scr_code_with_literals_and_wout_defs)
    valoperand += arg_n
    genvaloperand += 1 if arg_n != 0 else 0
    print("args:", arg_n)
    print("N2:", valoperand)


if __name__ == "__main__":
    main()
