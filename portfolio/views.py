from django.shortcuts import render,redirect
from portfolio.models import Contact, Blogs, Services


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def resume(request):
    return render(request,'resume.html')

def services(request):
    posts = Services.objects.all()
    context = {'posts':posts}
    return render(request,'services.html',context)
def handleblog(request):
    posts =Blogs.objects.all()
    context = {'posts':posts}
    return render(request, 'handleblog.html',context)

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphone = request.POST.get('num')
        fdesc = request.POST.get('desc')
        #print(fname, femail, fphone, fdesc)
        query = Contact(name=fname, email=femail, phone=fphone, description=fdesc)
        query.save()
        return redirect('/contact')


    return render(request, 'contact.html')