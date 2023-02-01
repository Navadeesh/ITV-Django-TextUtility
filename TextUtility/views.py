from django.shortcuts import HttpResponse, render
import re
import string

def home_func(request):
    return render(request, 'index.html')

def analyze_func(request):

    if request.method == 'POST':
        data = request.POST.get('input_text')
        cap = request.POST.get('make_capitalize')
        w_c = request.POST.get('word_count')
        remove_punc = request.POST.get('remove_punctuations')
        remove_white = request.POST.get('remove_whitespace')
        remove_newL = request.POST.get('remove_new_line')

        # mydict = {
        #     'data': data,
        #     'cap': make_capitalize(data) if cap else 'Not Selected',
        #     'word_count': word_count(data) if w_c else 'Not Selected',
        #     'remove_punc': remove_punctuations(data) if remove_punc else 'Not Selected',
        #     'remove_white': remove_whitespaces(data) if remove_white else 'Not Selected',
        #     'remove_new_line': remove_newline(data) if remove_newL else 'Not Selected'
        # }

        if cap:
            final_data = make_capitalize(data)
            mydict = {
                'Out': final_data
            }
            return render(request, 'output.html', mydict)
        elif w_c:
            final_data = word_count(data)
            mydict = {
                'Out': final_data
            }
            return render(request, 'output.html', mydict)
        elif remove_punc:
            final_data = remove_punctuations(data)
            mydict = {
                'Out': final_data
            }
            return render(request, 'output.html', mydict)
        elif remove_white:
            final_data = remove_whitespaces(data)
            mydict = {
                'Out': final_data
            }
            return render(request, 'output.html', mydict)
        if remove_newL:
            final_data = remove_newline(data)
            mydict = {
                'Out': final_data
            }
            return render(request, 'output.html', mydict)
        

        return render(request, 'output.html', mydict)

def make_capitalize(s):

    return s.upper()


def word_count(s):
    if s == '':
        return 0
    return len(s.replace('\n',' ').split(' '))


def remove_punctuations(s):

    pattern = string.punctuation
    # pattern.replace("'","\'")
    # pattern = '['+pattern+']'
    return re.sub(f'{pattern}','',s)


def remove_whitespaces(s):
    return re.sub('\s','',s)


def remove_newline(s):
    return s.replace('\n','')
