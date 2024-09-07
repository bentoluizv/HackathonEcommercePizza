# Hackaton Grupo 7

Hackaton Grupo 7

## Configurando o ambiente de desenvolvimento

### Instale Python 3.12.3

Você pode baixar python diretamente do site oficial mas é altamente recomendado usar um gerenciador de versão como o [pyenv](https://github.com/pyenv/pyenv) e o [pyenv-win](https://https://github.com/pyenv-win/pyenv-win).

Com o pyenv instalado você poderá instalar a versão do python adequada da seguinte forma:

#### Linux e Windows

```bash

# Instalando o pyenv
curl https://pyenv.run | bash

# Configurando o shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
exec "$SHELL"

pyenv version

# Instalando python 3.12.3

pyenv install 3.12.3
pyenv local 3.12.3


#######################################
#                                     #
###### UTILIZE PIP OU O POETRY ########
#   Instalando venv e dependências    #
#######################################

# PIP
python3 -m venv hackenv

. hackenv/bin/activate

pip install --upgrade pip
pip install .

# POETRY
sudo apt update
sudo apt install pipx

pipx ensurepath
pipx install poetry

poetry shell
poetry install


´´´


```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

pyenv --version

# Instalando python 3.12.3

pyenv install 3.12.3
pyenv local 3.12.3

#######################################
#                                     #
###### UTILIZE PIP OU O POETRY ########
#   Instalando venv e dependências    #
#######################################

# PIP

pip install --upgrade pip
pip install .

# POETRY
py -m pip install --user -U pipx
.\pipx.exe ensurepath

pipx install poetry
poetry shell
poetry install


### Clone o projeto diretamente do Github

link para o [Repositório](https://github.com/bentoluizv/HackathonEcommercePizza)!!

