if test -f ~/.fishmarks/marks.fish;
    source ~/.fishmarks/marks.fish;
end

set tacklebox_path ~/.tackle
set tacklebox_modules virtualfish virtualhooks
set tacklebox_plugins extract grc pip python up
set tacklebox_theme entropy
# set tacklebox_theme urdh

if test -f ~/.tacklebox/tacklebox.fish;
    source ~/.tacklebox/tacklebox.fish;
end

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

if test -f ~/.autojump/share/autojump/autojump.fish;
    source ~/.autojump/share/autojump/autojump.fish;
end

if test -f ~/.config/fish/functions/aliases.fish;
    source ~/.config/fish/functions/aliases.fish;
end

#set -gx LLVM_HOME /opt/llvm
set -gx LD_LIBRARY_PATH /usr/local/lib:/opt/llvm/lib $LD_LIBRARY_PATH:
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

# opam
source /home/ub15ax/.opam/opam-init/init.fish > /dev/null 2> /dev/null; or true
