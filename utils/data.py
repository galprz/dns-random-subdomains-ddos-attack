import urllib.request
import os
from tqdm import tqdm
import hdf5storage


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, target_folder, filename):
    # check if data exists
    print("Check if data exists on disk")
    if os.path.isdir(target_folder):
        print("Data directory already exists. ",
              "if from some reason the data directory structure is wrong please remove the data dir and rerun this script")
        return
    if not os.path.isdir(target_folder):
      print("Creating target folder")
      os.mkdir(target_folder)
    files = os.listdir(target_folder)
    if not files:
        print("Cannot find files on disk")
        print("Downloading files")
        with DownloadProgressBar(unit='B', unit_scale=True,
                                 miniters=1, desc=url.split('/')[-1]) as t:
            urllib.request.urlretrieve(url, filename=target_folder + filename, reporthook=t.update_to)
    print("Download completed!")
