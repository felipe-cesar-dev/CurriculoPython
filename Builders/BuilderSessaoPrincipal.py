from Builders.BuilderAbstract import BuilderAbstract
from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamento
from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Model.ClassesConcretas.ArmazenarSessaoPrincipal import ArmazenarSessaoPrincipal
from Model.Tratadores.TratarDataConcreta import TratarDataConcreta
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.SessaoPrincipal.ConhecimentosECursosView import ConhecimentoseCursos
from View.ClassesConcretas.SessaoPrincipal.ExperienciaProfissionalView import ExperienciaProfissional
from View.ClassesConcretas.SessaoPrincipal.FormacaoAcademicaView import FromacaoAcademica
from View.ClassesConcretas.SessaoPrincipal.SobreMimView import SobreMim


class BuilderSessaoPrincipal(BuilderAbstract):
    def __init__(self):
        super().__init__()
        self.__conhecCursos = ''
        self.__expProf = ''
        self.__formAcademica = ''
        self.__sobreMim = ''

    def construir_sessao(self):
        controleArmazenamento = ControleArmazenamento(ArmazenarSessaoPrincipal())
        self.__conhecCursos = ConhecimentoseCursos(controleArmazenamento)
        self.__expProf = ExperienciaProfissional(TratarDataConcreta(), controleArmazenamento)
        self.__formAcademica = FromacaoAcademica(TratarDataConcreta(), controleArmazenamento)
        self.__sobreMim = SobreMim(ControleTratamento(TratarPalavraConcreta()), controleArmazenamento)
        self.__sobreMim.capturar_dados()
        self.__expProf.capturar_dados()
        self.__conhecCursos.capturar_dados()
        self.__formAcademica.capturar_dados()