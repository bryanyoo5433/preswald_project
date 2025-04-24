# 📊 Stock Portfolio Dashboard (Preswald App)

Created using [Preswald](https://github.com/StructuredLabs/preswald) to demonstrate interactive data filtering, visualization, and UI composition using a sample stock portfolio dataset.

## 🧠 Features

### 🔄 Two-Level Filtering System
- **Step 1:** Select a column to filter by (`Ticker`, `Sector`, `Quantity`, `Close`, or `Weight`)
- **Step 2:** Depending on the column type:
  - Dropdown (`selectbox`) for categorical columns
  - Slider for numeric columns
- **Apply Filter:** Filters are applied only when the **"Apply Filter"** button is clicked, ensuring controlled reactivity

### 🧮 Row Selection Tool
- Slider to choose how many top rows to display
- Pressing **"Show Rows"** dynamically updates the table display

### 📊 Visualizations
- **Scatter Plot:** Quantity vs. Close Price by Sector
- **Pie Chart:** Stock weight distribution
- **Bar Chart:** Sector weight distribution

## ⚠️ Known Issues with Preswald (Platform Limitations)

### 🐞 1. `np.float_` Serialization Error
