# 📊 Predictive E-Commerce Analytics

> End-to-end exploratory data analysis of an e-commerce dataset to uncover sales trends, customer behavior, product performance, and profitability drivers.

---

## 🎯 Business Problem

An e-commerce company wants to understand:

- Which customers generate the most revenue?
- Which products are most profitable?
- Are sales and profits growing over time?
- Which regions and segments perform best?
- What factors are reducing profitability?

The goal is to transform raw transactional data into actionable business insights that support revenue growth and profit optimization.

---

## 🛠 Tech Stack

```python
Python
Pandas
NumPy
Matplotlib
Seaborn
Jupyter Notebook
```

---

## 📂 Project Workflow

```text
Business Understanding
        ↓
Data Quality Checks
        ↓
Univariate Analysis
        ↓
Bivariate Analysis
        ↓
Time Series Analysis
        ↓
Customer & Product Deep Dive
        ↓
Profitability Analysis
        ↓
Business Recommendations
```

---

# 1️⃣ Business Understanding

### Key Business Questions

✔ Which customers drive the most revenue?

✔ Which categories contribute the highest profit?

✔ What seasonal trends impact sales?

✔ Which products or regions generate losses?

✔ How can profitability be improved?

---

# 2️⃣ Data Quality Checks

## Validation Performed

```python
# Checked
Missing Values
Duplicate Records
Data Types
Date Consistency
Shipping Duration
Category Consistency
```

### Key Findings

| Check | Result |
|---------|---------|
| Missing Values | Minimal |
| Duplicate Records | None |
| Order Date Range | 2019-01-02 → 2020-12-31 |
| Ship Date Range | 2019-01-05 → 2021-01-05 |
| Average Shipping Time | ~3-4 Days |

✅ Dataset was clean and suitable for analysis.

---

# 3️⃣ Univariate Analysis

## Sales Distribution

### Findings

- Most orders have relatively low sales values.
- Few large orders contribute significant revenue.

### Insight

The business follows a typical long-tail revenue distribution.

---

## Profit Distribution

### Findings

```python
Average Profit ≈ $25
Median Profit ≈ $8
```

- Profit distribution is highly skewed.
- Many orders generate small profits.
- Some orders generate losses.

### Insight

Profitability improvement opportunities exist.

---

## Category Analysis

| Category | Observation |
|------------|-------------|
| Office Supplies | Highest order volume |
| Furniture | Moderate |
| Technology | Lowest volume |

---

# 4️⃣ Bivariate Analysis

## Sales vs Profit

### Observation

📈 Higher sales generally lead to higher profits.

However:

⚠ Several high-sales orders still produce losses.

### Business Insight

Revenue growth alone does not guarantee profitability.

---

## Category Performance

| Metric | Winner |
|----------|---------|
| Sales | Office Supplies |
| Profit | Technology |
| Quantity Sold | Office Supplies |

### Key Insight

🚀 Technology products generate the highest profit margins.

---

## Regional Performance

| Region | Performance |
|----------|-------------|
| West | Best |
| East | Strong |
| South | Weakest |

---

# 5️⃣ Time Series Analysis

## Monthly Sales Trend

### Findings

```text
Peak Season  → Nov-Dec
Low Season   → Jan-Feb
```

### Insight

Strong seasonality exists.

Q4 contributes the largest share of annual revenue.

---

## Year-over-Year Performance

| Metric | Growth |
|----------|---------|
| Sales | +66.5% |
| Profit | -19.05% |

### Critical Finding

⚠ Revenue increased dramatically.

⚠ Profit decreased.

This indicates margin erosion.

---

# 6️⃣ Customer & Product Deep Dive

## Top Customers

```python
Top 10 Customers Contribution = 7.7%
```

### Insight

Revenue is well diversified.

The business is not dependent on a small number of customers.

---

## Product Analysis

### Findings

✅ Several products consistently drive revenue.

⚠ Some products generate losses despite strong sales.

### Business Insight

Loss-making products require pricing and cost review.

---

## Loss-Making Cities

```text
Chicago
Philadelphia
Houston
Dallas
Phoenix
Aurora
Yuma
```

### Insight

Regional profitability varies significantly.

---

# 7️⃣ Profitability Analysis

## Most Profitable Category

🏆 Technology

Reasons:

- High margins
- Strong profit contribution
- Consistent performance

---

## Most Profitable Segment

🏆 Consumer

- Highest sales
- Highest profit

---

## Shipping Analysis

### Findings

Standard Class Shipping:

✅ Highest sales

✅ Highest profit

✅ Most popular option

### Insight

Customers prioritize value over delivery speed.

---

# 8️⃣ Key Findings

## Positive Findings

✅ Sales grew by 66.5%

✅ Strong Q4 demand

✅ Diversified customer base

✅ Technology drives profitability

✅ West region outperforms all others

---

## Areas of Concern

⚠ Profit declined by 19.05%

⚠ Loss-making products exist

⚠ Some cities consistently lose money

⚠ Furniture profitability remains weak

⚠ High sales do not always translate into profit

---

# 9️⃣ Business Recommendations

## Revenue Growth

```text
✓ Expand Technology offerings
✓ Increase Q4 marketing investment
✓ Promote cross-selling strategies
```

---

## Profit Improvement

```text
✓ Review discount policies
✓ Remove or reprice loss-making products
✓ Improve margin monitoring
```

---

## Customer Strategy

```text
✓ Retain high-value Consumer customers
✓ Grow Corporate segment
✓ Develop loyalty programs
```

---

## Regional Strategy

```text
✓ Replicate West region success
✓ Investigate South region performance
```

---

# 📌 Final Conclusion

The company is experiencing **strong sales growth (+66.5%)**, but profitability is declining (**-19.05%**).

The analysis suggests that future growth should focus on:

- Increasing margins
- Expanding profitable product lines
- Reducing loss-making transactions
- Leveraging strong Q4 demand

By addressing these issues, the business can achieve **sustainable and profitable growth** rather than revenue growth alone.

---

## 👨‍💻 Author

**Anish Don**

Aspiring Data Analyst | Python | SQL | Power BI | Statistics
