# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 01:06:40 2022

@author: jun xiang
"""
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader

class MapDataset(Dataset):
    def __init__(self, reservedMap, labels):
        self.labels = labels
        self.reservedMap = reservedMap
    def __len__(self):
        return len(self.labels)
    def __getitem__(self, idx):
        label = self.labels[idx]
        text = self.text[idx]
        sample = {"Text": text, "Class": label}
        return sample