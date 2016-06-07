# This file is NOT licensed under the GPLv3, which is the license for the rest
# of YouCompleteMe.
#
# Here's the license text for this file:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import os
import ycm_core
import re

_debug = 1
msys2='E:/usr/msys2'
llvm='E:/usr/LLVM'

# These are the compilation flags that will be used in case there's no
# compilation database set (by default, one is not set).
# CHANGE THIS LIST OF FLAGS. YES, THIS IS THE DROID YOU HAVE BEEN LOOKING FOR.
flags = [
'-Wall',
'-Wextra',
'-Werror',
#'-Wc++98-compat',
'-Wno-long-long',
'-Wno-variadic-macros',
'-fexceptions',
'-DNDEBUG',
# You 100% do NOT need -DUSE_CLANG_COMPLETER in your flags; only the YCM
# source code needs it.
'-DUSE_CLANG_COMPLETER',
# THIS IS IMPORTANT! Without a "-std=<something>" flag, clang won't know which
# language to use when compiling headers. So it will guess. Badly. So C++
# headers will be compiled as C headers. You don't want that so ALWAYS specify
# a "-std=<something>".
# For a C project, you would set this to something like 'c99' instead of
# 'c++11'.
'-fno-ms-compatibility',
'-std=c++14',
# ...and the same thing goes for the magic -x option which specifies the
# language that the files to be compiled are written in. This is mostly
# relevant for c++ headers.
# For a C project, you would set this to 'c' instead of 'c++'.
'-x',
'c++',
'-isystem',
llvm + '/include',
'-isystem',
llvm + '/tools/clang/include',
'-isystem',
msys2 + '/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.2.0/include',
'-isystem',
msys2 + '/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.2.0/../../../../include',
'-isystem',
msys2 + '/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.2.0/include-fixed',
'-isystem',
msys2 + '/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/5.2.0/../../../../x86_64-w64-mingw32/include',
'-isystem',
msys2 + '/mingw64/lib/gcc/../../include/c++/5.2.0',
'-isystem',
msys2 + '/mingw64/lib/gcc/../../include/c++/5.2.0/x86_64-w64-mingw32',
'-isystem',
msys2 + '/mingw64/lib/gcc/../../include/c++/5.2.0/backward',

'-include',
msys2 + '/mingw64/lib/gcc/../../include/c++/5.2.0/cstddef',
]

def Log(msg):
    if not _debug:
        return 

    f = open("c:/ycm.log", 'a+')
    f.write(msg + '\n')
    f.close()

# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
#
# You can get CMake to generate this file for you by adding:
#   set( CMAKE_EXPORT_COMPILE_COMMANDS 1 )
# to your CMakeLists.txt file.
#
# Most projects will NOT need to set this to anything; you can just change the
# 'flags' list of compilation flags. Notice that YCM itself uses that approach.
compilation_database_folder = ''

if os.path.exists( compilation_database_folder ):
  database = ycm_core.CompilationDatabase( compilation_database_folder )
else:
  database = None

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]

def DirectoryOfThisScript():
  Log("__file__ is %s" % __file__)
  Log("__file__ abspath is %s" % os.path.abspath( __file__ ))
  return os.path.dirname( os.path.abspath( __file__ ) )


def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  Log(working_directory)
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    if make_next_absolute:
      make_next_absolute = False
      if len(flag) > 1 and flag[1] != ':':
        new_flags.append(working_directory + '/' + flag)
        continue

    if flag in path_flags:
      make_next_absolute = True

    new_flags.append(flag)

  return new_flags


def IsHeaderFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.h', '.hxx', '.hpp', '.hh' ]


def GetCompilationInfoForFile( filename ):
  # The compilation_commands.json file generated by CMake does not have entries
  # for header files. So we do our best by asking the db for flags for a
  # corresponding source file, if any. If one exists, the flags for that file
  # should be good enough.
  if IsHeaderFile( filename ):
    basename = os.path.splitext( filename )[ 0 ]
    for extension in SOURCE_EXTENSIONS:
      replacement_file = basename + extension
      if os.path.exists( replacement_file ):
        compilation_info = database.GetCompilationInfoForFile(
          replacement_file )
        if compilation_info.compiler_flags_:
          return compilation_info
    return None
  return database.GetCompilationInfoForFile( filename )


## Add includes flags from the Makefile.
#
makefile_list = ['Makefile', 'makefile', '../Makefile', '../makefile']

def ExtractIncludesFromMakefile(path):
    Log('ExtractIncludesFromMakefile')
    include_flags = set()
    cmd = 'cd %s && make -Bn' % path
    Log('Make command:\n%s' % cmd);
    make_result = os.popen(cmd, 'r').read()
    Log('Make result:\n%s' % make_result);
    matchs = re.findall(r'-I\s*[^\s$]+', make_result)
    for m in matchs:
        include_path = m[2:].strip()
        if not os.path.isabs(include_path):
            include_path = os.path.join(path, include_path)
        include_flags.add(include_path)

    return include_flags

def MakefileIncludesFlags(filename):
    Log('MakefileIncludesFlags')
    mk_flags = []
    path = os.path.split(filename)[0]
    for mk in makefile_list:
        abs_mk = os.path.join(path, mk) 
        if not os.path.isfile(abs_mk):
            continue

        include_flags = ExtractIncludesFromMakefile(os.path.split(abs_mk)[0])
        for flag in include_flags:
            mk_flags.append('-I')
            mk_flags.append(flag)

        break

    Log(str(mk_flags))
    return mk_flags


def FlagsForFile( filename, **kwargs ):
  Log('-' * 30)
  Log("Process file: %s" % filename)
  Log("WorkDirectory is: %s" % os.getcwd())
  if database:
    Log('database case:')
    # Bear in mind that compilation_info.compiler_flags_ does NOT return a
    # python list, but a "list-like" StringVec object
    compilation_info = GetCompilationInfoForFile( filename )
    if not compilation_info:
      return None

    final_flags = MakeRelativePathsInFlagsAbsolute(
      compilation_info.compiler_flags_,
      compilation_info.compiler_working_dir_ )

    # NOTE: This is just for YouCompleteMe; it's highly likely that your project
    # does NOT need to remove the stdlib flag. DO NOT USE THIS IN YOUR
    # ycm_extra_conf IF YOU'RE NOT 100% SURE YOU NEED IT.
    try:
      final_flags.remove( '-stdlib=libc++' )
    except ValueError:
      pass
  else:
    Log('no database case:')
    relative_to = os.path.dirname(filename)
    final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  final_flags.extend(MakefileIncludesFlags(filename))
  final_flags.extend(['-I', os.path.dirname(filename)])

  Log(str(final_flags))

  return {
    'flags': final_flags,
    'do_cache': True
  }

