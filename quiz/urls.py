from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.level, name='level'),
    url(r'^(?P<level_id>[0-9]+)/tests/$', views.test, name='test'),
    url(r'^(?P<level_id>[0-9]+)/tests/results/$', views.result, name='result'),
    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]