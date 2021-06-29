sample = "HG00637"
filename = "SRR070520"

f = open("./phase3_data/" + sample + '/' + filename + ".filt.fastq", 'r')

outfile = open("./phase3_data/" + sample + '/' + filename + ".txt", 'w')

useNext = False

while True:
    text = f.readline()
    if len(text) == 0:
        break
    if text[0] == '+':
        useNext = False
    if useNext and (text[0] != '@'):
        outfile.write(text)
    if text[0] == '@':
        useNext = True

f.close()
outfile.close()
