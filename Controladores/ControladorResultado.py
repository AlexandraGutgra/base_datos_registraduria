from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        return self.repositorioResultado.findAll()

        """
        Asignacion mesa y candidato a resultado
        """

    def create(self, infoResultado, id_mesa, id_candidato):
        nuevoResultado = Resultado(infoResultado)
        elMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = elMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
    Modificación de inscripción (mesa y candidato)
    """

    def update(self, id, infoResultado, id_mesa, id_candidato):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.votos_candidato = infoResultado["votos_candidato"]
        elMesa= Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = elMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    "Obtener resultados de un candidato"

    def listarResultadosCandidato(self, id_candidato):
        return self.repositorioResultado.getListadoResultadosCandidato(id_candidato)

    "Obtener resultados de una mesa"
    def listarResultadosMesa(self, id_mesa):
        return self.repositorioResultado.getListadoResultadosMesa(id_mesa)


    "Obtener mayor numero de votos de candidato"

    def MayornumerovotosCandidato(self):
        return self.repositorioResultado.getMayorVotos()

    "Obtener suma de votos por candidato ordenados de forma ascendente"
    def sumaVotoscandidatoAscendente(self, id_candidato):
        return self.repositorioResultado.sumaVotoscandidatoAscendente(id_candidato)


    "Obtener suma de votos por mesa ordenados de forma ascendente"

    def sumaVotosmesaAscendente(self, id_mesa):
        return self.repositorioResultado.sumaVotosmesaAscendente(id_mesa)


    "Obtener listado partidos politicos con votos filtrado por mesa"

    def sumaVotospartidoAscendente(self,id_partido):
            return self.repositorioResultado.sumaVotospartidoAscendente(id_partido)


    "Obtener Mesas con numero de votos en total"

    def sumaVotosenMesa(self, id_mesa):
        return self.repositorioResultado.sumaVotosenMesa(id_mesa)


    "Obtener partidos politicos por cantidad de votos"
    def sumaVotosenPartido(self, id_partido):
        return self.repositorioResultado.sumaVotosenPartido(id_partido)
