
class SistemaCitas:
    def __init__(self):
        self.citas = {}

    def reservar(self, paciente, fecha, hora):
        if not paciente.strip():
            return False

        horario = (fecha, hora)

        if horario in self.citas:
            return True

        self.citas[horario] = paciente
        return True

    def disponible(self, fecha, hora):
        return (fecha, hora) not in self.citas

    def cancelar(self, fecha, hora):
        horario = (fecha, hora)

        if horario not in self.citas:
            return False

        del self.citas[horario]
        return True
