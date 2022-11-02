import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt

def generateCosineSimilarityScoreMatrix(vectors : np.array):
    cosineSimilarityScoreMatrix = np.empty((vectors.shape[0], vectors.shape[0]))
    for i in range(vectors.shape[0]):
        for j in range(vectors.shape[0]):
            cosineSimilarityScoreMatrix[i][j] = distance.cosine(vectors[i], vectors[j])*(-1) + 1
    
    return cosineSimilarityScoreMatrix

generatedArray = generateCosineSimilarityScoreMatrix(np.random.rand(10,4))

plt.matshow(generatedArray)
plt.set_cmap('bwr')
plt.show()