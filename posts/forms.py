from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
	content = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Your Message','class':'form-control'}))
	class Meta:
		model = Posts
		fields = ('content',)