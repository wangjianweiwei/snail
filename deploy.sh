#!/bin/zsh
source ~/.zshrc

nvm use v18.15.0
yarn build
scp -r dist/* root@8.152.160.172:/var/www/snail