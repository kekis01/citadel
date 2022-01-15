from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.db.models import Count, F
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect

# Create your views here
from .forms import *
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .models import *


def index(request):
    art = Article.objects.all()
    return render(request, 'home/home.html', {'articles': art, })


def news(request):
    articles = Article.objects.all()
    return render(request, 'home/news.html', {"articles": articles})


def LikeView(request, artid):
    comment = Comments.objects.get(id=request.GET.get('comment_id'))
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return HttpResponseRedirect(reverse('article', args=[str(artid)]))


def create_article(request):
    if not request.user.is_superuser:
        return redirect('news')
    elif request.method == "POST":
        form = AddPostForm(request.POST, request.FILES, )
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = AddPostForm()
    return render(request, 'home/create_article.html', {"form": form})


def update_article(request, artid):
    get_article = Article.objects.get(id=artid)
    if not request.user.is_superuser:
        return redirect('news')
    elif request.method == "POST":
        form = AddPostForm(request.POST, request.FILES, instance=get_article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('article', args=[str(artid)]))
    context = {
        'get_article': get_article,
        'update': True,
        'form': AddPostForm(instance=get_article)
    }
    return render(request, 'home/create_article.html', context)


def article(request, artid):
    if artid < Article.objects.last().id:
        return render(request, 'home/page404.html')
    post = Article.objects.get(id=artid)
    comment = Comments.objects.filter(article_id=artid)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.article_id = artid
            form.save()
            return HttpResponseRedirect(f"{(reverse('article', args=[str(artid)]))}#comments")
    elif request.user.is_authenticated:
        form = CommentForm
        Article.objects.filter(id=artid).update(views=F("views")+1)
    else:
        form = CommentFormDisabled
    return render(request, f'home/article.html', {"article_id": artid, "comments": comment, "form": form, 'post': post})


def delete_comment(request, artid):
    if artid < Article.objects.last().id:
        return render(request, 'home/page404.html')
    Comments.objects.filter(id=request.GET.get('comment_id')).delete()
    return HttpResponseRedirect(reverse('article', args=[str(artid)]))


def delete_article(request, artid):
    Article.objects.filter(id=artid).delete()
    return redirect('news', )


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
    HttpResponseNotFound(render_to_string('home/page404.html'))


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
