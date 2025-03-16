from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Designer.models import *
from User.models import *
from Shop.models import *
from datetime import datetime
from django.db.models import Q


# Create your views here.
def shophome(request):
    if 'sid' in request.session:
         return render(request, 'Shop/ShopHome.html')
    else:
         return redirect('Guest:Login')

def sprofile(request):
    if 'sid' in request.session:
         shop=tbl_shop.objects.get(id=request.session['sid'])
         return render(request, 'Shop/ShopProfile.html',{ 'shop':shop}) 
    else:
         return redirect('Guest:Login')

def shopedit(request):
     if 'sid' in request.session:
          shop=tbl_shop.objects.get(id=request.session['sid'])
          if request.method == "POST":
               shop.shop_name=request.POST.get("txtname")
               shop.shop_email=request.POST.get("txtemail")
               shop.shop_contact=request.POST.get("txtcontact")
               shop.shop_address=request.POST.get("address")
               shop.save()
               return redirect("Shop:editshop")
          else:
               return render(request, 'Shop/ShopEdit.html',{'shop':shop})
     else:
         return redirect('Guest:Login')

def changeshoppwd(request): 
    if 'sid' in request.session:      
         npassword=request.POST.get('txtpass')
         rpassword=request.POST.get('txtpassword')
         opassword=request.POST.get('txtpwd')
         shop=tbl_shop.objects.get(id=request.session['sid'])
         if request.method=="POST":
               if shop.shop_password == opassword:
                    if npassword==rpassword:
                         shop.shop_password=request.POST.get("txtpass")
                         shop.save()
                         return redirect("Shop:sprofile")
                    else:
                         return render(request,'Shop/ChangeShopPassword.html',{"msg":"Error in Confirm password"})
               else:
                    return render(request,'Shop/ChangeShopPassword.html',{"msg":"Error in Old password"})
         else:
            return render(request,'Shop/ChangeShopPassword.html')
    else:
         return redirect('Guest:Login')

def complaint(request):
     if 'sid' in request.session:
          shopcomplaint=tbl_complaint.objects.filter(shop=request.session['sid'])
          if request.method=="POST":
               tbl_complaint.objects.create(shop=tbl_shop.objects.get(id=request.session['sid']),
                                        complaint_title=request.POST.get("titile"),
                                        complaint_description=request.POST.get("content"))
               return redirect("Shop:complaint") 
          else:
               return render(request,'Shop/Complaint.html',{"shopcomplaint":shopcomplaint}) 
     else:
         return redirect('Guest:Login')   
     
def delcomplaint(request,id):
     tbl_complaint.objects.get(id=id).delete()
     return redirect("Shop:complaint")     
                   
def product(request):
     if 'sid' in request.session:
          cat = tbl_category.objects.all()
          product = tbl_product.objects.all()
          if request.method == "POST":
               tbl_product.objects.create(product_name=request.POST.get("txtname"),
                                   product_price=request.POST.get("txtprice"),
                                   product_details=request.POST.get("txtDetails"),
                                   product_photo=request.FILES.get("txtphoto"),
                                   subcategory=tbl_subcategory.objects.get(id=request.POST.get("SubCategory")),
                                   shop = tbl_shop.objects.get(id=request.session['sid']))
               return redirect("Shop:product")
          else:
               return render(request, 'Shop/AddProduct.html',{"category":cat,"product":product})
     else:
         return redirect('Guest:Login')
     
def ajaxsub(request):
     subcat = tbl_subcategory.objects.filter(category=request.GET.get("cid"))
     return render(request, 'Shop/Ajaxsub.html', {"subcat":subcat})   

def delproduct(request,id):
     tbl_product.objects.get(id=id).delete()
     return redirect("Shop:product")    

def stock(request,id):
      stock=tbl_stock.objects.all()
      if request.method=="POST":
           tbl_stock.objects.create(stock_count=request.POST.get("stock"),
                                    product=tbl_product.objects.get(id=id))
      return render(request, 'Shop/AddStock.html',{"stock":stock})


def delstock(request,id):
     tbl_stock.objects.get(id=id).delete()
     return redirect("Shop:product")    

def viewbooking(request):
     if 'sid' in request.session:
          shop = tbl_shop.objects.get(id=request.session["sid"])
          cart = tbl_cart.objects.filter(product__shop=shop)
          return render(request,"Shop/ViewBooking.html",{"cart":cart})
     else:
         return redirect('Guest:Login')

def logout(request):
     del request.session["sid"]
     return redirect('Guest:index')

def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Shop/Chat.html",{"user":user})

def ajaxchat(request):
    from_shop = tbl_shop.objects.get(id=request.session["sid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),shop_from=from_shop,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Shop/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    shop = tbl_shop.objects.get(id=request.session["sid"])
    chat_data = tbl_chat.objects.filter((Q(shop_from=shop) | Q(shop_to=shop)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Shop/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(shop_from=request.session["sid"]) | (Q(user_to=request.GET.get("tid")) )).delete()
    return render(request,"Shop/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def bookingstatus(request,id,sts):
     cart=tbl_cart.objects.get(id=id)
     cart.cart_status=sts
     cart.save()
     return redirect("Shop:viewbooking")  

def report(request):
     return render(request,"Shop/ViewReport.html")

def ajaxreport(request):
     if request.GET.get("fdate") != "" and request.GET.get("tdate") !="":
          cartdata = tbl_cart.objects.filter(booking__booking_date__gt=request.GET.get("fdate"),booking__booking_date__lt=request.GET.get("tdate"),product__shop=request.session["sid"])
          book = []
          for i in cartdata:
               book.append(i.booking.id)
          bkid = list(set(book))
          bdata = tbl_booking.objects.filter(id__in=bkid)
     elif request.GET.get("fdate") != "":
          cartdata = tbl_cart.objects.filter(booking__booking_date__gt=request.GET.get("fdate"),product__shop=request.session["sid"])
          book = []
          for i in cartdata:
               book.append(i.booking.id)
          bkid = list(set(book))
          bdata = tbl_booking.objects.filter(id__in=bkid)
     elif request.GET.get("tdate") != "":
          cartdata = tbl_cart.objects.filter(booking__booking_date__lt=request.GET.get("tdate"),product__shop=request.session["sid"])
          book = []
          for i in cartdata:
               book.append(i.booking.id)
          bkid = list(set(book))
          bdata = tbl_booking.objects.filter(id__in=bkid)
     total = 0
     for p in bdata:
          total = total + float(p.booking_totalamount)
     return render(request,"Shop/AjaxReport.html",{"data":bdata,"total":total})



   