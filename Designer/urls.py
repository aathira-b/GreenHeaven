from django.urls import path
from Designer import views
app_name="Designer"

urlpatterns = [


path('dhomepage/', views.dhomepage, name='dhomepage'),
path('dprofile/', views.dprofile, name='dprofile'),
path('designeredit/',views.designeredit,name="designeredit"),
 path('ChangeDPassword/',views.changeDpassword,name="changeDpassword"),
 path('addwork/',views.addwork,name='addwork'),
 path('delwork/<int:id>',views.delwork,name='delwork'),
 path('gallery/<int:id>',views.gallery,name='gallery'),     
 path('delgallery/<int:id>',views.delgallery,name='delgallery'),
 
  
  path('viewrequest/',views.viewrequest,name='viewrequest'),
  path('acceptrequest/<int:id>', views.acceptrequest, name='acceptrequest'),
  path('rejectrequest/<int:id>', views.rejectrequest, name='rejectrequest'),
  path('complaint/',views.complaint,name='complaint'),
  path('deldesignercomplaint<int:id>/',views.deldesignercomplaint,name='deldesignercomplaint'),
   path('logout/',views.logout,name='logout'),

   path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    path('verifieduser/',views.verifieduser,name="verifieduser"),
 
 
 
]