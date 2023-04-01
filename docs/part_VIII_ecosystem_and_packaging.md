# Part VIII - Ecosystem and Packaging

We've seen already the concept of a module, from Python's standard library, or one from a package that we've installed in our environment.
Also related concept is a "namespace". Let's try to make some sense with those concepts.

## Modules

A module is a (Python) file containing Python code. As simple as that.
We can import a module from another module. We can execute a module as a script from the command line.

```
python my_app.py
python -m my_app
```

We often have multiple modules (Python files).
We'll make our life easier by organizing those into directories (Operating-System folders).  
When we have a directory (and potentially subdirectories) with Python files (modules),
this is getting closer to become a Python package. 

To make it into a package, what is left is to introduce **\_\_init\_\_.py** in each directory.
The \_\_init\_\_.py file is often empty, yet it is still required.

``` py
import pandas as pd
from numpy.random import * # please avoid
from tqdm import tqdm # okay
```

Above we have imported the module 'pandas' and gave it the short-hand convention 'pd'.
In our namespace we've added the symbol 'pd' that happens to be a module.

Then we've imported from the (sub)module numpy.random everything that is available.
Using an asterisk is not recommended as we've lost track of what we've brought,
and we'll confuse ourselves and our friends with referring to items that we don't remember from which module they are.
In a quick, temporary, notebook session, you are welcome to use this "fetch all" import.

The last example with 'tqdm', is actually okay. The custom is to import the module, as we've done with 'pd' and to refer to classes and functions by adding (note the dot) 'pd.' in front of them, for example ```pd.DataFrame()```.  
If you know that you only need one specific thing out of the module, and you know that the name of the functionality you are using is self-explanatory, then, at least by my standards, this is okay.
'tqdm' is a useful utility to see progress bar:

``` py
a = 0
for _ in tqdm(range(100)):
    a = (a + 1) * 2
```

```
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:00<00:00, 1181494.08it/s]
```

Just a recap. Note the addition of 'pd' to the items in the namespace.

``` py
import pandas as pd


print(dir())
```

``` ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'pd'] ```

When we install a package, the relevant files are added to our Python environment.
There they can be found by the Python execution-time, and also by our development tools to provide tips and completions.

So a package is just a collection of modules. Another interpretation is that while we import modules in our Python code,
(or some functionality from a module), we install packages (that bring with them modules).
It is okay to confuse a little between those terms.

## Installable Packages

As mentioned already above, a package is a standard way to wrap modules and additional relevant files, add some metadata, and publish the work (internally or Open Source), to be available to consumption (installation).

