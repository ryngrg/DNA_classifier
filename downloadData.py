import requests

url_base = "http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/"

sample = "HG00637"
filename = "SRR070520"

url = url_base + sample + "/sequence_read/" + filename + ".filt.fastq.gz"

myfile = requests.get(url)

open("./phase3_data/" + sample + '/' + filename + ".filt.fastq.gz", 'wb').write(myfile.content)
