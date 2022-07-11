This project was made by Franco André alias in github: franco1316.

About the project, is divide in files.py, files.csv, readme.md and your respective folders.

The files.csv are results from quizziz to the gen-11-academlo of the professor Nicolás Rondon,
these files were made by rows and columns of data, each row is for just only 1 user of the gen-11,
every column is for 'Rank', 'First Name' 'Last Name', 'Accuracy', 'Score', the name of the files 
are quizz_, number of files and .csv (extension of the file).

The file project_1.md contains the original intructions and specifications for this project.
The file sumary.md is just what it means, write on my own.

The file __init__.py enable import files at the same route of respective folder.
The file info_quizizz.py is a file to add all the functionality for read the quizz.csv files but
also can do the same with other files if the users give the parameters file_path: str, 
file_name_start: str, file_name_end: str in get_info_quizizz, get information and return in a 
list, this file also have a function to procced information and reorganize it and find the winners
and your respective scores, for the end get users with equal or more score than a specific number.

Finally the main file of this project, the last file is for execute the info_quizizz.py for
fulfill the purpose describe in the folder instructions.

For the variables in main.py, I have variables for change the path from quizz or name, but I need that the difference
must be one number in your names, if is_acent = True then Nicolás Rondón -> Nicolás Rondón, but if is_acent = False,
Nicolás Rondón -> Nicolas Rondon, if ypu need others extra score just only add or change variables like add_score_x =
(name as str, score as int)