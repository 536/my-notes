# pyenv

<https://github.com/pyenv/pyenv>


## Installation

### pre-conditions

<https://github.com/pyenv/pyenv/wiki#suggested-build-environment>

### Install

<https://github.com/pyenv/pyenv-installer#install>

```bash
curl https://pyenv.run | bash

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

source ~/.bashrc

pyenv --version
```

### Upgrade

<https://github.com/pyenv/pyenv-installer#update>

```bash
pyenv update
```

### Uninstall

<https://github.com/pyenv/pyenv-installer#uninstall>

```bash
rm -fr ~/.pyenv

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

exec $SHELL
```

## Usage

![Usage](https://github.com/pyenv/pyenv/raw/master/terminal_output.png)
