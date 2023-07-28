from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User


def home(request):
    return render(request, 'home.html')


def main(request):
    title = 'Main Page'
    users_list = User.objects.all()
    context = {'title': title,
               'users_list': users_list}
    return render(request,
                  'accounts/main.html',
                  context)


def user_info(request):
    if request.method == 'GET':
        print('\n\nrequest.GET ==>>',
              request.GET,
              '\n\n')

        if request.session.get('username', False):
            userinfo = {
                'username': request.session['username'],
                'email': request.session['email'],
            }
        else:
            userinfo = False

        context = {'userinfo': userinfo,
                   'title': 'User Info Page'}
        template = 'accounts/user_info.html'
        return render(request,
                      template,
                      context)


def user_form(request):
    if request.method == 'GET':
        context = {'title': 'User Form Page'}
        template = 'accounts/user_form.html'

        return render(request,
                      template,
                      context)

    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        request.session['username'] = username
        request.session['email'] = email

        return redirect(reverse('accounts:user_info'))
