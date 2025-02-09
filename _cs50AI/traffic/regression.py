import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your CSV file
file_path = "combined.csv"  
data = pd.read_csv(file_path)


# Heatmap of Correlations
# plt.figure(figsize=(7, 7))
# sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
# plt.title("Correlation Heatmap")
# plt.show()

# # Regression Plots for Each Y vs X
for y in ['loss']:  # Replace with your dependent variables
    for x in ['layers', 'units', 'features']:  # Replace with your independent variables
        plt.figure(figsize=(6, 4))
        sns.regplot(x=data[x], y=data[y], line_kws={"color": "red"}, ci=None)
        plt.title(f"{y} vs {x}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.tight_layout()
        plt.show()
