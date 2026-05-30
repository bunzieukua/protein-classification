# Step 1: Find the largest contact vector length
max_length = max(len(vec) for vec in contact_vectors.values())

# Step 2: Normalize all vectors to the max_length (padding with zeros)
normalized_vectors = {}
for protein, vector in contact_vectors.items():
    padded_vector = np.zeros(max_length, dtype=int)  # Create zero-padding
    padded_vector[:len(vector)] = vector  # Fill with original data
    normalized_vectors[protein] = padded_vector

# Step 3: Construct the Contact Matrix (n x m)
contact_matrix = np.array(list(normalized_vectors.values()))

# Output results
print("Contact Matrix:")
print(len(contact_matrix[0]))
