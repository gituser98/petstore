Environment:
platform win32 -- Python 3.7.1, pytest-4.3.0, py-1.8.0, pluggy-0.9.0 <br>
pipenv installed - pipenv, version 2018.11.26 <br>

1. Clone the project
2. Go to project directory
3. Active shell -> $ pipenv shell
4. Install dependencies -> $ pipenv install
5. From project base dir (within pipenv shell), run pytest <br>
$ pytest --html=testresults.html
<br> ---> This will generate test results in html format in current directory

Tested these steps on my local windows and AWS EC2 Linux instance:<br>
platform linux -- Python 3.7.1, pytest-4.3.0, py-1.8.0, pluggy-0.9.0
