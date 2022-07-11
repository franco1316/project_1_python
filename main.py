import info_quizizz

is_acent = True
carpet_file = './quizizz'
file_name_start = 'quizz'
file_name_end = '.csv'

add_score_1 = ('Kevin Salvador', 8000)
add_score_2 = ('Diego Angeles', 2000)

winners_number = 2

gen_11_quizizz_all_data = info_quizizz.InfoQuizizz()

gen_11_quizizz_all_data.get_info_quizizz(file_path = carpet_file, file_name_start = file_name_start, file_name_end = file_name_end, acent = is_acent) 
gen_11_quizizz_all_data.list_reduced_score_gen_11 = gen_11_quizizz_all_data.proccess_info(key_name = 'score', index_info_column = 4)
gen_11_quizizz_all_data.score_gen_11 = gen_11_quizizz_all_data.sum_column(key_name = 'score', list_for_key_name = gen_11_quizizz_all_data.list_reduced_score_gen_11)


gen_11_quizizz_all_data.add_extra_score(add_score_1, add_score_2)
gen_11_quizizz_all_data.sort_ranking_score()

gen_11_quizizz_all_data.list_reduced_accuracy_gen_11 = gen_11_quizizz_all_data.proccess_info(key_name = 'accuracy', index_info_column = 3)
gen_11_quizizz_all_data.accuracy_gen_11 = gen_11_quizizz_all_data.sum_column(key_name = 'accuracy', list_for_key_name = gen_11_quizizz_all_data.list_reduced_accuracy_gen_11)

gen_11_quizizz_all_data.sort_ranking_accuracy()
gen_11_quizizz_all_data.get_all_data()
gen_11_quizizz_all_data.winners = gen_11_quizizz_all_data.get_top_x(n = winners_number)
gen_11_quizizz_all_data.show_dict(gen_11_quizizz_all_data.winners, color = 'turqoise')


gen_11_score_data = info_quizizz.InfoQuizizz()

gen_11_score_data.get_info_quizizz(file_path = carpet_file, file_name_start = file_name_start, file_name_end = file_name_end, acent = is_acent)
gen_11_score_data.list_reduced_score_gen_11 = gen_11_score_data.proccess_info(key_name = 'score', index_info_column = 4)
gen_11_score_data.score_gen_11 = gen_11_score_data.sum_column(key_name = 'score', list_for_key_name = gen_11_score_data.list_reduced_score_gen_11)
gen_11_score_data.add_extra_score(add_score_1, add_score_2)
gen_11_score_data.sort_ranking_score()

gen_11_score_data.get_all_data()
gen_11_score_data.winners = gen_11_score_data.get_top_x(n = winners_number, porcent_accuracy = '100 %')
gen_11_score_data.show_dict(gen_11_score_data.winners, color = 'turqoise')

#just only accuracy dont have any sense, it would something ilogic




