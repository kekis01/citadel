from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect

# Create your views here
from .forms import *
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

current_article_id = 0


def index(request):
    return render(request, 'home/home.html')


def news(request):
    return render(request, 'home/news.html')


def LikeView(request, artid):
    comment = Comments.objects.get(id=request.GET.get('comment_id'))
    comment.likes.add(request.user)
    return HttpResponseRedirect(reverse('article', args=[str(artid)]))


def article(request, artid):
    comment = Comments.objects.filter(article_id=artid)
    global current_article_id
    current_article_id = artid
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.article_id = artid
            form.save()
            return redirect('article', artid)
    else:
        form = CommentForm
    return render(request, f'home/article{artid}.html', {"article_id": artid, "comments": comment, "form": form})


def photos(request):
    return render(request, 'home/photos.html')


def player(request):
    return render(request, 'home/player.html')


def streams(request):
    return render(request, 'home/streams.html')


def video(request):
    return render(request, 'home/video.html')


def login(request):
    return render(request, 'home/login.html')


def shop(request):
    return render(request, 'home/blank.html')


def info(request):
    return render(request, 'home/blank.html')


def tournaments(request):
    return render(request, 'home/blank.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'home/login.html'

    def get_success_url(self):
        return reverse_lazy('Citadel')


def logout_user(request):
    logout(request)
    return redirect('login')