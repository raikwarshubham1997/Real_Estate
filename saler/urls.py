from django.urls import path, include
from . import views


app_name = 'saler'
urlpatterns = [
    path('', views.login_saler),
    path('dashboard/', views.dashboard),
    path('register/', views.Business_ac),
    # path('brokerhome/', views.broker_index),
    path('dashboard/', views.dashboard),
    path('propertType/', views.properties),
    # path('city/', views.city),
    # path('state/', views.state),
    # path('country/', views.country),
    path('logout/', views.logouts),
    path('client_enquiry/', views.client_Enquiry),
    
    path('getproperties/', views.getproperties),
    path('updateproperty/', views.updateproperty),
    path('delete_property/<int:id>/', views.deleteproperty, name="deletep"),
    path('update_property/<int:id>/', views.updateproperty, name="updatep"),
    
    # path('getstate/', views.getstate),
    # path('updatestate', views.updatestate),
    # path('delete_state/<int:id>/', views.deletestate, name="deletes"),
    # path('update_state/<int:id>/', views.updatestate, name="updates"),
    
    # path('getcity/', views.getcity),
    # path('updatecity', views.updatecity),
    # path('delete_city/<int:id>/', views.deletecity, name="delete"),
    # path('update_city/<int:id>/', views.updatecity, name="update"),

    # path('user/', views.user),

    # path('getcountry/', views.getcountry),
    # path('updatecountry', views.updatecountry),
    # path('delete_country/<int:id>/', views.deletecountry, name="deletecon"),
    # path('update_country/<int:id>/', views.updatecountry, name="updatecon"),

    
    
]
