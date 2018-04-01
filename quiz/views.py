from django.shortcuts import render
from django.http import Http404
from random import shuffle

from django.template import loader

# Create your views here.
from django.http import HttpResponse

from .models import Question, Level, Answer



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('quiz/index.html')
    context = {
    	'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))

def level(request):
	all_levels = Level.objects.all()
	template = loader.get_template('quiz/level.html')
	context = {
		'all_levels': all_levels
	}
	return HttpResponse(template.render(context, request))


def test(request, level_id):
	random_questions = Question.objects.filter(level=level_id).order_by('?')[:3]
	questions = []
	for question in random_questions:
		q = {'title': question.question_text, 'answers': []}		
		answers = Answer.objects.filter(question=question)
		for answer in answers:
			q['answers'].append(answer.answer_text)
		questions.append(q)
	context = {
		'random_questions': questions, 
		'level_id': level_id,
	}
	return render(request, 'quiz/test.html', context)

def result(request, level_id):
	context = {}
	return render(request, 'quiz/result.html', context)



# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'quiz/detail.html', {'question': question})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)











