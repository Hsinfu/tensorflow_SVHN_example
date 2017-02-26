try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve
from os.path import isfile, join
from scipy.io import loadmat
import numpy as np


dataset_dir = '../data/'
dataset_url = 'http://ufldl.stanford.edu/housenumbers/'
dataset = ['train_32x32.mat', 'test_32x32.mat']
train_mean_path = '../data/train_32x32_mean.npy'
# dataset = ['train_32x32.mat', 'test_32x32.mat', 'extra_32x32.mat']

# Download the dataset
for data in dataset:
    path = join(dataset_dir, data)
    url = join(dataset_url, data)
    if not isfile(path):
        print('downloading %s' % data)
        urlretrieve(url, path)

# Compute the pixels mean value of train data
if not isfile(train_mean_path):
    train_mat = loadmat('../data/train_32x32.mat')
    train_mean = np.mean(train_mat['X'], axis=3)
    np.save(train_mean_path, train_mean)
