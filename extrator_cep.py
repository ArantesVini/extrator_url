import re

endereco = "Rua do Barulho 409, apartamente 323," \
         " Cidade, Estado, ES, 95085020"

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)
