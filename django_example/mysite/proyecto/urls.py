from django.urls import path
from proyecto import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path('index', TemplateView.as_view(template_name="pagina_1.html"), name="pag1"),
    path('information', TemplateView.as_view(template_name="pagina_2.html"), name="pag2"),
    path('galery', TemplateView.as_view(template_name="pagina_3.html"), name="pag3"),
    path('new', TemplateView.as_view(template_name="pagina_4.html"), name="pag4"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

