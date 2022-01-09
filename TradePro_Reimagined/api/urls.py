from django.urls import path
from . import views

urlpatterns = [
        path("",views.Index.as_view(),name="index"),
        path("customer_service", views.customer_service, name="customer_service"),
        path("log_in", views.log_in, name="log_in"),
        path("log_out", views.log_out, name="log_out"),
        path("open_an_account", views.open_an_account, name="open_an_account"),
        path("profile", views.profile, name="profile"),
        path("risk_assessment_test", views.risk_assessment_test, name="risk_assessment_test")











]