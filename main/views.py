from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Shorturl
import random
import string


def main(request):
    return render(request, "main/main.html")


def contacts(request):
    return render(request, 'main/contacts.html')


def randomGenerator():
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(6))


@login_required(login_url='/user/authorization')
def dashboard(request):
    usr = request.user
    urls = Shorturl.objects.filter(user=usr)
    return render(request, 'main/link.html', {'urls': urls})


@login_required(login_url='/user/authorization')
def generate(request):
    if request.method == 'POST':
        if request.POST['original'] and request.POST['short']:
            usr = request.user
            original = request.POST['original']
            short = request.POST['short']
            check = Shorturl.objects.filter(shortQuery=short)
            if not check:
                check = Shorturl.objects.filter(originalURL=original, user = usr)
                if not check:
                    newURL = Shorturl(
                        user=usr,
                        originalURL=original,
                        shortQuery=short,
                    )
                    newURL.save()
                    return redirect(dashboard)
                else:
                    messages.error(request, 'Ссылка которую Вы вводите уже у Вас есть !')
                    return redirect(dashboard)
            else:
                messages.error(request, 'Короткая ссылка уже существует, выберите другую')
                return redirect(dashboard)
        elif request.POST['original']:
            usr = request.user
            original = request.POST['original']
            generated = False
            while not generated:
                short = randomGenerator()
                check = Shorturl.objects.filter(shortQuery=short)
                if not check:
                    check = Shorturl.objects.filter(originalURL=original, user = usr)
                    if not check:
                        newURL = Shorturl(
                            user=usr,
                            originalURL=original,
                            shortQuery=short,
                        )
                        newURL.save()
                        return redirect(dashboard)
                    else:
                        messages.error(request, 'Ссылка которую Вы вводите уже у Вас есть !')
                        return redirect(dashboard)
                else:
                    continue

        else:
            messages.error(request, 'Пожалуйста, введите корректные значения')
            return redirect(dashboard)
    else:
        return redirect('/link')


def redirecttoshort(request, query=None):
    if not query or query == None:
        return render(request, 'main/link.html')
    else:
        try:
            check = Shorturl.objects.get(shortQuery=query)
            check.visits += 1
            check.save()
            url_to_redirect = check.originalURL
            return redirect(url_to_redirect)
        except:
            messages.error(request, 'Ссылка не существует или что-то пошло не так.')
            return render(request, 'main/link.html')


@login_required(login_url='/user/authorization')
def deleteurl(request):
    if request.method == "POST":
        short = request.POST['delete']
        check = Shorturl.objects.filter(shortQuery=short)
        checkempty = list(check)
        if checkempty == []:
            messages.error(request, 'Ссылки уже нет или что-то пошло не так.')
            return redirect(dashboard)
        else:
            check.delete()
            return redirect(dashboard)
    else:
        return redirect(dashboard)
