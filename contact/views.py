from django.shortcuts import redirect, render
from . models import Contact
# Create your views here.

# Home
def index(request):
  contacts = Contact.objects.all()
  return render(request,'index.html',{'contacts':contacts})

# Add Contact
def add_contact(request):
  if request.method == 'POST':
    new_contact = Contact(
      full_name = request.POST['fullname'],
      relationship = request.POST['relationship'],
      email = request.POST['email'],
      phone_number = request.POST['phone-number'],
      address = request.POST['address']
    )
    new_contact.save()
    return redirect('/')
  return render(request,'new.html')

  # Profile
def contact_profile(request,pk):
  contact = Contact.objects.get(id=pk)
  return render(request,'contact-profile.html',{'contact':contact})