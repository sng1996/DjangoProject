from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



new_questions_list = [ ]

for i in range (30):
        new_questions_list.append({
                'title' : 'Question #{}. How to build a moon park?'.format(i),
                'body' : 'Guys, i have trouble with a moon park. Can\'t find the black-jack...',
        })

new_questions(request):
        return render(request, 'new_questions.html', {
                'new_questions' : new_questions_list,
        })

def paginate(request):
        paginator = Paginator(new_questions_list, 10)
        page = request.GET.get('page');
        try:
                questions = paginator.page(page)
        except PageNotAnInteger:
                questions = paginator.page(1)
        except EmptyPage:
                questions = paginator.page(paginator.num_pages)

        return render_to_response('new_questions.html', {"questions":questions})

