from downloadData import download_all_data
from unzipAllGz import unzipAll
from parseSequence import parseAllFastqs
from ML import ml_main

## Get data

samplesRange = (0, 30) # Eg. use first thirty samples only

# download files *.filt.fastq.gz
samples, files = download_all_data(samplesRange)
# unzip *.filt.fastq.gz into *.filt.fastq
unzipAll(samples, files)
# parse and save *.filt.fastq as *.bin
parseAllFastqs(samples, files)

## Machine learning part
ml_main()
