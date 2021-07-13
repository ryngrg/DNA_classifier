from downloadData import download_all_data
from unzipAllGz import unzipAll
from parseSequence import parseAllFastqs
from trainingData import prepData

## Get data

samplesRange = (0, 4) # use first four samples only

# download files *.filt.fastq.gz
samples, files = download_all_data(samplesRange)
print(samples)
print(files)
# unzip *.filt.fastq.gz into *.filt.fastq
unzipAll(samples, files)
# parse and save *.filt.fastq as *.txt
parseAllFastqs(samples, files)
# store one hot vectors in X, Y
X, Y = prepData(samples, files)

## Machine learning part
# initialize neural net
# train
# test
