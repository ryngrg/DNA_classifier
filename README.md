# DNA_classifier
## Ultimate objective: Use DNA sequence to determine population group of person

### As of 2021/07/05 1859hrs:
* samples_population.csv - CSV file summarizing the samples of 2607 people, their genders, population code and the population name.
* downloadData.py - downloads all sequence reads (.filt.fastq.gz) of all samples and stores it into ./phase3_data/sampleName/
* parseSequence.py - reads the data in the one unzipped data file (.filt.fastq) and stores the raw sequence from it in a plain text file (.txt)
* next to do:
  * include unzipping process in code
  * make code parse all files of one sample
  * make code parse files for all samples
