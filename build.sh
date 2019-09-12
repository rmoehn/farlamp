set -e

BUILD_P=build
SOURCE_NAME=supamp-reamp

mkdir -p $BUILD_P

grep -v '^ *%' references.bib >$BUILD_P/pandoc-references.bib

pandoc $SOURCE_NAME.md \
    --bibliography $BUILD_P/pandoc-references.bib --filter pandoc-citeproc \
    --csl=frontiers.csl \
    --include-in-header preamble.tex \
    -f markdown+yaml_metadata_block+simple_tables \
    -t latex -s -o $BUILD_P/$SOURCE_NAME.tex

cd $BUILD_P
xelatex -interaction=nonstopmode $SOURCE_NAME.tex
cd -

cp $BUILD_P/$SOURCE_NAME.pdf .
