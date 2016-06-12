from django.shortcuts import render, redirect
from django.template import Context
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cgi import parse_qsl, escape
from django.contrib import auth
from pprint import pformat
from ask.models import Question, Answer, Tag, Profile
from django.contrib.auth.models import User
from ask.forms import UserForm, QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

# Create your views here.

hot_questions_list = [ ]

for i in range (30):
	hot_questions_list.append({
		'title' : 'Question #{}. How to build a moon park?'.format(i),
		'body' : 'Guys, i have trouble with a moon park. Can\'t find the black-jack...',
	})

def paginator(request, objects):
	paginator = Paginator(objects, 10)
	try:
	    page_num = request.GET["page"]
	except KeyError:
	    page_num = 1
	listing = paginator.page(page_num)
	return listing

def hot_questions(request):

	questions = Question.questions.rating()[0:10]
	listing = paginator(request, questions)
	return render(request, 'questions.html', {
		'questions' : listing,
	})

def new_questions(request):

        questions = Question.questions.added()
        listing = paginator(request, questions)
        return render(request, 'questions.html', {
                'questions' : listing,
        })


def tag_questions(request):

        questions = Question.objects.order_by('-added_at')

        paginator = Paginator(questions, 10)
        try:
            page_num = request.GET["page"]
        except KeyError:
            page_num = 1
        listing = paginator.page(page_num)
        return render(request, 'tag_questions.html', {
                'new_questions' : listing,
        })

def tag(request, argv):
	question_list = Question.questions.tags(argv)
	return render(request, 'questions.html', {
		'questions' : question_list,
	})

@login_required
def profile(request):
	data = { 'login' : request.user.username,
		 'email' : request.user.email,
		 'nickname' : request.user.last_name }
	form = UserForm(data)
	if request.POST:
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			u = User.objects.get(username = request.user.username)
			u.username = form.cleaned_data.get('login')
			u.email = form.cleaned_data.get('email')
			u.last_name = form.cleaned_data.get('nickname')
			password = form.cleaned_data.get('password')
			if (password != '') and (password == form.cleaned_data.get('repeat_password')):
				u.set_password(password)
			u.profile.avatar = request.FILES['upload_avatar']
			u.save()
			user = auth.authenticate(username=form.cleaned_data.get('login'), password=password)
			if user is not None:
				auth.login(request, user)	
	return render(request, 'profile.html', { 'form' : form })

def signup(request):
	if request.POST:
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			password = form.cleaned_data.get('password')
			repeat_password = form.cleaned_data.get('repeat_password')
			if (password == repeat_password):
				username = form.cleaned_data.get('login')
				try:
					username = User.objects.get(username = username)
					return render(request, 'signup.html', { 'form' : form, 'user_error' : True })
				except User.DoesNotExist as error:	
					email = form.cleaned_data.get('email')
					last_name = form.cleaned_data.get('nickname')
					u = User.objects.create_user(username, email, password)
					u.last_name = last_name
					p = Profile(user = u, avatar = request.FILES.get('upload_avatar'))
					p.save()
					user = auth.authenticate(username=username, password=password)
					auth.login(request, user)
					return redirect('/')
		else:
			return render(request, 'signup.html', { 'form' : form })
	else:
		form = UserForm()
	return render(request, 'signup.html', { 'form' : form })

def index(request):	
	return render(request, 'index.html')

@login_required
def ask(request):
	if request.POST:
		form = QuestionForm(request.POST, author=request.user)
		if form.is_valid():
			question = form.save()
			tag = request.POST.get('tags')
			for word in tag.split(" "):
				t = Tag(name = word)
				t.save()
				t.question.add(question)
			return redirect('/')	
	form = QuestionForm()
	return render(request, 'ask.html', { 'form' : form })

def answer(request, question_id):
	answer = Answer.answers.answer(question_id)
	during_question = Question.questions.question(question_id)
	if request.POST:
		form = AnswerForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data.get('text')
			author = request.user
			question = during_question
			a = Answer(
				text = text,
				author = author,
				question = question)
			a.save()
			return redirect('/')
	form = AnswerForm()	
	return render(request, 'answer.html', {
		'answers' : answer,
		'question' : during_question,
		'form' : form
	})

def login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			return render(request, 'login.html', { 'login_error' : True})
	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def hello(request):
	response = 'Hello world from django views <br>'

	for key, value in request.GET.items():
		response = response + str(key) + " : " + str(value) + "<br>"
	for key, value in request.POST.items():
		response = response + str(key) + " : " + str(value) + "<br>"
	return HttpResponse(response)

