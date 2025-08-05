#!/bin/zsh
source ~/.zshrc

nvm use v18.20.8
yarn install
yarn build
scp -r dist/* root@8.152.160.172:/var/www/snail