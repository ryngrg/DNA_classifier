# DNA_classifier
## Ultimate objective: Use DNA sequence to determine population group of person

### As of 2021/07/03:
* samples_population.csv - CSV file summarizing the samples of 2607 people, their genders, population code and the population name.
* downloadData.py - downloads one hardcoded zipped sequence data file (.filt.fastq.gz) of one sample and stores it into ./phase3_data/sampleID/
* parseSequence.py - reads the data in the one unzipped data file (.filt.fastq) and stores the raw sequence from it in a plain text file (.txt)
* next to do:
  * include unzipping process in code
  * make code download all files of one sample
  * make code download files for all samples
