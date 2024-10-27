from scipy.stats import pearsonr 
import pandas as pd
#Load dataset
file_path = 'train.csv'
data =pd.read_csv(file_path)

#Calculate Pearson correlation coefficient between 'Applicant Income' and 'Loan Amount'
corr_income_loan, p_value_income_loan =pearsonr(data['ApplicantIncome'], data['LoanAmount'])

#Print the results
print("--- Hypothesis Testing for ApplicantIncome vs LoanAmount---")
print(f"\nNull Hypothesis (HB): There is no correlation between ApplicantIncome and LoanAmount.") 
print(f"Alternative Hypothesis (H1): There is a correlation between ApplicantIncome and LoanAmount.")
print(f"\nPearson Correlation Coefficient: {corr_income_loan:.4f}")
print(f"P-Value: {p_value_income_loan:.4f}")

alpha= 0.05 #Significance level
if p_value_income_loan < alpha:
    print("\nReject the null hypothesis (He). There is evidence to suggest a correlation between ApplicantIncome and LoanAmount.")
else:
    print("\nFail to reject the null hypothesis (HO). There is no evidence to suggest a correlation between ApplicantIncome and LoanAmount.")