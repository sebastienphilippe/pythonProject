# pythonProject
 
<!-- The goal of this project is to study the lobbying in france -->

# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

You first need to install virtual env to create a virtual environnement where you will be able to work on your project

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install virtualenv 
```

Then you need to create a virtual environnement with the following command : 

```bash
virtualenv projectName
```

After this you need to launch the virtual environnement

```bash
    source ./Scripts/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django on the virtual environnement.

```bash
pip install django 
```

Create a django project 
```bash
django-admin startproject projetpython
```

run the server 

```bash
python manage.py runserver
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)