
#Criando uma lista vazia
lista = []

#Inserindo dados na lista
lista.append('Tarefa 1')
lista.append('Tarefa 2')
lista.append('Tarefa 3')
lista.append('Tarefa 4')

#Exibindo lista
print ('Essa é minha lista original')
print(lista)

#usando a lista com base no ITERATOR
print('\nEsses são meus valores da lista')
for atividade in lista:
    print(atividade)

#inserindo uma tareffa em uma posição especiica
lista.insert(2, 'tarefa 6')
print(f'\nEssa é a lista depois do insert\n{lista}')

#Estendendo a nossa lista
afazeres = ['Tarefa 20', 'Tarefa 21', 'Tarefa 22']
lista.extend(afazeres)
print(f'\nEssa é a lista depois do extend\n{lista}')

#Removendo um elemento da lista
lista.remove('Tarefa 1')
print(f'\nEssa é a lista depois do REMOVE\n{lista}')

#Removendo um elemento ATRAVÉS DO POP
concluidas = lista.pop()
print(f'\n a tarefa {concluidas} foi atualizada')


#pegando a posição especiica de um valores
print(lista)
print ('\nposição do elemento Tarefa 3')
print(lista.index('Tarefa 3'))
print('\nDesconsiderando parte da lista')
print(lista.index('Tarefa 3', 2))
