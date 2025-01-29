
from  django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
            #as_view() creates an instance of the class and stores it
            #When a request is received, it calls the appropriate method based on the request type (GET, POST, etc.).
            #The request is processed and a response is returned


        path('user/',views.TestView.as_view(), name='tesing'),

        path('user/<int:id>',views.TestDetailView.as_view(), name='name'),

        path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
 
    ]

    


