# EEng Course Preparation

Software we will be using during the course:

1. Anaconda Python distribution: https://www.anaconda.com/products/distribution#Downloads
1. notepad++ Text Editor (for Windows users only): https://notepad-plus-plus.org/
1. LTspice: https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html
1. LibreOffice: https://www.libreoffice.org/download/download-libreoffice/ 


We will use several special Python packages. The following list is not comprehensive:

* jupyterlab
* numpy
* scipy
* matplotlib
* pandas
* ipywidgets


## git 

We use git to provide the course material. You should familiarize yourself with git. A short introduction on how to use git is given [here](git.md).

## Conda Environments  

In Python software development often the concept of _environments_ is used. Environments are  fully separated Python installations. An environment consists of a combination of Python packages with specific version numbers including the Python interpreter itself. Separate environment variables and configuration files can also be provided. In fact the separated environments are individual independent directory sub-trees on the file system. The developer can activate an environment and work with the particular software versions installed in the environment. 

The Anaconda Python distribution provides its own envrironment management and software installation system. The name of the command line interface (the command to be called on a terminal window prompt) is `conda`.

For more information see the [**conda-cheatsheet.pdf**](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

**Create a new Anaconda environment. Do NOT install the packages in the base environment!**

The following steps explain how to set up a new conda environment and to install software into it. It is demonstrated how **Jupyter-Lab** can be started in this environment. Environment setup as well as software installation can be performed with command line or with the Anaconda Navigator.

Please consult the very useful conda cheat sheet:<br>
https://kapeli.com/cheat_sheets/Conda.docset/Contents/Resources/Documents/index

Some more helpful information on environments in Jupyter:<br>
http://nero-docs.stanford.edu/jupyter-customEnv.html

## Create a New Conda Environment

**On Windows:** Open an **Anaconda Powershell Prompt** (Start -> Anaconda3 -> Anaconda Powershell Prompt). 

**Other operating systems:** Open a terminal. 

On the command line prompt you should see an indicator which Python environment is currently active, e.g. `(base) PS C:\Users\me`

The token `(base)` shows the active environment.

The fastest way to create the necessary conda environment named `eeng` for this course is:

```
conda create -c conda-forge -n eeng python=3 jupyterlab numpy scipy matplotlib pandas ipywidgets bqplot pyserial
```

This command installs packages from the **conda-forge** software 'channel'. A channel is a online software source, a huge repository providing the software packages for installation.

After successful creation **activate** the environment and start **jupyter-lab** from within the environment.

```
conda activate eeng

jupyter-lab
```

