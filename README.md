# Project api rest academy of magic

The academy of magic need a  profram sofware that assign once grimorio by magician.

Where such grimorio had 1 between 5 leaf clover like front page.

## Begin 🚀

This project was in github to download or clone repostitory, fork

How are  **Deployment**  of this project.

### Pre-requisitos 📋

You have that install python 3.11.2, pip and virtualenv.

```cmd
python venv venv
```

You need activate virtual enviroment activating the script activate.bat, in windows:

```tex
.\venv\Scripts\activate  
```

In linux is

```sh
source venv/bin/activate
```

### Instalation 🔧

In this project has requiriments.txt

```cmd
pip install -r requiriments.txt
```

Ready this part, continue with  django process, how migrate database and run server

First, you will have  that are make migrations of the model a to database (Postgres), the database configuration is in the .env file

```python
python manage.py makemigrations
```

then, you will have that are the migrate  the model to database

```cmd
python manage.py migrate
```

To finish, you will have to launch the server in your local host.

```bash
python manage.py runserver
```

## Deploy 📦
Using one client rest like postman o thunder client, query the paths, views in the index

```path
get/magos/
get/grimorio/
all/
post/
update/
del/
```

Example to post or update

```json
{
  "Name": "Merlin",
  "lastname": "Emrys",
  "age": 99
}
```

Example to delete 

```json
{
"id": "XsOSK7vhvs"
}
```

Example to get


```json
[{
    "Name": "Harry",
    "lastname": "Poter",
    "id": "ZIYv7weqsa",
    "magic_aff": "Magia de Rayo",
    "age": 98,
    "estado": true
    }
]
```
## Build with 🛠️

* [Django](https://www.djangoproject.com/) - The framework web Django
* [pip](https://pypi.org/project/pip/) -
Dependency manager
* [Python](https://www.python.org/downloads/) - Language python 3.11.2

## Version 📌

Be used [github](https://github.com/) for controll of version.

## Develop ✒️

* **Breyner Ocampo Cardenas** - [broc95](https://github.com/broc95)
