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
                        "$max": "$votos_candidato"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }

        pipeline = [query1]
        return self.queryAggregation(pipeline)



    def sumaVotoscandidatoAscendente(self, id_candidato):
        query1 = {
            "$group": {
                "_id": "$candidato",
                "suma": {
                    "$sum": "$votos_candidato"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        query2 = {
            "$sort": {"suma": 1}
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)


    def sumaVotosmesaAscendente(self, id_mesa):
        query1 = {
            "$group": {
                "_id": "$mesa",
                "suma": {
                    "$sum": "$votos_candidato"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        query2 = {
            "$sort": {"suma": 1}
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    def sumaVotospartidoAscendente(self,id_partido):
        query1 = {
            "$group": {
                "_id": "$partido",
                "suma": {
                    "$sum": "$votos_candidato"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        query2 = {
            "$sort": {"suma": 1}
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    def sumaVotosenMesa(self, id_mesa):
        query1 = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }
        query2 = {
            "$group": {
                "_id": "$mesa",
                "sum": {
                    "$sum": "$votos_candidato"
                }
            }
        }

        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)


    def getListadoResultadosMesa(self, id_mesa):
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    def getListadoResultadosPartido(self, id_partido):
        theQuery = {"partido.$id": ObjectId(id_partido)}
        return self.query(theQuery)



