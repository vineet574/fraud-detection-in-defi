import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("suspicious_transactions.csv")

plt.figure(figsize=(10, 6))
df["From"].value_counts().head(10).plot(kind="bar", color="red")
plt.xlabel("Sender Address")
plt.ylabel("Number of Suspicious Transactions")
plt.title("Top 10 Suspicious Addresses")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("suspicious_transactions_chart.png")
plt.show()
