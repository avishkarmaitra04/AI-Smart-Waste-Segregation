import matplotlib.pyplot as plt

metrics = ['Precision', 'Recall', 'F1-Score']
rule_based = [1.00, 1.00, 1.00]
ml_based = [0.85, 0.62, 0.64]

x = range(len(metrics))

plt.figure()
plt.bar(x, rule_based, width=0.4, label='Rule-Based')
plt.bar([i + 0.4 for i in x], ml_based, width=0.4, label='ML-Based')

plt.xticks([i + 0.2 for i in x], metrics)
plt.ylabel('Score')
plt.title('Performance Metrics Comparison')
plt.ylim(0, 1.1)
plt.legend()

plt.savefig("metrics_comparison.png")
plt.show()
