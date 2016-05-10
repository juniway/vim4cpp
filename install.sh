#!/usr/bash

# Install vim plugins and set vimrc
# packages that will be installed
# vim
# dos2unix
# ctags

# vim-Vundle
# vim-YouCompleteMe
# vim-airline
# vim-nerdtree
# vim-taglist

# config files:
# _vimrc
# .ycm_extra_conf.py

workdir=$(pwd)
VUNDLE_GIT=https://github.com/gmarik/Vundle.vim.git
YCM_GIT=https://github.com/Valloric/YouCompleteMe.git

set -e
sudo pacman -Syy

dos2unix --version || sudo pacman -S dos2unix
ctags --version || sudo pacman -S ctags
locate --version || sudo pacman -s mlocate

cp ./_vimrc $HOME/_vimrc
chmod 0666 $HOME/_vimrc
cp ./.ycm_extra_conf.py $HOME/

VIM_PATH=$HOME/.vim
VUNDLE_PATH=${VIM_PATH}/bundle/Vundle.vim

git clone ${VUNDLE_GIT} ${VUNDLE_PATH}
git clone ${YCM_GIT} $HOME/.vim/bundle/

vim +BundleInstall -c quitall

test_python_clang()
{
    sudo ldconfig
    echo 'import clang.cindex; s=clang.cindex.conf.lib' | python
}

install_python_clang_from_source()
{
    echo "python-clang does not exit"
    sudo pacman -S python-clang && \
    sudo pacman -S libclang-3.6-dev || echo "Error: failed to install libclang-3.6-dev"
}

build_llvm_clang()
{
    llvm_clang_dir=$HOME/llvm-clang
    sudo ${work_dir}/install_clang.sh $llvm_clang_dir
}

test_python_clang || install_python_clang_from_source

# compile YouCompleteMe
ycm_path=${vim_path}/bundle/youcompleteme
cd ${ycm_path}
./install.sh --clang-completer --system-libclang

test_python_clang || echo "Error: python-clang install error, please check libclang.so and cindex.py!";exit
echo 'vim-env is ok, good luck!'
