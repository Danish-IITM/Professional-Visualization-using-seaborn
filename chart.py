# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional style and context for presentation-ready visualization
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic realistic data for product performance insights
np.random.seed(42)
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
sales = np.random.randint(80, 500, size=len(products))
profit_margin = np.random.uniform(0.1, 0.4, size=len(products))

data = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit Margin": profit_margin
})

# Calculate profit as a business insight metric (optional)
data["Profit"] = data["Sales"] * data["Profit Margin"]

# Create a barplot visualizing Sales by Product with a professional color palette
plt.figure(figsize=(9, 8.88), dpi=64)  

barplot = sns.barplot(
    x="Product", 
    y="Sales", 
    data=data, 
    palette="deep"
)

# Customize titles and labels
barplot.set_title("Sales Performance by Product", fontsize=20, weight='bold')
barplot.set_xlabel("Product", fontsize=16)
barplot.set_ylabel("Total Sales (Units)", fontsize=16)

# Optionally annotate bars with sales values
for p in barplot.patches:
    height = p.get_height()
    barplot.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2., height),
                     ha='center', va='bottom', fontsize=14)

# Save the figure with exact 512x512 pixels
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()
