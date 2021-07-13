import numpy as np

def prepData(samples, all_files):
    x = []
    y = []
    decoding = [(1, 0, 0, 0),
                (0, 1, 0, 0),
                (0, 0, 1, 0),
                (0, 0, 0, 1)]
    for i in range(len(all_files)):
        sample = samples[i]
        popgp = get_y_sample(sample)
        for file in all_files[i]:
            y += [popgp]
            f = open("./phase3_data/" + sample + file[:-14] + ".bin", 'rb')
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
