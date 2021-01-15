from contact.models import Contact
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']
        user_id = request.POST['user_id']

        # TODO: sanitization of data
        contact = Contact(full_name=full_name, phone_no=phone_no, email=email, company_name=company_name, subject=subject, message=message, user_id=user_id)
        contact.save();
        messages.success(request, 'Thanks for reaching out.')
        return redirect('home')

