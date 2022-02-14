 
## To start the webserver:

```console
foo@user:~$ cd project_directory/env/projectnlp/
foo@user:~$ python3 -m venv env
foo@user:~$ source env/bin/activate
foo@user:~$ pip install django spacy requests nltk
foo@user:~$ python -m spacy download en_core_web_sm
foo@user:~$ python3 manage.py runserver
```

