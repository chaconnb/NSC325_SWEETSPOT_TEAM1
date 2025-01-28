# NSC325_GROUP1

## Contents


## Project Summary

## Developer Quick Start

### Prerequisites

- VSCode (IDE)
- UV (Python Development Tool)
- Git (and GitHub)

#### VSCode/UV install for Windows

1. Install WSL and VSCode by following these instructions. https://code.visualstudio.com/docs/remote/wsl
    - Install the WSL with the Ubuntu distribution

2. Install UV on the WSL side (Do not install it on the Windows side)

    Open an WSL terminal (Ubuntu), navigate to the `$HOME` directory, run the install script. 
    ```console
    cd ~
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

#### VSCode/UV install for MacOS and Linux

1. Install VSCode for your OS. https://code.visualstudio.com/Download

2. Install UV (from the terminal)
    ```console
    cd ~
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

Install git (from the terminal)

### Install Git 

It is likely that `git` is already installed on your system. To check if you have git install, run this command in your terminal: 
```console
git --version
```
<p align='center'>
<img src="https://learn.microsoft.com/nl-nl/windows/wsl/media/git-versions.gif" style="width:600px;height:auto;">
</p>
If you do not get a version message, install it by 
with your systems installers: 

(For WSL/Linux with an Ubuntu/debian distribution)
```console
sudo apt install git-all 
``` 

(For MacOS, If you don't have brew, install it https://brew.sh/)
```console
brew install git 
```

### Set up the Project Folder

Open a terminal. Create a "projects" directory from your `$HOME` directory. 
```console
cd ~
mkdir projects/
``` 


### Clone the Project Repository

First, navigate to your projects folder 
```console
cd ~/projects/ 
``` 

From the browser, navigate to the GitHub repository for your project. Clone the project 
by clicking the green "Code" button. Select "HTTPS" and copy the line in the text box. 

<p align="center">
<img src="./docs/imgs/screenshot-clone-repo.png" width='400x'>
</p>

On your terminal, navigate to the projects folder and clone the repository. 

```console
cd ~/projects/
git clone https://github.com/chaconnb/NSC325_GROUP1.git # this is an example
```

Navigate to the newly cloned repository and open VSCode from the repository root folder. 
```console
cd ~/projects/<your-repo-name>
code . 
``` 

### Set up Development Environment

With UV installed, you can set up the development environment by running this 
command in the project root directory: 
```console 
uv sync
``` 
This will set up a Python virtual environment and install any dependencies listed in 
the `pyproject.toml`. To activate the virtual environment on your terminal, run: 
```console
source .venv/bin/activate 
``` 

### Setting up a local Jupyter Notebook
You can use VSCode to run Jupyter notebooks. Read the VSCode docs for more information. 
https://code.visualstudio.com/docs/datascience/jupyter-notebooks 

You will need to set up the kernel. We suggest you use the local virtual environment we 
set up with UV. Follow these instructions on how to use your virtual environment in your 

<p align='center'>
<img src ="./docs/imgs/screenshot-select-kernel-source.png" width='600x'>
</p>

Jupyter notebook. VSCode should find and identify the project's virtual environment folder 
and recommend it (i.e., it should be `.venv/bin/python`)

<p align='center'>
<img src="./docs/imgs/screenshot-suggested-kernel.png" width='600x'> 
</p>
