from django.urls import path
from . import views


urlpatterns =[
    path('home/',views.Home.as_view(),name='home'),
    path('enquiry/',views.Enquiry.as_view(),name='enquiry'),
    path('staff/',views.Staffs.as_view(),name='staff'),
    path('student/',views.Student.as_view(),name='student'),
    path('form/',views.Form.as_view(),name='form'),
    path('student/',views.Show.as_view(),name='student'),
    path('edit/',views.Edit.as_view(),name='edit'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('editprofile/',views.EditProfile.as_view(),name='editprofile'),
    path('delete/',views.Delete.as_view(),name='delete'),


    
]