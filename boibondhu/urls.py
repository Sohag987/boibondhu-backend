
from django.contrib import admin
from django.urls import path,include
from book_for_sell.views import AllBookSellView,SingleBookSellView
from book_for_lend.views  import AllBookForLendView,SingleBookLendView
from book_for_fund.views import BookForFundListView,SingleBookForFund 
from django.conf import settings 
from django.conf.urls.static import static 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.urls import path
from user.views import RegisterView, LoginView, ProfileView, TokenRefreshView ,DashboardView
from contact.views import ContactView
urlpatterns = [
    path('register/',      RegisterView.as_view()),
    path('login/',         LoginView.as_view()),
    path('profile/',       ProfileView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns = [
    # for funding books 
    path('book-for-fund/',BookForFundListView.as_view()),
    path('book-for-fund/<slug:slug>/',SingleBookForFund.as_view()),
    # for Lending books 
    path('book-for-lend/',AllBookForLendView.as_view()),
    path('book-for-lend/<slug:slug>/',SingleBookLendView.as_view()),
    # foe selling books 
    path('book-for-sell/',AllBookSellView.as_view()),
    path('book-for-sell/<slug:slug>/',SingleBookSellView.as_view()),

    
    
    #system config 
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('tinymce/',include('tinymce.urls')),

    #path for JWT tokes 
    path("api/token/",TokenObtainPairView.as_view()),
    path("api/token/refresh",TokenRefreshView.as_view()),

    #path for user path('register/',      RegisterView.as_view()),
    path('login/',         LoginView.as_view()),
    path('profile/',       ProfileView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/',      RegisterView.as_view()),
    path('dashboard/',     DashboardView.as_view()),

    #path for contact 
    path('contact/',ContactView.as_view())


    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



