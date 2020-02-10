gedit-wordcount-plugin
======================

A gedit plugin which adds a Label to the status bar with the active documents 
linecount, where a line defined as '\n'
wordcount, where a word is definied as ``r"[a-zA-Z0-9]+[a-zA-Z0-9\-']*\s?"``
chractercount.

Installation
------------

Either run the script ``./install.sh`` provided or:

Copy ``wordcount.plugin`` and ``wordcount.py`` to ``~/.local/share/gedit/plugins`` then activate from Gedit's plugins dialog.

The plugin is a fork from https://github.com/footley/gedit-wordcount-plugin which supports in addition linecount and charactercount. 

## Usage

Install the plugin, run the Gedit and activate the plugin. From then on whenever you type a character you'll see at the bottom panel a summary of lines, words and characters in the file.
