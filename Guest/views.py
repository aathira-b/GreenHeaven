from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.

def login(request):
     msg="Your Account Has Been Blocked By Admin."
     msg1="Your Login Request Is Still Processing ."
     if request.method == "POST":
          email = request.POST.get("txtemail")
          password = request.POST.get("txtpassword")
          usercount = tbl_user.objects.filter(user_email=email,user_password=password).count()
          designercount = tbl_designer.objects.filter(designer_email=email,designer_password=password).count()
          admincount = tbl_adminregister.objects.filter(adminregister_email=email,adminregister_password=password).count()
          shopcount = tbl_shop.objects.filter(shop_email=email,shop_password=password).count()
          if usercount > 0:
               user = tbl_user.objects.get(user_email=email,user_password=password)
               if(user.user_status==0):
                    request.session["uid"] = user.id
                    return redirect("User:homepage")
               else:
                    return render(request,"Guest/Login.html",{"msg":msg})

                    
          elif  designercount > 0:
               designer = tbl_designer.objects.get(designer_email=email,designer_password=password)
               if(designer.designer_status==1):
                    request.session["did"] = designer.id
                    return redirect("Designer:dhomepage")
               elif (designer.designer_status==2):
                    return render(request,"Guest/Login.html",{"msg":msg})
               else:
                    return render(request,"Guest/Login.html",{"msg1":msg1})

          elif admincount > 0:
               admin = tbl_adminregister.objects.get(adminregister_email=email,adminregister_password=password)
               request.session["aid"] = admin.id
               return redirect("Admin:homepage")
          elif shopcount > 0:
               shop = tbl_shop.objects.get(shop_email=email,shop_password=password)
               if (shop.shop_status==1):
                    request.session["sid"] = shop.id
                    return redirect("Shop:shophome")
               elif (shop.shop_status==2):
                    return render(request,"Guest/Login.html",{"msg":msg})
               else:
                    return render(request,"Guest/Login.html",{"msg1":msg1})

          else:
               return render(request, 'Guest/Login.html',{"msg":"Invalid Email or Password"})
     else:
          return render(request, 'Guest/Login.html')

def register(request):
     dis = tbl_district.objects.all()
     if request.method == "POST":
          tbl_user.objects.create(user_name=request.POST.get("txtname"),
                                  user_email=request.POST.get("txtemail"),
                                  user_contact=request.POST.get("txtcontact"),
                                  user_address=request.POST.get("address"),
                                  user_password=request.POST.get("pass"),
                                  user_photo=request.FILES.get("txtphoto"),
                                   place=tbl_place.objects.get(id=request.POST.get("Place")))
          return redirect("Guest:Register")
     else:
          return render(request, 'Guest/UserRegistration.html',{"district":dis})

def ajaxplace(request):
     place = tbl_place.objects.filter(district=request.GET.get("did"))
     return render(request, 'Guest/AjaxPlace.html', {"place":place})



def designer(request):
     dis = tbl_district.objects.all()
     if request.method == "POST":
          tbl_designer.objects.create(designer_name=request.POST.get("txtname"),
                                  designer_email=request.POST.get("txtmail"),
                                  designer_contact=request.POST.get("txtcontact"),
                                  designer_address=request.POST.get("txtaddress"),
                                  designer_photo=request.FILES.get("txtphoto"),
                                  designer_proof=request.FILES.get("txtproof"),
                                  designer_password=request.POST.get("txtpass"),
                                   place=tbl_place.objects.get(id=request.POST.get("Place")))
          return redirect("Guest:designer")
     else:
          return render(request, 'Guest/Designer.html',{"district":dis})
     
def shopreg(request):
     dis = tbl_district.objects.all()
     if request.method == "POST":
          tbl_shop.objects.create(shop_name=request.POST.get("txtname"),
                                  shop_email=request.POST.get("txtemail"),
                                  shop_contact=request.POST.get("txtcontact"),
                                  shop_address=request.POST.get("address"),
                                  shop_photo=request.FILES.get("txtphoto"),
                                  shop_proof=request.FILES.get("txtproof"),
                                  shop_password=request.POST.get("pass"),
                                   place=tbl_place.objects.get(id=request.POST.get("Place")))
          return redirect("Guest:shopreg")
     else:
          return render(request, 'Guest/ShopRegister.html',{"district":dis})     
