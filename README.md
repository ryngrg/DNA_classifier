# DNA_classifier
## Ultimate objective: Use DNA sequence to determine population group of person

### As of 2021/07/06 0019hrs:
* master.py - main file of the project, run this. This calls everything. Should have no complex code.
* parseSequence.py - reads the data in all unzipped data files (.filt.fastq) and stores the raw sequences in a plain text file (.txt)
* downloadData.py - downloads all sequence reads (.filt.fastq.gz) of all samples and stores it into ./phase3_data/sampleName/
* samples_population.csv - CSV file summarizing the samples of 2607 people, their genders, population code and the population name.
* next to do:
  * include unzipping process in code
  * make code parse all files of one sample
  * make code parse files for all samples
