# This script is used for removing extra commas in "tableofSNP.csv"
# The working directory is same to "tableofSNP.csv" file
# The output file is tableofSNPs_deited.csv
# Usage:

sed -E 's/\"([0-9]+),([0-9]+)\"/\1\ \2/' tableofSNPs.csv | sed -E 's/\"([0-9]+),([0-9]+),([0-9]+)\"/\1\ \2\ \3/' | sed 's/ //g' > tableofSNPs_edited.csv

