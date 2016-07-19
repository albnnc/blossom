<p align="center">
    <img width="200" src="https://raw.githubusercontent.com/alexquot/blossom/master/blossom.png"/>
</p>

*Let your files blossom*

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2e8c82eeed594cdd844db0eca0ea2557)](https://www.codacy.com/app/alexquot/blossom?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=alexquot/blossom&amp;utm_campaign=Badge_Grade)

## What Is This?

The majority of us use various configuration files to setup our systems.
Because of the big number of those it's really hard and unaesthetic to
leave your [dotfiles](http://dotfiles.github.io/) as they are in home
directory or wherever else. So, here is where dotfiles managers
come. With them you can organize files as you want.

Blossom is a single-file script which allows you to clean up directories
and install files by creating symbolic links. It's easy as `git clone $repo
&& cd dotfiles && python blossom.py -l`. Most likely you are going to use
it to install your dotfiles; actually, there is no difference to Blossom
which files to perform with. The main goals of this project are:

* provide a tool which does its own job good;
* maximize simplicity of the code and usage;
* minimize the code base.

## Setup

First of all, you need to decide where to store your configuration files.
Usually this folder called *~/dotfiles*. Then you need to add the blossom
configuration file in it.

#### Configuration File

In this file you can specify script's behaviour: what directories should be
cleaned up and how exectly to link your configs. This file has to be in
the dotfiles directory (by default, *~/dotfiles*) and named **blossom.cfg**.

Config has simple structure divided into two sections: `[clean]` and
`[link]`. First one should contain a list of the directories to clean up
(absolute path), one per line. Each chosen directory will be cleaned from
all symbolic links. Second section has to list symlinks &mdash; targets
(relative to dotfiles) and destinations (absolute). You can read more
about the allowed syntax on python's configparser module
[documentation](https://docs.python.org/3/library/configparser.html).

Example blossom.cfg:

```ini
[clean]
~
~/.config

[link]
vim/vim         = ~/.vim
vim/vimrc       = ~/.vimrc
misc/bashrc     = ~/.bashrc
xorg/xinitrc    = ~/.xinitrc
xorg/xresources = ~/.Xresources
```

#### Command-Line Options

When running script those options are allowed:

```
-h, --help    show the help message and exit
-c, --clean   perform cleanup
-l, --link    perform linking
-f, --force   remove existing destination files
-d D, --dir D specify working directory (default is ~/dotfiles)
```

## Troubleshooting

##### Script fails with the 'failed to create symlink' error message!

In this situation the most common are those cases:

* The destination of symlink is exists already, so you can remove it
manually or just add the `--force` flag.

* You're trying to put a symbolic link in the nonexistent directory.
For example, you may want Blossom to place your *~/dotfiles/compton*
folder to *~/.config*, but the second directory doesn't exist. The only
workaround is just to create this folder manually.

##### Script execution does nothing!

If you are executing sctipt with the right flags and getting no result,
most likely you're using custom directory, so the script is getting nothing
from the *&lt;default directory&gt;/blossom.cfg*. You can specify custom
working directory with the `--dir` option.

## Contact

You can contact the developer via e-mail &mdash; alexquot@gmail.com.

## License

Copyright (c) 2016 Alex Quot. This software released under the MIT License.
