# DNA_classifier
## Ultimate objective: Use DNA sequence to determine the superpopulation group of a person

### As of 2021/08/13 1150hrs:
* **master.py** - Main file of the project, run this. This calls everything. Should have no complex code.
* **ML.py** - This file contains the LSTM creation and training function.
* **trainingData.py** - Contains generator function: Reads .bin files and stores data in one hot vectors.
* **parseSequence.py** - Reads the data in all unzipped data files (.filt.fastq) and encodes the raw sequences in a binary file (.bin)
* **unzipAllGz.py** - Unzips all .gz files
* **downloadData.py** - Downloads all sequence reads (.filt.fastq.gz) of all samples and stores it into ./phase3_data/sampleName/
* **samples_population.csv** - CSV file listing the samples and the superpopulation code.
* **./models/92files10epochs/** - contains model trained for 10 epochs on first 800 bases from 92 files (13 of which were skipped as they were not listed in samples_population.csv). Training took just a few seconds to complete
* **next to do**:
  * train model for subsets of data seperately and store trained weights
  * combine the weights trained on different subsets
