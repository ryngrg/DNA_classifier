from downloadData import download_all_data
from unzipAllGz import unzipAll
from parseSequence import parseAllFastqs
from trainingData import prepData

## Get all data
# download files *.filt.fastq.gz
samples, files = download_all_data()
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
