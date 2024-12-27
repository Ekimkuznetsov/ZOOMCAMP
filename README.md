# ZOOCAMP_Mike_regration
# Project Name

## Objective

@@ -9,7 +8,7 @@ The goal of this project is to apply everything we have learned in this course t

For the project, we will build an end-to-end ML project. This includes:

1. Selecting a dataset of interest. 
1. Selecting a dataset of interest.
2. Training a model on that dataset while tracking experiments.
3. Creating a model training pipeline.
4. Deploying the model in batch, as a web service, or in streaming mode.
@@ -25,70 +24,130 @@ For the project, we will build an end-to-end ML project. This includes:
- **CI/CD**: GitHub Actions
- **Infrastructure as Code (IaC)**: Terraform?

## Evaluation Criteria
## Project: Bike Demand Prediction

### Problem Description
- **0 points**: The problem is not described.
- **1 point**: The problem is described briefly or unclearly.
- **2 points**: The problem is well described and clearly identifies what the project solves.
### Cloud Usage
- **0 points**: Cloud is not used, and everything runs locally.
- **2 points**: The project is developed on the cloud, uses Localstack (or similar), or is deployed on Kubernetes or similar platforms.
- **4 points**: The project is developed on the cloud, and IaC tools are used to provision the infrastructure.
### Experiment Tracking and Model Registry
- **0 points**: No experiment tracking or model registry.
- **2 points**: Experiments are tracked, or models are registered in a registry.
- **4 points**: Both experiment tracking and model registry are used.
### Workflow Orchestration
- **0 points**: No workflow orchestration.
- **2 points**: Basic workflow orchestration is implemented.
- **4 points**: Fully deployed workflow orchestration.
### Model Deployment
- **0 points**: Model is not deployed.
- **2 points**: Model is deployed but only locally.
- **4 points**: Model deployment is containerized and deployable to the cloud, or advanced tools are used.
### Model Monitoring
- **0 points**: No model monitoring.
- **2 points**: Basic model monitoring calculates and reports metrics.
- **4 points**: Comprehensive monitoring includes alerts or conditional workflows (e.g., retraining, generating debugging dashboards, switching to different models).
### Reproducibility
- **0 points**: No instructions or missing data.
- **2 points**: Instructions are present but incomplete, or data is missing.
- **4 points**: Clear instructions, easy-to-run code, and dependencies are specified.
### Best Practices
- Unit tests: **1 point**
- Integration tests: **1 point**
- Linter/Formatter: **1 point**
- Makefile: **1 point**
- Pre-commit hooks: **1 point**
- CI/CD pipeline: **2 points**
## Resources
This project aims to predict the demand for bicycles using real-world data from bicycle rental services. The objective is to analyze trends and create a robust machine learning model to forecast bike demand based on various features such as weather conditions, time of year, and day of the week.
### Steps
1. **Setup Environment**:
   - Install `pyenv` to manage Python versions:
     ```bash
     curl https://pyenv.run | bash
     ```
     Add `pyenv` to your shell:
     ```bash
     export PATH="$HOME/.pyenv/bin:$PATH"
     eval "$(pyenv init --path)"
     eval "$(pyenv init -)"
     ```
     Restart your terminal and install Python 3.9:
     ```bash
     pyenv install 3.9.0
     pyenv global 3.9.0
     ```
     Verify Python version:
     ```bash
     python --version
     ```
   - Use `pipenv` to manage dependencies:
     ```bash
     pipenv --python 3.9
     ```
     This will create a `Pipfile` for the project.
   - Install required libraries:
     ```bash
     pipenv install pandas numpy scikit-learn matplotlib seaborn mlflow boto3
     ```
2. **Data Analysis**:
   - Explore the dataset to understand the key features and relationships.
   - Visualize trends in bike rentals.
3. **Feature Engineering**:
   - Process raw data into features suitable for training.
   - Handle missing data, encode categorical variables, and normalize numerical data.
4. **Model Training**:
   - Train a machine learning model (Random Forest) to predict demand.
   - Track experiments and log metrics using MLflow.
   - Evaluate the model's performance using metrics like RMSE and R².
5. **Pipeline Creation**:
   - Build a training and prediction pipeline.
6. **Deployment**:
   - Deploy the model locally or on a cloud service using Docker.
7. **Batch Prediction**:
   - Use the trained model to make predictions on new data.
   - Save the predictions to a CSV file.
8. **Monitoring**:
   - Implement a monitoring solution to track model performance.
### Current Progress
#### Latest Model Results:
- **Algorithm**: Random Forest Regressor
- **Performance**:
  - **Validation RMSE**: 70.93
  - **Validation R²**: 0.85
  - **Training RMSE**: 60.36
  - **Training R²**: 0.89
  - **Training MAE**: 40.05
- **Experiment Tracking**:
  - MLflow experiment: [Experiment 0](http://localhost:5000/#/experiments/0)
  - MLflow run details: [Run](http://localhost:5000/#/experiments/0/runs/322fcdb2f7764f8790d08cfa75da7f31)
### Automation via Makefile
The project includes a `Makefile` for automating common tasks:
- **Install dependencies**:
  ```bash
  make install
  ```
- **Format code**:
  ```bash
  make format
  ```
- **Lint code**:
  ```bash
  make lint
  ```
- **Run tests**:
  ```bash
  make test
  ```
- **Train the model**:
  ```bash
  make train
  ```
- **Process data**:
  ```bash
  make preprocess
  ```
- **Start LocalStack**:
  ```bash
  make localstack-up
  ```
- **Stop LocalStack**:
  ```bash
  make localstack-down
  ```
- **Batch prediction**:
  ```bash
  make predict
  ```
### Resources
### Datasets
You can explore and select datasets from:
- [Kaggle](https://www.kaggle.com/)
- [AWS Datasets](https://registry.opendata.aws/)
- [UK Government Open Data](https://data.gov.uk/)
- [GitHub Archive](https://www.githubarchive.org/)
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)
- [Million Songs Dataset](http://millionsongdataset.com/)
- [COVID-19 Datasets](https://github.com/CSSEGISandData/COVID-19)
- [Azure Datasets](https://azure.microsoft.com/en-us/services/open-datasets/)
- [Google's Dataset Search Engine](https://datasetsearch.research.google.com/)
- [European Statistics Datasets](https://ec.europa.eu/eurostat/data/database)
Feel free to explore other datasets from the course-provided resources or contribute additional suggestions.
- [Santander Bike Rentals Dataset](https://www.kaggle.com/datasets)
- [Open Data for Bike Sharing](https://data.gov.uk/)
