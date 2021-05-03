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

## Inside container
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


Q: error while `docker run` bash - can't read binary file
A: add -c to read commands after the entrypoint with bash

R: https://stackoverflow.com/questions/61055324/docker-cannot-execute-binary-file


good production image
https://github.com/python-poetry/poetry/discussions/1879
one more for web-server build up:
https://github.com/michael0liver/python-poetry-docker-example/blob/master/docker/Dockerfile


for some reason port exposing does nit work

docker inspect a33263af2792 | less
docker port a33263af2792

ref: https://www.ctl.io/developers/blog/post/docker-networking-rules/
