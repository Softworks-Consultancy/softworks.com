from django.conf.urls import include, url
from django.contrib import admin
from . import views
from rest_framework import routers
from home import views as homeviews

router = routers.DefaultRouter()
'''router.register(r'user', homeviews.UserViewSet)
router.register(r'student', homeviews.StudentViewSet)
router.register(r'highschool', homeviews.HighSchoolViewSet)
'''
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),


    url(r'^', include('home.urls')),
    url(r'partials/(?P<template_name>[-_\w]+/$)', views.Partial.as_view()),
    url(r'private_parts/(?P<template_name>[-_\w]+/$)',
        views.PrivatePartial.as_view()),

    # APIs
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls)),

]
