from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def contact(request):
	if request.method == "POST":

		author = request.POST['author']
		email = request.POST['email']
		subject = request.POST['subject']
		comment = request.POST['comment']

		# Send email
		send_mail(
			subject, # subject
			comment, # message
			email, # from email
			['xzgigabytexz@gmail.com'], # to email
			)

		return render(request, 'contact.html', {'author': author})
		
	else:
		return render(request, 'contact.html', {})

def gallery(request):
	return render(request, 'gallery.html', {})

def error(request):
	return render(request, '404.html', {})
