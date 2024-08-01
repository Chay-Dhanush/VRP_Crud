from django.urls import path

from crudapp import views

urlpatterns=[
     path('',views.Home),
    path('order/',views.CreateOrder),
    path('show/',views.ShowOrder),
    path('delete/<f_id>',views.DeleteOrder),
    path('confrim/',views.Confpage),
    path('update/<f_id>',views.UpdateOrder),
   
]