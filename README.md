# DNA_classifier
## Ultimate objective: Use DNA sequence to determine population group of person

### As of 2021/07/17 2037hrs:
* **master.py** - Main file of the project, run this. This calls everything. Should have no complex code.
* **ML.py** - This file contains the LSTM training algorithm.
* **trainingData.py** - Contains generator function: Reads .bin files and stores data in one hot vectors.
* **parseSequence.py** - Reads the data in all unzipped data files (.filt.fastq) and encodes the raw sequences in a binary file (.bin)
* **unzipAllGz.py** - Unzips all .gz files
* **downloadData.py** - Downloads all sequence reads (.filt.fastq.gz) of all samples and stores it into ./phase3_data/sampleName/
* **samples_population.csv** - CSV file summarizing the samples of 3202 people, their genders, population code and the superpopulation code.
* **next to do**:
  * define training data generator function in trainingData.py
  * train model for subsets of data seperately and store trained weights
  * combine the weights trained on different subsets
