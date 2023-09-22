1. clone or download the code from Github
    ```
    git clone https://github.com/Peanutt47/ku-polls.git
    ```
2. create a virtual environment and install dependencies
    ```
    cd ku-polls
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    or
    ```
    cd ku-polls
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    *** Note ***
    If you want to deactivate
    ```
    deactivate
    ```
4. run migrations
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
    or
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
6. run tests
    ```
    python manage.py test polls
    ```
7. Load data
    ```
    python manage.py loaddata data/polls.json data/users.json
    ```
    or
    ```
    python3 manage.py loaddata data/polls.json data/users.json
    ```
