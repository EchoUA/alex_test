from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from word_parse.forms import ContactForm
from django.views.generic.edit import FormView
import json
import re


def handler(alltext):
    dct = {}

    for ii, i in enumerate(re.split(r'[\.|\!|\?]\s(?=[A-Z])', alltext)):
        i = re.sub(r'\.$', '', i)
        for j in i.split(' '):
            j = re.sub(r'[\.$|:|,]', '', j)
            j = j.lower()

            try:
                dct[j][0] += 1
                dct[j][1] += ',' + str(ii+1)
            except:
                dct[j] = []
                dct[j].append(1)
                dct[j].append(str(ii+1))
    result_list = []
    for num, i in enumerate(dct):
        result_list.append('%s   {%s: %s}' % (i, dct[i][0], dct[i][1]))

    return sorted(result_list)

def numerator(umbre):
    one = (umbre / 26) + 1
    two = (umbre % 26)
    return unichr(97+two) * one

def get_text(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            datas = form.cleaned_data['intext']
            send_list = []
            statistic_data=handler(datas)
            for num, i in enumerate(statistic_data):
                send_list.append('%s.   %s'%(numerator(num), i))

            return render(request, 'word_parse/simple.html', {'form': form,'text_data':send_list})
    else:
        form = ContactForm()


    return render(request, 'word_parse/simple.html', {'form': form})


