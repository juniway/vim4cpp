# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
source ~/.fishmarks/marks.fish
set tacklebox_path ~/.tackle
set tacklebox_modules virtualfish virtualhooks
set tacklebox_plugins extract grc pip python up
set tacklebox_theme entropy
# set tacklebox_theme urdh
source ~/.tacklebox/tacklebox.fish

#set -gx PATH /opt/llvm/bin $PATH
set -gx LD_LIBRARY_PATH /usr/local/lib:/opt/llvm/lib $LD_LIBRARY_PATH:
# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
# HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
# shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
# HISTSIZE=1000
# HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
# shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)

# set variable identifying the chroot you work in (used in the prompt below)

# set a fancy prompt (non-color, unless we know we "want" color)

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

# some more ls aliases
alias ll 'ls -alF'
alias la 'ls -A'
#alias l 'ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
# alias alert 'notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
alias ll 'ls -l'
alias c11 'gcc -std=c11 -Wall -O2 -pedantic'
alias g11 'g++ -std=c++14 -Wall -O0 -pedantic'
alias tmux 'tmux -2'
# alias nv='nvim'
alias cl++ 'clang++ -std=c++11 -Wall -O0 -pedantic'
alias py3 'python3'
alias tn 'tmuxinator'
alias gbs 'gitbook serve'
alias gb 'gitbook'

if test -f /home/ub15ax/.autojump/share/autojump/autojump.fish; . /home/ub15ax/.autojump/share/autojump/autojump.fish; end

set -gx EDITOR '/usr/bin/vim'
set -gx CHEATCOLORS 'true'
set -gx ANT_HOME '/usr/local/apache-ant-1.9.6'
set -gx ZOOKEEPER_HOME '/usr/local/zookeeper-3.4.8'
set -gx CLASSPATH '.:/home/ub15ax/tmp/cloudsim-3.0.3/jars/*:/home/ub15ax/tmp/cloudsim-3.0.3/examples'
set -gx SOURCEPATH '.:/home/ub15ax/tmp/cloudsim-3.0.3/sources:examples'
set -gx MONGO_HOME '/usr/local/mongodb-linux-x86_64-3.2.7'
set -gx HA_HOME '/usr/local/haproxy'
set -gx GOROOT '/usr/local/go'
set -gx GOPATH '/media/sf_go'
set -g -x PATH {$HA_HOME}/sbin {$GOPATH}/bin {$GOROOT}/bin {$ANT_HOME}/bin {$ZOOKEEPER_HOME}/bin {$MONGO_HOME}/bin /usr/local/node-v4.6.0-linux-x64/bin /opt/llvm/bin $PATH ~/bin

function reload
    source ~/.config/fish/config.fish
end

function subl
    open -a "Sublime Text.app" $argv
end

function ll
    ls -lhG $argv
end

function la
    ls -lahG $argv
end

function lsd
    ls -d */
end

# opam configuration
source /home/ub15ax/.opam/opam-init/init.fish > /dev/null 2> /dev/null; or true
