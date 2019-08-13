import os
from platform import python_version
import json


class GerarDefault(object):

    def __init__(self):
        with open(
                'C:\\Users\\johann.albino\\Desktop\\repositório\\generate_default\\generate\\home\\classes\\programas.json') as file:
            self.programas_file = json.load(file)

        with open(
                'C:\\Users\\johann.albino\\Desktop\\repositório\\generate_default\\generate\\home\\classes\\names.json') as file:
            self.name_file = json.load(file)

        self.data = []
        self.mes = 0
        self.ano = 0
        self._diretorios = []
        self._programas = []
        self.response = []
        # print ("Listas carregadas com sucesso!")

    def get_information(self, cliente, ano, mes):
        self.mes = mes
        self.ano = ano
        self.client = cliente

        if len(self.client.split()) > 1:
            self.client = self.valida_name(self.client.split())

        # retornando uma lista
        return ['base_' + self.client, self.mes, self.ano]

    def get_directory(self, ano, mes):
        for i in self.programas_file['diretorios']:
            self._diretorios.append(i + f'{ano}{mes}* #')
            self._diretorios.append(i + f'{mes}{ano}* #')
        return self._diretorios

    def valida_name(self, name_base):
        _name_base = ''
        for i in name_base:
            _name_base += i
        return _name_base

    def gerando_file(self, cliente, setor, mes, ano):
        self.data = self.get_information(cliente, mes, ano)
        if int(self.data[1]) < 10:
            self.data[1] = '0' + str(self.data[1])

        self.get_directory(self.data[2], self.data[1])

        if setor is 'Fiscal':
            self._programas = self.programas_file['programas_fiscal']
        elif setor is 'Contabil':
            self._programas = self.programas_file['programas_contabeis']
        elif setor is 'Materiais':
            self._programas = self.programas_file['programas_materiais']
        elif setor is 'Financeiro':
            self._programas = self.programas_file['programas_financeiros']

        for i in self._programas, self.programas_file['programas_parametros'], self._diretorios:
            for x in i:
                self.response.append('rar a ' + self.data[0] + ' ' + str(x))
        self.response.append('mv ' + self.data[0] + '.rar /u/rede/avanco')
        return self.response
