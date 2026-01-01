"""Define URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Main page
    path('', views.index, name='index'),
    # Page with all topic list
    path('topics/', views.topics, name='topics'),
    # Page dedicated to a specific topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new post
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')

]