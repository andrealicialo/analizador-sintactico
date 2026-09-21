class ParserParentesis:

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
                f"Se esperaba '{esperado}'"
            )

    # Gramática:
    #
    # S -> (S)S | epsilon

    def S(self):

        if self.actual() == "(":

            self.consumir("(")

            self.S()

            self.consumir(")")

            self.S()

        # en cualquier otro caso:
        # epsilon

    def analizar(self):

        try:

            self.S()

            if self.posicion != len(self.cadena):

                raise SyntaxError(
                    "Símbolos sobrantes"
                )

            return True

        except SyntaxError:

            return False


def main():

    pruebas = [

        "()",
        "(())",
        "()()",
        "(()())",
        "((()))",

        "(()",
        "())",
        ")("
    ]

    print("=" * 60)
    print("EJERCICIO 3 - PARENTESIS EQUILIBRADOS")
    print("=" * 60)

    for cadena in pruebas:

        parser = ParserParentesis(cadena)

        if parser.analizar():

            resultado = "Cadena aceptada"

        else:

            resultado = "Error sintáctico"

        print(
            f"{cadena:<10} -> {resultado}"
        )


if __name__ == "__main__":
    main()