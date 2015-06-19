"""
server_note URL Configuration
"""
from django.conf.urls import url, include
from server_note import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
tag_urls = [
    url(r'^/$',
        views.SaveTag.as_view(), name='save_tag'),
    url(r'^/access/(?P<pk>\d+)$',
        views.TagGetAccess.as_view(), name='access_tag'),
]

color_urls = [
    url(r'^/$',
        views.SaveColor.as_view(), name='save_color'),
    url(r'^/access/(?P<pk>\d+)$',
        views.ColorGetAccess.as_view(), name='access_color'),
]

category_urls = [
    url(r'^/$',
        views.SaveCat.as_view(), name='save_cat'),
    url(r'^/access/(?P<pk>\d+)$',
        views.CategoryGetAccess.as_view(), name='access_cat'),
]

note_urls = [
    url(r'^/(?P<pk>\d+)$',
        views.NoteGetByUser.as_view(), name='user_note'),
    url(r'^/add/$',
        views.AddNote.as_view(), name='save_note'),
    url(r'^/cat/(?P<pk>\d+)/(?P<lg>\d+)$',
        views.NoteGetByCat.as_view(), name='cat_note'),
    url(r'^/del/(?P<pk>\d+)$',
        views.DelNoteById.as_view(), name='del_note'),
]

user_urls = [
    url(r'^/(?P<pk>\d+)$',
        views.UserGetAll.as_view(), name='all_users'),
    url(r'^/(?P<key>[0-9a-zA-Z_-]+)$',
        views.UserGetById.as_view(), name='id_user'),
    url(r'^/add/$',
        views.SaveNewUser.as_view(), name='save_user'),
]


urlpatterns = [
    url(r'^tags', include(tag_urls)),
    url(r'^color', include(color_urls)),
    url(r'^cat', include(category_urls)),
    url(r'^note', include(note_urls)),
    url(r'^user', include(user_urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
]
