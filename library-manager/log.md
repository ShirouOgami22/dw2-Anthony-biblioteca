# Project Development Log

#codebase 

uhh, i gotta do a school project of a library manager, no need to be too complex or overcomplicated, i wanted to use c# but i guess python is easier for this, i will need a web based front end, a local sqlite database of at least 100 books, well organized python files with a .bat file to act like a .exe would, just to start the program. also, i need you to make a log.md file and in this file put absolutely all prompts i make, without execption, everything i write here must be on this file
can you fix it up? pls tidy up the whole project, i feel its very messy
can you do all that for me?:
web interface, properly organized in its folder, with js css html, another folder for the python backend of the application, with all required python files, a local sqlite database file with at least 100 books with their respective info such as title, pub. year, author and genre. 
a .bat file with the trigger to start the application troguh the main python file with python3
and finally a log.md file, containing absolutely all prompts i make, just input the raw text from my prompts an separate them by a new line

ok, is there any other way to run a python script besides pyhton3? i dont currently have that one installed and i cant install it

the start_app.bat to work that way then? also, every time you touch the project, you can update the log.md to input past prompts

ok, cool, you may apply the changes... im not sure how you function yet, do i gotta change the 'ask' to 'edit'?

grüße, can you see the project? #codebase


aaand now this

Traceback (most recent call last):
	File "C:\Users\anthony_guerra\Downloads\aiProject\library-manager\backend\app.py", line 5, in <module>
		initialize_db()
		~~~~~~~~~~~~~^^
	File "C:\Users\anthony_guerra\Downloads\aiProject\library-manager\backend\database.py", line 8, in initialize_db
		conn = connect_db()
	File "C:\Users\anthony_guerra\Downloads\aiProject\library-manager\backend\database.py", line 4, in connect_db
		conn = sqlite3.connect('data/library.db')
sqlite3.OperationalError: unable to open database file
Traceback (most recent call last):
	File "C:\Users\anthony_guerra\Downloads\aiProject\library-manager\backend\app.py", line 5, in <module>
		initialize_db()
		~~~~~~~~~~~~~^^
	File "C:\Users\anthony_guerra\Downloads\aiProject\library-manager\backend\database.py", line 8, in initialize_db
		conn = connect_db()
	File "C:\Users\anthony_guerra\Downloads\aiProject\library-manager\backend\database.py", line 4, in connect_db
		conn = sqlite3.connect('data/library.db')
sqlite3.OperationalError: unable to open database file
Press any key to continue . . .

now got this

Traceback (most recent call last):
	File "C:\Users\anthony_guerra\Downloads\aiProject\library-manager\backend\app.py", line 6, in <module>
		@app.before_first_request
	 ^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Flask' object has no attribute 'before_first_request'. Did you mean: 'before_request'?
Traceback (most recent call last):
	File "C:\Users\anthony_guerra\Downloads\aiProject\library-manager\backend\app.py", line 6, in <module>
		@app.before_first_request
	 ^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Flask' object has no attribute 'before_first_request'. Did you mean: 'before_request'?
Press any key to continue . . .

i still get that server error, what could it be? can you fix it and explain?
#codebase
#file:instructions.txt 
#file:log.md 
#editFiles
