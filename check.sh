#!/bin/bash

cp -f userdict.txt dict.txt
bib2dict references.bib >>dict.txt

textidote --check en_UK --output html --dict dict.txt \
    overfail2.tex >check.html
