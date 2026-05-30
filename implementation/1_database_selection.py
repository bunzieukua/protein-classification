#install required packages 
import numpy as np
import sklearn.decomposition as decomposition
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from Bio.PDB import MMCIFParser
import matplotlib.pyplot as plt
from Bio.PDB import PDBParser
from scipy.linalg import svd
from Bio.PDB.MMCIFParser import MMCIFParser

# Here we work with 1ql4 protein. The file name with "1ql4" will change based on which protein you are interested in.
# List of hydrophobic residues
hydrophobic = {'ALA', 'VAL', 'ILE', 'LEU', 'MET', 'PHE', 'TRP', 'PRO'}

# Load your CIF file
cif_file = "/1ql4.cif"
parser = MMCIFParser(QUIET=True)
structure = parser.get_structure("structure", cif_file)

# Initialize an empty list to store residue + atom data
residue_1ql4 = []

# Iterate over all residues and all atoms
for model in structure:
    for chain in model:
        for residue in chain:
            resname = residue.get_resname()
            if resname in hydrophobic:  # Count only hydrophobic residues
                resid = residue.get_id()[1]
                chain_id = chain.id
                ca_atom = residue["CA"] if "CA" in residue else None
                if ca_atom:
                  x, y, z = ca_atom.coord
                  residue_1ql4.append({
                    "residue": resname,
                    "x": float(x),
                    "y": float(y),
                    "z": float(z)
                })
