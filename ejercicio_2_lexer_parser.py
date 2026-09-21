from enum import Enum, auto


class TipoToken(Enum):

    IDENTIFICADOR = auto()
    SUMA = auto()
    MULTIPLICACION = auto()

    PARENTESIS_IZQ = auto()
    PARENTESIS_DER = auto()

    FIN = auto()


class Token:

    def __init__(self, tipo, lexema):

        self.tipo = tipo
        self.lexema = lexema

    def __str__(self):

        return f"{self.tipo.name}({self.lexema})"


class Lexer:

    def __init__(self, texto):

        self.texto = texto
        self.posicion = 0

    def actual(self):

        if self.posicion >= len(self.texto):
            return None

        return self.texto[self.posicion]

    def avanzar(self):

        caracter = self.actual()
        self.posicion += 1

        return caracter

    def siguiente_token(self):

        # Saltar espacios

        while (
            self.actual() is not None
            and self.actual().isspace()
        ):
            self.avanzar()

        caracter = self.actual()

        if caracter is None:

            return Token(
                TipoToken.FIN,
                "EOF"
            )

        # Identificador

        if caracter.isalpha() or caracter == "_":

            lexema = ""

            while (
                self.actual() is not None
                and (
                    self.actual().isalnum()
                    or self.actual() == "_"
                )
            ):

                lexema += self.avanzar()

            return Token(
                TipoToken.IDENTIFICADOR,
                lexema
            )

        # Símbolos

        simbolos = {

            "+": TipoToken.SUMA,
            "*": TipoToken.MULTIPLICACION,

            "(": TipoToken.PARENTESIS_IZQ,
            ")": TipoToken.PARENTESIS_DER
        }

        if caracter in simbolos:

            self.avanzar()

            return Token(
                simbolos[caracter],
                caracter
            )

        raise SyntaxError(
            f"Caracter no válido: {caracter}"
        )


class Parser:

    def __init__(self, texto):

        self.lexer = Lexer(texto)

        self.token_actual = (
            self.lexer.siguiente_token()
        )

    def consumir(self, tipo):

        if self.token_actual.tipo == tipo:

            self.token_actual = (
                self.lexer.siguiente_token()
            )

        else:

            raise SyntaxError(
                f"Se esperaba {tipo.name} "
                f"pero apareció "
                f"{self.token_actual.tipo.name}"
            )

    # E -> T E'

    def E(self):

        self.T()
        self.EPrima()

    # E' -> + T E' | epsilon

    def EPrima(self):

        if (
            self.token_actual.tipo
            == TipoToken.SUMA
        ):

            self.consumir(
                TipoToken.SUMA
            )

            self.T()

            self.EPrima()

    # T -> F T'

    def T(self):

        self.F()
        self.TPrima()

    # T' -> * F T' | epsilon

    def TPrima(self):

        if (
            self.token_actual.tipo
            == TipoToken.MULTIPLICACION
        ):

            self.consumir(
                TipoToken.MULTIPLICACION
            )

            self.F()

            self.TPrima()

    # F -> id | (E)

    def F(self):

        if (
            self.token_actual.tipo
            == TipoToken.IDENTIFICADOR
        ):

            self.consumir(
                TipoToken.IDENTIFICADOR
            )

        elif (
            self.token_actual.tipo
            == TipoToken.PARENTESIS_IZQ
        ):

            self.consumir(
                TipoToken.PARENTESIS_IZQ
            )

            self.E()

            self.consumir(
                TipoToken.PARENTESIS_DER
            )

        else:

            raise SyntaxError(
                "Se esperaba identificador o '('"
            )

    def analizar(self):

        self.E()

        if (
            self.token_actual.tipo
            != TipoToken.FIN
        ):

            raise SyntaxError(
                "Existen tokens sobrantes."
            )


def mostrar_tokens(texto):

    lexer = Lexer(texto)

    resultado = []

    while True:

        token = lexer.siguiente_token()

        resultado.append(token)

        if token.tipo == TipoToken.FIN:
            break

    return resultado


def main():

    expresion = "a+b*c"

    print("=" * 65)
    print("EJERCICIO 2 - ANALIZADOR LEXICO + SINTACTICO")
    print("=" * 65)

    print("\nExpresión:")
    print(expresion)

    print("\nTOKENS:")

    for token in mostrar_tokens(expresion):
        print(token)

    print("\nANÁLISIS SINTÁCTICO:")

    try:

        parser = Parser(expresion)

        parser.analizar()

        print(
            "Expresión sintácticamente correcta."
        )

    except SyntaxError as error:

        print(
            "Error sintáctico:",
            error
        )


if __name__ == "__main__":
    main()