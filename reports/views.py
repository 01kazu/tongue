from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from .forms import SignUpForm, ReportForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Report


activate_email_info = ""
def home(request):
    return render(request, 'home.html')


def index(request):
    pass



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # profile.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('reports/html/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            print(type(user.pk))
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(force_bytes(urlsafe_base64_decode(uid)))

            activate_email_info = 'We have sent you an email, please confirm your email address to complete registration'
            return render(request, 'reports/html/confirm_email.html', {"active": activate_email_info})
            # 'We have sent you an email, please confirm your email address to complete registration'
    else:
        form = SignUpForm()
    return render(request, 'reports/html/signup.html', {'form': form})


def activate_email(request):
    return render(request, 'reports/html/confirm_email.html', {"active": activate_email_info})


#activate account
def activate_account(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    print(uidb64)
    print(token)
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        print(account_activation_token.check_token(user, token))
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend') 

        activate_success = 'Your account has been activated successfully'
        return render(request, 'reports/html/confirm_email.html', {"active": activate_success})
    else:
        activate_failure = 'Activation link is invalid!'
        return render(request, 'reports/html/confirm_email.html', {"active": activate_failure})


def password_reset(request):
    return render(request, 'reports/html/registration/password_reset_form.html')


def login_user(request):
    print(request)
    print(request.POST)
    print(dir(request))
    error=""
    username  = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse("reports:welcome"))
        else:
            return render(request, "registration/login.html")
    else:
            error = "Username and Password do not match. Try again"

    return render(request, "reports/html/login.html", { "error" : error } )


@login_required
def welcome(request):
    # print(dir(request.user))
    if request.method == "POST":
        form = ReportForm(request.POST)
        form.user = request.user.username
        print("hello")
        print(dir(request))
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user.username
            form.save()
            return redirect("reports:all_posts")
    else:
        form = ReportForm()
    return render(request, "reports/html/welcome.html" , {"form" :form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("reports:login_user"))
        
    
# @login_required
class AllPosts(ListView, LoginRequiredMixin):
    model = Report
    context_object_name = 'post_list'
    template_name = "reports/html/all_posts.html"
    ordering = ['-date']
    paginate_by = 10
    login_url = ''
    


class AllPostsDetail(View, LoginRequiredMixin):
    login_url = ''

    def get(self, request, pk):
        post_detail = Report.objects.get(pk=pk)
        return render(request, 'reports/html/all_posts_detail.html', {'post_detail': post_detail})