A package often have **dependencies**.
Our package shall not contain a copy of the modules from packages that we want to use,
but rather indicate the need for those packages.
When we install, for example with *pip* (package installer for Python), *conda*, or maybe *poetry*,
the tool (say *pip*) shall fetch the dependencies for example from [pypi.org](https://pypi.org/)

```
pip install numpy
```

Above we've installed the package 'numpy'. The module 'numpy' share the name with its package.
It is not always the case that the module has the same name as the relevant package. For example:

```
pip install opencv-python
```

But then:

``` py
import cv2
```

A library is a cross-language, or maybe OS-related, concept, that means about the same as a package.
For example, if you install a Python package for computer vision, or for graphics, it may bring with it, additional libraries,
that are needed (and were for example developed in *C++* and compiled/linked into an installable OS library.)

If you happen to "accidently" refer to a package as a 'library', no harm was done.

Packages have versions. This is a way to indicate progress, compatibility, changes in the interface.
When you use a package (install it in your environment, or add it as a dependency of your code),
you can indicate that you are okay with the "latest and greatest", or that you actually need a specific version.

The version is a string with a trivial "lexicographic" order interpretation.

```
pip show pandas
```

```
Name: pandas
Version: 1.5.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: The Pandas Development Team
Author-email: pandas-dev@python.org
License: BSD-3-Clause
Location: /home/oren/projects/yapy3c/venv/lib/python3.8/site-packages
Requires: python-dateutil, numpy, pytz
Required-by:
```

One option to "dive" deeper and see the dependencies versions:

```
pip install johnnydep

johnnydep pandas
```

```
2023-03-27 12:57:53 [info     ] init johnnydist                [johnnydep.lib] dist=pandas parent=None
2023-03-27 12:57:55 [info     ] init johnnydist                [johnnydep.lib] dist=numpy>=1.20.3 parent=pandas
2023-03-27 12:57:59 [info     ] init johnnydist                [johnnydep.lib] dist=python-dateutil>=2.8.1 parent=pandas
2023-03-27 12:58:00 [info     ] init johnnydist                [johnnydep.lib] dist=pytz>=2020.1 parent=pandas
2023-03-27 12:58:01 [info     ] init johnnydist                [johnnydep.lib] dist=six>=1.5 parent=python-dateutil>=2.8.1
name                        summary
--------------------------  -----------------------------------------------------------------------
pandas                      Powerful data structures for data analysis, time series, and statistics
├── numpy>=1.20.3           Fundamental package for array computing in Python
├── python-dateutil>=2.8.1  Extensions to the standard Python datetime module
│   └── six>=1.5            Python 2 and 3 compatibility utilities
└── pytz>=2020.1            World timezone definitions, modern and historical
```

Also useful ```pip freeze | grep pandas``` or any other package you're interested to find the current installed version.

## Virtual Environments

We keep installing stuff, how do we know that we don't break previous functionality that we had with other projects?
It is a good practice to have a separate Python environment for different projects.
You can use for each of the environments even a different Python version.
When you create the environment, you should use the "right" Python version.
Then you activate the environment and you have some protection against breaking the installation of other projects,
and that you or someone else break your installation.

There are multiple tools to achieve above.
'Poetry' and 'Conda' among others. If no specific preference, try first the standard 'venv' module:

```
python3 -m venv venv
```

Here we choose the name 'venv' to our newly created virtual environment.

On **Linux** (bash), we would then do:

```
source ./venv/bin/activate
```

And one can verify the (bash) environment variable:

```
env | grep VIRTUAL
```

``` VIRTUAL_ENV=/home/oren/projects/yapy3c/venv ```

```
tree -L 1 venv
```

```
venv
├── LICENSE
├── bin
├── etc
├── include
├── lib
├── lib64 -> lib
├── pyvenv.cfg
└── share
```

```
which pip
```

``` /home/oren/projects/yapy3c/venv/bin/pip ```

```
ls venv/lib/python3.8
```

``` site-packages ```

On **Windows** (PS):

```
.\env\Scripts\activate
```

Verify (PS)

```
dir env: | out-string -stream | select-string VIRTUAL
```

```
_OLD_VIRTUAL_PATH              C:\Python310\Scripts\;C:\Python310\;C:\Perl64\bin;C:\Users\zbenm\AppData\Roaming\Acti...
VIRTUAL_ENV                    C:\Users\zbenm\projects\sols_challenge\env
```

We can then verify the version of Python, and the versions of our installed packages ('pip show' as above).

```
python --version
```

``` Python 3.10.8 ```

## Version Control Repositories (probably 'git')

I assume here that you are familiar with the concept of version control and that you are using git.

Let's say I'm using Github, and want to work on a new project in Python, that shall use Flask.

- I'll start by creating a new repository on Github. Alternatively one can just create a new local folder for the project, for example, ```../projects/my_flask_based_web``` and ```git init``` there.

- Let's continue with the Github example. When we create the new repository we're given the option to add a README.md file and .gitignore file. We'll add .gitignore and let Github know that we're planning to use Python.

- We'll clone our new Github repository under our "projects" directory.

- We'll change directory into the just cloned repository.

- It make sense now to have here a Python virtual environment. Alternatively one can "share" virtual environments among projects. It is up to you.

- We'll choose to create a new virtual environment.

```
python3 -m venv venv
```

We're using here 'venv' (rather than the many other ways to create a virtual environment).

Let's see what is the ```git status```.

Interesting enough the new directory 'venv' is not shown as a new directory. This is thanks to the contents of '.gitignore', if this is not the case for you, consider adding a line to your '.gitignore' with the directory with your virtual environment. We usually don't add the virtual environment to the git repository.

- Let's make sure to activate now the virtual environment.

- We want to install, in the example, Flask. Instead of quickly ```pip install Flask``` let's create a new text file 'requirements.txt' and add one line "Flask". Then we can do:

```
pip install -r requirements.txt
```

Let's check:

```
pip show Flask
```

For me is showed:

```
Name: Flask
Version: 2.2.3
Summary: A simple framework for building complex web applications.
Home-page: https://palletsprojects.com/p/flask
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD-3-Clause
Location: /home/oren/projects/try_flask/venv/lib/python3.8/site-packages
Requires: Jinja2, importlib-metadata, Werkzeug, click, itsdangerous
Required-by:
```

- remember to add 'requirements.txt` to the repository with ```git add requirements.txt```. This text file we do want to keep.

- Now we need a flask application. We'll create for example, 'app.py' and add some contents from an example.

``` py title='app.py'
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/<name>")
def hello_world(name):
    return render_template('hello.html', name=name)
```

``` html title="templates/hello.html"
<!doctype html>
<html>
<head>
<title>Hello from Flask</title> 
</head>
<body>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}  
</body>
</html>
```

Please note that the installation of 'Flask' also added a command to our environment.

```
which flask
```

For me it is found here:

```
/home/oren/projects/try_flask/venv/bin/flask
```
- Run the application.

```
flask --app app.py run
```

- Now add all necessary files to git, then ```git commit -m "initial version"``` for example, (and potentially push to Github).

We had only one Python module (the 'app.py' file). Nothing prevents us from adding additional modules that may be imported from 'app.py'.
We can also add package requirements to 'requirements.txt' and issue again ```pip install -r requirements.txt```.

Static files and templates can also be created and added to the directory and to the git repository.

When our colleagues want to have access to the project and potentially join the efforts, we give them a link to the Github repository.
We also remind them that they need to install the required packages before trying the application.
This can be documented also, for example, in the README.md file.

Some of our colleagues will follow you, and do as follows:

```
python3 -m venv venv
pip install -r requirements.txt
```

Others may wish to work in their existing virtual environment (or even their global Python environment), and issue immediately:

```
pip install -r requirements.txt
```

Some may want to use other tools, for example, Poetry for the task.

Note that since the virtual environment mechanism was not part of the repository, each of us can pick his/her favourite way.

Also note that it is possible to share a single (git) repository among multiple projects.
There are advantages for each way.
For example, if each project has its own repository, the projects can advance each in its own pace.
Less confusion and interdependencies.
On the other way, if we have multiple (team related) projects in the same repository,
then the team members are aware of each other work and can iteratively "code review", catch early miscommunications etc. 

It is up to the team to decide what works for the team the best.

Each of us on his laptop could have a single Python virtual environment for all the projects,
or a separate Python virtual environment in each project directory.

Again, up to you to decide what makes sense in your settings and constraints.

## Publishing a package rather than a (git) repository

Above, "trying Flask", is a top-level project. Our "sharing mechanism" was the version control.

There are projects that we want to allow others to install in their existing environments,
so that they can import the functionality from our modules in their own code, without cloning our repository first, or maybe with cloning, but then without being part of the repository maintainers, but rather being "users" of our package.

We're not far from achieving above. Let's have another project.
This time our project, let's call it 'tiny', will be a utility package for the use of the previous "trying Flask" project, potentially also for additional projects.

I've created a new git repository, intended for Python. I've created a new virtual environment and made sure it is activated and there is where I'm working.

I've started the same, I have a 'requirements.txt' file in which I list 'numpy' as I know I'm going to use it next. I've installed the requirements with ``` pip install -r requirements.txt ``` and started to edit my 'tiny' package.

The directory where I'm working (the git repository) is named 'tiny_package'. This is how I've named the new repository. But The actual modules I'll have under the (one level deeper) directory 'tiny'. My 'tiny' package shall accept variable number of arguments, and shall return a matching 'numpy array'. This is the functionality I'll introduce.

Under the directory 'tiny' I'll have a Python module (a Python file) 'mat_math.py', and also the required '\_\_init\_\_.py'.
Below is the content of the files:

``` title="tiny/mat_math.py"
import numpy as np


def to_numpy_arr(*args: int) -> "np.ndarray[int]":
    """
    This function takes a variable amount of argument and
    returns the matching numpy array

    >>> to_numpy_arr(1, 2, 3)
    array([1, 2, 3])
    """
    return np.array(args)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
```

``` title="tiny/__init__.py"
from .mat_math import to_numpy_arr

__version__ = "0.0.1"


__all__ = ["to_numpy_arr"]
```

I wanted to make 'to_numpy_arr' functionality available directly from the 'tiny' package.
This is done with the '\_\_all\_\_' list variable.  
'\_\_version\_\_' will be linked and available also in the metadata of the package (see below in 'setup.cfg').

I have a 'doctest' for the module. I have also added an "external" test.
This external test will be added to the repository yet will not be included in the package.

``` title="test.py"
import tiny


def test1():
    print("test1")
    assert tiny.to_numpy_arr(1, 7).sum() == 8
    print("test1 passed")


if __name__ == "__main__":
    test1()
```

We are almost there. We still need either 'setup.py' (the old way of packaging),
or 'setup.cfg' + 'pyproject.toml' (a newer way to package).
I've chosen the second way.

``` title="setup.cfg"
[metadata]
name = tiny
version = attr: tiny.__version__
author = Oren Zeev-Ben-Mordehai
author_email = zbenmo@gmail.com
url = https://github.com/zbenmo/tiny_package
description = for use in a tutorial
long_description = file: README.md
long_description_content_type = text/markdown
keywords = Reinforcement Learning, Framework, Integration
license_files = LICENSE.txt
classifiers =
    Intended Audience :: Developers
    Intended Audience :: Science/Research
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    License :: OSI Approved :: MIT License
    Topic :: Scientific/Engineering
    Topic :: Scientific/Engineering :: Artificial Intelligence

[options]
packages = find:
zip_safe = True
include_package_data = True
install_requires =
    numpy

[options.package_data]
* = README.md
```

``` title="pyproject.toml"
[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
```

I've issued the following command:

```
pip install -e .
```

This commands tells 'pip' to install the package from the current directory in "development" mode.

If you got an error:

```
ERROR: File "setup.py" not found. Directory cannot be installed in editable mode: /home/oren/projects/tiny_package
(A "pyproject.toml" file was found, but editable mode currently requires a setup.py based build.)
```

Issue: ```pip install -U pip```, and try again ```pip install -e .```.

I've verified my external test with:

```
python test.py
```

Note: 'requirements.txt' is not needed any more here. We could have ```pip uninstall numpy```, and ```pip install -e .``` would have brought 'numpy' again as it is a dependency of 'tiny' project. 'requirements.txt' can be removed from git if was previously added (here in the 'tiny_package' repository.). We do want to add to the repository 'test.py', 'setup.cfg', 'pyproject.toml', and the Python files.

To build the package, we can use ```pip install build``` and issue ```python -m build```.
to publish the build package for example to 'pypi.org' we can use ```pip install twine``` and issue something like ```python -m twine upload --repository pypi dist/*``` (we'll need an account for this on 'pypi.org').

We'll skip the build and the publishing. Instead we'll install the new 'tiny' package also in the other Python virtual environment used for playing with Flask.

If you wish you can first commit the changes to the 'tiny_package' repository.

Let's switch to the Python virtual environment used for the Flask experiments.
We'll introduce a new dependency, a one of the 'tiny' package.
Declaring the dependency should be done in 'requirements.txt' there.
We'll make another shortcut for now.

- While in the Python virtual environment of the Flask project, navigate to the directory with the 'tiny_package' repository.

- Make sure you __do not__ activate the Python virtual environment there but are still with the virtual environment from the Flask project.

- ```pip install -e .``` This will install the 'tiny' package now in the current Python virtual environment used for the Flask project.

In the Flask project, I've added the following "endpoint":

``` py
..
import tiny

..

@app.get('/try_tiny/<int:first>')
def try_tiny(first: int):
    ret = list(tiny.to_numpy_arr(first, 2 * first, 3 * first))
    return list(map(int, ret))
```

The code receives an int, 'first' and returns a "JSON" list with 'first', 'first' multiplied by 2, and 'first' multiplied by 3.

I needed to convert the 'numpy' array into a list, and the items to 'int' from 'numpy.int32' as the "jsonify" functionality does not know to work with 'numpy'.

If you are using someone's else package, say an Open Source that is maintained in the example on Github,
and you believe you've found a bug, you may attempt to solve it by:

- Fork the Github repository of the package.

- Clone (your) relevant Github repository into your laptop.

- ```pip install -e .``` in the just cloned repository (note you are using the Python virtual environment of your project).

- If all above succeeded you can now attempt to fix the bug.

- If you have a fix, add the changes and commit, then push to your Github repository, and open a PR.

- You now have to keep track of the status of that project / Python package. Your code is working, subject that the fix is present.
You currently have the fix only in your clone of the original repository. Till it is accepted and updated on pypi.org, you have to keep working with your own copy. This delays also the availability of your project / package for others.  
You do have the option to require the specific point of the package, from the commit in your repository. Read more on [Stack Overlow](https://stackoverflow.com/a/16584935/1614089).

## A few words on packages' versions and dependencies

Our original project for experimenting with 'Flask' did not need 'numpy'. Let's keep it like that.
The fact that 'tiny' brought with it 'numpy' is just fine.
If in a future version 'tiny' will drop that dependency or upgrade the requirement to a higher 'numpy' version,
that should not influence us.

In 'tiny' with just added a requirement to 'numpy' (any version). That is not a good practice. We've tested 'tiny' with a specific 'numpy' version, maybe with a previous version or with a future version, our code does not work?

It is a good practice to require the specific version we've used.
If I run ```pip freeze | grep numpy``` I get ```numpy==1.24.2```.
We should say that ```numpy >= 1.24.2, < 1.25``` should be okay.
We've allowed more 'numpy' versions than the one we've used. '1.24.3' should also be okay according to our specification.
There is a convention, that if a "breaking change" is introduced the version must be incremented in the second position.

Remember that those are conventions and bugs can still crawl in.
On the other hand, in many situations it is okay to be a bit "lazy" and just wait till someone complains.
When this happens, check with the user of your package what 'numpy' he/she have in their Python virtual environment.
Check yourself what happens when you have this 'numpy' version with your package, and decide what is the right remedy. 

What happens when your project needs ```numpy < 1.25``` while a dependencie of your project, say 'pandas' needs ```numpy >= 1.26```?
You'll have to investigate. Maybe you can allow also for 'numpy' version '1.26', potentially by modifying a little your code?
Maybe the dependency 'pandas' has a previous version that can live with ```numpy < 1.25``` and is still good for your project,
then just require that version of the dependency 'pandas', for example (fictional) ```pandas >= 2.3.0, < 2.3.6```. Sometimes it is more drastic and you'll need to break your project into two processes or use other packages. May the odds be ever in your favour.  

In some situations, as of regulatory requirements, you may be asked to list all the dependencies of your software (Open Source and other) and the versions used.
As far as I can tell, listing the top level of your dependencies is good enough (no need to follow dependencies of your dependencies, if I am not mistaken. Check that with your accompanying regulatory officer).

## Docker

The last thing I want to bring here is a little philosophical.
Most likely we'll all going to use Docker these days, that way or another.  
Does it mean that some of the mechanism above are redundant and we can decide not to make use of them?

My feeling is that it is a good thing to have all above mechanisms and also Docker.
Each mechnism helps us to "wrap" and "isolate" our development / deployment software in another layer of "trust". Each helps us achieve reproducability and reliability.

When you have a Docker image, the image may have some Python functionality before you join with your software, tools, and processes. By introducing a Python virtual environment, you know that your code shall be happy, while the other things that happen in the containers are as the designer of the image / container wanted.

You can give someone a Docker image, in which you've already installed the right Python packages and other dependencies. Then this user can run a container with your software and never worry about git repositories, Python packages, versions, dependencies, etc.  
You as the maintainer of the code, will most likely need from time to time to create a new version of the Docker image, and there you will be probably happier if you have the mechanisms above to keep your sanity.
