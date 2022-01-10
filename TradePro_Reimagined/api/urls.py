from django.urls import path
from . import views

urlpatterns = [
        path("",views.Index.as_view(),name="index"),
        path("customer_service", views.CustomerService.as_view(), name="customer_service"),
        path("log_in", views.log_in, name="log_in"),
        path("log_out", views.log_out, name="log_out"),
        path("open_an_account", views.open_an_account, name="open_an_account"),
        path("profile", views.Profile.as_view(), name="profile"),
        path("risk_assessment_test", views.RAT.as_view(), name="risk_assessment_test"),
        path("change_password", views.ChangePassword.as_view(), name="change_password")




]