Comand -> PRINT STRING | ADD NUMBER NUMBER | SUB NUMBER NUMBER
STRING -> "\"" [a-zA-Z ,.!?']* "\""
NUMBER -> [0-9]+
Comand
  |
PRINT
  |
STRING
  |
"Hello, World!"
Comand
  |
SUB
  |
NUMBER   NUMBER
  |       |
  15      4
Comand
  |
ADD
  |
NUMBER   NUMBER
  |       |
  5       10
import re

def parse_command(command):
    # Expressões regulares para verificar os padrões
    print_pattern = r'^PRINT\s+"[^"]+"$'
    add_pattern = r'^ADD\s+\d+\s+\d+$'
    sub_pattern = r'^SUB\s+\d+\s+\d+$'

    if re.match(print_pattern, command):
        return "Comando PRINT válido"
    elif re.match(add_pattern, command):
        return "Comando ADD válido"
    elif re.match(sub_pattern, command):
        return "Comando SUB válido"
    else:
        return "Erro de Comando Desconhecido"

# Testando comandos válidos e inválidos
commands = [
    "PRINT \"Hello, World!\"",
    "SUB 15 4",
    "ADD 5 10",
    "MULT 5 3",
    "ADD 5",
    "PRINT 5",
    "ADD \"Hello\" 5",
    "PRINT Hello World!",
    "PRINT \"Hello\"World!\"",
    "ADD 5.5 3",
    "ADD \"Hello\" 5"
]

for command in commands:
    result = parse_command(command)
    print(f"{command} - {result}")
