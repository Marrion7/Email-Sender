from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')        
        email = request.POST.get('email')
        send_mail(
            subject,
            message,
            'marrionhodonou@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse('Your Email is already send!')
    return render(request, 'auto/email.html')