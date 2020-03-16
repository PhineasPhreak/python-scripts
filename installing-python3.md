# Installing Python 3.8 on Debian 10
Building Python 3.8 on Debian is a relatively straightforward process and will only take a few minutes.

**1.** Start by installing the packages necessary to build Python source :
```bash
$ sudo apt update
$ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev curl
```

**2.** Download the latest release’s source code from the [Python download page](https://www.python.org/downloads/source/) with wget or [curl](https://linuxize.com/post/curl-command-examples/). At the time of writing this article, the latest release is `3.8.2` :
```bash
$ curl -O https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz
```

**3.** When the download is complete, extract the tarball :
```bash
$ tar -xf Python-3.8.2.tar.xz
```

**4.** Navigate to the Python source directory and run the `configure` script :
```bash
$ cd Python-3.8.2
$ ./configure --enable-optimizations
```
The script performs a number of checks to make sure all of the dependencies on your system are present. </br>
The `--enable-optimizations` option will optimize the Python binary by running multiple tests, which will make the build process slower.

**5.** Run `make` to start the build process :
```bash
$ make -j 4
```
Modify the `-j` to correspond to the number of cores in your processor. You can find the number by typing `nproc`.

**6.** Once the build is done, install the Python binaries by running the following command as a user with sudo access :
```bash
$ sudo make altinstall
```
Do not use the standard `make install` as it will overwrite the default system `python3` binary.

**7.** At this point, Python 3.8 is installed on your Debian system and ready to be used. You can verify it by typing :
```bash
$ python3.8 --version
```
```bash
Output
Python 3.8.2
```

# Creating a Virtual Environment
Python virtual environment is a self-contained directory tree that includes a Python installation and a number of additional packages. It allows you to install Python modules in an isolated location for a specific project, rather than being installed globally. This way, you do not have to worry about affecting other Python projects.

In this example, we’ll create a new Python 3.8 project called `my_app` inside the user home directory.

* First, create the project directory and switch to it :
```bash
$ mkdir ~/my_app && cd ~/my_app
```

* From inside the project root run the following command to create a virtual environment named `my_app_venv` :
```bash
python3.8 -m venv my_app_venv
```

* Activate the environment :
```bash
$ source my_app_venv/bin/activate
```
Once activated, the shell prompt will be prefixed with the name of the environment. Starting with Python 3.4, when creating virtual environments pip, the package manager for Python is installed by default.

* Within the virtual environment, you can use `pip` instead of `pip3.8` and `python` instead of `python3.8` :
```bash
(my_app_venv) $ python -v
```
```bash
Output
Python 3.8.1
```
Once you are done with your work to `deactivate` the environment, type deactivate, and you will return to your normal shell.
```bash
(my_app_venv) $ deactivate
```

# Conclusion
We have shown you how to install Python 3.8 on Debian 10. You can now create a virtual environment and start developing your Python 3 projects.
