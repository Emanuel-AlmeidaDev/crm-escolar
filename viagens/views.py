from datetime import datetime, timedelta

from alunos.models import Aluno
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import AgendaViagem


def viagens(request):
    date = None
    if request.GET.get('date'): 
        date = datetime.strptime(
            request.GET.get('date'), '%Y-%m-%d').date()
    viagens = AgendaViagem.objects.all().order_by('datetime')

    if date:
        viagens = AgendaViagem.objects.filter(datetime__date=date).order_by('datetime')
    
    print(date)

    paginator = Paginator(viagens, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'alunos': Aluno.objects.all(),
        'count': AgendaViagem.objects.all().count(),
        'page_obj': page_obj,
        'paginator': paginator
    }
    template_name = 'viagens.html'
    return render(request, template_name, context)


def create_viagens(request):
    print(f"SEGUNDA IDA {request.POST.get('segunda_ida', None)}")
    print(f"SEGUNDA VOLTA {request.POST.get('segunda_volta', None)}")
    print(f"TERÇA IDA {request.POST.get('terca_ida', None)}")
    print(f"TERÇA VOLTA {request.POST.get('terca_volta', None)}")
    print(f"QUARTA IDA {request.POST.get('quarta_ida', None)}")
    print(f"QUARTA VOLTA {request.POST.get('quarta_volta', None)}")
    print(f"QUINTA IDA {request.POST.get('quinta_ida', None)}")
    print(f"QUINTA VOLTA {request.POST.get('quinta_volta', None)}")
    print(f"SEXTA IDA {request.POST.get('sexta_ida', None)}")
    print(f"SEXTA VOLTA {request.POST.get('sexta_volta', None)}")
    print(f"SÁBADO IDA {request.POST.get('sabado_ida', None)}")
    print(f"SÁBADO VOLTA {request.POST.get('sabado_volta', None)}")
    print(f"DOMINGO IDA {request.POST.get('domingo_ida', None)}")
    print(f"DOMINGO VOLTA {request.POST.get('domingo_volta', None)}")

    def range_dates(start, end, delta):
        curr = start
        while curr <= end:
            yield curr
            curr += delta

    primeiro_dia = datetime.strptime(
        request.POST.get('primeiro_dia'), '%Y-%m-%d').date()
    ultimo_dia = datetime.strptime(
        request.POST.get('ultimo_dia'), '%Y-%m-%d').date()

    cronograma = [
        (request.POST.get('segunda_ida', None),
         request.POST.get('segunda_volta', None)),
        (request.POST.get('terca_ida', None),
         request.POST.get('terca_volta', None)),
        (request.POST.get('quarta_ida', None),
         request.POST.get('quarta_volta', None)),
        (request.POST.get('quinta_ida', None),
         request.POST.get('quinta_volta', None)),
        (request.POST.get('sexta_ida', None),
         request.POST.get('sexta_volta', None)),
        (request.POST.get('sabado_ida', None),
         request.POST.get('sabado_volta', None)),
        (request.POST.get('domingo_ida', None),
         request.POST.get('domingo_volta', None)),
    ]

    aluno = Aluno.objects.get(id=int(request.POST.get('aluno', None)))

    viagens = []
    for date_atual in range_dates(primeiro_dia, ultimo_dia, timedelta(days=1)):
        dia_da_semana = date_atual.weekday()

        if cronograma[dia_da_semana][0]:
            horario_viagem = cronograma[dia_da_semana][0]
            viagem = AgendaViagem(
                aluno=aluno,
                datetime=datetime.combine(
                    date_atual,
                    datetime.strptime(horario_viagem, '%H:%M').time(),
                    tzinfo=timezone.utc
                ),
                tipo="I")
            viagens.append(viagem)

        if cronograma[dia_da_semana][1]:

            horario_viagem = cronograma[dia_da_semana][1]
            viagem = AgendaViagem(
                aluno=aluno,
                datetime=datetime.combine(
                    date_atual,
                    datetime.strptime(horario_viagem, '%H:%M').time(),
                    tzinfo=timezone.utc
                ),
                tipo="V")
            viagens.append(viagem)

    AgendaViagem.objects.bulk_create(viagens)

    return redirect('viagens:viagens')
