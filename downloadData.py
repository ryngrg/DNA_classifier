import requests
import os

url_base = "http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/"

def get_all_links(url):
    """This function returns a list of all links in the webpage
    Eg:- get list of all samples, or list of all files for a sample
    NOTE: only works for these particular webpages only, it is hardcoded
    """
    links = []
    try:
        webPage = requests.get(url).text
    except requests.exceptions.RequestException as e:
        print("[Exception]:\n", e)
        return []
    allinvs = webPage.split('"')
    for i in range(3, len(allinvs)):
        if i % 2 == 1:
            links += [allinvs[i]]
    return links

def download_file(sample, filename):
    """This function downloads the file asked for
    and saves it in the path:
        ./phase3_data/sampleName/file
    returns True if successful, False if not
    """
    global url_base
    url = url_base + sample + "sequence_read/" + filename
    try:
        myfile = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Download failed for file:", filename)
        print("[Exception]:", e)
        return False
    f = open("./phase3_data/" + sample + filename, 'wb')
    f.write(myfile.content)
    f.close()
    return True

def download_all_data(samplesRange):
    """This is the main function.
    It downloads and saves all phase 3 sequence reads for samples in given range
    And returns list of samples, list of lists of files for each sample
    """
    start, end = samplesRange
    global url_base
    num_downloads = 0
    samps = get_all_links(url_base)
    samples = samps[start:end]
    all_files = []
    for sample in samples:
        print("Sample:", sample)
        # create new directory for the sample
        try:
            os.mkdir("./phase3_data/" + sample)
        except FileExistsError:
            print("Folder for sample already exists")
        files = get_all_links(url_base + sample + "sequence_read/")
        all_files += [files]
        for file in files:
            if not(os.path.isfile("./phase3_data/" + sample + file)):
                if not(os.path.isfile("./phase3_data/" + sample + file[:-14] + ".bin")):
                    print("-> downloading file:", file)
                    # download file onto your computer
                    if download_file(sample, file):
                        num_downloads += 1

    print("Successfully downloaded", str(num_downloads), "files for", str(len(samples)), "samples.")

    return samples, all_files
