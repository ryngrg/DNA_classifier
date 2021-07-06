import requests
import os
import sys

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
    """
    global url_base
    url = url_base + sample + "sequence_read/" + filename
    try:
        myfile = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Download failed for flie:", filename)
        print("[Exception]:", e)
        return None
    open("./phase3_data/" + sample + filename, 'wb').write(myfile.content)

def download_all_data():
    """This is the main function.
    It downloads and saves all phase 3 sequence reads for all samples
    And returns list of samples, list of lists of files for each sample
    """
    global url_base
    num_downloads = 0
    samples = get_all_links(url_base)
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
            print("-> downloading file:", file)
            # downloads file onto your computer
            if not(os.path.isfile("./phase3_data/" + sample + file)):
                download_file(sample, file)
                num_downloads += 1

    print("Successfully downloaded", str(num_downloads), "files for", str(len(samples)), "samples.")

    return samples, all_files
