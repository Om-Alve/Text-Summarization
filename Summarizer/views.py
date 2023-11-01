from django.shortcuts import render
from django.http import JsonResponse
from .models import Text
from .forms import TextForm
from . import pipe


def summarize_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.save()
            summary = pipe(text.content)['summary']  # You can adjust the word count for the summary.
            return render(request, 'summary.html', {'text': text, 'summary': summary})
    else:
        form = TextForm()
    return render(request, 'summarize.html', {'form': form})
