import os
import gzip
import shutil

def unzip_file(sample, filename):
    """This function unzips a .fastq.gz file into a .fastq file
    returns True if successful, False if not
    """
    try:
        f_in = gzip.open("./phase3_data/" + sample + filename, 'rb')
    except:
        print("[Error]: Could not access file:", filename, "for sample:", sample[:-1])
        return False
    f_out = open("./phase3_data/" + sample + filename[:-3], 'wb')
    shutil.copyfileobj(f_in, f_out)
    f_in.close()
    f_out.close()
    return True

def unzipAll(samples, all_files):
    """This is the main function
    It calls the unzipper on every file for all samples
    """
    num_unzipped = 0
    for i in range(len(all_files)):
        sample = samples[i]
        for file in all_files[i]:
            if not(os.path.isfile("./phase3_data/" + sample + file[:-3])):
                print("Extracting:", file)
                if unzip_file(sample, file):
                    num_unzipped += 1

    print("Successfully unzipped", num_unzipped, "files")
