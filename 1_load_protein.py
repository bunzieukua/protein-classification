import numpy as np
import sklearn.decomposition as decomposition
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from Bio.PDB import MMCIFParser
import matplotlib.pyplot as plt
from Bio.PDB import PDBParser
from scipy.linalg import svd

#first choose your proteins of interest and download its sequence from RCSB Protein Data Bank
#the protein should be loaded 
