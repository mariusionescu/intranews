from django.conf.urls import url
from wall.views import ComponentAPI, CommentAPI

urlpatterns = [
    url(r'^api/component/(?P<component_id>.*)/$', ComponentAPI.as_view()),
    url(r'^api/component/$', ComponentAPI.as_view()),
    url(r'^api/comment/(?P<comment_id>.*)/$', CommentAPI.as_view()),
    url(r'^api/comment/$', CommentAPI.as_view())
]
