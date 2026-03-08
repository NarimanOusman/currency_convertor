from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings



# Create your views here.
def index(request):
     return render(request, 'index.html')

def dashboard(request):
     return render(request, 'dashboard.html')

def privacy_policy(request):
     return render(request, 'privacy_policy.html')

def terms_of_service(request):
     return render(request, 'terms_of_service.html')

def contact(request):
     if request.method == 'POST':
          name = request.POST.get('name', '')
          email = request.POST.get('email', '')
          subject = request.POST.get('subject', '')
          message = request.POST.get('message', '')

          # Validate form data
          if not all([name, email, subject, message]):
               return render(request, 'contact.html', {'error': 'All fields are required.'})

          try:
               # Create email message
               email_subject = f"New Contact Form Submission: {subject}"
               email_body = f"""
Hello,

You have received a new contact form submission from your website.

From: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
This is an automated message from your CurrencyX contact form.
               """

               # Send email to yourself
               send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    ['narimanrobo8@gmail.com'],
                    fail_silently=False,
               )

               # Return success message
               return render(request, 'contact.html', {'success': 'Your message has been sent successfully! We will get back to you soon.'})

          except Exception as e:
               return render(request, 'contact.html', {'error': f'Error sending message: {str(e)}'})
     
     return render(request, 'contact.html') 