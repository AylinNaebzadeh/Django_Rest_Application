from django.urls import path
from quickstart import views
from rest_framework.urlpatterns import  format_suffix_patterns



urlpatterns = format_suffix_patterns([
    path('' , views.api_root),
    path('snippets/' , views.GenericSnippetList.as_view() , name='snippet-list'),
    path('snippets/<int:pk>/' , views.GenericSnippetDetail.as_view(),name='snippet-detail'),
    path('snippet/<int:pk>/highlight/',views.SnippetHighlight.as_view(),name='snippet-highlight'),
    path('users/' , views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/',views.UserDetail.as_view(),name='user-detail')
])