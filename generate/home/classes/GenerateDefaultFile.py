class GenerateDefault(object):

    def __init__(self, programs, program_geral, program_directory):
        self.__programs_file = programs + program_geral
        self.__directory = program_directory
        self.__date = []
        self.__mounth = 0
        self.__year = 0
        self.__response = []

    def get_information(self, client, year, mounth):
        self.__mounth = mounth
        self.__year = year

        if len(client.split(' ')) > 1:
            client = GenerateDefault.validate_name(client.split(' '))

        # retornando uma lista
        return ['base_' + client, self.__mounth, self.__year]

    def get_directory(self, year, mounth):
        dir = []
        for i in self.__directory:
            dir.append(i.directory_program + f'{year}{mounth}* #')
            dir.append(i.directory_program + f'{mounth}{year}* #')
        return dir

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

        directory = self.get_directory(self.__date[2], self.__date[1])

        for i in self.__programs_file, directory:
            for x in i:
                self.__response.append('rar a ' + self.__date[0] + ' ' + str(x))
        self.__response.append('mv ' + self.__date[0] + '.rar /u/rede/avanco')
        return self.__response
