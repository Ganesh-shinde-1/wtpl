from django.shortcuts import render , redirect , get_object_or_404 , HttpResponseRedirect
from .models import address , contact_form , WorkwithUS  , blogs , blog_comment , services_contact , it_services  , con_services , about_us , slider , brand_logo , social_media



def home(request):
    social=social_media.objects.first()
    sliders=slider.objects.filter(active=True)
    brand_l=brand_logo.objects.filter(active=True)
    blog1=blogs.objects.filter(active=True)
    data={
        'slider':sliders,
        'brand_logo':brand_l,
        'blogs':blog1,
        'social':social,
    }
    return render(request, 'index.html' , data)

def services(request):
    social=social_media.objects.first()
    data={
        'social':social,
    }

    return render(request, 'services.html' , data  )

def mat_ser(request):
    social=social_media.objects.first()

    ser=con_services.objects.filter(active=True)
    data={
        'services':ser,
        'social':social,

    }
    # print(data['services'])
    return render(request, 'material_sup.html', data )

def it_ser(request):
    social=social_media.objects.first()

    ser=it_services.objects.filter(active=True)
    data={
        'services':ser,
        'social':social,

    }

    return render(request, 'it_Services.html' ,data )

def ser_cont(request):
    social=social_media.objects.first()

    try:
        if request.method == 'POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            sub=request.POST.get('subject')
            msg=request.POST.get('message')
            services_contact.objects.create(name=name, email=email, phone=phone, subject=sub, msg=msg)
            # return redirect
    except:
       pass
    data={
        'social':social,

    }
    return render(request, 'con_Ser.html' , data )

def aboutUs(request):
    social=social_media.objects.first()

    about=about_us.objects.filter(active=True)
    data={
        "aboutus":about,
        'social':social,

    }

    return render(request, 'about_us.html' ,data)

def contactus(request):
    social=social_media.objects.first()

    d1=address.objects.first()
    try:
        if request.method == 'POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            sub=request.POST.get('subject')
            msg=request.POST.get('message')
            contact_form.objects.create(name=name, email=email, phone=phone, subject=sub, msg=msg)
    except:
       pass
    
    data={
        'd1':d1.office_loacation,
        'd2':d1.phone,
        'd3':d1.email,
        'd4':d1.adr,
        'd5':d1.office_time,
        'social':social,


    }

    

    return render(request, 'contact.html' , data )

def blog_full(request , id):
    social=social_media.objects.first()

    blog1 = get_object_or_404(blogs, id=id)
    blog_com=blog_comment.objects.filter(blog_id=id)
    
    data={
        'blogs':blog1,
        'com':blog_com,
        'social':social,

    }
    return render(request, 'blog-single.html', data)

def blog(request):
    social=social_media.objects.first()

    blog1=blogs.objects.filter(active=True)
    data={
        'blogs':blog1,
        'social':social,

    }
    
    return render(request, 'blog.html' , data )

def blog_c(request):
    social=social_media.objects.first()

    if request.method == 'POST':
        com_id=request.POST['id']
        next_url=request.POST.get('path')
        first_name=request.POST.get('first-name')
        last_name=request.POST.get('last-name')
        email=request.POST.get('email')
        msg=request.POST.get('message')
        print(msg)
        print(first_name)
        print(last_name)
        blog1 = get_object_or_404(blogs, id=com_id)
        if email:
            blog_comment.objects.create(blog_id=blog1,first_name=first_name, email=email, last_name=last_name, msg=msg)
        print(id)

        full_url = request.build_absolute_uri(f'{next_url}')
    
    return HttpResponseRedirect(full_url)

def WorkWithUS(request):
    social=social_media.objects.first()

    try:
        if request.method == 'POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            sub=request.POST.get('subject')
            msg=request.POST.get('message')
            WorkwithUS.objects.create(name=name, email=email, phone=phone, subject=sub, msg=msg)
            # return redirect
    except:
       pass

    data={
        'social':social,

    }
    return render(request, 'appointment.html' )
