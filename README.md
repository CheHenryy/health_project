# Objectives 
The goal of this project is to analyze health data of 800 participants and make inference about their health. 
# Procedure 
I start by cleaning the data (NB: data was relatively in good shape already),checking for duplicates and providing basic summary statistics of the important variables. I proceeded to producing summary plots. Following that,  I calculated the confidence interval of the mean systolic blood pressure.

## Inferential statistics
I performed statistical inference to investifate if there is a difference in mean systolic blood pressure between smokers and nonsmokers
  and calculated the CI using bootstrap approach.
In the next step, 
I fitted a Simple and multivariable linear regression using two different libraries to predict systolic blood pressure using the a set of variables from the dataset
Lastly, i verified the assumptions of linear regression and plottted the output. 


# Folders and files 
## Data folder:
Holds the data file used for this project called data.csv
## The scr folder:
Holds the different files with code performing particular aspects of the analysis. The files include:
### data_class.py 
This holds a class that produces summary statistics for both the numerical and categorical variables in the dataset. 

### Viz.py
This holds functions for producing differnt visualisations 

### report.ipynb
This notebook contains all the output and description of the results. This is the main file to look if you are interested in the consolidated report of the codes written in the other files mentioned above. 


# Directives 
Clone the repository and change the path for the dataset accordingly
clone: git clone https://github.com/CheHenryy/health_project.git

install required packages: pip install -r requirements.txt

click run all 


