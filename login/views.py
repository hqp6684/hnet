from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login

from login.forms import loginForm, AuthenticationForm

from django.http import HttpResponseRedirect, HttpResponse


from django.core.urlresolvers import reverse_lazy


import warnings

from django.conf import settings
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse

from django.utils.encoding import force_text
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.utils.six.moves.urllib.parse import urlparse, urlunparse
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters




def login_redirect(request, template_name='login/login_success.html'):
    data={}

    return render(request, template_name, data)

# Login user method
def loginUser(request):
    # Checks if user is already logged in
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")  # Redirect to home
    form = loginForm(request.POST or None)
    # Logs in user and sends user to a page redirect
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/")  # Redirect to a success page.
    return render(request, 'login/login.html', {'form': form})

@sensitive_post_parameters()
@csrf_protect
@never_cache
def loginTest1(request, template_name='login/login.html'):
    args = {}
    if request.user.is_authenticated():
        return redirect('login_redirect')
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('login_redirect')
    else:
        form = AuthenticationForm()
    args['form'] = form
    return render(request, template_name,args)
'''
@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='login/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    context = {
        'form': form,
    }

    return TemplateResponse(request, template_name, context)

'''



def logout(request,
           template_name='login/loggedout.html'):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    auth_logout(request)
    context ={}
    return render(request, template_name, context)



