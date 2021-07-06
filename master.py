from downloadData import download_all_data
from parseSequence import parseAllFastqs

# download files
samples, files = download_all_data()

# call function for unzipping files here

# parse and save files as .txt
parseAllFastqs(samples, files)
