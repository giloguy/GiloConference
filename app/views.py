from django.shortcuts import render
from .models import Register,Contact,Program

def home_page(request):

    prog1 = Program.objects.filter(day="Day 1")
    prog2 = Program.objects.filter(day="Day 2")
    prog3 = Program.objects.filter(day="Day 3")
    prog4 = Program.objects.filter(day="Day 4")
    
    
    if "register" in request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        topic = request.POST["topic"]
        description = request.POST["description"]

        register = Register(
                name              =name,
                email             =email,
                phone             =phone,
                address           =address,
                topic  =topic,
                description =description,
    )
        register.save()
        print("Registered successfully.....")
        return render(request, "home_page.html")
    context= {
        'prog1':prog1,
        'prog2':prog2,
        'prog3':prog3,
        'prog4':prog4,
            }
    return render(request, 'home_page.html', context)

def contact_us(request):
    if "send" in request.POST:
        sname = request.POST["name"]
        semail = request.POST["email"]
        smsg = request.POST["message"] 
        
        contact = Contact(name=sname,email=semail,message=smsg)

        contact.save()

        print("Message sent successfully.....")
    return render(request, 'contactus.html', {})    