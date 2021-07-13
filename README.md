# DNA_classifier
## Ultimate objective: Use DNA sequence to determine population group of person

### As of 2021/07/13 1151hrs:
* **master.py** - main file of the project, run this. This calls everything. Should have no complex code.
* **trainingData.py** - reads .bin files and stores data in one hot vectors
* **parseSequence.py** - reads the data in all unzipped data files (.filt.fastq) and encodes the raw sequences in a binary file (.bin)
* **unzipAllGz.py** - unzips all .gz files
* **downloadData.py** - downloads all sequence reads (.filt.fastq.gz) of all samples and stores it into ./phase3_data/sampleName/
* **samples_population.csv** - CSV file summarizing the samples of 3202 people, their genders, population code and the superpopulation code.
* **next to do**:
  * implement RNN model
  * train model for subsets of data seperately and store trained weights
  * combine the weights trained on different subsets
