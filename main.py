from Controller.ClassesConcretas.ControleArmazenamento import ControleArmazenamento
from Controller.ClassesConcretas.ControleTratamento import ControleTratamento
from Model.ClassesConcretas.ArmazenarSessaoPrincipal import ArmazenarSessaoPrincipal
from Model.Tratadores.TratarPalavraConcreta import TratarPalavraConcreta
from View.ClassesConcretas.SessaoPrincipal.SobreMimView import SobreMim

tratar = TratarPalavraConcreta()
ctratar = ControleTratamento(tratar)

armaz = ArmazenarSessaoPrincipal()
carmaz = ControleArmazenamento(armaz)

a = SobreMim(ctratar, carmaz)
a.capturar_dados()