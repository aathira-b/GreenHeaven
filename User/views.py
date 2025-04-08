from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Designer.models import *
from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Q
import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Wishlist
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import tbl_product, Wishlist
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    if 'uid' in request.session:
         return render(request, 'User/HomePage.html')
    else:
          return redirect('Guest:Login')

def myprofile(request):
    if 'uid' in request.session:
         user=tbl_user.objects.get(id=request.session['uid'])
         return render(request,'User/MyProfile.html',{'user':user})
    else:
          return redirect('Guest:Login')


def editprofile(request):
     if 'uid' in request.session:
          user=tbl_user.objects.get(id=request.session['uid'])
          if request.method == "POST":
               user.user_name=request.POST.get("txtname")
               user.user_email=request.POST.get("txtemail")
               user.user_contact=request.POST.get("txtcontact")
               user.user_address=request.POST.get("address")
               user.save()
               return redirect("User:myprofile")
          else:
               return render(request, 'User/EditProfile.html',{'user':user})
     else:
          return redirect('Guest:Login')
         
def changepassword(request):
     if 'uid' in request.session:
           npassword=request.POST.get('txtpass')
           rpassword=request.POST.get('txtpassword')
           opassword=request.POST.get('txtpwd')
           user=tbl_user.objects.get(id=request.session['uid'])
           if request.method=="POST":
               if user.user_password == opassword:
                    if npassword==rpassword:
                         user.user_password=request.POST.get("txtpass")
                         user.save()
                         return redirect("User:myprofile ")
                    else:
                         return render(request,'User/ChangePassword.html',{"msg":"Error in Confirm password"})
               else:
                    return render(request,'User/ChangePassword.html',{"msg":"Error in Old password"})
           else:
                    return render(request,'User/ChangePassword.html')
     else:
          return redirect('Guest:Login')
         
      
def sendrequest(request,id):
     if request.method=="POST":
         tbl_designrequest.objects.create(user = tbl_user.objects.get(id=request.session['uid']),
                                      work = tbl_work.objects.get(id=id),
                                      designrequest_todate=request.POST.get("txtdate"))
     return render(request,'User/SendRequest.html')

def myrequest(request):
     if 'uid' in request.session:
          designerequest=tbl_designrequest.objects.all()
          work=tbl_work.objects.all()
          designer=tbl_designer.objects.all()
          return render(request,'User/MyRequest.html', {"designerequest":designerequest,"work":work,"designer":designer})
     else:
          return redirect('Guest:Login')

def feedback(request):
      if 'uid' in request.session:
           if request.method=="POST":
                tbl_feedback.objects.create(user = tbl_user.objects.get(id=request.session['uid']),
                                      feedback_content = request.POST.get("Feedback"))
                return redirect("User:feedback")
           else:
                return render(request,'User/Feedback.html')
      else:
          return redirect('Guest:Login')
     
def complaint(request):
     if 'uid' in request.session:
          complaint=tbl_complaint.objects.filter(user=request.session['uid'])
          if request.method=="POST":
               tbl_complaint.objects.create(user=tbl_user.objects.get(id=request.session['uid']),
                                       complaint_title=request.POST.get("titile"),
                                       complaint_description=request.POST.get("content"))
               return redirect("User:complaint") 
          else:
               return render(request,'User/Complaint.html',{"complaint":complaint}) 
     else:
          return redirect('Guest:Login')   
     
def delcomplaint(request,id):
     tbl_complaint.objects.get(id=id).delete()
     return redirect("User:complaint")     
          
     


