from django.contrib.auth.views import LoginView, LogoutView

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
