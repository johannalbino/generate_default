import json
from django.conf import settings
import os


class GenerateDefault(object):

    def __init__(self):
        with open(os.path.join(settings.BASE_DIR, 'home/classes/programas.json')) as file:
            self.__programs_file = json.load(file)
        self.__date = []
        self.__mounth = 0
        self.__year = 0
        self.__directory = []
        self.__programs = []
        self.__response = []

    def get_information(self, client, year, mounth):
        self.__mounth = mounth
        self.__year = year

        if len(client.split(' ')) > 1:
            client = GenerateDefault.validate_name(client.split(' '))

        # retornando uma lista
        return ['base_' + client, self.__mounth, self.__year]

    def get_directory(self, year, mounth):
        for i in self.__programs_file['diretorios']:
            self.__directory.append(i + f'{year}{mounth}* #')
            self.__directory.append(i + f'{mounth}{year}* #')
        return self.__directory

    @classmethod
    def validate_name(cls, name_base):
        _name_base = ''
        for i in name_base:
            _name_base += i
        return _name_base

    def generate_file(self, client, departament, mounth, year):
        """Função que gera o arquivo e retorna para a view"""
        self.__date = self.get_information(client, mounth, year)
        if int(self.__date[1]) < 10:
            self.__date[1] = '0' + str(self.__date[1])

        self.get_directory(self.__date[2], self.__date[1])

        if departament == 'Fiscal':
            self.__programs = self.__programs_file.get('programas_fiscal', {'msg': 'Not found program Fiscal!'})
        elif departament == 'Contabil':
            self.__programs = self.__programs_file.get('programas_contabeis', {'msg': 'Not found program Contabil!'})
        elif departament == 'Materiais':
            self.__programs = self.__programs_file.get('programas_materiais', {'msg': 'Not found program Materiais!'})
        elif departament == 'Financeiro':
            self.__programs = self.__programs_file.get('programas_financeiros', {'msg': 'Not found program Financeiro!'})

        for i in self.__programs, self.__programs_file.get('programas_parametros',
                                                           {'msg': 'Not found program Paramatros!'}), self.__directory:
            for x in i:
                self.__response.append('rar a ' + self.__date[0] + ' ' + str(x))
        self.__response.append('mv ' + self.__date[0] + '.rar /u/rede/avanco')
        return self.__response