def viewproduct(request):
     if "uid" in request.session:
          category=tbl_category.objects.all()
          ar=[1,2,3,4,5]
          parry=[]
          avg=0
          product = tbl_product.objects.all()
          for i in product:
               total_stock = tbl_stock.objects.filter(product=i.id).aggregate(total=Sum('stock_count'))['total']
               total_cart = tbl_cart.objects.filter(product=i.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
               # print(total_stock)
               # print(total_cart)
               if total_stock is None:
                    total_stock = 0
               if total_cart is None:
                    total_cart = 0
               total =  total_stock - total_cart
               i.total_stock = total
               tot=0
               ratecount=tbl_rating.objects.filter(product=i.id).count()
               if ratecount>0:
                    ratedata=tbl_rating.objects.filter(product=i.id)
                    for j in ratedata:
                         tot=tot+j.rating_data
                         avg=tot//ratecount
                         #print(avg)
                    parry.append(avg)
               else:
                    parry.append(0)
                    # print(parry)
          datas=zip(product,parry)
          return render(request,"User/ViewProduct.html",{"product":datas,"ar":ar,'category':category})
     else:
          return redirect('Guest:Login')  
    

def Addcart(request,pid):
    productdata=tbl_product.objects.get(id=pid)
    userdata=tbl_user.objects.get(id=request.session["uid"])
    bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(user=userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"User/ViewProduct.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata)
            msg="Added To cart"
            return render(request,"User/ViewProduct.html",{'msg':msg})
    else:
        bookingdata = tbl_booking.objects.create(user=userdata)
        tbl_cart.objects.create(booking=tbl_booking.objects.get(id=bookingdata.id),product=productdata)
        msg="Added To cart"
        return render(request,"User/ViewProduct.html",{'msg':msg})

def Mycart(request):
     if 'uid' in request.session:     

          if request.method=="POST":
               bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
               bookingdata.booking_totalamount=request.POST.get("carttotalamt")
               bookingdata.booking_adv_amount=float(request.POST.get("carttotalamt"))*10
               bookingdata.booking_status=1
               bookingdata.save()
               cart = tbl_cart.objects.filter(booking=bookingdata)
               for i in cart:
                    i.cart_status = 1
                    i.save()
               return redirect("User:productpayment")
          else:
               bookcount = tbl_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
               if bookcount > 0:
                    book = tbl_booking.objects.get(user=request.session["uid"],booking_status=0)
                    request.session["bookingid"] = book.id
                    cart = tbl_cart.objects.filter(booking=book)
                    for i in cart:
                         total_stock = tbl_stock.objects.filter(product=i.product.id).aggregate(total=Sum('stock_count'))['total']
                         total_cart = tbl_cart.objects.filter(product=i.product.id, cart_status=0).aggregate(total=Sum('cart_qty'))['total']
                         print(total_stock)
                    # print(total_cart)
                         if total_stock is None:
                              total_stock = 0
                         if total_cart is None:
                              total_cart = 0
                         total =  total_stock - total_cart
                         i.total_stock = total
                         print(total)
                    return render(request,"User/MyCart.html",{'cartdata':cart})
               else:
                    return render(request,"User/MyCart.html")
     else:
          return redirect('Guest:Login')  
     
          

def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("User:Mycart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("User:Mycart")   


def productpayment(request):
     if 'uid' in request.session:
          bookingdata = tbl_booking.objects.get(id=request.session["bookingid"])
          amt = bookingdata.booking_adv_amount
          cart = tbl_cart.objects.filter(booking=bookingdata)
          if request.method == "POST":
               for i in cart:
                    i.cart_status = 2
                    i.save()
               bookingdata.booking_status = 2
               bookingdata.save()
               return redirect("User:mybooking")
          else:
               return render(request,"User/Payment.html",{"total":amt})
     else:
          return redirect('Guest:Login')  
     


def payment(request,id):
     if 'uid' in request.session:
          bookingdata = tbl_booking.objects.get(id=id)
          amt = bookingdata.booking_amount
          cart = tbl_cart.objects.filter(booking=bookingdata)
          
          if request.method == "POST":
               for i in cart:
                    i.cart_status = 2
                    i.save()
               bookingdata.booking_status = 2
               bookingdata.save()
               return redirect("User:mybooking")
          else:
               return render(request,"User/Payment.html",{"total":amt})
     else:
          return redirect('Guest:Login') 
     

def mybooking(request):
     if 'uid' in request.session:
          booking=tbl_booking.objects.filter(user=request.session['uid'],booking_status__gte=0)
          cartdata = []
          for booking_obj in booking:
               carts_for_booking = tbl_cart.objects.filter(booking=booking_obj)
               cartdata.extend(carts_for_booking)
          return render(request,"User/MyBooking.html",{"cart":cartdata})
     else:
          return redirect('Guest:Login')  
     
     

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(product=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(product=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,product=tbl_product.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(product=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(product=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(product=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)




def logout(request):
     del request.session["uid"]
     return redirect('Guest:index')

def viewgallery(request,id):
     gallery=tbl_gallery.objects.filter(work=id)
     return render(request, 'User/ViewGallery.html',{"gallery":gallery})

def viewwork(request,did):
     work=tbl_work.objects.filter(designer=did)
     return render(request, 'User/ViewWork.html',{"work":work})

def viwedesigner(request):
     if 'uid' in request.session:
    
          designer= tbl_designer.objects.all()
          return render(request, 'User/ViewDesigner.html',{"designer":designer})
     else:
          return redirect('Guest:Login')  
       


def chatpage(request,id):
    shop  = tbl_shop.objects.get(id=id)
    return render(request,"User/Chat.html",{"shop":shop})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_shop = tbl_shop.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,shop_to=to_shop,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(shop_from=tid) | Q(shop_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(shop_to=request.session["tid"])) .delete()
    
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})



def chat(request,id):
    designer  = tbl_designer.objects.get(id=id)
    return render(request,"User/ChatD.html",{"designer":designer})

def ajaxchatD(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_designer = tbl_designer.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,designer_to=to_designer,chat_file=request.FILES.get("file"))
    return render(request,"User/ChatD.html")

def ajaxchatviewD(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(designer_from=tid) | Q(designer_to=tid))).order_by('chat_time')
    return render(request,"User/ChatViewD.html",{"data":chat_data,"tid":int(tid)})

def clearchatD(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(designer_to=request.session["tid"])) .delete()
    
    return render(request,"User/ClearChatD.html",{"msg":"Chat Deleted Sucessfully...."})


def ajaxsearchproduct(request):
     category=tbl_category.objects.all()
     ar=[1,2,3,4,5]
     parry=[]
     avg=0
     if((request.GET.get("sid")!="")):
          product = tbl_product.objects.filter(subcategory=request.GET.get("sid"))
          # print(request.GET.get("sid"))
          for i in product:
               total_stock = tbl_stock.objects.filter(product=i.id).aggregate(total=Sum('stock_count'))['total']
               total_cart = tbl_cart.objects.filter(product=i.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
               # print(total_stock)
               # print(total_cart)
               if total_stock is None:
                    total_stock = 0
               if total_cart is None:
                    total_cart = 0
               total =  total_stock - total_cart
               i.total_stock = total
               tot=0
               ratecount=tbl_rating.objects.filter(product=i.id).count()
               if ratecount>0:
                    ratedata=tbl_rating.objects.filter(product=i.id)
                    for j in ratedata:
                         tot=tot+j.rating_data
                         avg=tot//ratecount
                         #print(avg)
                    parry.append(avg)
               else:
                    parry.append(0)
                    # print(parry)
          datas=zip(product,parry)
          # print(datas)
     elif( (request.GET.get("cid")!="")):
          product = tbl_product.objects.filter(subcategory__category=(request.GET.get("cid")))
          for i in product:
               total_stock = tbl_stock.objects.filter(product=i.id).aggregate(total=Sum('stock_count'))['total']
               total_cart = tbl_cart.objects.filter(product=i.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
               # print(total_stock)
               # print(total_cart)
               if total_stock is None:
                    total_stock = 0
               if total_cart is None:
                    total_cart = 0
               total =  total_stock - total_cart
               i.total_stock = total
               tot=0
               ratecount=tbl_rating.objects.filter(product=i.id).count()
               if ratecount>0:
                    ratedata=tbl_rating.objects.filter(product=i.id)
                    for j in ratedata:
                         tot=tot+j.rating_data
                         avg=tot//ratecount
                         #print(avg)
                    parry.append(avg)
               else:
                    parry.append(0)
                    # print(parry)
          datas=zip(product,parry)
     return render(request,"User/AjaxSearchProduct.html",{"product":datas,"ar":ar,'category':category})

def bill(request, id):
     rand=random.randint(111111,999999)
     cart = tbl_cart.objects.get(id=id)
     bkid = cart.booking.id
     # print(bkid)
     cartdata = tbl_cart.objects.filter(booking=bkid)
     book = tbl_booking.objects.get(id=bkid)
     total = book.booking_totalamount
     user = tbl_user.objects.get(id=book.user.id)
     return render(request,"User/Bill.html",{"bill":cartdata,"tot":total,"book":book,'ran':rand,"user":user})



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import tbl_product, Wishlist

@csrf_exempt  # You can use csrf_protect instead if you prefer
def add_to_wishlist(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if not product_id:
            return JsonResponse({'success': False, 'message': 'Product ID not provided.'}, status=400)

        try:
            product = get_object_or_404(Product, id=product_id)
            user = request.user

            # Check if the item is already in the user's wishlist
            if Wishlist.objects.filter(user=user, product=product).exists():
                return JsonResponse({'success': False, 'message': 'Item already in wishlist.'})

            # Add the product to the wishlist
            Wishlist.objects.create(user=user, product=product)

            return JsonResponse({'success': True, 'message': 'Item added to wishlist!'})

        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Product not found.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
