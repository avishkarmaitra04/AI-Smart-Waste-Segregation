import matplotlib.pyplot as plt

methods = ['Rule-Based', 'TF-IDF + Naive Bayes']
accuracy = [1.00, 0.625]

plt.figure()
plt.bar(methods, accuracy)
plt.xlabel('Classification Method')
plt.ylabel('Accuracy')
plt.title('Accuracy Comparison of Waste Segregation Methods')
plt.ylim(0, 1.1)

plt.savefig("accuracy_comparison.png")
plt.show()
