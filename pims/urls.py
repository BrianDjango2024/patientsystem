from django.urls import path
from . import views

app_name = 'pims'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('record/', views.CreateRecordView.as_view(), name='record'),

    path('record_done/', views.RecordSuccessView.as_view(), name='record_done'),

    path('user-list/<int:user>', views.UserView.as_view(), name = 'user_list'),

    path('record-detail/<int:pk>', views.DetailView.as_view(), name = 'record_detail'),

    path('mypage/', views.MypageView.as_view(), name = 'mypage'),

    path('contact/', views.ContactFormView.as_view(), name ='contact'),
    
    path('contact/result', views.ContactResultView.as_view(), name ='contact_result'),

]