import re
import string

def make_capitalize(s):

    return s.upper()


def word_count(s):
    if s == '':
        return 0
    return len(s.replace('\n',' ').split(' '))


def remove_punctuations(s):

    pattern = string.punctuation
    
    #Method 1
    # pattern.replace("'","\'")
    # pattern = '['+pattern+']'

    # return re.sub(f'{pattern}','',s)

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
    for i in s:
        if i in pattern:
            s = s.replace(i,'')

    return s



def remove_whitespaces(s):
    return re.sub('\s','',s)


def remove_newline(s):
    return s.replace('\n','')
