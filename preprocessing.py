import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer


def features_remove(met_data):
    """
    Input: DNA methylation data
    Output: DNA methylation data loại bỏ đi feature bị thiếu hơn 20% giá trị
    """
    missing_percentage = met_data.isna().mean(axis=1) * 100
    features_to_remove = list(missing_percentage[missing_percentage > 20].index)
    filtered_data = met_data.drop(index = features_to_remove)
    filrered_data = filtered_data.reset_index(drop=True)
    return filtered_data


def KNNimpute(met_data, neighbors = 5):
    """
    Input: DNA methylation data
    Output: DNA methylation data sau khi được thêm các feature bị thiếu bằng phương pháp KNN
    """
    imputer = KNNImputer(n_neighbors=neighbors)
    filled_data = pd.DataFrame(imputer.fit_transform(met_data.iloc[:, 1:]), columns=met_data.columns[1:], index=met_data.index)
    return filled_data