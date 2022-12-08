from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="partials/form.html",
    extra_context={
        "form_name": "회원가입",
        "submit_label": "회원가입",
    },
    success_url=reverse_lazy("accounts:login"),
)


login = LoginView.as_view(
    template_name="partials/form.html",
    extra_context={
        "form_name": "로그인",
        "submit_label": "로그인",
    },
)

logout = LogoutView.as_view(
    next_page="accounts:login",
)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


profile = ProfileView.as_view()
