#!/bin/sh
if [ ! -f modelchecking.zip ]; then
    wget http://www.open.ou.nl/jke/games/modelchecking.zip
fi
mkdir -p modelchecking && unzip -nj modelchecking.zip "modelchecking/games/*" -d modelchecking
if [ ! -f equivchecking.zip ]; then
    wget http://www.open.ou.nl/jke/games/equivchecking.zip
fi
mkdir -p equivchecking && unzip -nj equivchecking.zip "equivchecking/games/*" -d equivchecking
