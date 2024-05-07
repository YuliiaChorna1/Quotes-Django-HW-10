import logging
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page

from .models import Quotes, Authors, Tag, TagView
from .forms import AuthorForm, QuoteForm

logger = logging.getLogger(__name__)

# @cache_page(60 * 15)
def main(request, page=1):
    quotes = Quotes.objects()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)

    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def author(request, author_name):
    author = Authors.objects(fullname=author_name.replace("-", " ").title()).first()
    return render(request, "quotes/author.html", context={"author": author})


def tag(request, tag_name, page=1):
    quotes = Quotes.objects(tags__name=tag_name)
    tag = TagView(name=tag_name, quotes=quotes)

    return render(request, "quotes/tag.html", context={"tag": tag})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)            
            author_obj = Authors(
                fullname=author.fullname,
                born_date=author.born_date,
                born_location=author.born_location,
                description=author.description
            )
            author_obj.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_author.html', {'form': form})

    return render(request, 'quotes/add_author.html', {'form': AuthorForm()})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)            
            author = Authors.objects(fullname=quote.author).first()
            tags = [Tag(name=tag) for tag in quote.tags.split(',')]
            quote_obj = Quotes(
                tags=tags,
                author=author.id,
                quote=quote.quote
            )
            quote_obj.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_quote.html', {'form': form})

    return render(request, 'quotes/add_quote.html', {'form': QuoteForm()})
