from django.conf.urls.defaults import *
urlpatterns = patterns('',
    #events related URL
    url(r'^$', 'Perfumes.views.show_contest', name="show_contest"),
    url(r'^perfumes_info$', 'Perfumes.views.get_selected_perfume_info', name="get_selected_perfume_info")

)