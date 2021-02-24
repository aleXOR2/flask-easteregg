# Easter egg sample project

## Prerequisites

* Python3.6+
* Poetry Package for Python installed globally
## Usage

1. in the project root directory, run 
    ```sh
    $ poetry run python3 src/easter_egg.py

    ```
1. Open browser at http://127.0.0.1:8080/ and see the name and the photo
1. You can change change the name in file `src/static/user_name.txt`


## Log

Using https://manytools.org/hacker-tools/convert-images-to-ascii-art/go/ to convert it

Template snippet is taken from https://stackoverflow.com/questions/46785507/python-flask-display-image-on-a-html-page/46794505


Q: flask jinja2.exceptions.TemplateNotFound: index.html
A: 
You must create your template files in the correct location; in the templates subdirectory next to the python module (== the module where you create your Flask app).

The error indicates that there is no home.html file in the templates/ directory. Make sure you created that directory in the same directory as your python module, and that you did in fact put a home.html file in that subdirectory. If your app is a package, the templates folder should be created inside the package.

myproject/
    app.py
    templates/
        home.html
myproject/
    mypackage/
        __init__.py
        templates/
            home.html
R: https://stackoverflow.com/questions/23327293