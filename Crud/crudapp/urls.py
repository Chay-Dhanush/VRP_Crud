from django.urls import path

from crudapp import views

urlpatterns=[
     path('',views.Home),
    path('order/',views.CreateOrder,name='order'),
    path('show/',views.ShowOrder,name='show'),
    path('delete/<f_id>',views.DeleteOrder,name='delete'),
    path('confrim/',views.Confpage,name='confrim'),
    path('update/<f_id>',views.UpdateOrder,name='update'),
    path('serialize/',views.serialize),
    path('getse/',views.gserialize),
    path('pse/<f_id>',views.Pserialize),
    path('dse/<f_id>',views.Delete),
   
]