# Michael Package

## Instructions for packaging local python projects
Using the instructions from python [here](https://packaging.python.org/tutorials/packaging-projects/)

Get the latest version of pip
```
python -m pip install --upgrade pip
```

### Project structure
```
michaelpackage/
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
├── src/
│   └── basketball/
│       ├── __init__.py
│       └── team.py
└── tests/
```

### Create a distribution
Get the latest version of build
```
python -m pip install --upgrade build
```

In the *michaelpackage* directory (i.e. the same directory that has the *pyproject.toml* file) run the following to create 2 files (a tar.gz file AND a .whl file) in the *dist* directory
```
python -m build
```
Here is an example of the output
```
Python-Packaging\michaelpackage> python -m build
* Creating venv isolated environment...
* Installing packages in isolated environment... (setuptools>=42, wheel)
* Getting dependencies for sdist...

...
...
...

adding 'michael_package-0.0.1.dist-info/LICENSE'
adding 'michael_package-0.0.1.dist-info/METADATA'
adding 'michael_package-0.0.1.dist-info/WHEEL'
adding 'michael_package-0.0.1.dist-info/top_level.txt'
adding 'michael_package-0.0.1.dist-info/RECORD'
removing build\bdist.win-amd64\wheel
Successfully built michael-package-0.0.1.tar.gz and michael_package-0.0.1-py3-none-any.whl
```

### Install package locally
```
python -m pip install wheel
```

Before installing package locally
```
Python-Packaging\michaelpackage> pip list
Package    Version
---------- -----------
build      0.6.0.post1
colorama   0.4.4
packaging  21.0
pep517     0.11.0
pip        21.2.4
pyparsing  2.4.7
selenium   3.141.0
setuptools 49.2.1
tomli      1.2.1
urllib3    1.26.3
wheel      0.37.0
```

To directly install the wheel
```
python -m pip install <filepath to .whl file>
```

Here is an example of the output
```
Python-Packaging\michaelpackage> pip install Python-Packaging\michaelpackage\dist\michael_package-0.0.1-py3-none-any.whl
Processing python-packaging\michaelpackage\dist\michael_package-0.0.1-py3-none-any.whl
Installing collected packages: michael-package
Successfully installed michael-package-0.0.1
```

### Verify and Test
```
Python-Packaging\michaelpackage> pip list
Package         Version
--------------- -----------
build           0.6.0.post1
colorama        0.4.4
michael-package 0.0.1   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
packaging       21.0
pep517          0.11.0
pip             21.2.4
pyparsing       2.4.7
selenium        3.141.0
setuptools      49.2.1
tomli           1.2.1
urllib3         1.26.3
wheel           0.37.0
```

Here is a test script called *test.py* located in a different directory from *michaelpackage* with the following code
```
from basketball import team

print(team.get_roster())
```
Since the custom package, *michael-package*, was installed, the *basketball* module is available system-wide

Here is an example of the output
```
Desktop> python .\test.py
['LeBron', 'Kawhi', 'Giannis', 'Steph', 'Klay']
```
