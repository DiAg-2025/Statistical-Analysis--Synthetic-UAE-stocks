# Synthetic UAE Stocks

[Dataset](https://github.com/DiAg-2025/Statistical-Analysis--Synthetic-UAE-stocks/blob/main/Synthetic_UAE_Stock_Data.csv)

Introduction: This is synthetically generated data from Open AI that contains price data of a few UAE Stocks: EMIRATESNBD, DIB, EMAAR, CBD, MASQ, and DEWA. This comprehensive dataset spans from July 1, 2021, to March 30, 2025. The prices are denominated in AED and are indexed.

Objective:
1. Select three numerical variables, such as X1, X2, and X3, from the dataset. Create scatterplots to visualize the relationships between these variable pairs. For instance, generate scatterplots for X1 vs. X2, X2 vs. X3, and so on. Additionally, provide insights regarding the observed relationships between these variable pairs based on the scatterplot visualizations.
2. Calculate the covariance for the chosen pairs of numerical variables, such as Cov(X1, X2), Cov(X2, X3), and Cov(X1, X3). Then, analyze and interpret the relationships between these variables based on the computed covariance values.
3. Calculate the mean and standard deviation for the three chosen numerical variables. Afterward, provide an interpretation of the results to better understand the characteristics of these variables.
4. Formulate a statement to find a suitable bound (both an upper bound and a lower bound) by applying Chebyshev's inequality. Subsequently, give an interpretation of this result to understand the significance of the bound in terms of the variable's behavior and variability.

![Python](https://img.shields.io/badge/Py_libraries-Pandas,_Numpy,_Matplotlib-blue)

![Stats](https://img.shields.io/badge/Statistical_features-Scatterplot,_Linear_approximation,_Covariance,_Mean,_Standard_deviation,_Chebyshev's_inequality-beige)

[Analysis](https://github.com/DiAg-2025/Statistical-Analysis--Synthetic-UAE-stocks/blob/main/JupyterAnalysis.ipynb)

Findings:
1. X1="EMIRATESNBD", X2="EMAAR", X3="MASQ". From the generated scatter plots, it is evident that there exists a weak negative association between EMIRATESNBD and EMAAR, a strong positive association between EMAAR and MASQ, and a moderate negative association between MASQ and EMIRATESNBD.
2. The stocks show unique covariances: EMIRATESNBD and EMAAR move oppositely, EMAAR and MASQ move together, MASQ and EMIRATESNBD move oppositely.
3. All three stocks have varying means and standard deviations, with MASQ having the least price variability and EMIRATESNBD having the highest.
4. Calculation of bounds by using Chebyshev’s inequality:
One practical question that comes to the investor's mind is what the upper and lower bounds are on the probability that these stocks will move a certain standard deviation from the mean. 

- Calculation of bounds for MASQ

A) What is the upper bound on the probability that MASQ will make a move of more than AED75 from its mean in the coming time given the data?

![masqupper](https://github.com/user-attachments/assets/a21fccf4-4dcf-4ce7-9058-05ea53dee587)

Interpretation:
The chance that MASQ will make a move above AED75 from mean is at most 0.077. Hence, there is a very very low probability that there will be a move of that magnitude in MASQ. 

B) What is the lower bound on the probability of MASQ to make a move of less than AED75 from its mean in the coming time given the data?

![masqlower](https://github.com/user-attachments/assets/bedc60f3-76bd-4822-b4d2-f1f0289b3b8b)

Interpretation:
The chance that MASQ will make a move less than AED75 from mean is at least  0.923. Hence there is more than 90% chance that there will be less than AED75 move in any upcoming days in MASQ.


- Calculation of bounds for EMAAR

C) What is the upper bound on the probability of EMAAR to make a move of more than AED300 from its mean in the coming time given the data?

![emaarupper](https://github.com/user-attachments/assets/b682314d-f97d-45ac-88dd-feddeea6f2c3)

Interpretation:
The chance that EMAAR will make a move above AED300 from mean is at most  0.020. Hence there is a very very low probability that there will be a move of that magnitude in EMAAR. 

D) What is the lower bound on the probability of EMAAR to make a move less than AED300 from its mean in the coming time given the data?

![emaarlower](https://github.com/user-attachments/assets/485aac8a-9761-455e-9729-7f10a5847e7b)

Interpretation:
The chance that EMAAR will make a move less than AED300 from mean is at least 0.980. Hence it's very likely that there will be a move of AED300 in EMAAR. 


- Calculation of bounds for EMIRATESNBD

E) What is the upper bound on the probability that EMIRATESNBD will make a move of more than AED375 from its mean in the coming time given the data?

![nbdupper](https://github.com/user-attachments/assets/0f8ae423-2afc-4234-a361-fdcb49a3b2fd)

Interpretation:
The chance that EMIRATESNBD will make a move above AED375 from mean is at most  0.044. Hence there is a very very low probability that there will be a move of that magnitude in EMIRATESNBD stock price.

F) What is the lower bound on the probability of EMIRATESNBD making a move of less than AED375 from its mean in the coming time given the data?

![nbdlower](https://github.com/user-attachments/assets/528e14a4-866c-45d0-8172-2c81ee5b785a)

Interpretation:
The chance that EMIRATESNBD will make a move less than AED375 from mean is at least 0.956. Hence the chance of making a move lower AED375 is likely and more than 95% in EMIRATESNBD stock price.
