from django.conf.urls import url
from rest_framework import urlpatterns
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

#Definir las direcciones URL de las API
# url(r'^api/RUTAPI/$',views.NOMBREVIEWSET.as_view()),
# url(r'^api/RUTAPI/(?P<NOMBREPARAMETRO>.+)/$',views.NOMBREVIEWSET.as_view()),
urlPatterns = [
    url(r'^api/solitrab/$',views.SolTrabViewSet.as_view()),
    url(r'^api/solitraagregar/$',views.SolTrabCreateViewSet.as_view()),
    url(r'^api/soltrabbuscar/(?P<correo>.+)/$',views.SolTrabSearchViewSet.as_view()),
    url(r'^api/trabuscar/(?P<email>.+)/$',views.TrabSearchViewSet.as_view()),
]
#La maquina reconoce ^ $
urlpatterns=format_suffix_patterns(urlPatterns)