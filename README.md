# 💰 Salary Seeker

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/Dzivilord/Salary_Seeker?style=for-the-badge)](https://github.com/Dzivilord/Salary_Seeker/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Dzivilord/Salary_Seeker?style=for-the-badge)](https://github.com/Dzivilord/Salary_Seeker/network)
[![GitHub issues](https://img.shields.io/github/issues/Dzivilord/Salary_Seeker?style=for-the-badge)](https://github.com/Dzivilord/Salary_Seeker/issues)
[![GitHub license](https://img.shields.io/github/license/Dzivilord/Salary_Seeker?style=for-the-badge)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

**A data science project predicting salaries based on various factors.**

</div>

## 📖 Overview

This project uses machine learning to predict salaries based on collected data. It involves data crawling, preprocessing, model training, and a user interface for salary prediction.  The target audience is anyone interested in salary prediction, data science, or job market analysis. The key problem solved is providing a tool to estimate potential salary based on various job-related inputs.


## ✨ Features

- **Data Crawling:** Scrapes job data from online sources (details in `crawdata.ipynb`).
- **Data Preprocessing:** Cleans and prepares the data for model training (`dataPreprocessing.ipynb`).
- **Model Training:** Trains a machine learning model to predict salaries (`model.ipynb`).  A pre-trained model (`salary_model.pkl`) is provided.
- **Salary Prediction:**  Predicts salaries using the trained model via a user-friendly Python interface (`main.py` and `UI.py`).
- **Docker Support:**  Includes a `Dockerfile` for easy deployment and reproducibility.


## 🛠️ Tech Stack

**Languages & Libraries:**

- [![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
- [![Jupyter Notebook](https://img.shields.io/badge/jupyter-notebook-orange.svg)](https://jupyter.org/)
- [![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
- [![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
- [![Pickle](https://img.shields.io/badge/pickle-green?logo=python&logoColor=white)](https://docs.python.org/3/library/pickle.html)
- [![Matplotlib](https://img.shields.io/badge/Matplotlib-%23829196.svg?logo=matplotlib&logoColor=white)](https://matplotlib.org/)
- [![Tkinter](https://img.shields.io/badge/Tkinter-blue?logo=python&logoColor=white)](https://docs.python.org/3/library/tk.html)


**Containerization:**

- [![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)](https://www.docker.com/)

## 🚀 Quick Start

### Prerequisites

- Python 3.x (Ensure you have `pip` installed)
- Required packages:
  ```bash
  pip install -r requirements.txt
  ```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dzivilord/Salary_Seeker.git
   cd Salary_Seeker
   ```

2. **Install dependencies:** (Already listed above in Prerequisites).


### Running the Application

1. **Run using Python:**
    ```bash
    python main.py
    ```

2. **Running with Docker (Recommended):**

    ```bash
    docker build -t salary_seeker .
    docker run -it salary_seeker
    ```

## 📁 Project Structure

```
Salary_Seeker/
├── UI.py             # User Interface script
├── main.py           # Main script to run the prediction application
├── Utils/            # (Empty directory - Potentially for future utility functions)
├── __pycache__/      # Compiled Python bytecode
├── crawdata.ipynb    # Jupyter Notebook for data crawling
├── dataPreprocessing.ipynb # Jupyter Notebook for data preprocessing
├── model.ipynb       # Jupyter Notebook for model training
├── requirements.txt  # Project dependencies
├── salary_model.pkl  # Trained prediction model
├── salary_scaler.pkl # Scaler for input data
├── Dockerfile        # Docker configuration file
└── LICENSE           # Project license
```

## ⚙️ Configuration

No specific configuration files are used besides the `requirements.txt` file which manages the project's Python dependencies.  The trained model (`salary_model.pkl`) and scaler (`salary_scaler.pkl`) are used for prediction.

## 🧪 Testing

No formal unit tests are included in this repository.  The notebooks contain experiments and analysis, which serve as a form of testing and validation.  Future iterations could include more rigorous testing procedures.

## 🚀 Deployment

The application can be deployed using Docker for easy reproducibility and portability. The `Dockerfile` provides the necessary instructions for building and running the application within a container.

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE) - see the LICENSE file for details.


---

<div align="center">

**HOW IT GOING**
![alt text](result.png)
</div>