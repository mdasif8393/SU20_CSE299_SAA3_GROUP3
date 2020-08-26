from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from .forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomerSignUpForm, SellerSignUpForm
from .models import User


# Create your views here.

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'accounts/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'accounts/seller_register.html'
    

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect("/")

def login_page(request):
    return render(request, 'accounts/login.html')

def login_request(request):
    if request.method == 'POST':
        valuenext= request.POST.get('next')
        form =     AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and valuenext =='':
                login(request,user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            if user is not None and valuenext !='':
                login(request, user)
                messages.info(request,"You have successfully logged in")
                context= {'form': form, 'valuenext':valuenext}
                return redirect(valuenext)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "accounts/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")
      