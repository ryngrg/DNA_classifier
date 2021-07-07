# DNA_classifier
## Ultimate objective: Use DNA sequence to determine population group of person

### As of 2021/07/07 0004hrs:
* master.py - main file of the project, run this. This calls everything. Should have no complex code.
* parseSequence.py - reads the data in all unzipped data files (.filt.fastq) and stores the raw sequences in a plain text file (.txt)
* unzipAllGz.py - unzips all .gz files
* downloadData.py - downloads all sequence reads (.filt.fastq.gz) of all samples and stores it into ./phase3_data/sampleName/
* samples_population.csv - CSV file summarizing the samples of 2607 people, their genders, population code and the population name.
* next to do:
  * include unzipping process in code
  * have meeting with professor to discuss machine learning part
  * implement machine learning algorithm
  * find way to store data for running final code
