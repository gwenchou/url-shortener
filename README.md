# url-shortener

## Run
```
docker-compose -f docker-compose.yml up
```
That's it! Everything should work on http://127.0.0.1:8099

## Run test

```
pip install -r requirements.txt

cd src/

python3 manage.py test
```

## Coverage report
```
cd src/

coverage run --source='.' manage.py test

coverage report
```
