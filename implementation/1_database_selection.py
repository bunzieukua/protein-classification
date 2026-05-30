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

# Load your CIF file (downloaded from RCSB Protein Data Bank)
cif_file = "/1dw3.cif" #file name will change based on your selected protein. here we're working with 1dw3
parser = MMCIFParser(QUIET=True)
structure = parser.get_structure("structure", cif_file)

# Initialize an empty list to store residue + atom data
residue_1dw3 = []

# Iterate over all residues and all atoms
for model in structure:
    for chain in model:
        for residue in chain:
            resname = residue.get_resname()
            resid = residue.get_id()[1]
            chain_id = chain.id

            for atom in residue:
                atom_name = atom.get_name()
                x, y, z = atom.coord
                residue_1dw3.append({
                    "residue": resname,
                    "resid": resid,
                    "chain": chain_id,
                    "atom": atom_name,
                    "x": float(x),
                    "y": float(y),
                    "z": float(z)
                })

# Output or use the list
print(residue_1dw3[:5])  # Preview first 5 entries
