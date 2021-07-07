import os

def parse_file(sample, filename):
    """This function converts a .fastq file into a .txt file
    while doing so, it only retains the raw sequence reads
    returns True if successful, False if not
    """
    try:
        f = open("./phase3_data/" + sample + filename, 'r')
    except:
        print("[Error]: Could not access file:", filename, "for sample:", sample[:-1])
        return False
    outfile = open("./phase3_data/" + sample + filename[:-11] + ".txt", 'w')
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
    return True

def parseAllFastqs(samples, all_files):
    """This is the main function
    It calls the parser on every file for all samples
    """
    num_parsed = 0
    for i in range(len(all_files)):
        sample = samples[i]
        for file in all_files[i]:
            if not(os.path.isfile("./phase3_data/" + sample + file.split('.')[0] + ".txt")):
                print("parsing file:", file)
                if parse_file(sample, file[:-3]):
                    num_parsed += 1

    print("Successfuly parsed", num_parsed, "files")
