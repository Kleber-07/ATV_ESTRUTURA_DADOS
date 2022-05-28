from Aula_Es_Dados2 import Tarefa
import os

minhas_atividades = []

def criar_tarefa():
    os.system('cls')
    print("============= CRIAR TAREFA")
    tarefa_nome = input('Descrição: ')
    data_inicio = input ("Data: ")
    hora_inicio = input ('Horário: ')
    nova_tarefa = Tarefa()
    nova_tarefa.criar_nova_tarefa(tarefa_nome, data_inicio, hora_inicio)
    if(len(minhas_atividades)!=0):
        for t in minhas_atividades:
            posicao = minhas_atividades.index(t)
            tarefa = t.retornar_valores()
            i = tarefa[2]
            if hora_inicio < i:
                minhas_atividades.insert(posicao, tarefa)
            else:
                minhas_atividades.append(nova_tarefa)
    else:
        minhas_atividades.append(nova_tarefa)





def exibir_tarefa():
    os.system('cls')
    print('============= LISTANDO TAREFAS\n')
    print('_____________________________________________')
    for t in minhas_atividades: #iterator
        tarefa = t.retornar_valores()
        print(f'Tarefa: {tarefa[0]}')
        print(f'Data: {tarefa[1]}')
        print(f'Horário: {tarefa[2]}')
        print('_____________________________________________')
    input('Fim das tarefas. [ENTER] para continuar.')



def pesquisar_tarefa(retorna=False):
    os.system('cls')
    print('============= PESQUISAR TAREFA\n')
    atividade = input('Pesquisar por: ')
    for t in minhas_atividades:
        tarefa = t.retornar_valores()
        if tarefa[0].lower() == atividade.lower():
            if not retorna:
                print(f'Atividade na posição {minhas_atividades.index(t)}')
                print(f'Tarefa: {tarefa[0]}')
            else:
                return minhas_atividades.index(t)



def editar_tarefa():
    posicao = pesquisar_tarefa(True)
    os.system('cls')
    print('============= EDITAR TAREFA\n')
    minhas_atividades[posicao].alterar_tarefa()




def excluir_tarefa():
    posicao = pesquisar_tarefa(True)
    tarefa_temp = minhas_atividades[posicao]
    os.system('cls')
    print('============= EXCLUIR TAREFA\n')
    minhas_atividades.remove(tarefa_temp)






pode_contiunar = True
while pode_contiunar:
    print(' ============== Menu ===============')
    print('[C]riar Tarefa')
    print('[L]istar Tarefas')
    print('[P]esquisar Tarefa')
    print('[E]ditar Tarefa')
    print('E[x]cluir Tarefa')
    print('[S]air')
    op = input('> ')
    if op.lower() == 'c':
        criar_tarefa()
    elif op.lower() == 'l':
        exibir_tarefa()
    elif op.lower() == 'p':
        pesquisar_tarefa()
    elif op.lower() == 'e':
        editar_tarefa()
    elif op.lower() == 'x':
        excluir_tarefa()
    elif op.lower() == 's':
        print("Fim do programa!")
        pode_contiunar = False
    else:
        os.system('cls')
        input('Opção inválida. [ENTER] para continuar')
