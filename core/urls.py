
from django.contrib import admin
from django.urls import path
from apps.reports.views import DominioLogChartView, EmailLogChartView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dominio-chart/', DominioLogChartView.as_view(), name='dominio_chart'),
    path('user-chart/', EmailLogChartView.as_view(), name='email_chart'),


]
