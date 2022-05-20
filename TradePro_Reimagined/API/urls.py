from django.urls import path
from . import views
from .web3_views import web3_views
from .portfolio_views import portfolio_views


urlpatterns = [

        path("",views.Index.as_view(),name="index"),
        path("portfolio", views.Portfolio.as_view(), name="portfolio"),
        path("portfolio/historical_returns", portfolio_views.PortfolioHistoricalReturns.as_view(), name="portfolio/historical_returns"),
        path("log_in", views.log_in, name="log_in"),
        path("log_out", views.log_out, name="log_out"),
        path("open_an_account", views.open_an_account, name="open_an_account"),
        path("profile", views.Profile.as_view(), name="profile"),
        path("risk_assessment_test", views.RAT.as_view(), name="risk_assessment_test"),
        path("risk_assessment_test/<int:reset>", views.RAT.as_view(), name="risk_assessment_test"),
        path("change_password", views.ChangePassword.as_view(), name="change_password"),
        path("recovery_questions", views.RecoveryQuestions.as_view(), name="recovery_questions"),
        path("recover_account", views.RecoverAccount.as_view(), name="recover_account"),
        path("web3_home", web3_views.Web3_Home.as_view(), name="web3_home"),
        path("web3_social", web3_views.Web3_Social.as_view(), name="web3_social"),
        path("web3_portfolio",web3_views.Web3_Portfolio.as_view(), name="web3_portfolio"),
        path("receive_web_3_info", views.Web3Info.as_view()),
]