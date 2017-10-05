# How to compile

In this tutorial we assume that you have an empty directory `~/FOO` and we are going to install everything therein.

## clone the dependencies

```
cd ~/FOO
git clone https;//github.com/LaurentClaessens/mazhe
git clone https://github.com/LaurentClaessens/pytex
git clone https://github.com/LaurentClaessens/exocorr
git clone https://github.com/LaurentClaessens/latexparser
```

For the last one, you have to write 'latexparser', and not 'LaTeXparser' as the url in github shows. I created this repository before to read the [pep8](https://www.python.org/dev/peps/pep-0008/). I'm really sorry about that.


## Make it available for bash, python and latex

- The directory `~/FOO/latexparser` must be available for the python's import mechanism.
- The directory `~/FOO/pytex` must be available for bash.
- The directory `~/FOO/exocorr` must be available for LaTeX's usepackage mechanism.

The simplest is to append the following in `~/.bashrc` :
```
export PYTHONPATH=$PYTHONPATH:~/docu/
PATH=$PATH:~/docu/pytex
```




