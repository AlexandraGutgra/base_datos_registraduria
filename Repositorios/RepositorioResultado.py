from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado


from bson.objectid import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoResultadosCandidato(self,id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    def getMayorVotos(self):
        query1 = {
                "$group": {
                    "_id": "$candidato",
                    "max": {
                        "$max": "$votoscandidato"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }

        pipeline = [query1]
        return self.queryAggregation(pipeline)

