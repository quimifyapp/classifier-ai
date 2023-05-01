#!/bin/bash

# Data location:

source_directory=./source

inorganic_formulas_source=${source_directory}/inorganic-formulas.txt
organic_formulas_source=${source_directory}/organic-formulas.txt
inorganic_names_source=${source_directory}/inorganic-names.txt
organic_names_source=${source_directory}/organic-names.txt

# Result location:

destination_directory=./split

if [ ! -d $destination_directory ]; then # Didn't exist already
  mkdir ${destination_directory}
  echo "Created '${destination_directory}' directory."
fi

formula_name_directory=${destination_directory}/formula-name
formula_inorganic_organic_directory=${destination_directory}/formula-inorganic-organic
name_inorganic_organic_directory=${destination_directory}/name-inorganic-organic

if [ -d ${formula_inorganic_organic_directory} ] || [ -d ${formula_name_directory} ] ||
  [ -d ${name_inorganic_organic_directory} ]; then # Already existed
  echo "Error: directory '${destination_directory}' seems to contain data."
  exit 1
fi

# Make directories:

mkdir ${formula_name_directory}

mkdir ${formula_name_directory}/train
mkdir ${formula_name_directory}/train/formula
mkdir ${formula_name_directory}/train/name

mkdir ${formula_name_directory}/test
mkdir ${formula_name_directory}/test/formula
mkdir ${formula_name_directory}/test/name

mkdir ${formula_inorganic_organic_directory}

mkdir ${formula_inorganic_organic_directory}/train
mkdir ${formula_inorganic_organic_directory}/train/inorganic
mkdir ${formula_inorganic_organic_directory}/train/organic

mkdir ${formula_inorganic_organic_directory}/test
mkdir ${formula_inorganic_organic_directory}/test/inorganic
mkdir ${formula_inorganic_organic_directory}/test/organic

mkdir ${name_inorganic_organic_directory}

mkdir ${name_inorganic_organic_directory}/train
mkdir ${name_inorganic_organic_directory}/train/inorganic
mkdir ${name_inorganic_organic_directory}/train/organic

mkdir ${name_inorganic_organic_directory}/test
mkdir ${name_inorganic_organic_directory}/test/inorganic
mkdir ${name_inorganic_organic_directory}/test/organic

# Line count of each file:

formulas_count=$(cat ${source_directory}/formulas.txt | wc -l)
names_count=$(cat ${source_directory}/names.txt | wc -l)
inorganic_formulas_count=$(cat ${inorganic_formulas_source} | wc -l)
organic_formulas_count=$(cat ${organic_formulas_source} | wc -l)
inorganic_names_count=$(cat ${inorganic_names_source} | wc -l)
organic_names_count=$(cat ${organic_names_source} | wc -l)

# In 'formula-name':

# Formulas:

head -$(($formulas_count / 10)) ${source_directory}/formulas.txt > \
  ${formula_name_directory}/test/formulas-10%.txt

split -l 1 ${formula_name_directory}/test/formulas-10%.txt \
  ${formula_name_directory}/test/formula/ \
  --additional-suffix=.txt

tail -$(($formulas_count * 9 / 10)) ${source_directory}/formulas.txt > \
  ${formula_name_directory}/train/formulas-90%.txt

split -l 1 ${formula_name_directory}/train/formulas-90%.txt \
  ${formula_name_directory}/train/formula/ \
  --additional-suffix=.txt

# Names:

head -$(($names_count / 10)) ${source_directory}/names.txt > \
  ${formula_name_directory}/test/names-10%.txt

split -l 1 ${formula_name_directory}/test/names-10%.txt \
  ${formula_name_directory}/test/name/ \
  --additional-suffix=.txt

tail -$(($names_count * 9 / 10)) ${source_directory}/names.txt > \
  ${formula_name_directory}/train/names-90%.txt

split -l 1 ${formula_name_directory}/train/names-90%.txt \
  ${formula_name_directory}/train/name/ \
  --additional-suffix=.txt

# In 'formula-inorganic-organic':

# Inorganic formulas:

head -$(($inorganic_formulas_count / 10)) ${inorganic_formulas_source} > \
  ${formula_inorganic_organic_directory}/test/inorganic-10%.txt

split -l 1 ${formula_inorganic_organic_directory}/test/inorganic-10%.txt \
  ${formula_inorganic_organic_directory}/test/inorganic/ \
  --additional-suffix=.txt

tail -$(($inorganic_formulas_count * 9 / 10)) ${inorganic_formulas_source} > \
  ${formula_inorganic_organic_directory}/train/inorganic-90%.txt

split -l 1 ${formula_inorganic_organic_directory}/train/inorganic-90%.txt \
  ${formula_inorganic_organic_directory}/train/inorganic/ \
  --additional-suffix=.txt

# Organic formulas:

head -$(($organic_formulas_count / 10)) ${organic_formulas_source} > \
  ${formula_inorganic_organic_directory}/test/organic-10%.txt

split -l 1 ${formula_inorganic_organic_directory}/test/organic-10%.txt \
  ${formula_inorganic_organic_directory}/test/organic/ \
  --additional-suffix=.txt

tail -$(($organic_formulas_count * 9 / 10)) ${organic_formulas_source} > \
  ${formula_inorganic_organic_directory}/train/organic-90%.txt

split -l 1 ${formula_inorganic_organic_directory}/train/organic-90%.txt \
  ${formula_inorganic_organic_directory}/train/organic/ \
  --additional-suffix=.txt

# In 'name-inorganic-organic':

# Inorganic names:

head -$(($inorganic_names_count / 10)) ${inorganic_names_source} > \
  ${name_inorganic_organic_directory}/test/inorganic-10%.txt

split -l 1 ${name_inorganic_organic_directory}/test/inorganic-10%.txt \
  ${name_inorganic_organic_directory}/test/inorganic/ \
  --additional-suffix=.txt

tail -$(($inorganic_names_count * 9 / 10)) ${inorganic_names_source} > \
  ${name_inorganic_organic_directory}/train/inorganic-90%.txt

split -l 1 ${name_inorganic_organic_directory}/train/inorganic-90%.txt \
  ${name_inorganic_organic_directory}/train/inorganic/ \
  --additional-suffix=.txt

# Organic names:

head -$(($organic_names_count / 10)) ${organic_names_source} > \
  ${name_inorganic_organic_directory}/test/organic-10%.txt

split -l 1 ${name_inorganic_organic_directory}/test/organic-10%.txt \
  ${name_inorganic_organic_directory}/test/organic/ \
  --additional-suffix=.txt

tail -$(($organic_names_count * 9 / 10)) ${organic_names_source} > \
  ${name_inorganic_organic_directory}/train/organic-90%.txt

split -l 1 ${name_inorganic_organic_directory}/train/organic-90%.txt \
  ${name_inorganic_organic_directory}/train/organic/ \
  --additional-suffix=.txt
