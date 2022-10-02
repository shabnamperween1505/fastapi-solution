# fastapi-solution

To run all the tests on API of Task-1 :
```
pytest app/test.py 
```

To run all tests on the solution for valid-parantheses problem of Task-2 :
```
pytest app/valid-parentheses.py
```

To run the code for the valid-parantheses problem, paste the statement -> print("{[(){}]}", Solution.isValid(self= Solution, s="{[(){}]}"))
and run :
```
python app/valid-parentheses.py
```


# Initial Assessment instructions
A simple example of using Fast API in Python.

## Preconditions:

- Python 3

## Run local

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload
```

### Run test

```
pytest app/test.py
```

## Run with docker

### Run server

```
docker-compose up -d --build
```

### Run test

```
docker-compose exec app pytest test/test.py
```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

### Run server

```
docker-compose exec db psql --username=fastapi --dbname=fastapi_dev
```
