class ParserAgrupadores:

    def __init__(self, cadena):

        self.cadena = cadena
        self.posicion = 0

    def actual(self):

        if self.posicion >= len(self.cadena):
            return None

        return self.cadena[self.posicion]

    def consumir(self, esperado):

        if self.actual() == esperado:

            self.posicion += 1

        else:

            raise SyntaxError(
                f"Se esperaba '{esperado}', "
                f"pero apareció '{self.actual()}'"
            )

    # Gramática:
    #
    # S -> (S)S
    #    | [S]S
    #    | epsilon

    def S(self):

        if self.actual() == "(":

            self.consumir("(")

            self.S()

            self.consumir(")")

            self.S()

        elif self.actual() == "[":

            self.consumir("[")

            self.S()

            self.consumir("]")

            self.S()

        # epsilon en cualquier otro caso

    def analizar(self):

        try:

            self.S()

            if self.posicion != len(self.cadena):

                raise SyntaxError(
                    "Quedan símbolos sin procesar."
                )

            return True

        except SyntaxError:

            return False


def main():

    pruebas = [

        # Correctas

        "()",
        "[]",
        "([])",
        "[()]",
        "(()[])",
        "([][])",

        # Incorrectas

        "([)]",
        "(]",
        "[(",
        "([)"
    ]

    print("=" * 70)
    print("EJERCICIO 4 - PARENTESIS Y CORCHETES")
    print("=" * 70)

    for cadena in pruebas:

        parser = ParserAgrupadores(cadena)

        if parser.analizar():

            resultado = "CADENA ACEPTADA"

        else:

            resultado = "ERROR SINTÁCTICO"

        print(
            f"{cadena:<12} -> {resultado}"
        )


if __name__ == "__main__":
    main()