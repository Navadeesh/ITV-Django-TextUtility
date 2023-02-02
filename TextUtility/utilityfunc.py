import re
import string

def make_capitalize(s):

    return s.upper()


def word_count(s):
    if s == '':
        return 0
    return len(s.replace('\n',' ').split(' '))


def remove_punctuations(s):

    
    #Method 1
    
    # pattern = '[\\!"#$%&\'*+,-.:;<=>?@]'   # Cant remove \ (Backslash)

    # pattern = r'[\W\\]+'   # This removes spaces or newline

    pattern = r'[^\w\s]'     # Correct pattern
    print(re.sub(pattern,'',s))
    return re.sub(pattern,'',s)

    # pat = '[a-zA-Z0-9\s]+'

    # final_s = ''

    # for i in re.findall(pat,s):
    #     final_s += i

    # return final_s

    #Method 2
    # final_s = ''
    # for i in s:
    #     if i in pattern:
    #         continue
    #     else:
    #         final_s+=i
    # 
    # return final_s

    #Method 3
    # for i in s:
    #     if i in pattern:
    #         s = s.replace(i,'')

    # return s



def remove_whitespaces(s):
    
    #Method 1
    # return re.sub('\s','',s)

    #Method 2
    pat = string.whitespace
    for i in s:
        if i in pat:
            s = s.replace(i,'')
    return s
        


def remove_newline(s):

    return s.replace('\n','')