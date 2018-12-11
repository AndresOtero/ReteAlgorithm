class Constants:
    @staticmethod
    def getConstant(key, value):
        dicc = {}
        diccExperiencia = {"0": "Inexperto", "1": "Experimentado en Short", "2": "Experimentado en IronMan 70.3",
                           "3": "Experimentado en IronMan 140.6"}
        dicc["Experiencia"] = diccExperiencia
        diccDistanciaObjetivo = {"0": "Short", "1": "IronMan 70.3", "2": "IronMan 140.6"}
        dicc["distancia objetivo"] = diccDistanciaObjetivo

        return dicc[key][value]

    @staticmethod
    def hasKey(key):
        return  key in ["Experiencia","distancia objetivo"]