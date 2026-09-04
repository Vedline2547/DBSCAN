# DBSCAN Clustering

## 📌 Overview

This project demonstrates how to use the **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** algorithm for clustering data points in a 2D space.

Unlike algorithms such as K-Means, DBSCAN does not require the number of clusters to be specified beforehand. It groups points based on their density and can also identify **noise and outliers**.

---

## 🧠 What is DBSCAN?

**DBSCAN** is an unsupervised machine learning algorithm that forms clusters by identifying areas where data points are densely packed together.

It is particularly useful when:

* The number of clusters is unknown.
* Clusters have irregular shapes.
* The dataset contains outliers.
* You want the algorithm to automatically identify noise.

---

## ⚙️ How DBSCAN Works

DBSCAN primarily uses two parameters:

### 1. `eps`

`eps` defines the maximum distance between two points for them to be considered neighbors.

In this project:

```python
eps=3
```

This means points within a distance of 3 can be considered neighbors.

### 2. `min_samples`

`min_samples` specifies the minimum number of points required within the `eps` neighborhood for a point to be considered part of a dense region.

In this project:

```python
min_samples=2
```

---

## 📊 Dataset

A small 2D dataset is used for demonstration:

```python
X = np.array([
    [1, 2],
    [2, 2],
    [2, 3],
    [8, 7],
    [8, 8],
    [25, 80]
])
```

The dataset contains two groups of nearby points and one point that is far away from the others.

The point:

```text
[25, 80]
```

is expected to be classified as **noise/outlier**.

---

## 🏷️ Cluster Labels

DBSCAN assigns a numerical label to every data point.

For example:

```text
Labels: [0 0 0 1 1 -1]
```

The labels mean:

| Label | Meaning         |
| ----- | --------------- |
| `0`   | First cluster   |
| `1`   | Second cluster  |
| `-1`  | Noise / outlier |

Therefore:

* `[1,2]`, `[2,2]`, `[2,3]` → Cluster 0
* `[8,7]`, `[8,8]` → Cluster 1
* `[25,80]` → Noise

---

## 💻 Technologies Used

* Python
* NumPy
* Scikit-learn
* DBSCAN

---

## 📦 Installation

Install the required libraries using:

```bash
pip install numpy scikit-learn
```

---

## 🚀 Usage

Run the Python script:

```bash
python main.py
```

The program will output the cluster labels:

```text
Labels: [0 0 0 1 1 -1]
```

---

## 📝 Complete Code

```python
# Import necessary libraries
from sklearn.cluster import DBSCAN
import numpy as np

# Sample data (e.g. points in 2D space)
X = np.array([
    [1, 2],
    [2, 2],
    [2, 3],
    [8, 7],
    [8, 8],
    [25, 80]
])

# Initialize and fit the model
dbscan = DBSCAN(eps=3, min_samples=2)
dbscan.fit(X)

# Get the labels (-1 indicates noise)
labels = dbscan.labels_

print("Labels:", labels)
```

---

## 🔍 DBSCAN vs K-Means

| Feature                     | DBSCAN               | K-Means               |
| --------------------------- | -------------------- | --------------------- |
| Type                        | Unsupervised         | Unsupervised          |
| Number of clusters required | ❌ No                 | ✅ Yes                 |
| Detects outliers            | ✅ Yes                | ❌ Not directly        |
| Handles irregular clusters  | ✅ Well               | ❌ Usually not         |
| Main parameters             | `eps`, `min_samples` | `n_clusters`          |
| Based on                    | Density              | Distance to centroids |

---

## 🎯 Key Learning Outcomes

Through this project, you will learn:

* How DBSCAN clustering works.
* How to use `DBSCAN` from Scikit-learn.
* The purpose of `eps`.
* The purpose of `min_samples`.
* How DBSCAN identifies noise.
* How to interpret DBSCAN cluster labels.
* The difference between density-based and centroid-based clustering.

---

## 📂 Project Structure

```text
DBSCAN-Clustering/
│
├── main.py
└── README.md
```

---

## 📚 Conclusion

DBSCAN is a powerful clustering algorithm for discovering groups of data points based on density. One of its biggest advantages is its ability to **identify outliers automatically** and work without requiring the number of clusters in advance.

In this example, DBSCAN successfully identifies two clusters and classifies the distant point `[25,80]` as noise.

---

## 👨‍💻 Author

**Vedline Ochieng**

Civil Engineering Student | Machine Learning Enthusiast | Python Developer | Future AI Engineer
