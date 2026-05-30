proteins_residues = {"protein5" : residue_5aur}

# Define cutoff distance (e.g., 7 Å)
cutoff = 7.0

# Dictionary to store contact maps for each protein
contact_maps = {}
contact_vectors = {}

# Iterate over each protein
for protein_name, residues in proteins_residues.items():
    num_residues = len(residues)
    print(num_residues)
    contact_map = np.zeros((num_residues, num_residues))

    for i in range(num_residues):
        for j in range(num_residues):
            if i != j:
                dist = np.sqrt(
                    (residues[i]["x"] - residues[j]["x"])**2 +
                    (residues[i]["y"] - residues[j]["y"])**2 +
                    (residues[i]["z"] - residues[j]["z"])**2
                )
                if dist <= cutoff:
                    contact_map[i, j] = 1

    # Convert contact map to contact vector using Formula 1
    contact_vector = np.zeros(num_residues ** 2, dtype=int)

    for x in range(num_residues):
        for y in range(num_residues):
            i = (x) * num_residues + y  # Formula 1: Linearization
            contact_vector[i] = int(contact_map[x, y])  # Convert to binary

    # Store contact vector
    contact_vectors[protein_name] = contact_vector
    contact_maps[protein_name] = contact_map

# Output the contact vectors for verification
for protein, vector in contact_vectors.items():
    print(f"Contact Vector for {protein}:\n", vector)

# Output the contact maps for verification
for protein, matrix in contact_maps.items():
    print(f"Contact Map for {protein}:\n", matrix)

#Visualize contact map
for protein, contact_map in contact_maps.items():
    plt.imshow(contact_map, cmap='Greys', origin='lower') # Use 'matrix' here
    plt.xlabel("Residue index")
    plt.ylabel("Residue index")
    plt.title(f"Contact Map for {protein}") # Add protein name to title
    plt.colorbar(label='Contact (1 = black)')
    plt.show()
