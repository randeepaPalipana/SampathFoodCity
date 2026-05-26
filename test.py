# import pytest

# def getBranchNames(df):
#     return df["Branch"].unique().tolist()

# import pandas as pd

# def test_get_branch_names_wrong():
#     df = pd.DataFrame({"Branch": ["Galle", "Galle"]})
#     result = getBranchNames(df)
#     assert result == ["Kandy"]  


# import pytest
# import pandas as pd
# from your_module import getAmount, getDiscount, getBranchNames

# def test_get_branch_names_negative(): 
#     df = pd.DataFrame({"Branch": ["Galle", "Galle"]})
#     assert getBranchNames(df) == ["Kandy"]  





# # TEST_FILE_PATH = "data/Sampath Food City (PVT) Ltd.csv"


# # def load_data():
# #     return pd.read_csv(TEST_FILE_PATH)


# # def test_file_loading():
# #     df = load_data()
# #     assert not df.empty, "CSV file appears to be empty!"
# #     assert "Item" in df.columns, "'Item' column is missing in CSV!"
# #     assert "Quantity" in df.columns, "'Quantity' column is missing in CSV!"


# # def test_data_types():
# #     df = load_data()
# #     assert pd.api.types.is_numeric_dtype(df["Price (LKR)"]), "Price column should be numeric!"
# #     assert pd.api.types.is_numeric_dtype(df["Quantity"]), "Quantity column should be numeric!"


# # def test_total_sales_calculation():
# #     df = load_data()
# #     df["Total_Sales"] = df["Price (LKR)"] * df["Quantity"]
# #     assert "Total_Sales" in df.columns, "Total_Sales column not created!"
# #     assert all(df["Total_Sales"] >= 0), "Total sales contains negative values!"


# # def test_branch_names():
# #     df = load_data()
# #     unique_branches = df["Branch"].unique()
# #     assert len(unique_branches) > 0, "No branches found in the dataset!"


# # def test_week_column_generation():
# #     df = load_data()
# #     df["Date"] = pd.to_datetime(df["Date"])
# #     df["Week"] = df["Date"].dt.isocalendar().week
# #     assert "Week" in df.columns, "Week column not generated!"
# #     assert df["Week"].min() >= 1, "Invalid week number detected!"

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

# If you already have app functions, replace these with:
# from your_module import branch_quantity, product_quantity, branch_revenue

def branch_quantity(df: pd.DataFrame) -> pd.DataFrame:
    out = df.groupby("Branch", as_index=False)["Quantity"].sum().sort_values("Branch").reset_index(drop=True)
    return out

def product_quantity(df: pd.DataFrame) -> pd.DataFrame:
    out = df.groupby("Item", as_index=False)["Quantity"].sum().sort_values("Item").reset_index(drop=True)
    return out

def branch_revenue(df: pd.DataFrame) -> pd.DataFrame:
    tmp = df.assign(Revenue=df["Price"] * df["Quantity"])
    out = tmp.groupby("Branch", as_index=False)["Revenue"].sum().sort_values("Branch").reset_index(drop=True)
    return out


@pytest.fixture
def df_sample():
    return pd.DataFrame(
        {
            "Transaction_ID": ["T1","T2","T3","T4","T5","T6","T7"],
            "Branch": ["Colombo","Kandy","Colombo","Badulla","Gampaha","Kandy","Badulla"],
            "Item": ["Milk","Tea","Bread","Milk","Rice","Rice","Tea"],
            "Price": [200,150,120,200,180,180,150],
            "Quantity": [3,2,5,1,4,2,3],
            "Year": [2025]*7,
            "Month": [7,7,7,7,7,7,7],
            "Date": [1,2,2,3,3,4,4],
        }
    )

# ---------- Test Case 1: Branch-wise Quantity ----------
def test_branch_quantity_positive(df_sample):  # ✅
    actual = branch_quantity(df_sample)
    expected = pd.DataFrame(
        {
            "Branch": ["Badulla","Colombo","Gampaha","Kandy"],
            "Quantity": [1+3, 3+5, 4, 2+2],  # Badulla(1+3 from T4,T7), Colombo(3+5 from T1,T3)...
        }
    ).sort_values("Branch").reset_index(drop=True)
    assert_frame_equal(actual, expected)

def test_branch_quantity_negative(df_sample):  # ❌
    actual = branch_quantity(df_sample)
    expected = pd.DataFrame(
        {
            "Branch": ["Badulla","Colombo","Gampaha","Kandy"],
            "Quantity": [1, 8, 5, 4],  # intentionally wrong
        }
    ).sort_values("Branch").reset_index(drop=True)
    with pytest.raises(AssertionError):
        assert_frame_equal(actual, expected)

# ---------- Test Case 3: Product-wise Quantity ----------
def test_product_quantity_positive(df_sample):  # ✅
    actual = product_quantity(df_sample)
    expected = pd.DataFrame(
        {
            "Item": ["Bread","Milk","Rice","Tea"],
            "Quantity": [5, 3+1, 4+2, 2+3],  # Bread=5, Milk=4, Rice=6, Tea=5
        }
    ).sort_values("Item").reset_index(drop=True)
    assert_frame_equal(actual, expected)

def test_product_quantity_negative(df_sample):  # ❌
    actual = product_quantity(df_sample)
    expected = pd.DataFrame(
        {
            "Item": ["Bread","Milk","Rice","Tea"],
            "Quantity": [6, 4, 6, 5],  # Bread intentionally wrong
        }
    ).sort_values("Item").reset_index(drop=True)
    with pytest.raises(AssertionError):
        assert_frame_equal(actual, expected)

# ---------- Test Case 5: Branch-wise Revenue ----------
def test_branch_revenue_positive(df_sample):  # ✅
    actual = branch_revenue(df_sample)
    expected = pd.DataFrame(
        {
            # Revenue = Price * Quantity aggregated by branch
            "Branch": ["Badulla","Colombo","Gampaha","Kandy"],
            "Revenue": [
                200*1 + 150*3,     # Badulla (T4=200*1, T7=150*3)
                200*3 + 120*5,     # Colombo (T1, T3)
                180*4,             # Gampaha (T5)
                150*2 + 180*2,     # Kandy (T2, T6)
            ],
        }
    ).sort_values("Branch").reset_index(drop=True)
    assert_frame_equal(actual, expected)

def test_branch_revenue_negative(df_sample):  # ❌
    actual = branch_revenue(df_sample)
    expected = pd.DataFrame(
        {
            "Branch": ["Badulla","Colombo","Gampaha","Kandy"],
            "Revenue": [200, 1000, 720, 600],  # intentionally wrong
        }
    ).sort_values("Branch").reset_index(drop=True)
    with pytest.raises(AssertionError):
        assert_frame_equal(actual, expected)
