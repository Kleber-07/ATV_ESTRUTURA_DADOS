#tarefa.py
class Tarefa:
    _descricao = None
    _data_inicio = None
    _horario_inicio = None

    def criar_nova_tarefa(self, desc, data, hora):
        self._descricao = desc
        self._data_inicio = data
        self._horario_inicio = hora
        print('Tarefa cadastrada com sucesso!')

    def retornar_valores(self):
        return (self._descricao, self._data_inicio, self._horario_inicio)

    def alterar_tarefa(self):
        print('[ENTER] para manter os valores!')
        temp = input('Digite a nova tarefa: ')
        if len(temp) > 0:
            self._descricao = temp

        temp = input('Digite a nova Data: ')
        if len(temp) > 0:
            self._data_inicio = temp

        temp = input('Digite o novo Horário: ')
        if len(temp) > 0:
            self._horario_inicio = temp
