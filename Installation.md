1. clone or download the code from Github
    ```
    git clone https://github.com/Peanutt47/ku-polls.git
    ```
2. create a virtual environment and install dependencies
    ```
    python -m venv venv
    venv/bin/activate
    pip install -r requirement.txt
    ```
    *** Note ***
    If you want to deactivate
    ```
    deactivate
    ```
3. run migrations
    ```
    python manage.py migrate
    ```
4. run tests
    ```
    python manage.py test polls
    ```
5. Dump data only for the Question and Choice tables (no votes).
   ```
   python manage.py dumpdata --indent=2 polls.question polls.choice
   ```
   Dump the auth.user data to a file data/users.json
   ```
   python manage.py dumpdata --indent=2 -o data/users .json auth.user
   ```
