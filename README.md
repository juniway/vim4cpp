# Cppenv: complete vim environment for coding C++
***
**source:** [https://github.com/juniway/vim4cpp](http://github.com/juniway/vim4cpp)

## Overview ##
This project aims to build a whole vim envoronment for cpp programming, it provides a well tuned vim settings and plugins which provide an IDE-like coding experience under vim editor.

This project has two parts:

- **Vim installation**
- **Vim plugins for coding C++**
  
Vim environment includes some tools below:

 - g++
 - git
 - cmake
 - python2
    
Plugins includes:

- Vundle
- YouCompleteMe
- syntastic
- auto-pairs
- NerdTree
- vim-airline
- taglist
- cscope
- tagbar 
- CtrlP 
- vim-gitgutter
- vim-fugitive 
- ultisnips
- vim-snippet 
- Cpp11-Syntax-Support
- nerdcommenter
- powerline/fonts
- vim-colorschemes
- gundo.vim

    
You can run the script `autoconf/install` to install all of the vim environment I provide. It will automatically install all of the tools and plugins above. If you are in China, it takes only 4 minutes.

## Install ##

```shell
$ git clone https://github.com/juniway/vim4cpp
$ cd vim4cpp
$ ./install.sh
```

The script will install `_vimrc`, `.ycm_extra_conf.py` and other plugins in `~/.vim`.

An auto command that will recoginze cpp file look like this:
- `au BufNewFile,BufRead *.h,*.hpp,*.inl,*.ipp,*.cpp,*.c,*.cc,*.go execute cppenv#infect()`

## AutoComplete ##

`vim4cpp` provides auto complete for cpp(and other languages like c, python, etc), supported by `YouCompleteMe`.

**Auto complete brackets:**
This feature supports `class`, `struct`, `union`, `function`, `lambda` and `C++ coroutine lambda`.
The `C++ coroutine lambda` refers to [https://github.com/yyzybb537/cpp_features](https://github.com/yyzybb537/cpp_features)
***

![brackets](http://i.imgur.com/RVNcD8o.gif)

**Auto complete class-methods definitions:**
This feature supports all of combination `class` and `method` types below:

- `normal class`
- `template class`

**and**

- `normal method`
- `template method`
- `static method`
- `static template method`

![defclass](http://imgur.com/npFkaoj.gif)

## Jump File ##

`cppenv` provides some shortcut keys for jump between c/c++ `header file` and c/c++ `source file`.

- `gs`
- `gns`
- `gS`
- `gvs`
- `gvns`

Use `gs` can jump between `header` and `source` if there were in a same folder. If the two files have the same parent folder, you can use `gns` to jump between there. If the two files were not in a same folder and have not the same parent folder, the `gs` cannot work, here, you can use `gS`. `gS` will use `locate` command to find the files in all of your file-system, and show the results in `quickfix` window when the results more than one.

`gvs`, `gvns` are as same as `gs`, `gns` nearly. Difference was the shortcut key including `v` will split the window vertical, and show the other file buffer on right.

## Vim environment ##

If you install the complete vim environment, the `_vimrc` taken effect. It will give you a lot of shortcut key to boost your coding efficiency.

#### Plugins

`YouCompleteMe` provides syntax complete and check.

![YouCompleteMe GIF demo](http://i.imgur.com/0OP4ood.gif)

`NerdTree` provides show the files tree.

![NerdTree](http://img.hoop8.com/attachments/1511/4341900695509.gif)

`TagList` provides show the functions in current file.

![taglist](http://img.hoop8.com/attachments/1511/6051900695509.gif)

#### ShortcutKey

I used `;` as the vim leader charactor, so seted below:

- **`;b`**  jump to begin of line. as `^`
- **`;e`**  jump to end of line. as `$`
- **`;w`**  save to file. as `:w`
- **`;q`**  quit the buffer. as `:quit` 
- **`;Q`**  quit the vim. as `:quitall`
- **`;hw`** jump to left window. as `<C-w>h`
- **`;jw`** jump to under window. as `<C-w>j`
- **`;kw`** jump to over window. as `<C-w>k`
- **`;lw`** jump to right window. as `<C-w>l`
- **`;/`**  cancel highlight. as `:nohls<CR>`
- **`;`** as `"`, e.g. you can use `;ay` to copy selection into `a` register, and use `;ap` to paste `a` register words into cursor position.

- **`F3`** toggle the `NerdTree` window, show the files tree.
- **`F4`** static syntax check current source file.

#### Jump

- **`gy`** jump to the word on the cursor definition or declaration. as call the YCM method `GoToDefinitionElseDeclaration`.
- **`gY`** show the word on the cursor definition or declaration on right window. 
- **`gl`** jump to last buffer. as `:b#<CR>`
- **`gL`** jump to last buffer and show current buffer on right window


#### TabPage

- **`<C-h>`** jump to previous tabpage. as `:tabprevious<CR>`
- **`<C-l>`** jump to next tabpage. as `:tabnext<CR>`

#### Build and Run

- **`F7`** build current file, output `out.exe`
- **`F5`** build and run. output `out.exe`
- **`F8`** build and run with libboost. output `out.exe`

#### Complete By Snippet

- **`<C-j>`** trigge the snippet.

Support snippet trigger list below:

- **`time`** the output for e.g:  `2015-11-20 23:56:18`
- **`date`** output for e.g: `2015-11-20`
- **`namespace <name>`**

	e.g.

	input:

		namespace ucorf

	output:

        namespace ucorf
    	{
    
    	} //namespace ucorf

- **`GNU License <name>`** Make gnu license copyright header in source file.


	![license](http://i.imgur.com/C2cN20p.gif)

- **`def <class name>`** First, you must save your class definition. Then, input `def <class name>`, will output all method definitions of the class.
