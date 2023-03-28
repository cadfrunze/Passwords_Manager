import pandas as pd

data_dict = {
    'website': [],
    'email_username': [],
    'password': []
}

data = pd.DataFrame(data_dict)

data.to_csv('./save_data/save_data.csv')