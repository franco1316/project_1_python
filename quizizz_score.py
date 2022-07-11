from info_quizizz import InfoQuizizz


class Score(InfoQuizizz):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def proccess_info(self, my_list: list, dict_prop_name_1: str = 'username', dict_prop_name_2: str = 'score', old_prop_name_1: str = 'First Name', old_prop_name_2: str = 'Last Name', old_prop_name_3: str = 'Score') -> None:
        return super().proccess_info(my_list, dict_prop_name_1, dict_prop_name_2, old_prop_name_1, old_prop_name_2, old_prop_name_3 = 'Score')
    
    def sum_scores(self) -> None:
        return super().sum_scores()

    def add_extra_score(self, *args: tuple) -> None:
        return super().add_extra_score(*args)

    def sort_ranking(self) -> None:
        return super().sort_ranking()