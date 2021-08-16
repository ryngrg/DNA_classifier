import numpy as np
import os

def trainDataGenerator(num_epochs):
    """This function gives a generator containing 1 file at a time.
    It yields the sequence, superpopulation as one-hot vectors.
    """
    samples, all_files = get_filenames()
    for num in range(num_epochs):
        for i in range(len(samples)):
            sample = samples[i]
            for file in all_files[i]:
                ohvs, Y = prepData(sample, file)
                if (ohvs == []):
                    continue
                X = np.array([ohvs[:800]])
                yield X, Y
                # for i in range(0, len(ohvs), 400):
                    # X = np.array([ohvs[i : i+400]])
                    # print("\tX shape =", X.shape)
                    # yield X, Y

def testDataGenerator():
    samples, all_files = get_filenames()
    for i in range(len(samples)):
        sample = samples[i]
        for file in all_files[i]:
            ohvs, Y = prepData(sample, file, False)
            if (ohvs == []):
                continue
            X = np.array([ohvs[800:1600]])
            yield X, Y
                    
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

def prepData(sample, file, train = True):
    """This function converts a file's contents into a
    list of one-hot vectors.
    """
    y = get_y_sample(sample)
    if y == None:
        return [], np.array([])
    Y = np.array([y])
    
    try:
        f = open("./phase3_data/" + sample + "/" + file, 'rb')
    except:
        print("[Error]: Could not access file:", file, "for sample:", sample)
        return [], np.array([])
    
    decoding = [(1, 0, 0, 0),
                (0, 1, 0, 0),
                (0, 0, 1, 0),
                (0, 0, 0, 1)]
    raw = list(f.read())
    f.close()
    ohvs = []
    if train:
        limit = 200
    else:
        limit = 400
    for t in range(len(raw)):
        if t > limit:
            break
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

    print(sample, file, "\n\tY =", Y)
    return ohvs, Y

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
        return None
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
