#!/bin/bash

if [ ! -d ~/.local/share/gedit ]; then
	mkdir ~/.local/share/gedit
fi

if [ ! -d ~/.local/share/gedit/plugins ]; then
	mkdir ~/.local/share/gedit/plugins
fi

if [ -f ~/.local/share/gedit/plugins/wordcount.py ]; then 
    echo remove any old version
    rm ~/.local/share/gedit/plugins/wordcount.*
fi 

echo copy plugin files
cp wordcount.plugin ~/.local/share/gedit/plugins/
cp wordcount.py ~/.local/share/gedit/plugins/
