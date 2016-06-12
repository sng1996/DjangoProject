from django import forms
from ask.models import Question


class UserForm(forms.Form):
	login = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
	nickname = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(required = False, widget = forms.PasswordInput(attrs={'class':'form-control'}))
	repeat_password = forms.CharField(required = False, widget = forms.PasswordInput(attrs={'class':'form-control'}))
	upload_avatar = forms.ImageField(required = False)

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = [ 'title', 'body']
		widgets = {
			'title' : forms.TextInput(attrs={'class' : 'form-control'}),
			'body' : forms.Textarea(attrs={'class' : 'form-control'}),
		}
	
	def __init__(self, *args, **kwargs):
		self.author = kwargs.pop('author', None)
		super(QuestionForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		obj = super(QuestionForm, self).save(commit=False)
		obj.author = self.author
		if commit:
			obj.save()
		return obj

class AnswerForm(forms.Form):
	text = forms.CharField(widget = forms.Textarea(attrs = {'class':'form-control',
								'style':'margin-bottom:20px; height:150px; padding_top:20px;',
								'placeholder':'Enter your answer here...'}))	


