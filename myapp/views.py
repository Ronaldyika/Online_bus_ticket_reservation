from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()
    
    context={
        'form' : form
    }
    return render(request,'admin_login/signup.html', context)


def signin(request):
    return render(request, 'templates/admin_login/signin')

def index(request):
    chooses =Choose.objects.all()
    latest_blogs = Blog.objects.order_by('-date_created')[:3]
    slide = SlideShow.objects.all()
    

    context={
        'chooses' : chooses,
        'latest_blogs' : latest_blogs,
        'slide' : slide,
    }
    return render(request, 'transport/index.html', context)

def choose(request):
    choose = Choose.objects.all()
    context={
        # 'context' : context
    }
    return render(request, 'transport/choose/choose.html')

def payticket(request):
    return render(request, 'transport/payticket.html')


def blog(request):
    blogs = Blog.objects.all()
    context={
        'blogs' : blogs
    }
    return render(request, 'transport/blog/blog.html', context)

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogForm()

    context={
        'form' : form
    }
    return render(request,'transport/blog/create_blog.html', context)


def blog_update(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST or None, request.FILES or None, instance= blog)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogForm(instance=blog)
    
    context={
        'form' : form
    }    
    return render(request, 'transport/blog/blog_update.html', context)

def blog_delete(request, pk):
    blog = Blog.objects.get(id = pk)
    blog.delete()
    return redirect('blog')
    
def blog_content(request, pk):
    blog_content = Blog.objects.get(id = pk)
    
    context={
        'blog_content' : blog_content
    }
    return render(request, 'transport/blog/blog_content.html', context)

def contact(request):
    return render(request, 'transport/contact.html')



# user registration
def customer_registration(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            
            customer_registration= form.save(commit=False)
            
            begin = customer_registration.current_destination
            end = customer_registration.final_destination
            no_of_sits= customer_registration.no_of_sites
            
            if begin == end:
                messages.info(request, 'The Current and Final destinations must be different.')
                return redirect('customer_registration')
            
            elif no_of_sits <1:
                
                messages.info(request, 'The Current and Final destinations must be different.')
                return redirect('customer_registration')
            
            else:
                customer_registration.save()
    
    else:
        form = CustomerRegistrationForm()
    
    context={
        'form' : form
    }
    return render(request, 'transport/customer/customer_registration.html', context)


