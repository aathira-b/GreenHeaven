from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def homepage(request):
     return render(request, 'Admin/AdminHome.html')

def Add(request):
    if request.method=='POST':
         num1=int(request.POST.get('FirstNumber'))
         num2=int(request.POST.get('SecondNumber'))
         result=num1+num2
         return render(request,'Admin/Add.html',{'res':result})
    else:
          return render(request, 'Admin/Add.html')
 
def largest(request):
    if request.method=='POST':
        num1=int(request.POST.get('FirstNumber'))
        num2=int(request.POST.get('SecondNumber'))
        if num1>num2:
            result=num1
        else:
            result=num2
        return render(request,'Admin/largest.html',{'res':result})
    else:
        return render(request, 'Admin/largest.html')
      
def calculator(request):
    if request.method=='POST':
        num1=int(request.POST.get('FirstNumber'))
        num2=int(request.POST.get('SecondNumber'))
        button=request.POST.get('CHECk')
        if button=='+':
            result=num1+num2
        elif button=='-':
            result=num1-num2
        elif button=='*':
            result=num1*num2 
        elif button=='/':
            result=num1/num2 
        return render(request,'Admin/calculator.html',{'res':result})
    else:
        return render(request, 'Admin/calculator.html')
def register(request):
    if request.method=='POST':
       firstname=(request.POST.get('firstname'))
       lastname=(request.POST.get('lastname'))
       name=firstname+" "+lastname
       gender=(request.POST.get('gender'))
       address=(request.POST.get('address'))
       contact=(request.POST.get('contact'))
       District=(request.POST.get('District'))
      
       return render(request,'Admin/register.html',{'name':name,'gender':gender,'address':address,'contact':contact,'district':District})
    else:
        return render(request, 'Admin/register.html')
    
