from rest_framework import viewsets
from .models import *
from .serializers import *

class AlunosView(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

class ProfessoresView(viewsets.ModelViewSet):
    queryset = Professores.objects.all()
    serializer_class = ProfessoresSerializer

class DisciplinasView(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinasSerializer

class DisciplinaAlunoView(viewsets.ModelViewSet):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer

class FrequenciaView(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class PlanoAulaView(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = PlanoAulaSerializer

class AtividadesView(viewsets.ModelViewSet):
    queryset = Atividades.objects.all()
    serializer_class = AtividadesSerializer

class FrequenciaAlunoView(viewsets.ModelViewSet):
    queryset = FrequenciaAluno.objects.all()
    serializer_class = FrequenciaAlunoSerializer

class AtividadeAlunoView(viewsets.ModelViewSet):
    queryset = AtividadeAluno.objects.all()
    serializer_class = AtividadeAlunoSerializer












