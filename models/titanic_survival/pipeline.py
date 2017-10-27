def extrapolate_features(dataset, *features):
    pass


def plot_feature_relation(dataset, feature_1, feature_2, path=None):
    pass

def plot_all_feature_pairs(dataset, path=None):
    pass


def extrapolate_correlation(dataset, path=None):
    pass

def plot_correlated_features(dataset, path=None):
    pass

def unique_values(dataset, feature):
    return dataset[feature].unique()

def one_hotter_encoding(dataset, features):
    encoded = dataset.copy()
    
    for feature in features:
        unique_vals = unique_values(encoded, feature)
        for value in unique_vals:
            encoded[f"{feature}_{value}"] = (encoded[feature] == value).astype(float)
    
    return encoded    