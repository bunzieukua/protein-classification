# Step 1: Apply SVD for Latent Semantic Indexing
k = 100  # Select top-k dimensions
svd = TruncatedSVD(n_components=k)
reduced_matrix = svd.fit_transform(contact_matrix)

# Step 2: Retrieve Similar Proteins
query_protein = reduced_matrix[0]  # Use first protein as query
similarities = cosine_similarity([query_protein], reduced_matrix)

# Step 3: Rank Proteins by Similarity
ranked_proteins = np.argsort(similarities[0])[::-1]

# Output Results
print("Reduced Contact Matrix (Latent Space Representation):")
print(reduced_matrix)

print("\nSimilarity Scores for Query Protein:")
print(similarities[0])

print("\nRanked Protein Indices (Most Similar First):")
print(ranked_proteins)
