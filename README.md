# Smart Waste Segregation using Intelligent Approaches

## 📌 Project Title
A Comparative Study of Intelligent Approaches for Smart Waste Segregation

---

## 📖 Project Overview
Improper waste segregation is a significant environmental challenge that leads to inefficient recycling, increased landfill usage, and environmental pollution. Correct classification of waste into wet, dry, and e-waste categories is essential for sustainable waste management.

This project focuses on the design, implementation, and comparison of two intelligent approaches for smart waste segregation:
1. Rule-Based Semantic Classification
2. Machine Learning-Based Classification using TF-IDF and Naive Bayes

The objective is to analyze the performance of both methods and identify an efficient approach for waste classification.

---

## 🎯 Objectives
- To design a rule-based intelligent system for waste segregation
- To implement a machine learning-based text classification model
- To prepare a waste item dataset for experimentation
- To compare the performance of both methods using evaluation metrics
- To analyze the effectiveness of intelligent techniques for sustainable waste management

---

## 🌍 Sustainable Development Goals (SDGs)
- SDG 12: Responsible Consumption and Production
- SDG 11: Sustainable Cities and Communities
- SDG 13: Climate Action
- SDG 3: Good Health and Well-Being

---

## 🧠 Methods Implemented

### Method 1: Rule-Based Semantic Classification
- Uses keyword matching and semantic rules
- Classifies waste into wet, dry, and e-waste
- Acts as a baseline and is fully explainable
- Simple and transparent logic

### Method 2: TF-IDF + Naive Bayes Classifier
- Converts waste item names into numerical features using TF-IDF
- Uses Naive Bayes for classification
- Data-driven and scalable
- Provides improved accuracy compared to rule-based method

---

## 📁 Dataset Description
The dataset (`waste_dataset.csv`) contains waste item names and their corresponding categories:
- Wet waste
- Dry waste
- E-waste

The dataset is manually curated and can be extended easily for future experimentation.

---

## 📊 Evaluation Metrics
Both methods are evaluated using:
- Accuracy
- Precision
- Recall
- F1-score (for Machine Learning model)

The results are compared to determine the most effective approach.

---

## ⚙️ Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Naive Bayes Classifier

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd waste-segregation-project
