import pytest
import pandas as pd
import numpy as np
from numpy import nan


@pytest.fixture
def df():
    df3 = pd.read_excel('/Users/macbook/Desktop/IBM/KPMG_intership/01 _Data_Quality_Assessment/KPMG.xlsx', sheet_name='CustomerDemographic', skiprows= 1)
    return df3

# check column if exist
def test_col_exist(df3):
    name= 'customer_id'
    assert name in df3.columns
    
# check null
def test_null_check(df3):
    assert df3['customer_id'].notnull().all()