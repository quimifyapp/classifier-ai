#!/bin/bash

# Source files

dest=$1
source=./source
inorganicFormula=$source/inorganic-formulas.txt
inorganicName=$source/inorganic-names.txt
organicFormulas=$source/organic-formulas.txt
organicNames=$source/organic-names.txt

# Directories

formulaInorganicOrganic=./formula-inorganic-organic
formulaName=./formula-name
nameInorganicOrganic=./name-inorganic-organic

# Check if $dest is a directory, if not, make it

if [ ! -d $dest ]; then
    mkdir ${dest}
    echo "${dest} directory created"
else
    echo "${dest} will be emptied"
    rm -rf ${dest}/*
fi

# Make directories

mkdir ${dest}/${formulaInorganicOrganic}
mkdir ${dest}/${formulaName}
mkdir ${dest}/${nameInorganicOrganic}

# Test and train directories

mkdir ${dest}/${formulaInorganicOrganic}/test
mkdir ${dest}/${formulaInorganicOrganic}/train

mkdir ${dest}/${formulaInorganicOrganic}/test/organic
mkdir ${dest}/${formulaInorganicOrganic}/test/inorganic
mkdir ${dest}/${formulaInorganicOrganic}/train/organic
mkdir ${dest}/${formulaInorganicOrganic}/train/inorganic

mkdir ${dest}/${formulaName}/test
mkdir ${dest}/${formulaName}/train

mkdir ${dest}/${nameInorganicOrganic}/test
mkdir ${dest}/${nameInorganicOrganic}/train

# Lines of files

organicNamesLines=`cat ${source}/organic-names.txt | wc -l`
organicFormulasLines=`cat ${source}/organic-formulas.txt | wc -l`
inorganicFormulasLines=`cat ${source}/inorganic-formulas.txt | wc -l`
inorganicNamesLines=`cat ${source}/inorganic-names.txt | wc -l`

# Formula Inorganic - Organic

# Organic files

head -$(( $organicFormulasLines / 10 )) ${source}/organic-formulas.txt > \
               ${dest}/${formulaInorganicOrganic}/test/organic-10%.txt

split -l 1 ${dest}/${formulaInorganicOrganic}/test/organic-10%.txt \
           ${dest}/${formulaInorganicOrganic}/test/organic/ \
           --additional-suffix=.txt

head -$(( $organicFormulasLines * 9 / 10 )) ${source}/organic-formulas.txt > \
               ${dest}/${formulaInorganicOrganic}/train/organic-90%.txt

split -l 1 ${dest}/${formulaInorganicOrganic}/train/organic-90%.txt \
            ${dest}/${formulaInorganicOrganic}/train/organic/ \
            --additional-suffix=.txt

# Inorganic files

tail -$(( $inorganicFormulasLines / 10 )) ${source}/inorganic-formulas.txt > \
               ${dest}/${formulaInorganicOrganic}/test/inorganic-10%.txt

split -l 1 ${dest}/${formulaInorganicOrganic}/test/inorganic-10%.txt \
           ${dest}/${formulaInorganicOrganic}/test/inorganic/ \
           --additional-suffix=.txt

tail -$(( $inorganicFormulasLines * 9 / 10 )) ${source}/inorganic-formulas.txt > \
               ${dest}/${formulaInorganicOrganic}/train/inorganic-90%.txt

split -l 1 ${dest}/${formulaInorganicOrganic}/train/inorganic-90%.txt \
           ${dest}/${formulaInorganicOrganic}/train/inorganic/ \
           --additional-suffix=.txt