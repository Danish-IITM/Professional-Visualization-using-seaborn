# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Generate realistic synthetic data

data = {
    "Product": ["A", "B", "C", "D", "E"],
    "Sales": [350, 420, 280, 510, 460]
}
df = pd.DataFrame(data)


# Seaborn styling

sns.set_style("whitegrid")
sns.set_context("talk")
palette = sns.color_palette("Blues_d", n_colors=len(df["Product"].unique()))


# Create the barplot

plt.figure(figsize=(8, 8))  # 8 inches x 8 inches → 512x512 px at dpi=64
ax = sns.barplot(
    data=df,
    x="Product",
    y="Sales",
    hue="Product",           # ensure palette is applied
    palette=palette,
    legend=False             # remove redundant legend
)


# Customize chart

ax.set_title("Product Sales Performance", fontsize=18, weight="bold")
ax.set_xlabel("Product", fontsize=14)
ax.set_ylabel("Sales (Units)", fontsize=14)

sns.despine()

# Save the chart

plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
