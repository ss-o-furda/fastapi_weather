# FastAPI Weather Service

Written on python using FastAPI, openweathermap. Based on Modern APIs with FastAPI and Python Course

# How to run?

## You need to get a free API key

Go to https://openweathermap.org/ , register and get a free api key to send requests to their server.

## Place the received key in the `settings.json` file

You need to create a `settings.json` file and put the api key you got earlier in it. You can see how to do it correctly in the example in the `settings_template.json` file.

## Create a new environment for your python

Let's assume that you already have the latest version of Python installed. If not, go to https://www.python.org/. There are detailed instructions on how to do it for your operating system.

The project was written and tested on Python `v3.10.0`, but should run on `v3.5` and higher.

First, you need to install a new environment using the command:

```sh
python3 -m venv /path/to/new/virtual/environment
```

Next, you need to activate the previously created environment:
| Platform | Shell | Command to activate virtual environment |
|----------|-----------------|-----------------------------------------|
| POSIX | bash/zsh | $ source <venv>/bin/activate |
| | fish | $ source <venv>/bin/activate.fish |
| | csh/tcsh | $ source <venv>/bin/activate.csh |
| | PowerShell Core | $ <venv>/bin/Activate.ps1 |
| Windows | cmd.exe | C:\> <venv>\Scripts\activate.bat |
| | PowerShell | PS C:\> <venv>\Scripts\Activate.ps1 |

## Install the dependencies

Next, you need to install dependencies in the created and activated environment:

```sh
pip install -r requirements.txt
```

## Run the project

```sh
python main.py
```

## Check the result

Open your browser and go to http://127.0.0.1:8000/ and you will see the project page.