def district(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get("District")
        DISTRICTCOUNT = tbl_district.objects.filter(district_name__iexact=district).count()
        if DISTRICTCOUNT > 0:
            return render(request, 'Admin/District.html', {'msg': "District Already Exists"})
        else:
            tbl_district.objects.create(
                district_name=district
            )
            return render(request, 'Admin/District.html', {'msg': "Data Inserted SuccessFully"})
    else:
        return render(request, 'Admin/District.html',{'district':dis})    
    
def editdistrict(request, id):
    district = tbl_district.objects.get(id=id)
    if request.method=="POST":
        district.district_name = request.POST.get("District")
        district.save()
        return redirect("Admin:district")
    else:
        return render(request, 'Admin/District.html',{"disdata":district})
    
def category(request):
    cate=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get("category")
        tbl_category.objects.create(
            category_name=category
        )
        return render(request,"Admin/category.html",{'msg':"Data Inserted SuccessFully"})
    else:
        return render(request, 'Admin/category.html',{'category':cate})  

def editcategory(request, id):
    category = tbl_category.objects.get(id=id)
    if request.method=="POST":
        category.category_name = request.POST.get("category")
        category.save()
        return redirect("Admin:category")
    else:
        return render(request, 'Admin/category.html',{"catdata":category})      
    

def delcategory(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect('Admin:category')
    
def deldistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect('Admin:district')

def adminregister(request):
    if 'aid' in request.session:
        reg=tbl_adminregister.objects.all()
        if request.method=="POST":
            name=request.POST.get("Name")
            email=request.POST.get("Email")
            password=request.POST.get("Password")
            tbl_adminregister.objects.create(
                adminregister_name=name,
                adminregister_email=email,
                adminregister_password=password
                )
            return render(request, 'Admin/AdminRegistration.html',{'msg':"Data Inserted SuccessFully"})    
        else:
            return render(request, 'Admin/AdminRegistration.html',{'admin':reg})
    else:
          return redirect('Guest:Login')  
    
def editadminreg(request, id):
    adminreg = tbl_adminregister.objects.get(id=id)
    if request.method=="POST":
        adminreg.adminregister_name = request.POST.get("Name")
        adminreg.adminregister_email = request.POST.get("Email")
        adminreg.adminregister_password = request.POST.get("Password")
        adminreg.save()
        return redirect("Admin:adminregister")
    else:
        return render(request, 'Admin/AdminRegistration.html',{"regdata":adminreg})          

def deladminreg(request,id):
    tbl_adminregister.objects.get(id=id).delete()
    return redirect('Admin:adminregister')

def place(request):
    place = tbl_place.objects.all()
    dis = tbl_district.objects.all()
    if request.method=="POST":

        place_name = request.POST.get("Place")
        # Check if the place already exists in the database
        placecount = tbl_place.objects.filter(place_name__iexact=place_name).count()
        if placecount > 0:
            return render(request, 'Admin/Place.html', {'msg': "Place Already Exists"})
        else:
            # If the place does not exist, create a new one
            district = tbl_district.objects.get(id=request.POST.get("District"))  
            tbl_place.objects.create(place_name=place_name,
                                    district=district)
            return redirect("Admin:place")
    else:
        return render(request, 'Admin/Place.html',{"district":dis,'place':place})

def delplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect('Admin:place')

def editplace(request, id):
    dis = tbl_district.objects.all()
    place = tbl_place.objects.get(id=id)
    if request.method=="POST":
        place.district = tbl_district.objects.get(id=request.POST.get("District"))
        place.place_name = request.POST.get("Place")
        place.save()
        return redirect("Admin:place")
    else:
        return render(request, 'Admin/Place.html',{"placedata":place,"district":dis,})   
    
def subcategory(request):
    sub = tbl_subcategory.objects.all()
    cat= tbl_category.objects.all()
    if request.method=="POST":
        subcategory=request.POST.get("Subcategory")
        subcount = tbl_subcategory.objects.filter(subcategory_name__iexact=subcategory).count()
        if subcount > 0:
            return render(request, 'Admin/Subcategory.html', {'msg': "Subcategory Already Exists"})
        else:
            category = tbl_category.objects.get(id=request.POST.get("category"))
            tbl_subcategory.objects.create(subcategory_name=request.POST.get("Subcategory"),
                                    category=category)
            return redirect("Admin:subcategory")
    else:
        return render(request, 'Admin/Subcategory.html',{"category":cat,'sub':sub})    
     
def delsub(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect('Admin:subcategory')     

def editsub(request, id):
    cat = tbl_category.objects.all()
    sub = tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
        sub.category = tbl_category.objects.get(id=request.POST.get("category"))
        sub.subcategory_name = request.POST.get("Subcategory")
        sub.save()
        return redirect("Admin:subcategory")
    else:
        return render(request, 'Admin/Subcategory.html',{"category":cat,'edit':sub})    
    
def verification(request): 
     if 'aid' in request.session: 
        user=tbl_user.objects.all()
        return render(request, 'Admin/UserVerification.html',{ 'user':user}) 
     else:
          return redirect('Guest:Login')  


# def useraccept(request,id):
#     user = tbl_user.objects.get(id=id)
#     user.user_status = 1
#     user.save()
#     return redirect("Admin:verification")     

def userreject(request,id):
    user = tbl_user.objects.get(id=id)
    user.user_status = 1
    user.save()
    return redirect("Admin:verification")  


# def product(request):
#      cat = tbl_category.objects.all()
#      if request.method == "POST":
#           tbl_product.objects.create(product_name=request.POST.get("txtname"),
#                                   product_price=request.POST.get("txtprice"),
#                                   product_details=request.POST.get("txtDetails"),
#                                   product_photo=request.FILES.get("txtphoto"),
#                                   subcategory=tbl_subcategory.objects.get(id=request.POST.get("SubCategory")))
#           return redirect("Admin:product")
#      else:
#           return render(request, 'Admin/Product.html',{"category":cat})
     
def ajaxsub(request):
     subcat = tbl_subcategory.objects.filter(category=request.GET.get("cid"))
     return render(request, 'Admin/Ajaxsub.html', {"subcat":subcat})    

def newdesigner(request): 
     if 'aid' in request.session: 
        designer=tbl_designer.objects.filter(designer_status=0)
        return render(request, 'Admin/NewDesigner.html',{ 'designer':designer}) 
     else:
          return redirect('Guest:Login')  

def designeraccept(request,id):
    designer = tbl_designer.objects.get(id=id)
    designer.designer_status = 1
    designer.save()
    return redirect("Admin:newdesigner")

def designerreject(request,id):
     designer = tbl_designer.objects.get(id=id)
     designer.designer_status = 2
     designer.save()
     return redirect("Admin:newdesigner")

def accepteddesigner(request):
    if 'aid' in request.session:
        designer= tbl_designer.objects.filter(designer_status = 1)
        return render(request, 'Admin/AcceptedDesigner.html',{ 'designer':designer})
    else:
          return redirect('Guest:Login')  
    

def rejecteddesigner(request):
    if 'aid' in request.session:
        designer= tbl_designer.objects.filter(designer_status = 2)
        return render(request, 'Admin/RejectedDesigners.html',{ 'designer':designer})
    else:
          return redirect('Guest:Login') 

def adminhome(request):
    if 'aid' in request.session:
        userdata=tbl_user.objects.all()
        shopdata=tbl_shop.objects.all()
        designerdata=tbl_designer.objects.all()
        complaints=tbl_complaint.objects.all()
        feedback=tbl_feedback.objects.all()
        ucount=userdata.count()
        scount=shopdata.count()
        dcount=designerdata.count()
        complaint=complaints.count()
        feedback=feedback.count()
        return render(request, 'Admin/AdminHome.html',{'ucount':ucount,'dcount':dcount,'scount':scount,'complaint':complaint,'feedback':feedback} )
    else:
          return redirect('Guest:Login')  

def newshops(request):
    if 'aid' in request.session:   
        shop=tbl_shop.objects.filter(shop_status=0)
        return render(request, 'Admin/New Shops.html',{ 'shop':shop}) 
    else:
          return redirect('Guest:Login')  

def shopaccept(request, id):
    # Fetch the shop details from the database
    shop = tbl_shop.objects.get(id=id)
    
    # Update the shop status to verified
    shop.shop_status = 1
    shop.save()
    
    
    return redirect("Admin:newshops")

def shopreject(request, id):
    # Fetch the shop details from the database
    shop = tbl_shop.objects.get(id=id)
    
    # Update the shop status to rejected
    shop.shop_status = 2
    shop.save()
    
    
    return redirect("Admin:newshops")

def acceptedshops(request):
    if 'aid' in request.session:
        shop= tbl_shop.objects.filter(shop_status = 1)
        return render(request, 'Admin/AcceptedShops.html',{ 'shop':shop})
    else:
          return redirect('Guest:Login')  

def rejectedshops(request):
   if 'aid' in request.session:
    rshops= tbl_shop.objects.filter(shop_status = 2)
    return render(request, 'Admin/RejectedShops.html',{ 'shop':rshops})
   else:
          return redirect('Guest:Login')  

def viewfeeback(request):
    if 'aid' in request.session:
        feedback = tbl_feedback.objects.all()
        return render(request, 'Admin/ViewFeedback.html',{"feedback":feedback})
    else:
          return redirect('Guest:Login')  

def viewcomplaints(request):
    if 'aid' in request.session:
        user=tbl_user.objects.all()
        desginer=tbl_designer.objects.all()
        shop=tbl_shop.objects.all()
        usercomplaint=tbl_complaint.objects.filter(user__in=user,complaint_status=0)
        designercomplaint=tbl_complaint.objects.filter(desginer__in=desginer,complaint_status=0)
        shopcomplaint=tbl_complaint.objects.filter(shop__in=shop,complaint_status=0)
        return render(request,'Admin/ViewComplaints.html',{"usercomplaint":usercomplaint,"designercomplaint":designercomplaint,"shopcomplaint":shopcomplaint})
    else:
          return redirect('Guest:Login')  

def replay(request,id):
    replay=tbl_complaint.objects.get(id=id)
    if request.method=="POST":
        replay.complaint_replay=request.POST.get("replay")
        replay.complaint_status=1
        replay.save()
        return redirect("Admin:viewcomplaints" )
    else:
        return render(request,'Admin/Replay.html',{"replay":replay})
    
def replayedcomplaint(request):
    if 'aid' in request.session:
        user=tbl_user.objects.all()
        desginer=tbl_designer.objects.all()
        shop=tbl_shop.objects.all()
        replayedusercomplaint=tbl_complaint.objects.filter(user__in=user,complaint_status=1)
        designercomplaint=tbl_complaint.objects.filter(desginer__in=desginer,complaint_status=1)
        shopcomplaint=tbl_complaint.objects.filter(shop__in=shop,complaint_status=1)
        return render(request,'Admin/ReplaydComplaints.html',{"replayedusercomplaint":replayedusercomplaint,"designercomplaint":designercomplaint,"shopcomplaint":shopcomplaint})  
    else:
          return redirect('Guest:Login')  
     
def logout(request):
     del request.session["aid"]
     return redirect('Guest:index') 






      

     








    
    
        

 