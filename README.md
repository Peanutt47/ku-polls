[![Django CI](https://github.com/Peanutt47/ku-polls/actions/workflows/django.yml/badge.svg)](https://github.com/Peanutt47/ku-polls/actions/workflows/django.yml)
## KU Polls: Online Survey Questions 

An application to conduct online polls and surveys based
on the [Django Tutorial project][django-tutorial], with
additional features.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Install and Run

1. Clone this repository
    ```commandline
    https://github.com/Peanutt47/ku-polls.git
    ```
2. Install the required libraries
    ```commandline
    cd ku-polls
    ```
    ```commandline
    pip install -r requirements.txt
    ```
3. Run the program
    ```commandline
    python manage.py makemigrations
    python manage.py migrate
    ```
    ```commandline
    python manage.py runserver
    ```

## Demo Users
| Username  | Password        |
|-----------|-----------------|
|   demo1   | stupidpassword1 |
|   demo2   | stupidpassword2 |

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Product backlog](https://github.com/users/Peanutt47/projects/1/views/1)
- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Development Plan](../../wiki/Development)
- [Iteration 1 Plan](https://github.com/Peanutt47/ku-polls/wiki/Iteration-1-Plan) and [Task Board](https://github.com/users/Peanutt47/projects/1/views/3)
- [Iteration 2 Plan](https://github.com/Peanutt47/ku-polls/wiki/Iteration-2-Plan) and [Task Board](https://github.com/users/Peanutt47/projects/1/views/4)
- [Iteration 3 Plan](https://github.com/Peanutt47/ku-polls/wiki/Iteration-3-Plan) and [Task Board](https://github.com/users/Peanutt47/projects/1/views/5)

[django-tutorial]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/
