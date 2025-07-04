import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# loading the dataset
dataset = pd.read_csv('Synthetic_UAE_Stock_Data.csv')
print(dataset)

# creating alias for convinience
A,B,C = dataset["EMIRATESNBD"],dataset["EMAAR"],dataset["MASQ"]
X,Y,Z = "EMIRATESNBD","EMAAR","MASQ"


# scatterplot 1
plt.scatter(A,B, c="orange")

# best_fit linear association for scatterplot 1
fit = np.polyfit(A,B,1)
best_fit = np.poly1d(fit)
plt.plot(A,best_fit(A),color="b")

# graph labeling
plt.title(f"Scatterplot of {Y} VS {X}")
plt.xlabel(f"{X}")
plt.ylabel(f"{Y}")
plt.show()


# scatterplot 2
plt.scatter(B,C, c="orange")

# best_fit linear association for scatterplot 2
fit = np.polyfit(B,C,1)
best_fit = np.poly1d(fit)
plt.plot(B,best_fit(B),color="b")

# graph labeling
plt.title(f"Scatterplot of {Z} VS {Y}")
plt.xlabel(f"{Y}")
plt.ylabel(f"{Z}")
plt.show()


# scatterplot 3
plt.scatter(C,A, c="orange")

# best_fit linear association for scatterplot 3
fit = np.polyfit(C,A,1)
best_fit = np.poly1d(fit)
plt.plot(C,best_fit(C),color="b")

# graph labeling
plt.title(f"Scatterplot of {X} VS {Z}")
plt.xlabel(f"{Z}")
plt.ylabel(f"{X}")
plt.show()


# Calculating co-variance matrix for each of the pair

dic1={X:[],Y:[],Z:[]}

for _ in [A,B,C]:
    for __ in [A,B,C]:
        if __.equals(A):
            dic1[X].append(np.cov(_,__,ddof=1)[0,1])
        elif __.equals(B):
            dic1[Y].append(np.cov(_,__,ddof=1)[0,1])
        elif __.equals(C):
            dic1[Z].append(np.cov(_,__,ddof=1)[0,1])

co_var_matrix = pd.DataFrame(dic1,index=[X,Y,Z])
print(co_var_matrix)


# Calculating mean and standard-deviation matrix for each of the selected three companies
M,N="MEAN","STAND. DEVIA."

dic2={M:[],N:[]}

for _ in [A,B,C]:
    if _.equals(A):
        dic2[M].append(np.mean(_))
        dic2[N].append(np.std(_))
    elif _.equals(B):
        dic2[M].append(np.mean(_))
        dic2[N].append(np.std(_))
    elif _.equals(C):
        dic2[M].append(np.mean(_))
        dic2[N].append(np.std(_))

mean_std_matrix = pd.DataFrame(dic2,index=[X,Y,Z])
print(mean_std_matrix)