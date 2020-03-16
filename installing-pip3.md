# How to Install Pip3
Pip is a package management system that allows you to install Python packages. With pip, you can install packages from the [Python Package Index (PyPI)](https://pypi.org/) and other repositories.

In this guide, we will explain how to install `pip3` on Debian 10, Buster, using the apt package manager. We will also show you how to install and manage Python packages with pip3.

## Installing pip for Python3
Perform the following steps as a user with sudo privileges to install Pip for Python 3 on Debian 10:

**1.** Start by updating the package list :
```bash
$ sudo apt update
```

**2.** Install pip for Python 3 and all of its dependencies with the following command :
```bash
$ sudo apt install python3-pip
```

**3.** Print the pip3 version to verify the installation :
```bash
$ pip3 --version
```
The version number may be different, but it will look something like the one below :
```bash
Output
pip 18.1 from /usr/lib/python3/dist-packages/pip (python 3.7)
```

## Command Completion
pip comes with support for command line completion in bash, zsh and fish.

**1.** To setup for bash :
```bash
$ pip3 completion --bash >> ~/.profile
```
```bash
# pip bash completion start
_pip_completion()
{
    COMPREPLY=( $( COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   PIP_AUTO_COMPLETE=1 $1 ) )
}
complete -o default -F _pip_completion pip3
# pip bash completion end
```
> Output of this command `pip3 completion --bash` copy this to `~/.profile` or `~/.bashrc`.

## Using pip
In this section, we will talk about the basic pip commands. With pip, you can install packages from PyPI, version control, local projects, and from distribution files but in most cases, you will install packages from PyPI.

If you want to install a python module globally, you should prefer to install it as a package using the `apt` manager. Use pip to install python modules globally only if there is no package available.

Usually, you would use pip inside a [virtual environment](https://docs.python.org/3/library/venv.html) only. Python Virtual Environment allows you to install Python modules in an isolated location for a specific project, rather than being installed globally. This way you do not have to worry about affecting other Python projects.

Let’s say you want to install a package named `urllib3`, you can do that by issuing the following command :
```bash
$ pip install urllib3
```
> urllib3 is a powerful HTTP client for Python.

* Uninstalling a package :
```bash
$ pip uninstall package_name
```

* Searching packages from PyPI :
```bash
$ pip search "search_query"
```

* Listing installed packages :
```bash
$ pip list
```

* Listing outdated packages :
```bash
$ pip list --outdated
```

## Conclusion
We have shown you how to install pip on your Debian system and how to manage Python packages using pip. For more information about pip, check the [pip user guide](https://pip.pypa.io/en/stable/user_guide/).