#!/bin/bash

# Source files

dest=./data-model
source=./source
inorganicFormula=${source}/inorganic-formulas.txt
inorganicName=${source}/inorganic-names.txt
organicFormulas=${source}/organic-formulas.txt
organicNames=${source}/organic-names.txt

# Check if user provided an argument to name the folder

if [ $1 ]; then
    dest=./$1
fi

# Directories

formulaInorganicOrganic=${dest}/formula-inorganic-organic
formulaName=${dest}/formula-name
nameInorganicOrganic=${dest}/name-inorganic-organic

# Check if $dest is a directory, if not, make it

if [ ! -d $dest ]; then
    mkdir ${dest}
    echo "${dest} directory created"
fi

# Checks if the folder already exists

if [ -d ${formulaInorganicOrganic} ] \
     || [ -d ${formulaName} ] \
     || [ -d ${nameInorganicOrganic} ]; then
    echo "This folder already contains data. Please, select another folder" 
    exit 1
fi

# Make directories

mkdir ${formulaInorganicOrganic}
mkdir ${formulaName}
mkdir ${nameInorganicOrganic}


## Test and train directories

# Formula: Inorganic - Organic

mkdir ${formulaInorganicOrganic}/test
mkdir ${formulaInorganicOrganic}/train

mkdir ${formulaInorganicOrganic}/test/organic
mkdir ${formulaInorganicOrganic}/test/inorganic
mkdir ${formulaInorganicOrganic}/train/organic
mkdir ${formulaInorganicOrganic}/train/inorganic


# Formula - Name

mkdir ${formulaName}/test
mkdir ${formulaName}/train

mkdir ${formulaName}/test/name
mkdir ${formulaName}/test/formula
mkdir ${formulaName}/train/name
mkdir ${formulaName}/train/formula


# Name: Inorganic - Organic

mkdir ${nameInorganicOrganic}/test
mkdir ${nameInorganicOrganic}/train

mkdir ${nameInorganicOrganic}/test/organic
mkdir ${nameInorganicOrganic}/test/inorganic
mkdir ${nameInorganicOrganic}/train/organic
mkdir ${nameInorganicOrganic}/train/inorganic

# Lines of files

organicNamesLines=`cat ${organicNames} | wc -l`
organicFormulasLines=`cat ${organicFormulas} | wc -l`
inorganicFormulasLines=`cat ${inorganicFormula} | wc -l`
inorganicNamesLines=`cat ${inorganicName} | wc -l`
namesLines=`cat ${source}/names.txt | wc -l`
formulasLines=`cat ${source}/formulas.txt | wc -l`

########## Formula: Inorganic - Organic

# Organic files

head -$(( $organicFormulasLines / 10 )) ${organicFormulas} > \
               ${formulaInorganicOrganic}/test/organic-10%.txt

split -l 1 ${formulaInorganicOrganic}/test/organic-10%.txt \
           ${formulaInorganicOrganic}/test/organic/ \
           --additional-suffix=.txt

tail -$(( $organicFormulasLines * 9 / 10 )) ${organicFormulas} > \
               ${formulaInorganicOrganic}/train/organic-90%.txt

split -l 1 ${formulaInorganicOrganic}/train/organic-90%.txt \
            ${formulaInorganicOrganic}/train/organic/ \
            --additional-suffix=.txt

# Inorganic files

head -$(( $inorganicFormulasLines / 10 )) ${inorganicFormula} > \
               ${formulaInorganicOrganic}/test/inorganic-10%.txt

split -l 1 ${formulaInorganicOrganic}/test/inorganic-10%.txt \
           ${formulaInorganicOrganic}/test/inorganic/ \
           --additional-suffix=.txt

tail -$(( $inorganicFormulasLines * 9 / 10 )) ${inorganicFormula} > \
               ${formulaInorganicOrganic}/train/inorganic-90%.txt

split -l 1 ${formulaInorganicOrganic}/train/inorganic-90%.txt \
           ${formulaInorganicOrganic}/train/inorganic/ \
           --additional-suffix=.txt

########## Formula - Name

# Formula files

head -$(( $formulasLines / 10 )) ${source}/formulas.txt > \
               ${formulaName}/test/formulas-10%.txt

split -l 1 ${formulaName}/test/formulas-10%.txt \
           ${formulaName}/test/formula/ \
           --additional-suffix=.txt

tail -$(( $formulasLines * 9 / 10 )) ${source}/formulas.txt > \
               ${formulaName}/train/formulas-90%.txt

split -l 1 ${formulaName}/train/formulas-90%.txt \
            ${formulaName}/train/formula/ \
            --additional-suffix=.txt

# Name files

head -$(( $namesLines / 10 )) ${source}/names.txt > \
               ${formulaName}/test/names-10%.txt

split -l 1 ${formulaName}/test/names-10%.txt \
           ${formulaName}/test/name/ \
           --additional-suffix=.txt

tail -$(( $namesLines * 9 / 10 )) ${source}/names.txt > \
               ${formulaName}/train/names-90%.txt

split -l 1 ${formulaName}/train/names-90%.txt \
           ${formulaName}/train/name/ \
           --additional-suffix=.txt


########## Name: Inorganic - Organic

# Organic files

head -$(( $organicNamesLines / 10 )) ${organicNames} > \
               ${nameInorganicOrganic}/test/organic-10%.txt

split -l 1 ${nameInorganicOrganic}/test/organic-10%.txt \
           ${nameInorganicOrganic}/test/organic/ \
           --additional-suffix=.txt

tail -$(( $organicNamesLines * 9 / 10 )) ${organicNames} > \
               ${nameInorganicOrganic}/train/organic-90%.txt

split -l 1 ${nameInorganicOrganic}/train/organic-90%.txt \
            ${nameInorganicOrganic}/train/organic/ \
            --additional-suffix=.txt

# Inorganic files

head -$(( $inorganicNamesLines / 10 )) ${inorganicName} > \
               ${nameInorganicOrganic}/test/inorganic-10%.txt

split -l 1 ${nameInorganicOrganic}/test/inorganic-10%.txt \
           ${nameInorganicOrganic}/test/inorganic/ \
           --additional-suffix=.txt

tail -$(( $inorganicNamesLines * 9 / 10 )) ${inorganicName} > \
               ${nameInorganicOrganic}/train/inorganic-90%.txt

split -l 1 ${nameInorganicOrganic}/train/inorganic-90%.txt \
           ${nameInorganicOrganic}/train/inorganic/ \
           --additional-suffix=.txt
