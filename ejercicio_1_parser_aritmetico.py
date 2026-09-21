import re


class ParserError(Exception):
    pass


class ParserAritmetico:

    def __init__(self, expresion):
        self.tokens = self.tokenizar(expresion)
        self.posicion = 0

    def tokenizar(self, expresion):
        """
        Convierte temporalmente la entrada en símbolos simples.
        En el ejercicio 2 construiremos un lexer formal.
        """

        patron = r"[A-Za-z_][A-Za-z0-9_]*|\+|\*|\(|\)"

        tokens = re.findall(patron, expresion)

        return tokens

    def actual(self):

        if self.posicion < len(self.tokens):
            return self.tokens[self.posicion]

        return None

    def avanzar(self):
        self.posicion += 1

    def consumir(self, esperado):

        if self.actual() == esperado:
            self.avanzar()
        else:
            raise ParserError(
                f"Se esperaba '{esperado}' "
                f"pero se encontró '{self.actual()}'"
            )

    # ------------------------------------
    # E -> T E'
    # ------------------------------------

    def E(self):

        self.T()
        self.EPrima()

    # ------------------------------------
    # E' -> + T E' | epsilon
    # ------------------------------------

    def EPrima(self):

        if self.actual() == "+":

            self.consumir("+")

            self.T()

            self.EPrima()

    # ------------------------------------
    # T -> F T'
    # ------------------------------------

    def T(self):

        self.F()
        self.TPrima()

    # ------------------------------------
    # T' -> * F T' | epsilon
    # ------------------------------------

    def TPrima(self):

        if self.actual() == "*":

            self.consumir("*")

            self.F()

            self.TPrima()

    # ------------------------------------
    # F -> id | (E)
    # ------------------------------------

    def F(self):

        token = self.actual()

        if token is None:

            raise ParserError(
                "Se esperaba identificador o '('"
            )

        if re.fullmatch(
            r"[A-Za-z_][A-Za-z0-9_]*",
            token
        ):

            self.avanzar()

        elif token == "(":

            self.consumir("(")

            self.E()

            self.consumir(")")

        else:

            raise ParserError(
                f"Token inesperado: {token}"
            )

    def analizar(self):

        try:

            self.E()

            if self.actual() is not None:

                raise ParserError(
                    f"Token sobrante: {self.actual()}"
                )

            return True, "Expresión sintácticamente correcta"

        except ParserError as error:

            return False, f"Expresión incorrecta: {error}"


def main():

    pruebas = [
        "A + b",
        "A * b",
        "A + b * c",
        "(A + b) * c",
        "A + * b",
        "(A + b",
        "A * b+"
    ]

    print("=" * 65)
    print("EJERCICIO 1 - ANALIZADOR SINTACTICO DESCENDENTE")
    print("=" * 65)

    for expresion in pruebas:

        parser = ParserAritmetico(expresion)

        valido, mensaje = parser.analizar()

        print(f"\nExpresión: {expresion}")
        print(mensaje)


if __name__ == "__main__":
    main()