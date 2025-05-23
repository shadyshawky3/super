from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User


# Register View
class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # تشفير كلمة المرور
        user.save()
        messages.success(self.request, "Account created successfully. Please log in.")
        return super().form_valid(form)


# Login View
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        messages.success(self.request, "Welcome back!")
        return super().form_valid(form)
        #  return reverse_lazy('product_list')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)



# Logout View
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out.")
        return super().dispatch(request, *args, **kwargs)
