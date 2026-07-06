from parser.text_parser import TextParser

texto = """
Preencher formulário: Requisicao_Deficiente_EstacionamentoV1

Paciente: João Silva
Idade: 32
CPF: 123.456.789-00
Endereço: Rua Leopoldina, 44
"""

dados = TextParser.parse(texto)

print(dados)