from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def main(request):
    title = 'Main Page'

    return render(request,
                  'accounts/main.html',
                  {'title': title})


def user_info(request):
    userinfo = {
        'username': 'Olha',  # Put your name here
        'country': 'Ukraine',  # Put your country here
    }
    context = {'userinfo': userinfo,
               'title': 'User Info Page'}

    return render(request,
                  'accounts/user_info.html',
                  context)
