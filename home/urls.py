from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', listtodo, basename='user')
urlpatterns = router.urls
# urlpatterns += [
#     path('detail/<int:pk>',Detailtodo.as_view()),
#     path('',listtodo.as_view()),
#     path('create', Createtodo.as_view()),
#     path('delete/<int:pk>',Deletetode.as_view()), 
#     path('update/<int:pk>',UpdateTodo.as_view()),
# ]