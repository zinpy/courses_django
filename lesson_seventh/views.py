from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, View, ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from lesson_sixth.models import Human
from .forms import UserCreateForm


# class MainView(TemplateView):
#     template_name = 'main_seventh.html'
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             humans = Human.objects.all()
#             ctx = {}
#             ctx['humans'] = humans
#             return render(request, self.template_name, ctx)
#         else:
#             return render(request, self.template_name, {})

class MainView(ListView):
    template_name = 'main_seventh.html'
    # queryset = Human.objects.all()
    context_object_name = 'humans'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Human.objects.all()
        # else:
        #     return None


class RegisterFormView(FormView):
    # какая форма будет использоваться при регистрации
    form_class = UserCreateForm
    # срабатывает в случае успешной регистрации
    success_url = "/lesson-seventh/login/"

    template_name = "register.html"

    # метод отвечает за успешную регистрацию
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    # def form_invalid(self, form):
    #
    #     return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/lesson-seventh/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        user = form.get_user()
        # Выполняем аутентификацию пользователя.
        login(self.request, user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/lesson-seventh/")

