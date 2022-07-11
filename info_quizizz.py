from array import array
import os
import csv
import operator

from colors import Colors

class InfoQuizizz:

    list_gen_11 = []
    list_reduced_score_gen_11 = []
    list_reduced_accuracy_gen_11 = []
    accuracy_gen_11 = {}
    rep_accuracy = {}
    score_gen_11 = {}
    dict_gen_11 = {}
    winners = {}

    def __init__(self, *args, **kwargs) -> None:
        if len(args) > 0:
            for arg in args:
                self.arg = arg
        if len(kwargs) > 0:
            for kwarg in kwargs.values():
                self.kwarg = kwarg

    def __normalize(self, phrase: str) -> str:
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for á, a in replacements:
            phrase = phrase.replace(á, a).replace(á.upper(), a.upper())
        return phrase

    def __set_index_file(self, file_name: str, index_file: int = 0, route_start: str = 'quizz_', route_end: int = 1) -> int:
        while route_end <= self.__number_files:
            if file_name.startswith(f'{route_start}{route_end}'):
                index_file = route_end - 1
            route_end += 1
        return index_file

    def get_info_quizizz(
        self, file_path: str, file_name_start: str, file_name_end: str, acent: bool = True, index_file: int = 0, number_files: int = 4, 
        number_columns: int = 5, mayus_for_columns: array = [1, 2]
    ) -> None:
        self.__number_files = number_files
        self.__max_students = [0] * number_files
        files = os.scandir(file_path)
        list_quizizz = [''] * number_files
        for file in files:
            if file.name.startswith(file_name_start) and file.name.endswith(file_name_end):
                index_file = self.__set_index_file(file.name, number_files)
                with open(f"{file_path}/{file.name}", encoding="utf-8") as csv_file:
                    file_to_process = csv.DictReader(csv_file)
                    totalrows = len(csv_file.readlines()) - 1
                    self.__max_students[index_file] = totalrows
                    list_quizizz[index_file] = [''] * totalrows
                index_user = 0
            
                with open(f"{file_path}/{file.name}", encoding="utf-8") as csv_file:
                    file_to_process = csv.DictReader(csv_file)
                    for dictionary in file_to_process:
                        list_quizizz[index_file][index_user] = [''] * number_columns
                        index_prop = 0
                        while index_prop < number_columns: #just only have 5 columns each quizz, I dont had considered another posibility
                            if(index_prop == mayus_for_columns[0] or index_prop == mayus_for_columns[1]): 
                                if not acent:
                                    list_quizizz[index_file][index_user][index_prop] = {
                                        f'{list(dictionary.keys())[index_prop]}': self.__normalize(f'{list(dictionary.values())[index_prop].title()}')
                                    }
                                else:
                                    list_quizizz[index_file][index_user][index_prop] = {
                                        f'{list(dictionary.keys())[index_prop]}': f'{list(dictionary.values())[index_prop].title()}'
                                    }
                            else:
                                list_quizizz[index_file][index_user][index_prop] = {
                                    f'{list(dictionary.keys())[index_prop]}': f'{list(dictionary.values())[index_prop]}'
                                }
                            index_prop += 1
                        index_user += 1
                        
        self.list_gen_11 = list_quizizz
    
    def proccess_info(self, key_name: str, index_info_column: int) -> list:
        index_file = 0
        list_reduced = [''] * len(self.list_gen_11)

        for sub_list in self.list_gen_11:
            list_reduced[index_file] = [''] * len(sub_list)
            index_user = 0
            for my_own_dictionary in sub_list:
                key_username_value = f"{my_own_dictionary[1]['First Name']} {my_own_dictionary[2]['Last Name']}"
                key_name_value = my_own_dictionary[index_info_column][key_name.title()]
                if key_name_value[-1] != '%':
                    list_reduced[index_file][index_user] = {
                        'username': key_username_value, 
                        key_name: int(key_name_value)
                    }
                else: 
                    list_reduced[index_file][index_user] = {
                        'username': key_username_value, 
                        key_name: int(key_name_value.split(' ')[0])
                    }
                index_user += 1

            index_file += 1
        return list_reduced

    def sum_column(self, key_name: str, list_for_key_name: list) -> dict:
        ranking_gen_11 = {}
        index_files = 0
        while index_files < self.__number_files:
            index_students = 0
            while index_students < self.__max_students[index_files]:
                user = list_for_key_name[index_files][index_students]
                username = user['username']
                keyname = user[key_name]
                try:
                    if key_name == 'accuracy':
                        self.rep_accuracy.update({username: self.rep_accuracy[username] + 1})
                    ranking_gen_11.update({username: ranking_gen_11[username] + keyname})
                except KeyError:
                    if key_name == 'accuracy': 
                        self.rep_accuracy[username] = 1
                    ranking_gen_11[username] = keyname
                index_students += 1
            index_files += 1
        return ranking_gen_11

    def add_extra_score(self, *args: tuple) -> None:
        ranking_gen_11 = self.score_gen_11
        for arg in args:
            name = arg[0]
            score = arg[1]
            try:
                ranking_gen_11.update({name: ranking_gen_11[name] + score})
            except KeyError:
                ranking_gen_11[name] = score
            try:
                self.accuracy_gen_11.update({name: self.accuracy_gen_11[name] + 100})
                self.rep_accuracy.update({name: self.rep_accuracy[name] + 1})
            except KeyError:
                self.accuracy_gen_11[name] = 100
                self.rep_accuracy[name] = 1
        self.score_gen_11 = ranking_gen_11

    def sort_ranking_score(self) -> None:
        rank = self.score_gen_11
        rank_sorted = sorted(rank.items(), key = operator.itemgetter(1), reverse = True)
        rank = {}
        index_user = 0
        for user in rank_sorted:
            rank[user[0]] = user[1]
            index_user += 1

        self.score_gen_11 = rank

    def sort_ranking_accuracy(self) -> None:
        rank = self.accuracy_gen_11
        rank_sorted = sorted(rank.items(), key = operator.itemgetter(1), reverse = True)
        rank = {}
        index_user = 0
        for user in rank_sorted:
            rank[user[0]] = f"{user[1]/self.rep_accuracy[user[0]]} %"
            index_user += 1

        self.accuracy_gen_11 = rank

    def get_all_data(self) -> None:
        all_data = {}
        for user in self.score_gen_11:#I priority score over accuracy
            score = self.score_gen_11[user]
            try:
                accuracy = self.accuracy_gen_11[user]
            except KeyError: 
                accuracy = '100 %' #this happend because I've at least one user without accuracy
            all_data[user] = {'score': score, 'accuracy': accuracy}
        
        self.dict_gen_11 = all_data
        self.show_dict(all_data)

    def get_top_x(self, n: int = 2, porcent_accuracy: str = '70 %') -> dict:
        dict_winners = {}
        i = 0
        while(i < n): 
            try:
                name = list(self.dict_gen_11)[i]
            except IndexError:
                break
            index_porcent = porcent_accuracy.find('%')
            try:
                index_porcent_2 = self.dict_gen_11[name]['accuracy'].find('%')
                porcent_in_dict = float(self.dict_gen_11[name]['accuracy'][0:index_porcent_2 - 1])
            except AttributeError:
                index_porcent_2 = 0
                porcent_in_dict = float(self.dict_gen_11[name]['accuracy'])
                print(porcent_in_dict)
            
            porcent_required = float(porcent_accuracy[0 : index_porcent - 1])
            if porcent_in_dict >= porcent_required: 
                dict_winners[name] = self.dict_gen_11[name] 
            i += 1
        return dict_winners

    def show_dict(self, dict: list, color: str = 'green') -> None:
        color = color.upper()
        colors = Colors()
        if color == 'GREEN':
            color = colors.GREEN
        if color == 'TURQOISE':
            color = colors.TURQOISE
        index = 0
        print()
        print(color, f' {len(dict)} Winners '.center(75, "=") + "\n")
        print(f'    winners{colors.DEFAULT}' + ': {')
        for user in dict:
            if index < len(dict) - 1:
                print(f'        {color}{user}{colors.DEFAULT}: {dict[user]},')
            else:
                print(f'        {color}{user}{colors.DEFAULT}: {dict[user]}')
            index += 1
        print('    }', "\n")
        print(color, f' {len(dict)} Winners '.center(75, "=") + "\n")
        print(colors.DEFAULT)

