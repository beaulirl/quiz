from django.shortcuts import render
from django.http import Http404
from random import shuffle

from django.template import loader

# Create your views here.
from django.http import HttpResponse

from .models import Question, Level, Answer, Language, User


def level(request):
	all_levels = Level.objects.all()
	all_languages = Language.objects.all()
	template = loader.get_template('quiz/level.html')
	context = {
		'all_levels': all_levels,
		'all_languages': all_languages
	}
	return HttpResponse(template.render(context, request))


def test(request, language_id, level_id):
	random_questions = Question.objects.filter(level=level_id, language_id=language_id).order_by('?')[:3]
	questions = []
	for question in random_questions:
		q = {'title': question, 'answers': []}		
		answers = Answer.objects.filter(question=question)
		for answer in answers:
			q['answers'].append(answer)
		questions.append(q)
	context = {
		'random_questions': questions, 
		'level_id': level_id,
	}
	return render(request, 'quiz/test.html', context)

def result(request, level_id):
	correct = 0
	wrong = 0
	for k, v in request.POST.items():
		if k != 'csrfmiddlewaretoken':
			if Answer.objects.get(id=v).is_correct:
				correct += 1
			else:
				wrong += 1

	context = {
		'correct': correct,
		'wrong': wrong,
	}
	return render(request, 'quiz/test.html', context)


def login(request):
	context = {}
	return render(request, 'quiz/login.html', context)


def parse(request):
	log = 0
	try:
		User.objects.get(name=request.POST['uname'], password=request.POST['psw'])
	except User.DoesNotExist:
		log = 'Please, try again'
		page = 'quiz/login.html'
	else:
		page = 'quiz/level.html'
	context = {
		'log': log
		}
	return render(request, page, context)


