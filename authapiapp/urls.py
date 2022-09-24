from django.urls import path
from authapiapp.views import ( TestAPIVIew,CheckListsAPIView,CheckListAPIView
)


urlpatterns = [ 
    path('', TestAPIVIew.as_view()),
    path('api/checklist/', CheckListsAPIView.as_view()),
    path('api/checklist/<int:pk>/', CheckListAPIView.as_view()),
  
    
    
]
