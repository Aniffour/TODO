from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView , LogoutView  , PasswordResetDoneView, PasswordResetView , PasswordChangeView , PasswordChangeDoneView , PasswordResetCompleteView ,PasswordResetConfirmView  


urlpatterns = [
    path("login/" , views.Login.as_view() , name ="login") , 
    path('register/' , views.Register.as_view() , name='register'),
    path('logout/' , LogoutView.as_view(next_page='login'),name='logout'),
    path('delete-account/' , views.DeleteAcc.as_view() , name='deleteACC'),
    path('change-password/' ,PasswordChangeView.as_view(template_name='log/changePASS.html') , name='changePASS'),
    path('change-password/DONE/' ,PasswordChangeDoneView.as_view(template_name='log/changePASSdone.html') , name='password_change_done'),


    path('tasks/' , views.Home.as_view() , name='home') , 
    path('delete/<int:pk>/' , views.DeleteTask.as_view() , name='delete'),
    path('update/<int:pk>/' , views.UpdateTask.as_view() , name='update'),


    path('reset-password/' , PasswordResetView.as_view(template_name='log/resetpass/PasswordReset.html') ,  name='password_reset'),
    path('reset-password/done/' , PasswordResetDoneView.as_view(template_name='log/resetpass/PasswordResetDone.html') , name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/' , PasswordResetConfirmView.as_view(template_name='log/resetpass/PasswordResetConfirmView.html'),  name='password_reset_confirm'),
    path('reset-password/complete/' , PasswordResetCompleteView.as_view(template_name='log/resetpass/PasswordResetCompleteView.html' ) ,name='password_reset_complete'),
    

]
 