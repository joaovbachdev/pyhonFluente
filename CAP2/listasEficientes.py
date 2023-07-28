#AQUI TEREMOS ALGUNS EXEMPLOS DE COMO USAR list DE FORMA MAIS EFICIENTE

#list comprehensions = listcomps e expressoes geradoras = genexps

###################################################################################################################
#EXEMPLO PADRAO
symbolsExemplo1 = '@#$%'
codesExemplo1 = []
for i in symbolsExemplo1:
    codesExemplo1.append(ord(i))

print(codesExemplo1)


#EXEMPLO COM LISTCOMPS
symbolsExemplo2 = '@#$%'
codesExemplo2 = [ord(i) for i in symbolsExemplo2]

print(codesExemplo2)
#####################################################################################################################

#LIST COMPS PODE SER MUITO MAIS RAPIDO E MELHOR DO QUE MAP/FILTER

####################################################################################################################



