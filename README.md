

# SimpleCrawler: A Single Domain Sitemap Generator

Given a root Web Page URL that uses either the http:// or https:// protocol, SimpleCrawler will recursively traverse
all the connected Web Pages that are in the same domain as the root Web Page URL.
The output consists of a list of recursively connected Web pages. For each page listed, three additional lists
are printed : one for all the connected pages in the same domain, one for all the connected pages that are
not in the same domain, and one for all the images that are on the page.

## Getting Started

Python 3 is required. You can check this by simply running:

```
$ python --version
```

You should get some output like 3.6.2.
If you do not have Python, please install the latest 3.x version
from python.org.

There are several ways to install SimpleCrawler. Method one is to check out the project and install
all the application's dependencies. Method two is to download the source files into a diectory,
create a virtual environment, and use the tools in the newly created  virtualenv
to load the required Python libraries automatically. Another method uses a combination of methid one and method two.

This document addresses method two, and so virtualenv needs to be installed on your system.

Prior to veryfying if virtualenv is installed, you’ll need to make sure you have pip available.
You can check this by running:

```
$ pip --version
```

Pip can be installed in a number of ways, including using sudo, homebrew, etc.
If pip is not installed , please refer to the documentation for your platform.
For example, on a MAC, pip can be installed as follows:

```
$ sudo easy_install pip
```

To verify that virtualenv is installed, run the command

```
$ virtualenv --version
```

If virtualenv is not installed, install it as follows:

```
$ pip install --user virtualenv
```


### Installing

Download the project files from github into a project directory.

Open a new terminal window and  cd to the project directory.
Install a virtual environment as follows

```
$ virtualenv env
```

This will create new directory in the project called env.
Now activate this virtual environment for the tereminal window by entering the following command

```
$ source env/bin/activate
```

This will update the environment for the terminal window by adding VIRTUAL_ENV= and adding ../env/bin
the head of the PATH.

Now install the required packages into the newly created virtual environment

```
$ python3 -m pip install -r requirements.txt
```

This will insure that the libraries specified in the requirements.txt file are properly
installed in the virtual environment


## Running the tests

After the virtual environment  has been set up the installation can be verified by running
the project tests in the top level project directory as follows

```
$ python3 -m unittest
```

This will run a battery of tests. The last test will scrape the website wiprodigital.com and
output a sitemap report.


## Running the application

To run the SimpleCrawler application enter the following command in the top level project directory

```
$ python3 run.py -r'ValidUrl'
```

where 'ValidUrl' is a valid url address with a protocol of either http:// or https;//