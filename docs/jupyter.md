# Install Jupyter Notebook
Make sure you have installed conda and activated the Python3.7 environment before proceeding.

## Install Jupyter
```
pip install jupyter
```

## Generate Jupyter configuration file
```bash
mkdir -p ~/.jupyter/
jupyter notebook --generate-config
```

## Create a password for Jupyter
```bash 
jupyter notebook password
```
You will need to enter the password later when you open Jupyter in browser.

## Edit Jupyter config file
Choose your favorite editor to edit the file `~/.jupyter/jupyter_notebook_config.py`.
Use `gedit` if you have not learnt to use `vim` or `emacs`. 
```bash
gedit ~/.jupyter/jupyter_notebook_config.py
```
Change the following configs. You will need to remove the leading '#' to uncomment the lines first.
```bash
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.allow_remote_access = True
```

## Configure key mapping
```bash
mkdir -p ~/.jupyter/nbconfig/
```
Open `~/.jupyter/nbconfig/notebook.json` and add the following content
```json
{
  "command": {
    "unbind": [
      "ctrl-enter"
    ],
    "bind": {
      "cmd-enter": "jupyter-notebook:run-cell"
    }
  },
  "edit": {
    "unbind": [
      "ctrl-enter"
    ],
    "bind": {
      "cmd-enter": "jupyter-notebook:run-cell"
    }
  }
}
```
Save and exit.

## Start Jupyter
Now you can start Jupyter notebook by typing
```bash
jupyter notebook
```
Control + Click (or Command + Click on MacOS) on the link in the console to open your browser.

## (Optional) Start Jupyter from host machine
If you want to open the jupyter notebook outside the VM from your host machine, do the following
1. Change network from NAT to Bridge. 

    Shutdown the VM, in settings -> Network, change "Attached to" from "NAT" to "Bridged Adapter". 
2. Start the VM, install `ifconfig` and find the ip address of the bridge network
    ```bash
    sudo apt install -y ifconfig
    ifconfig | grep inet
    ```
    You should see something like the following in the output
    ```bash
    inet 192.168.1.191  netmask ...
    ```
    Write down the ip address right after "inet". In my case it is 192.168.1.191. 
3. Start Jupyter again

    To access Jupyter from the host machine, replace the hostname of the URL with this IP. 
    In my case the URL is http://192.168.1.191:8888/.
