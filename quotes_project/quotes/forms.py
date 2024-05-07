from django.forms import ModelForm, CharField, TextInput, DateField, DateInput
from .models import Tag, Authors, Quotes, Author, Quote


class AuthorForm(ModelForm):

    fullname = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_date = DateField(required=True, widget=DateInput())
    born_location = CharField(min_length=3, required=True, widget=TextInput())
    description = CharField(min_length=3, required=True, widget=TextInput())
    
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):

    tags = CharField(required=True, widget=TextInput())
    author = CharField(min_length=3, required=True, widget=TextInput())
    quote = CharField(min_length=3, required=True, widget=TextInput())
    
    class Meta:
        model = Quote
        fields = ['tags', 'author', 'quote']

