import numpy as np
import os

def trainDataGenerator():
    """This function gives a generator containing 1 file at a time.
    It yields the sequence, superpopulation as one-hot vectors.
    """
    samples, all_files = get_filenames()
    for i in range(len(samples)):
        sample = samples[i]
        for file in all_files[i]:
            yield prepData(sample, file)

def get_filenames():
    """This function looks in the data directory and returns lists
    of all samples and their files available.
    """
    datadir = "./phase3_data/"
    samples = os.listdir(datadir)
    all_files = []
    for i in range(len(samples)):
        sampfiles = []
        datadir = "./phase3_data/" + samples[i]
        files = os.listdir(datadir)
        for file in files:
            if file.endswith(".bin"):
                sampfiles += [file]
        all_files += [sampfiles]
    return samples, all_files

def prepData(sample, file):
    """This function converts a file's contents into a
    numpy array of one-hot vectors.
    """
    try:
        f = open("./phase3_data/" + sample + "/" + file, 'rb')
    except:
        print("[Error]: Could not access file:", file, "for sample:", sample)
        return None
    decoding = [(1, 0, 0, 0),
                (0, 1, 0, 0),
                (0, 0, 1, 0),
                (0, 0, 0, 1)]
    raw = list(f.read())
    f.close()
    ohvs = []
    for t in range(len(raw)):
        base = (int)(raw[t] / 4**3)
        ohvs += [decoding[base]]
        raw[t] %= (4**3)
        base = (int)(raw[t] / 4**2)
        ohvs += [decoding[base]]
        raw[t] %= (4**2)
        base = (int)(raw[t] / 4**1)
        ohvs += [decoding[base]]
        raw[t] %= (4**1)
        base = (int)(raw[t])
        ohvs += [decoding[base]]

    X = np.array([ohvs])
    Y = np.array([get_y_sample(sample)])
    print(sample, file, "\n\tX shape =", X.shape)
    print("\tY =", Y)
    return X, Y

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
    if sp == "AFR":
        return (1, 0, 0, 0, 0)
    elif sp == "AMR":
        return (0, 1, 0, 0, 0)
    elif sp == "EAS":
        return (0, 0, 1, 0, 0)
    elif sp == "EUR":
        return (0, 0, 0, 1, 0)
    elif sp == "SAS":
        return (0, 0, 0, 0, 1)
