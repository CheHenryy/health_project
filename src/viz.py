
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def vizualize_data(data):
    fig, axes = plt.subplots(2,3, figsize=(15,10))

    axes[0,0].hist(data['height'], bins=20, color='blue', alpha=0.7)
    axes[0,0].set_title('Histogram of height')
    axes[0,1].hist(data['weight'], bins=20, color='green', alpha=0.7)
    axes[0,1].set_title('Histogram of weight')
    axes[0,2].hist(data['systolic_bp'], bins=20, color='red', alpha=0.7)
    axes[0,2].set_title('Histogram of systolic_bp')
    axes[1,0].hist(data['age'], bins=20, color='purple', alpha=0.7)
    axes[1,0].set_title('Histogram of age')
    axes[1,1].hist(data['cholesterol'], bins=20, color='orange', alpha=0.7)
    axes[1,1].set_title('Histogram of cholesterol')
    axes[1,2].axis('off') 
    fig.suptitle('Distributions of continuous variables', fontsize=16)
    plt.tight_layout()

    plt.show()

def bar_smoker(data):
    data['smoker'].value_counts(normalize=True).plot(kind='bar', color=['cyan', 'magenta'])
    plt.title('Bar chart of smoking status')  
    plt.xlabel('Smoking Status')
    plt.ylabel('Proportion')    
    plt.show()


def box_sex(data):
    data.boxplot(column='weight', by='sex', color = 'blue', grid=True)
    plt.title('Boxplot of weight by sex')
    plt.suptitle('')  
    plt.xlabel('Sex')
    plt.ylabel('Weight')
    plt.show()

def box_bp_sex(data):
    data.boxplot(column='systolic_bp', by='sex', color = 'blue', grid=True)
    plt.title('Boxplot of systolic blood pressure by sex')
    plt.suptitle('')  
    plt.xlabel('Sex')
    plt.ylabel('systolic blood pressure')
    plt.show()





def age_bp_plot(data):
    plt.scatter(data['age'], data['systolic_bp'])
    plt.title('Scatter plot of Systolic Blood Pressure and Age')
    plt.xlabel('Age')
    plt.ylabel('Systolic Blood Pressure') 
    plt.grid(True)  
    plt.show()



def weight_bp_plot(data):
    plt.scatter(data['weight'], data['systolic_bp'])
    plt.title('Scatter plot of Systolic Blood Pressure and Weight')
    plt.xlabel('Weight')
    plt.ylabel('Systolic Blood Pressure')
    plt.grid(True)   
    plt.show()




def correlation_heatmap(data):
    import seaborn as sns

    corr = data[['systolic_bp', 'age', 'weight', 'cholesterol']].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix Heatmap')
    plt.show()