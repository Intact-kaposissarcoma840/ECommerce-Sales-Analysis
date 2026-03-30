import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    try:
        df = pd.read_csv("data/sales.csv")
        print("Dataset loaded successfully!\n")
        return df
    except FileNotFoundError:
        print("Error: sales.csv file not found in data folder")
        exit()

def clean_data(df):
    print("Missing values:\n", df.isnull().sum(), "\n")

    # Convert date column
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # Add Month column
    df['Month'] = df['Order Date'].dt.month

    return df

def basic_analysis(df):
    print("===== BASIC ANALYSIS =====")

    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()

    print("Total Sales:", total_sales)
    print("Total Profit:", total_profit, "\n")

def top_products(df):
    print("===== TOP PRODUCTS =====")

    top = df.groupby('Product Name')['Sales'].sum() \
            .sort_values(ascending=False).head(10)

    print(top, "\n")

    top.plot(kind='bar')
    plt.title("Top 10 Products")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("top_products.png")
    plt.show()

def category_analysis(df):
    print("===== CATEGORY ANALYSIS =====")

    category = df.groupby('Category')['Sales'].sum()
    print(category, "\n")

    category.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Sales by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("category_sales.png")
    plt.show()

def monthly_analysis(df):
    print("===== MONTHLY SALES =====")

    monthly = df.groupby('Month')['Sales'].sum()
    print(monthly, "\n")

    monthly.plot(kind='line', marker='o')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("monthly_sales.png")
    plt.show()

def region_analysis(df):
    print("===== REGION ANALYSIS =====")

    region = df.groupby('Region')['Sales'].sum()
    print(region, "\n")

def top_customers(df):
    print("===== TOP CUSTOMERS =====")

    customers = df.groupby('Customer ID')['Sales'].sum() \
                  .sort_values(ascending=False).head(5)

    print(customers, "\n")

def main():
    df = load_data()
    df = clean_data(df)

    basic_analysis(df)
    top_products(df)
    category_analysis(df)
    monthly_analysis(df)
    region_analysis(df)
    top_customers(df)

    print("Analysis Completed Successfully!")

if __name__ == "__main__":
    main()