# Install node.js

<https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl#install-nvm-nodejs-and-npm>

```bash
sudo apt-get install curl
# https://github.com/nvm-sh/nvm#install--update-script
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

nvm ls
nvm install --lts
# nvm install node

nvm use --lts
# nvm use node
# nvm use v8.2.1
```
