📈 S&P 500 Stock Analysis and Machine Learning Deployment



📝 Introduction

In this project, we utilize the S&P 500 stock dataset from Kaggle, which contains historical price data for companies listed in the S&P 500 index. The dataset includes key financial metrics such as open, close, high, low, volume, and adjusted close prices, covering multiple stocks across different sectors. This rich financial dataset allows us to:

- Apply clustering techniques to identify behavioral patterns and group similar stocks based on their historical characteristics.
  
- Build predictive models for stock performance classification.



🎯 Business Objective
The objective of this project is to apply machine learning techniques to historical S&P 500 stock data. We aim to build two core models:

- Stock Clustering Using Financial Indicators
Perform an Clustering of companies based on key financial indicators, with the goal of identifying distinct groups or market player types that exhibit similar behavior across features such as trading volume, stock price, market capitalization, EBITDA, revenue growth, and portfolio weight. We will be using K Means clustering to implement this unsupervised learning.

- Develop a predictive model that classifies whether a stock is likely to outperform the market over the next 20 days, based on technical and fundamental indicators.


📦 Project Dependencies
Python Libraries

numpy
pandas
scipy
matplotlib
seaborn
tqdm
joblib
xgboost
imblearn
scikit-learn

Install Dependencies using:


pip install numpy pandas scipy matplotlib seaborn tqdm joblib xgboost imbalanced-learn scikit-learn
pip install notebook ipython


🏗️ System Architecture
The deployment follows a modular microservices approach:


- Components:
GUI POD (Nginx):
Serves the frontend interface and forwards HTTPS GET requests to the backend services.

- Model Training Service:
Handles model training and retraining based on new data using gRPC communication.

- Model Service:
Hosts the trained model and provides prediction APIs via gRPC to the GUI POD.

- Model Update Module:
Periodically fetches live stock data via yFinance and updates models or retrains them as needed.

- Cloud Integration:
    - Uses cloud platforms (AWS, Azure, Oracle Cloud) for scalability.

    - Saves trained models and data to cloud storage using HTTPS APIs.

- CI/CD Pipeline:
Integrated with GitHub to automatically build, test, and deploy services.



📦 Project Folder structure



| Folder/File | Description|
|----------|----------|
| .github/workflows   | Script for CI/CD Workflow |
| data    | Contains initial raw data in CSV format  |
| deploy    | Script for deployment Workflow |
| eda    | Code for EDA, Deployed as part of EDA container |
| gui    | Code for GUI, Deployed as part of GUI container |
| model_service    | Code for loading teh saved trained data, Deployed as part of MODEL Service container |
| model_training    | Code for traioning the model, clustring, Deployed as part of MODEL training container |
| saved_model    | Folder for saving trained data |

