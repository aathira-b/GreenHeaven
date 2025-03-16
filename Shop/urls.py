from django.urls import path
from Shop import views
app_name="Shop"

urlpatterns = [
    path('shophome/', views.shophome, name='shophome'),
    path('sprofile/',views.sprofile,name='sprofile'),
    path('shopedit/',views.shopedit,name='editshop'),
    path('changespwd/',views.changeshoppwd,name='changeshoppwd'),
    path('complaint/',views.complaint,name='complaint'),
    path('delcomplaint<int:id>/',views.delcomplaint,name='delcomplaint'),
    path('product/', views.product, name='product'),
    path('ajaxsub/', views.ajaxsub, name='ajaxsub'),
    path('delproduct<int:id>/',views.delproduct,name='delproduct'),
    path('stock/<int:id>',views.stock,name='stock'),
    path('delstock<int:id>/',views.delstock,name='delstocks'),
    path("viewbooking/", views.viewbooking,name="viewbooking"),
    path("bookingstatus/<int:id>/<int:sts>", views.bookingstatus,name="bookingstatus"),
     path('logout/',views.logout,name='logout'),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('report/',views.report,name="report"),
    path('ajaxreport/',views.ajaxreport,name="ajaxreport"),
    

]

