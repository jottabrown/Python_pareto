# Pareto Chart in Python

This repository contains a simple Python script to generate a Pareto chart using `matplotlib`.

## 📌 Description
The script visualizes categorical data with a bar chart while simultaneously displaying cumulative values as a line plot. The goal is to help identify the most significant categories contributing to a dataset.

## 📜 Requirements
Make sure you have Python installed along with the necessary library:
```bash
pip install matplotlib
```

## 🚀 Usage
Run the script using Python:
```bash
python script.py
```

## 📝 Code Overview
```python
import matplotlib.pyplot as plt

# Define categories and values
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [80, 20, 50, 30]

# Create a bar chart
fig, ax1 = plt.subplots()
ax1.bar(categories, values, color='skyblue')
ax1.set_ylabel('Values', color='skyblue')
ax1.tick_params('y', colors='skyblue')
ax1.set_xlabel('Categories', color='skyblue')

# Create a line chart for cumulative values
ax2 = ax1.twinx()
cumulative_values = [sum(values[:i+1]) for i in range(len(values))]
ax2.plot(categories, cumulative_values, color='red', marker='o')
ax2.set_ylabel('Cumulative Values', color='red')
ax2.tick_params('y', colors='red')

# Set the title and display the plot
plt.title('Pareto Chart')
plt.show()
```

## 📊 Output
The script generates a Pareto chart where:
- The **blue bars** represent individual category values.
- The **red line** shows the cumulative values.

## 🎯 Purpose
Pareto charts are useful for identifying the most significant factors in a dataset, commonly used in quality control and decision-making.

## 🤝 Contributions
Feel free to open issues or submit pull requests to enhance the script!

## 📄 License
This project is licensed under the MIT License.