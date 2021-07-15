import os

def parse_file(sample, filename):
    """This function converts a .fastq file into a .bin file
    while doing so, it only retains the raw sequence reads
    returns True if successful, False if not
    """
    try:
        f = open("./phase3_data/" + sample + filename, 'r')
    except:
        print("[Error]: Could not access file:", filename, "for sample:", sample[:-1])
        return False
    outfile = open("./phase3_data/" + sample + filename[:-11] + ".bin", 'wb')
    useNext = False
    remaining = ""
    while True:
        text = f.readline()
        if len(text) == 0:
            break
        if text[0] == '+':
            useNext = False
        if useNext and (text[0] != '@'):
            noNs = text.replace('N', '')
            noNs = noNs.replace('\n', '')
            if (len(noNs) > 1) and (noNs[1] in ['0', '1', '2', '3']):
                noNs = (noNs.split('.'))[0]
                noNs = colorSpace_to_letterSpace(noNs)
            noNs = remaining + noNs
            if len(noNs) % 4 == 0:
                outfile.write(text_to_base4(noNs))
                remaining = ""
            elif (len(noNs) > 4):
                outfile.write(text_to_base4(noNs[:(-1 * (len(noNs) % 4))]))
                remaining = noNs[(-1 * (len(noNs) % 4)):len(noNs)]
            else:
                remaining = noNs
        if text[0] == '@':
            useNext = True
    f.close()
    outfile.close()
    return True

def colorSpace_to_letterSpace(text):
    enc = [["AA", "CC", "GG", "TT"],
           ["AC", "CA", "GT", "TG"],
           ["AG", "CT", "GA", "TC"],
           ["AT", "CG", "GC", "TA"]]
    let_seq = ""
    let_seq += text[0]
    for i in range(1, len(text)):
        for j in range(4):
            if enc[(int)(text[i])][j][0] == let_seq[i-1]:
                let_seq += enc[(int)(text[i])][j][1]
                break
    return let_seq

def text_to_base4(text):
    encoding = {"A":0, "C":1, "G":2, "T":3}
    nums = []
    i = 0
    for i in range(0, len(text) - 4, 4):
        num = 0
        num += encoding[text[i]] * (4**3)
        num += encoding[text[i+1]] * (4**2)
        num += encoding[text[i+2]] * (4**1)
        num += encoding[text[i+3]]
        nums += [num]
    num = 0
    num += encoding[text[i]] * (4**3)
    if len(text) > i + 1:
        num += encoding[text[i+1]] * (4**2)
        if len(text) > i + 2:
            num += encoding[text[i+2]] * (4**1)
            if len(text) > i + 3:
                num += encoding[text[i+3]]
    nums += [num]
    return bytearray(nums)
    
def parseAllFastqs(samples, all_files):
    """This is the main function
    It calls the parser on every file for all samples
    """
    num_parsed = 0
    for i in range(len(all_files)):
        sample = samples[i]
        for file in all_files[i]:
            if not(os.path.isfile("./phase3_data/" + sample + file.split('.')[0] + ".bin")):
                print("parsing file:", file[:-3])
                if parse_file(sample, file[:-3]):
                    num_parsed += 1

    print("Successfuly parsed", num_parsed, "files")
