class FeatureCreation:
    def __init__(self, df):
        self.df = df.copy()

    def createFeatures(self):
        self.df['house_age'] = 2025 - self.df['yr_built']
        self.df['renovated'] = (self.df['yr_renovated'] > 0).astype(int)
        self.df['living_to_lot_ratio'] = self.df['sqft_living'] / (self.df['sqft_lot'] + 1)
        self.df['bath_per_bed'] = self.df['bathrooms'] / (self.df['bedrooms'] + 1)
        self.df['rooms_per_floor'] = (self.df['bedrooms'] + self.df['bathrooms']) / (self.df['floors'] + 0.01)

        return self
    
    def getDataset(self):
        return self.df


class FeatureSelection:
        def __init__(self, df, target):
            self.df = df.copy()
            self.target = target
        
        def filter_by_correlation(self):
            corr = self.df.corr()[self.target].abs()
            selected_features = corr[corr >= 0.2].index.tolist()

            if self.target in selected_features:
                selected_features.remove(self.target)

            self.selected_features = selected_features
            return self
        
        def get_selected_features(self):
            return self.selected_features