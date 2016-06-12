from django.db import models
from django.contrib.auth.models import User
import datetime
import MySQLdb
from PIL import Image

# Create your models here.

class QuestionQuerySet(models.QuerySet):
	def rating(self):
		return self.order_by('-rating')

	def added(self):
		return self.order_by('-added_at')
	
	def tags(self, argv):
		return self.filter(tag__name = argv)

	def question(self, question_id):
		return self.get(id = int(question_id))

class QuestionManager(models.Manager):
	def get_queryset(self):
		return QuestionQuerySet(self.model, using=self._db)

	def rating(self):
		return self.get_queryset().rating()

	def added(self):
		return self.get_queryset().added()

	def tags(self, argv):
		return self.get_queryset().tags(argv)

	def question(self, question_id):
		return self.get_queryset().question(question_id)

class Question(models.Model):
	title = models.CharField(max_length=128)
	body = models.TextField()
	added_at = models.DateTimeField(default=datetime.datetime.now)
	author = models.ForeignKey(User)
	rating = models.IntegerField(default = 0)
	votes = models.ManyToManyField(User, related_name='voted_users', through = 'Like') 
	questions = QuestionManager()

class AnswerQuerySet(models.QuerySet):
	def answer(self, question_id):
		return self.filter(question__pk = int(question_id))

class AnswerManager(models.Manager):
	def get_queryset(self):
		return AnswerQuerySet(self.model, using=self._db)

	def answer(self,question_id):
		return self.get_queryset().answer(question_id)

class Answer(models.Model):
	text = models.TextField()
	author = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	added_at = models.DateTimeField(default=datetime.datetime.now)
	answers = AnswerManager()

class Like(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	is_Like = models.BooleanField()

class Tag(models.Model):
	name = models.CharField(max_length=32)
	rating = models.IntegerField(default = 0)
	question = models.ManyToManyField(Question)

class Profile(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField()
