from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User
from ask.models import Question, Answer, Tag

class Command(BaseCommand):
	help = 'Fill the database'

	def handle(self, *args, **options):
		user = User.objects.get(email='nuf@nuf.nu')
		list_tags = ["Perl", "Python", "TechnoPark", "MySQL", "Django", "Mailru", "Voloshin", "Firefox", "black-jack", "bender"]
		Question.objects.all().delete()
		Answer.objects.all().delete()
		Tag.objects.all().delete()
		for i in range(0, 100):
			q=Question(
				author=user,
				body='body ' + str(i),
				title = 'title ' + str(i),
			)
			q.save()
			for j in range(1, 3):
				a=Answer(
					text='answer ' + str(i) + ' ' + str(j),
					author=user,
					question=q,
				)
				a.save()
			tmp = i%10
			t=Tag(
				name = list_tags[tmp],
				rating = tmp,
			)
			t.save()
			t.question.add(q)
	
				
