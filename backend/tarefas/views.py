from django.http import JsonResponse
from .models import Tarefa
from datetime import date

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_abertas(request):
    tarefas_abertas = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas_abertas), safe=False)

def listar_por_prioridade(request, prioridade):
    tarefas = Tarefa.objects.filter(prioridade=prioridade).values()
    return JsonResponse(list(tarefas), safe=False)

def buscar_por_id(request, id):
    try:
        tarefa = Tarefa.objects.values().get(id=id)
        return JsonResponse(tarefa, safe=False)
    except Tarefa.DoesNotExist:
        return JsonResponse({'erro': 'Tarefa nao encontrada'}, status=404)
    
def listar_urgentes_abertas(request):
    tarefas = Tarefa.objects.filter(status='ABERTA', prioridade='URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)

def listar_atrasadas(request):
    hoje = date.today()
    tarefas = Tarefa.objects.filter(data_entrega__lt=hoje).exclude(status='CONCLUIDA').values()
    return JsonResponse(list(tarefas), safe=False)

def buscar_por_titulo(request, palavra):
    tarefas = Tarefa.objects.filter(titulo__icontains=palavra).values()
    return JsonResponse(list(tarefas), safe=False)