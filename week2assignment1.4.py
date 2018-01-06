import numpy as np

def normalizeRows(x):
    x_norm = np.linalg.norm(x, axis=1, keepdims=True)

    x = x / x_norm

    return x

x = np.array([[0, 3, 4],[1, 6, 4]])
print("The shape of x:" + str(x.shape))
print("normalizeRows(x) = " + str(normalizeRows(x)))
