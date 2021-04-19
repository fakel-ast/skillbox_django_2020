from datetime import datetime

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views import View

from app_users.forms import UserLoginForm


def user_login_view(request):

    if request.method == 'POST': #
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:

                if user.is_active:
                    login(request, user)
                    if user.is_superuser:
                        form.add_error('__all__', 'Администратор не может быть авторизован')
                    if 8 > int(datetime.now().strftime('%H')) > 22:
                        form.add_error('__all__', 'С 22 до 8 часов нельзя авторизовываться!')
                    if not form.errors:
                        return HttpResponse('<h2>Вы успешно авторезировались</h2>')



                else:
                    form.add_error('__all__', 'Учетная запись пользователя не активна!')
            else:
                form.add_error('__all__', 'Неправильный логин или пароль!')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'app_users/user_login.html', context=context)


class AnotherUserLoginView(LoginView):
    template_name = 'app_users/user_login.html'


class MainPageView(View):

    def get(self, request):
        return render(request, 'home.html')
