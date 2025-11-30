import pandas as pd
import numpy as np
import sys

data = pd.read_csv('C:/Users/chn03/Desktop/Python lessons/health_project/data/data.csv')

class analyzeData:
    def __init__(self, data_frame):
        if not isinstance(data_frame, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        
        self.df = data_frame
        
        # specify numerical and categorical columns
        self.numerical_cols = self.df[["age", "systolic_bp", "height", "cholesterol", "weight"]].columns.tolist()
        self.categorical_cols = self.df[["disease", "smoker", "sex"]].columns.tolist()

    def generate_numerical_stats(self, custom_stats=None):
   
        if custom_stats is None:
            custom_stats = [
                'count',
                'mean',
                'median',
                'std',
                'min',
                lambda x: x.quantile(0.25),
                lambda x: x.quantile(0.75),
                'max'
            ]
        
        stats_df = self.df[self.numerical_cols].agg(custom_stats)

        # set explicit row labels so index is clear / unique
        labels = [
            'Count',
            'Mean',
            'Median',
            'Std Dev',
            'Minimum',
            '25th Percentile (Q1)',
            '75th Percentile (Q3)',
            'Maximum'
        ]
        if len(stats_df.index) == len(labels):
            stats_df.index = labels
        
        return stats_df.round(2)

    def generate_categorical_stats(self):
        results = {}
        for col in self.categorical_cols:
            counts = self.df[col].value_counts(dropna=False)
            props = self.df[col].value_counts(normalize=True, dropna=False).round(3)
            summary = pd.DataFrame({'count': counts, 'proportion': props})
            results[col] = {'summary': summary}
        return results

    def generate_all_stats(self):
        num_stats = self.generate_numerical_stats()
        
        cat_stats = self.generate_categorical_stats()

        return num_stats, cat_stats
    
summary_stats = analyzeData(data)
all_stats = summary_stats.generate_all_stats()
print(all_stats)





