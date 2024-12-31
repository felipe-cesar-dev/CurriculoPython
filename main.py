from Model.ClassesAbstratas.TratarData import TratarData
from Model.ClassesConcretas.ArmazenarSessaoPrincipal import ArmazenarSessaoPrincipal
from Model.Tratadores.TratarDataConcreta import TratarDataConcreta
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.SessaoPrincipal.ConhecimentosECursosView import ConhecimentoseCursos
from View.ClassesConcretas.SessaoPrincipal.ExperienciaProfissionalView import ExperienciaProfissional
from View.ClassesConcretas.SessaoPrincipal.SobreMimView import SobreMim
from View.ClassesConcretas.SessaoPrincipal.FormacaoAcademicaView import FromacaoAcademica

t = TratarPalavraConcreta()
ar = ArmazenarSessaoPrincipal()
u = TratarDataConcreta()



c = ExperienciaProfissional(u, ar)




c.capturar_dados()


print(ar.get_dado())
