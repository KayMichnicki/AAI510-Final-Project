📈 S&P 500 Stock Analysis and Machine Learning Deployment



📝 Introduction

In this project, we utilize the S&P 500 stock dataset from Kaggle, which contains historical price data for companies listed in the S&P 500 index. The dataset includes key financial metrics such as open, close, high, low, volume, and adjusted close prices, covering multiple stocks across different sectors. This rich financial dataset allows us to:

- Build predictive models for stock price forecasting.

- Apply clustering techniques to identify behavioral patterns and group similar stocks based on their historical characteristics.



🎯 Business Objective
The objective of this project is to apply machine learning techniques to historical S&P 500 stock data. We aim to build two core models:

- Stock Price Prediction
Forecast future price movements to provide insights into market trends and investment opportunities.

- Stock Clustering Using Financial Indicators
Use KMeans clustering to group companies based on financial features like:

    - Trading Volume

    - Stock Price

    - Market Capitalization

    - EBITDA

    - Revenue Growth

    - Portfolio Weight This enables identifying similar stock behavior, aiding portfolio diversification and strategy formation.

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

