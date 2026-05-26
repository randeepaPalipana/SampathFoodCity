from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class ProcessSelector:
    def runStrategy(self, strategy):
        strategy.analyzeData()

class MenuHandler:
    def showOptions(self):
        while True:
            print("\nChoose the Sales Report You Want:")
            print("1 - Branch-Based Sales")
            print("2 - Weekly Sales Summary")
            print("3 - Product Price Overview")
            print("4 - Product Popularity")
            print("5 - Sales Revenue Distribution")
            print("6 - Exit")

            try:
                user_choice = int(input("Enter your choice: "))
                if user_choice == 1:
                    ProcessSelector().runStrategy(BranchSales())
                elif user_choice == 2:
                    ProcessSelector().runStrategy(WeeklySales())
                elif user_choice == 3:
                    ProcessSelector().runStrategy(ProductPrice())
                elif user_choice == 4:
                    ProcessSelector().runStrategy(ProductPopularity())
                elif user_choice == 5:
                    ProcessSelector().runStrategy(SalesRevenue())
                elif user_choice == 6:
                    print("Program closed. Goodbye!")
                    break
                else:
                    print("Invalid option! Please try a number from 1 to 6.")
            except ValueError:
                print("Please enter a valid number.")

class SalesAnalysis(ABC):
    @abstractmethod
    def analyzeData(self):
        pass

class BranchSales(SalesAnalysis):
    def analyzeData(self):
        df = pd.read_csv("data/Sampath Food City (PVT) Ltd.csv")
        branch_summary = df.groupby("Branch")["Quantity"].sum().reset_index()
        print("\nTotal Quantity by Branch:")
        print(tabulate(branch_summary, headers="keys", tablefmt="grid"))

        plt.bar(branch_summary["Branch"], branch_summary["Quantity"], color=["violet", "gold", "skyblue"])
        plt.title("Branch-Wise Quantity Sold")
        plt.xlabel("Branch")
        plt.ylabel("Quantity")
        plt.tight_layout()
        plt.show()

class WeeklySales(SalesAnalysis):
    def analyzeData(self):
        df = pd.read_csv("data/Sampath Food City (PVT) Ltd.csv")
        df["Date"] = pd.to_datetime(df["Date"])
        df["Week"] = df["Date"].dt.isocalendar().week
        weekly_summary = df.groupby("Week")["Quantity"].sum().reset_index()

        print("\nWeekly Sales Quantity:")
        print(tabulate(weekly_summary, headers="keys", tablefmt="grid"))

        plt.plot(weekly_summary["Week"], weekly_summary["Quantity"], marker='o', linestyle='--')
        plt.title("Weekly Sales Performance")
        plt.xlabel("Week Number")
        plt.ylabel("Total Quantity")
        plt.tight_layout()
        plt.show()

class ProductPrice(SalesAnalysis):
    def analyzeData(self):
        df = pd.read_csv("data/Sampath Food City (PVT) Ltd.csv")
        price_summary = df.groupby("Item")["Price (LKR)"].mean().reset_index()
        price_summary.columns = ["Product", "Average Price"]

        print("\nProduct Price Analysis:")
        print(tabulate(price_summary, headers="keys", tablefmt="grid"))

        plt.bar(price_summary["Product"], price_summary["Average Price"], color="lightcoral")
        plt.title("Average Product Prices")
        plt.xlabel("Product")
        plt.ylabel("Average Price (LKR)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

class ProductPopularity(SalesAnalysis):
    def analyzeData(self):
        df = pd.read_csv("data/Sampath Food City (PVT) Ltd.csv")
        item_sales = df.groupby("Item")["Quantity"].sum().reset_index()

        print("\nProduct Sales Quantities:")
        print(tabulate(item_sales, headers="keys", tablefmt="grid"))

        plt.pie(item_sales["Quantity"], labels=item_sales["Item"], autopct="%1.1f%%", startangle=90)
        plt.title("Most Preferred Products")
        plt.tight_layout()
        plt.show()

class SalesRevenue(SalesAnalysis):
    def analyzeData(self):
        df = pd.read_csv("data/Sampath Food City (PVT) Ltd.csv")
        df["Revenue"] = df["Price (LKR)"] * df["Quantity"]
        revenue_by_branch = df.groupby("Branch")["Revenue"].sum().reset_index()

        print("\nTotal Revenue by Branch:")
        print(tabulate(revenue_by_branch, headers="keys", tablefmt="grid"))

        plt.bar(revenue_by_branch["Branch"], revenue_by_branch["Revenue"], color="skyblue")
        plt.title("Revenue Distribution by Branch")
        plt.xlabel("Branch")
        plt.ylabel("Total Revenue (LKR)")
        plt.tight_layout()
        plt.show()
