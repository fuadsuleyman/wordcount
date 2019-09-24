import operator

from django.http import HttpResponse
from django.shortcuts import render


def default(request):
    return HttpResponse('<h1>Salam Aleykum from default Page, we have other pages- /home, /fuad, /zehra</h1>')


def text(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    leni = len(word_list)
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    sorted_dict = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    print(word_dictionary)

    return render(request, 'count.html', {'fult': fulltext, 'count': leni, 'word_dictionary': sorted_dict})

