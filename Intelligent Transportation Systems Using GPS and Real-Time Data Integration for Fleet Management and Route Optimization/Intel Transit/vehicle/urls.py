from . import views
from django.urls import path
urlpatterns = [
   # path('', views.first,name="first"),
    #path('pathway/signdowner/', views.signdowner,name="signdowner"),
    #path('pathway2/driver/', views.driver,name="driver"),
    #path('recording', views.recording,name="recording"),
    ##path('recordupdate_onarrival/', views.recordupdate_onarrival,name="recordupdate_onarrival"),
    #path('pathway/ownerlogin/', views.ownerlogin,name="ownerlogin"),
    #path('pathway2/driverlogin/', views.driverlogin,name="driverlogin"),
    #path('decsionmakerondriver/', views.decsionmakerondriver,name="decsionmakerondriver"), 
    #path('ownerform/', views.ownerform,name="ownerform"),
    #path('driverform/', views.driverform,name="driverform"),
    #path('pathway2/', views.pathway2,name="pathway2"),
    #path('pathway',views.login, name="pathway"),
    path('',views.login, name="logins"),
    path('setups/',views.setups, name="setups"),
    path('pathway/',views.sign, name="sign"),
    path('pathway2/',views.driverupdate, name="driverupdate"),
    path("setups/driverreg/",views.drivereg, name="setups"),
    path("setups/careg/",views.carreg, name="setups"),
    path('fleetmanagement/',views.fleetmngt, name="fleetmanagement"),
    
    #('pathway/setups/',views.setups, name="setups"),
    path('routemanagement/',views.route, name="routemanagement"),
    path("FleetTracking/",views.freettracking, name="FleetTracking"),
    path('drivermanagement/',views.drivermngt, name="drivermngt"),
    path('report/',views.report, name="drivermngt"),
    path('notification/',views.notification, name="drivermngt"),
    #path('pathway/',views.dasboard, name="dasboard")#for pathways
            
]
