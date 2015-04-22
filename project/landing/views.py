from landing.models import Emails, EmailForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render


def landing(request):
    return render_to_response("landing/index.html", RequestContext(request))


def form(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            mail = form.cleaned_data['email']
            try:
                obj = Emails.objects.get(email = mail)
                status = 2
            except Emails.DoesNotExist:
                obj = Emails(email = mail)
                obj.save()
                status = 1
                return HttpResponseRedirect('/thanks/')

            # Emails.objects.get_or_create(email = mail)
        else:
            status = 3
    else:
        status = 4

    # status = 1 -- Email добавлен в бд
    # status = 2 -- Email занят
    # status = 3 -- Form'a не валидна
    # status = 4 -- не POST запрос

    if status >= 2 and status <= 4:
        return render(request, 'landing/subscribe.html', {'status': status})
    elif status == 1:
        return HttpResponseRedirect('/thanks/')

    #    return render_to_response("landing/subscribe.html", status, RequestContext(request))


def thanks(request):
    return render_to_response("landing/thanks.html", RequestContext(request))


def about(request):
    return render_to_response("landing/about.html", RequestContext(request))
