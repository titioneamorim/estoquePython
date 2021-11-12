from django.urls import path

from historicos.views import adiciona_historico, consulta_historico, home_historico

namespace = 'historicos'

urlpatterns = [
    path('historicos/', home_historico, name="home_historicos"),
    path('historicos/add_historico/', adiciona_historico, name="adiciona_historico"),
    path('historicos/busca/', consulta_historico, name="consulta_historico"),

]
