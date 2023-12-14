from django.urls import path
from contabil import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("cadastro-func", views.cadastro_func, name="cadastro-func"),
    path("lista-func", views.lista_func, name="lista-func"),
    path("calculo-recisao", views.calculo_recisao, name="calculo-recisao"),
    path("cadastro-projeto", views.cadastro_projeto, name="cadastro-projeto"),
    path("orcamentos", views.orcamentos, name="orcamentos"),
    path("rubricas", views.rubricas, name="rubricas"),
    path("log-in", views.login, name="log-in"),
    path("settings", views.settings, name="settings"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)