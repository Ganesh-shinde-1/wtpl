from django.db import models

# Create your models here.


class address(models.Model):
    phone=models.IntegerField()
    email=models.EmailField()
    adr=models.TextField(max_length=255)
    office_time=models.TextField(max_length=255)
    office_loacation=models.TextField(max_length=255)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.adr} - {self.created_at}'

class contact_form(models.Model):
    name=models.CharField(max_length=255)
    phone=models.IntegerField()
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    msg=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'

class WorkwithUS(models.Model):
    name=models.CharField(max_length=255)
    phone=models.IntegerField()
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    msg=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name} - {self.created_at}'

# class contact_form(models.Model):
#     name=models.CharField(max_length=255)
#     phone=models.IntegerField()
#     email=models.EmailField()
#     subject=models.CharField(max_length=255)
#     msg=models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

class blogs(models.Model):
    title=models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/' , default=True)
    content=models.TextField()
    created_At=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} - {self.created_at}'

class blog_comment(models.Model):
    blog_id=models.ForeignKey(blogs, related_name="blog", on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    email=models.EmailField()
    msg=models.TextField(max_length=255)
    time=models.TimeField(auto_now=True)
    date=models.DateField(auto_now=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.blog_id.title} - {self.email}  - {self.created_at} '

class it_services(models.Model):
    title=models.CharField(max_length=255)
    image = models.ImageField(upload_to='it_services/' , default=True)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title} - - {self.created_at}'
    
class con_services(models.Model):
    title=models.CharField(max_length=255)
    image = models.ImageField(upload_to='mat_services/' , default=True)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title} - {self.created_at}'

class services_contact(models.Model):

    name=models.CharField(max_length=255)
    phone=models.IntegerField()
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    msg=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f'{self.name} - {self.created_at}'    

class about_us(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    image = models.ImageField(upload_to='about_us/' , default=True)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}  - {self.created_at}'


class slider(models.Model):
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=255)
    image = models.ImageField(upload_to='sliders/' , default=True)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=True)

    
    

    def __str__(self):
        return f'{self.title} - {self.created_at}'
    

class brand_logo(models.Model):
    title=models.CharField(max_length=255)
    image = models.ImageField(upload_to='brand_logo/' , default=True)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}  - {self.created_at}'


class social_media(models.Model):
    title=models.CharField(max_length=255)
    instagram=models.CharField(max_length=255)
    facebook=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    twitter=models.CharField(max_length=255)
    whatsapp=models.CharField(max_length=255)
    active=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    