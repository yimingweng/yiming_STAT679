# This script is used to do A-T exchange in tableofSNPs.csv file
# The working directory is same as tableofSNPs.csv
# The output will be written in the same directory as "tableofSNPs_ATextrange.csv"
# Usage:

sed -E 's/A/a/g' tableofSNPs.csv | sed -E 's/T/t/g' | sed -E 's/a/T/g' | sed -E 's/t/A/g' > tableofSNPs_ATextrange.csv
