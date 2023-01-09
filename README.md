# ADUser-Group-TreeViewer
This project will be a python based tool, to view all groups and subgroups of a specified Active Directory User.

Read more in the [Wiki Section](https://github.com/KevFischer/aduser-group-treeviewer/wiki).

## How to run

## Prerequisites

### Python

First of all you need to make sure that Python is installed.

Check if python is installed by typing the following line in shell / command-prompt:

    python -V
    
or eventually:

    python3 -V
    
You should get a similar output like this:

    Python 3.10.6
    
If you don't get an output like this or an error message, you should install Python first.

You can get it [here](https://www.python.org/downloads/).

Or if you using Linux, you can simply paste following commands in your shell:

    $ sudo apt-get update
    $ sudo apt-get install python3.10

In development i'm using the following version:

    Python 3.10.6
  
To make sure everything is working fine, you should have at least the version mentioned above.

### PIP

To install python packages I'm using pip with the following version:

    pip 22.2.1 from C:\Python310\lib\site-packages\pip (python 3.10)
    
To make sure everything is working fine, you should have at least the version mentioned above.

Note: PIP can be automatically installed with python together.

### Virtual environment

I am using a [virtual environment](https://pypi.org/project/virtualenv/) (short venv) to prevent e.g. class name duplications.

To set up a venv, you need to have virtualenv installed.

You can install it by typing the following line in your prompt:

    pip install virtualenv
    
I am using the following version of virtualenv:

    virtualenv==20.16.4
    
You can check your version of virtualenv by using following command:

    pip show virtualenv

The output should look like this:

    Name: virtualenv
    Version: 20.16.4
    Summary: Virtual Python Environment builder
    Home-page: https://virtualenv.pypa.io/
    Author: Bernat Gabor
    Author-email: gaborjbernat@gmail.com
    License: MIT
    Location: c:\users\wm01114\appdata\local\programs\python\python310\lib\site-packages
    Requires: distlib, filelock, platformdirs
    Required-by:

Now, in your project directory you can create a virtual environment by typing the following line:

    python -m venv [NAME OF VENV]
    
Note: Replace [NAME OF VENV] with a name you like. I'm usually using "venv" as the name of the virtual environment for simplicity.

You can activate the virtual environment as following:

On windows:

    .\venv\Scripts\activate

Note: If your PowerShell execution policy rejects you from executing the activate.ps1, you can try the activate.bat in a Command Prompt, rather than in a PowerShell Environment.
    
On Linux:

    source \venv\bin\activate.sh
    
Now you're ready to install required packages in the environment by hitting the following line:

    pip install -r requirements.txt
    
Note: You need to be in the same directory where requirements.txt is located.

## Run the program

There are some start arguments which are necessary to run the program:
    
|Short Option|Long Option|Parameters|Description|Required|
|---|---|---|---|---|
|-h|--help|None|List all options with it's description|No|
|-ng|--nogui|-|Decide wether the tree should be displayed in a GUI or not|No|
|-o|--outfile|String|File where results should be safed in|No|
|-u|--user|String|SamAccountName of ADUser|No|

So running the program can look the following:

    .\aduser-group-treeviewer.exe --nogui --user "abc123" --outfile "test.txt"

## Troubleshooting

Feel free to create [issues](https://github.com/KevFischer/aduser-group-treeviewer/issues) if you have troubles starting the app or setting up one of the prerequisites.

I'm looking forward to help with every issue.

## Roadmap

You can have an indepth view of planned Features, Bugfixes and more in the [issues section](https://github.com/KevFischer/aduser-group-treeviewer/issues).
