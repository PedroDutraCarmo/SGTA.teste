from django.urls import path
from .views import listar_tarefas, listar_tarefas_abertas, listar_por_prioridade, buscar_por_id, listar_urgentes_abertas, listar_atrasadas, buscar_por_titulo

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/abertas/', listar_tarefas_abertas),
    path('tarefas/prioridade/<str:prioridade>/', listar_por_prioridade),
    path('tarefas/<int:id>/', buscar_por_id),
    path('tarefas/urgentes-abertas/', listar_urgentes_abertas),
    path('tarefas/atrasadas/', listar_atrasadas),
    path('tarefas/busca/<str:palavra>', buscar_por_titulo),
]