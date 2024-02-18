gedit-wordcount-plugin
======================

A gedit plugin that adds a label to the status bar with the active document's line count, where a line defined as ``\n``,
wordcount, where a word is defined as ``r"\w+[\w\-'’]*\s?"``, and character count.

Installation
------------

Either run the script ``./install.sh`` provided or:

Copy ``wordcount.plugin`` and ``wordcount.py`` to ``~/.local/share/gedit/plugins`` then activate from Gedit's plugins dialog.

The plugin is a fork from https://github.com/javadr-forky/gedit-wordcount-plugin but displays the word count for only the selected portion when anything is highlighted.

https://github.com/javadr-forky/gedit-wordcount-plugin is a fork of https://github.com/footley/gedit-wordcount-plugin but also supports line count, character count and unicode words. 

## Usage

Install the plugin, run the Gedit and activate the plugin. From then on whenever you type a character you'll see at the bottom panel a summary of lines, words and characters included in the file.
