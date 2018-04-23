from django.shortcuts import render
from django.http import Http404
from random import shuffle

import datetime

from django.template import loader

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import redirect

from .models import Question, Level, Answer, Language, User, Test, TestQuestion

# from django.contrib.auth.models import User

from django.contrib.auth import authenticate


def level(request):
	all_levels = Level.objects.all()
	all_languages = Language.objects.all()
	template = loader.get_template('quiz/level.html')
	context = {
		'all_levels': all_levels,
		'all_languages': all_languages,
		# 'user': request.session['user']
	}
	return HttpResponse(template.render(context, request))
	

def register(request):
	return render(request, 'quiz/register.html')


def register_user(request):
	user = User.objects.create_user(request.POST['uname'], request.POST['email'], request.POST['psw'])
	request.session['user'] = user.id
	return redirect(level)


def test(request, language_id, level_id):

	try:
		user = User.objects.get(pk=request.session['user'])
	except KeyError:
		user = User.objects.get(username='GUEST')
	test = Test(user_id=user, date=datetime.datetime.now())
	test.save()
	random_questions = Question.objects.filter(level=level_id, language_id=language_id).order_by('?')[:3]
	questions = []
	for question in random_questions:
		q = {'title': question, 'answers': []}		
		answers = Answer.objects.filter(question=question)
		test_question = TestQuestion(test_id=test, question_id=question)
		test_question.save()
		for answer in answers:
			q['answers'].append(answer)
		questions.append(q)
	context = {
		'random_questions': questions, 
		'level_id': level_id,
		'test_id': test.id if test else None
	}
	return render(request, 'quiz/test.html', context)





def result(request, level_id, test_id):
	correct = 0
	wrong = 0
	user = Test.objects.get(id=test_id).user_id
	date = Test.objects.get(id=test_id).date
	for k, v in request.POST.items():
		if k != 'csrfmiddlewaretoken':
			if Answer.objects.get(id=v).is_correct:
				correct += 1
			else:
				wrong += 1

	context = {
		'correct': correct,
		'wrong': wrong,
		'user': user,
		'date': date,
		'test': test_id
	}
	return render(request, 'quiz/result.html', context)


def login(request):
	return render(request, 'quiz/login.html')


def parse(request):
	log = 0
	user = authenticate(username=request.POST['uname'], password=request.POST['psw'])
	if not user:
		log = 'Please, try again'
		return render(request, 'quiz/login.html', {'log': log})
	request.session['user'] = user.id
	return redirect(level)

