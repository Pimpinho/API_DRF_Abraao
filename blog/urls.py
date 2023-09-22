from rest_framework import routers
from .views import *


routerBlog = routers.DefaultRouter()
routerBlog.register(r'Alunos', AlunosView)
routerBlog.register(r'Professores', ProfessoresView)
routerBlog.register(r'Disciplinas', DisciplinasView)
routerBlog.register(r'DisciplinaAluno', DisciplinaAlunoView)
routerBlog.register(r'Frequencia', FrequenciaView)
routerBlog.register(r'PlanoAula', PlanoAulaView)
routerBlog.register(r'Atividades',AtividadesView)
routerBlog.register(r'FrequenciaAluno',FrequenciaAlunoView)
routerBlog.register(r'AtividadeAluno', AtividadeAlunoView)
