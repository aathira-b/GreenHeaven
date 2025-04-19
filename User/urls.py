from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('ChangePassword/',views.changepassword,name="changepassword"),
    path('sendrequest<int:id>/',views.sendrequest,name='sendrequest'),
    path('myrequest/',views.myrequest,name='myrequest'),
    path('feedback/',views.feedback,name='feedback'),
     path('complaint/',views.complaint,name='complaint'),
     path('delcomplaint<int:id>/',views.delcomplaint,name='delcomplaint'),


    path('viewshop/',views.viewshop, name='viewshop'),   
    path('viewproduct/<int:id>',views.viewproduct, name='viewproduct'),   
    path('Addcart/<int:pid>',views.Addcart, name='Addcart'),   
    path('Mycart/',views.Mycart, name='Mycart'),   
    path("DelCart/<int:did>", views.DelCart,name="delcart"),
    path("CartQty/", views.CartQty,name="cartqty"),

path("productpayment/", views.productpayment,name="productpayment"),
path("payment/<int:id>", views.payment,name="payment"),
path("mybooking/", views.mybooking,name="mybooking"),

    path('rating/<int:mid>',views.rating,name="rating"),  
path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
path('starrating/',views.starrating,name="starrating"),
 
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
  
    path('clearchat/',views.clearchat,name="clearchat"),
    path('logout/',views.logout,name='logout'),
    path('viwedesigner/',views.viwedesigner,name='viwedesigner'), 
     path('viewwork/<int:did>',views.viewwork,name='viewwork'), 
  path('viewgallery/<int:id>',views.viewgallery,name='viewgallery'),
  path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),


     path('chat/<int:id>',views.chat,name="chatd"),
    path('ajaxchatd/',views.ajaxchatD,name="ajaxchatD"),
    path('ajaxchatviewd/',views.ajaxchatviewD,name="ajaxchatviewD"),
    path('clearchatd/',views.clearchatD,name="clearchatD"),


    path('ajaxsearchproduct/',views.ajaxsearchproduct,name="ajaxsearchproduct"),

    path("bill/<int:id>", views.bill, name="bill"),

    path('add_to_wishlist/', views.add_to_wishlist, name='AddToWishlist'),
    # Remove from wishlist AJAX endpoint
    # path('remove_from_wishlist/<int:product_id>/', views.remove_from_wishlist, name='RemoveFromWishlist'),


]