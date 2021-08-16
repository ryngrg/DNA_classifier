import os
from trainingData import get_filenames

def stats_main():
    f = open("stats.csv", "w")
    samples, all_files = get_filenames()
    for i in range(len(samples)):
        sample = samples[i]
        for file in all_files[i]:
            text = writeData(sample, file)
            f.write(text)
    f.close()

def writeData(sample, file):
    text = sample + ", " + file + ", " + get_y_sample(sample) + "\n"
    return text

def get_y_sample(sample):
    """This function returns the superpopulation group of a sample
    encoded as a one-hot vector
    """
    f = open("./samples_population.csv")
    f.readline()
    while True:
        row = f.readline()
        if len(row) == 0:
            break
        (samp, gen, pop, supop) = row.split(',')
        if samp == sample:
            sp = supop.strip()
            break
    f.close()
    try:
        sp
    except:
        return "unknown"
    return sp

stats_main()
