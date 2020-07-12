# Install miniconda

## Download the installer
Run the following command in your terminal:
```bash
# for MacOS users
CONDA_INSTALLER=Miniconda3-latest-MacOSX-x86_64.sh
# for Ubuntu users
CONDA_INSTALLER=Miniconda3-latest-Linux-x86_64.sh

wget -q https://repo.anaconda.com/miniconda/${CONDA_INSTALLER}
```
You can find the download links at https://docs.conda.io/en/latest/miniconda.html#macosx-installers

## Install miniconda
```bash
bash ${CONDA_INSTALLER} -b -p ~/miniconda3
```
After successful installation, you can remove the installer
```bash
rm -f ${CONDA_INSTALLER}
```

## Create a conda env
Active the conda environment
```bash
. ~/miniconda3/etc/profile.d/conda.sh
```
Create a Python3.7 environment
```bash
conda create -y -n python3.7 python=3.7.7
```
To automatically activate the environment when you open a new shell, add the following lines to
`~/.bashrc` (for Ubuntu users) and `~/.zshrc` (for MacOS Catalina users).
```bash
. ~/miniconda3/etc/profile.d/conda.sh
conda activate python3.7
```
You can do this via command line
```bash
# replace ~/.bashrc with ~/.zshrc for MacOS
echo ". ~/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate python3.7" >> ~/.bashrc
```
Open another tab in terminal, you should see a `(python3.7)` prefix in your prompt. 
Type `which python3` in your terminal, you should see the path like 
```bash
/home/<your username>/miniconda3/envs/python3.7/bin/python3
```
