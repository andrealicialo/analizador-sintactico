# Actividad 9 - Analizadores Sintácticos Descendentes

Práctica de la materia Tecnología de Compiladores.

## Objetivo

Implementar analizadores sintácticos descendentes
utilizando Python y aplicar gramáticas libres de contexto.

## Ejercicio 1

Analizador de expresiones aritméticas.

Gramática:

E  -> T E'
E' -> + T E' | epsilon

T  -> F T'
T' -> * F T' | epsilon

F  -> id | (E)

## Ejercicio 2

Integración de un analizador léxico que reconoce:

- IDENTIFICADOR
- SUMA
- MULTIPLICACION
- PARENTESIS_IZQ
- PARENTESIS_DER
- FIN

## Ejercicio 3

Analizador descendente para paréntesis equilibrados.

Gramática utilizada:

S -> (S)S | epsilon

## Ejercicio 4

Analizador descendente para paréntesis y corchetes.

Gramática:

S -> (S)S | [S]S | epsilon

## Tecnologías

- Python
- Visual Studio Community
- Git
- GitHub

## Ejecución

```bash
python ejercicio_1_parser_aritmetico.py
python ejercicio_2_lexer_parser.py
python ejercicio_3_parentesis.py
python ejercicio_4_parentesis_corchetes.py