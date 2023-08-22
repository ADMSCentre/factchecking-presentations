from django.urls import path

from . import views

app_name = 'screen'
urlpatterns = [
    path('', views.index, name='index'),
    path('report', views.report, name='report'),
    path('report/<int:article_id>/<int:condition_id>', views.report, name='report'),
    path('task', views.task, name='task'),
    path('start', views.start, name='start'),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('demographics', views.demographics, name='demographics'),
    path('complete', views.complete, name='complete'),
    path('log', views.log, name='log')

]