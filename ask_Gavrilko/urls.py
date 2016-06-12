"""ask_Gavrilko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ask import views as ask_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^signup/?', ask_views.signup, name='signup'),	
	url(r'^profile/?', ask_views.profile, name='profile'),
	url(r'^tag/(\w+)/?', ask_views.tag, name='tag'),
	url(r'^index/?', ask_views.index, name='index'),
	url(r'^question/(\d+)/?', ask_views.answer, name='answer'),
	url(r'^ask/?', ask_views.ask, name='ask'),
	url(r'^login/?', ask_views.login, name='login'),
	url(r'^logout/?', ask_views.logout, name='logout'),
	url(r'^hello?', ask_views.hello, name='hello'),
	url(r'^hot/?', ask_views.hot_questions, name='hot_questions'),
	url(r'^/?', ask_views.new_questions, name='new_questions'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

