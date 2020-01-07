import numpy as np
import matplotlib.pyplot as plt


# ============================================
'''
X --> Z ---> Y
'''
N = 10000
X = np.random.random(size = N)
X = (X - np.mean(X))/np.std(X)

noise1 = np.random.random(size=N)
noise1 = (noise1 - np.mean(noise1))/np.std(noise1)

print("X mean is", np.mean(X))
print("X std is ", np.std(X))

cXZ = 0.3
Z = cXZ * X + cXZ * noise1
# Z = (Z - np.mean(Z))/np.std(Z)

cYZ = 0.5
Y = cYZ * Z + cYZ * noise1
# Y = (Y - np.mean(Y))/np.std(Y)
print("===================== X --> Z --> Y=======================")
print("Correlation between X, Z is", np.corrcoef(X, Z)[0, 1])
print("Correlation between Z, Y is", np.corrcoef(Y, Z)[0, 1])
print("Correlation between X, Y is", np.corrcoef(X, Y)[0, 1])
print("Partial Correlation between X,Y|Z is", \
      (np.corrcoef(X,Y)[0, 1] - np.corrcoef(X,Z)[0, 1] * np.corrcoef(Y,Z)[0, 1])/ \
      (np.sqrt(1-np.corrcoef(X,Z)[0, 1]**2)*np.sqrt(1-np.corrcoef(Y,Z)[0, 1]**2)))

print("EX is ", np.mean(X))
print("EZ is ", np.mean(Z))
print("EXZ is", np.mean(X*Z))
print("SX is", np.var(X))
print("SZ is", np.var(Z))
print("SXZ is", np.var(X*Z))
print("pXZ is", (np.mean(X*Z) - np.mean(X)*np.mean(Z))/(np.var(X)*np.std(Z)))


# ============================================
'''
X <-- Z ---> Y
'''
N = 10000
Z = np.random.random(size = N)

cXZ = 0.3
cYZ = 0.5
X = cXZ * Z + cXZ * np.random.random(size=N)
Y = cYZ * Z + cYZ * np.random.random(size=N)
print("===================== X <-- Z --> Y======================")
print("Correlation between X, Z is", np.corrcoef(X, Z)[0, 1])
print("Correlation between Z, Y is", np.corrcoef(Y, Z)[0, 1])
print("Correlation between X, Y is", np.corrcoef(X, Y)[0, 1])
print("Partial Correlation between X,Y|Z is", \
      (np.corrcoef(X,Y)[0, 1] - np.corrcoef(X,Z)[0, 1] * np.corrcoef(Y,Z)[0, 1])/ \
      (np.sqrt(1-np.corrcoef(X,Z)[0, 1]**2)*np.sqrt(1-np.corrcoef(Y,Z)[0, 1]**2)))
# ============================================
'''
X --> Z <--- Y
'''
N = 10000
X = np.random.random(size = N)
Y = np.random.random(size = N)

cXZ = 0.3
cYZ = 0.5
Z = cXZ * X + cYZ * Y + (cXZ + cYZ)/2 * np.random.random(size=N)
print("===================== X --> Z <-- Y======================")
print("Correlation between X, Z is", np.corrcoef(X, Z)[0, 1])
print("Correlation between Z, Y is", np.corrcoef(Y, Z)[0, 1])
print("Correlation between X, Y is", np.corrcoef(X, Y)[0, 1])
print("Partial Correlation between X,Y|Z is", \
      (np.corrcoef(X,Y)[0, 1] - np.corrcoef(X,Z)[0, 1] * np.corrcoef(Y,Z)[0, 1])/ \
      (np.sqrt(1-np.corrcoef(X,Z)[0, 1]**2)*np.sqrt(1-np.corrcoef(Y,Z)[0, 1]**2)))