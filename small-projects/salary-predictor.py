print("Programa iniciado")
from sklearn.linear_model import LinearRegression
import numpy as np

# dados simples: anos de experiência -> salário
X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2000,3000,4000,5000,6000])

model = LinearRegression()
model.fit(X,y)

pred = model.predict([[6]])

print("Salário previsto:", pred[0])