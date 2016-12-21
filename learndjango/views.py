from django.shortcuts import render, HttpResponse, get_object_or_404
from . models import Question
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    output = '<br>'.join([q.question_text for  q in latest_question_list])

    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'learndjango/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'learndjango/detail.html', {'question' : question})

def result(request, question_id):
    return HttpResponse("You're looking at results of question: %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question: %s." % question_id)

