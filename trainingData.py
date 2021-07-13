import numpy as np

def prepData(samples, all_files):
    x = []
    y = []
    for i in range(len(all_files)):
        sample = samples[i]
        popgp = get_y_sample(sample)
        for file in all_files[i]:
            y += [popgp]
            f = open("./phase3_data/" + sample + file[:-14] + ".txt", 'r')
            raw = f.read()
            f.close()
            ohvs = []
            for t in range(len(raw)):
                if raw[t] == 'A':
                    ohvs += [(1, 0, 0, 0)]
                elif raw[t] == 'C':
                    ohvs += [(0, 1, 0, 0)]
                elif raw[t] == 'G':
                    ohvs += [(0, 0, 1, 0)]
                elif raw[t] == 'T':
                    ohvs += [(0, 0, 0, 1)]
            x += [ohvs]
    X = np.array(x)
    Y = np.array(y)
    print("X shape =", X.shape)
    print("Y shape =", Y.shape)
    return X, Y

def get_y_sample(sample):
    f = open("./samples_population.csv")
    f.readline()
    while True:
        row = f.readline()
        if len(row) == 0:
            break
        (samp, gen, pop, supop) = row.split(',')
        if samp == sample[:-1]:
            sp = supop
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
