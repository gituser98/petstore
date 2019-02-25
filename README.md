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


Important Info regarding tests and assertions:

Petstore Swagger documentation is not very accurate. <br>
Some calls with invalid data returns '200' instead of any error codes (400, 404, 405 etc). <br>
I mentioned these in the code while doing assertions. 

I also skipped implementation of some tests since they take time and this is a sample project.
<br>
I marked those tests as 'pass'