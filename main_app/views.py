import random
import string
from django.shortcuts import render, redirect
from .models import URL_Short
from .forms import UrlForm

class Shorten:
    token_size = 5

    def __init__(self, token_size=None):
        self.token_size = token_size if token_size is not None else 5

    def issue_token(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(self.token_size))


def Update(request):
    form = UrlForm(request.POST)
    up_url = ""

    url_list = URL_Short.objects.all()
    if request.method == "POST":
        if form.is_valid():
            newUrl = form.save(commit=False)
            if not (newUrl.short_url):
                up_url = Shorten().issue_token()
                newUrl.short_url = up_url
            newUrl.save()
        else:
            form = UrlForm()
            up_url = "Invalid URL"

    return render(request, 'home.html', {'form': form, 'url_list': url_list, 'up_url': up_url})



def Page(request, token):
    long_url = URL_Short.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)