from django import forms
from BlogApp.models import Comments

class EmailForm(forms.Form):
    # Used bootstrap classes
    name = forms.CharField(label = 'Name', min_length=4, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    to_email = forms.EmailField(label = 'To Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    comments = forms.CharField(label = 'Comments', widget=forms.Textarea(attrs={'class': 'form-control'}))

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','email','comment']
