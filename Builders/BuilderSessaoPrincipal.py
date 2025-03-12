from Builders.BuilderAbstract import BuilderAbstract
from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Model.Tratadores.TratarDataConcreta import TratarDataConcreta
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.SessaoPrincipal.ConhecimentosECursosView import ConhecimentoseCursos
from View.ClassesConcretas.SessaoPrincipal.ExperienciaProfissionalView import ExperienciaProfissional
from View.ClassesConcretas.SessaoPrincipal.FormacaoAcademicaView import FromacaoAcademica
from View.ClassesConcretas.SessaoPrincipal.SobreMimView import SobreMim


class BuilderSessaoPrincipal(BuilderAbstract):
    def __init__(self):
        super().__init__()
        self.__dados = []
        self.__cc = ''
        self.__experiencia = ''
        self.__formacao = ''
        self.__sobreMim = ''

    def construir_sessao(self):
        cc = ConhecimentoseCursos()
        experiencia = ExperienciaProfissional(TratarDataConcreta())
        formacao = FromacaoAcademica(TratarDataConcreta())
        sobreMim = SobreMim(ControleTratamento(TratarPalavraConcreta()))
        cc.capturar_dados()
        experiencia.capturar_dados()
        formacao.capturar_dados()
        sobreMim.capturar_dados()
        self.__experiencia = experiencia.get_dado()
        self.__cc = cc.get_dado()
        self.__formacao = formacao.get_dado()
        self.__sobreMim = sobreMim.get_dado()
        return self.__dados.append([self.__experiencia, self.__cc, self.__formacao, self.__sobreMim])

    def get_dados(self):
        return self.__dados
