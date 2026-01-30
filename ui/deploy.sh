#!/bin/zsh
source ~/.zshrc

nvm use v20.19.6
yarn install
yarn build
scp -r dist/* root@8.152.160.172:/var/www/snail