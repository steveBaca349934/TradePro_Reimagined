from django.urls import path
from . import views

urlpatterns = [
        path("",views.index,name="index"),
        path("customer_service", views.customer_service, name="customer_service"),
        path("log_in", views.log_in, name="log_in"),
        path("open_an_account", views.open_an_account, name="open_an_account"),
        path("profile", views.profile, name="profile"),
        path("risk_assessment_test", views.risk_assessment_test, name="risk_assessment_test"),
        path("add_email", views.add_email, name="add_email"),
        path("add_pw", views.add_pw, name="add_pw")








]