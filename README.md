# Mental Wellness Prediction System

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Hugging%20Face-yellow)](https://huggingface.co/spaces/Jobanjps/Mental_Wellness)
[![Notebook](https://img.shields.io/badge/Notebook-Google%20Colab-blue)](https://colab.research.google.com/drive/1MwHbFQsmL1PuD_epcWl6xjQEBdbEThDX#scrollTo=a54c4c28)
[![GitHub](https://img.shields.io/badge/Source-GitHub-black)](https://github.com/Jobanjps089/Mental_Wellness)

A machine learning-powered web application that predicts mental wellness scores based on lifestyle factors including screen time, sleep patterns, and work-related screen exposure. This project leverages data science techniques to provide insights into how daily habits impact mental well-being.

## 🌟 Features

- **Predictive Analytics**: Uses machine learning to predict mental wellness scores
- **Interactive Web Interface**: User-friendly Flask-based web application
- **Real-time Predictions**: Instant results based on user input
- **Lifestyle Factor Analysis**: Considers screen time, sleep hours, and work screen exposure
- **Deployed Solution**: Live application hosted on Hugging Face Spaces

## 🚀 Live Demo

Try the application here: [Mental Wellness Predictor](https://jobanjps-Mental_Wellness.hf.space)

## 📊 Project Overview

Mental health is influenced by various lifestyle factors. Recent evidence has suggested that machine learning algorithms such as decision trees, support vector machines, and neural networks provide the most accurate prediction model for psychological issues including stress, depression, and anxiety. This project aims to predict mental wellness scores using three key behavioral indicators:

- **Screen Time**: Total daily screen exposure (hours)
- **Sleep Hours**: Duration of nightly sleep (hours)  
- **Work Screen Time**: Work-related screen exposure (hours)

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn, joblib
- **Data Processing**: NumPy, Pandas
- **Frontend**: HTML, CSS, Bootstrap
- **Deployment**: Hugging Face Spaces
- **Development**: Google Colab

## 📁 Project Structure

```
Mental_Wellness/
├── app.py                 # Flask application
├── mental_wellness.pkl    # Trained ML model
├── templates/
│   └── index.html        # Web interface template
├── requirements.txt      # Python dependencies
├── mental_wellness.ipynb # Model training notebook
└── README.md            # Project documentation
```

## 🔧 Installation & Setup

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jobanjps089/Mental_Wellness.git
   cd Mental_Wellness
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv mental_wellness_env
   source mental_wellness_env/bin/activate  # On Windows: mental_wellness_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

## 💻 Usage

### Web Application

1. Navigate to the [live demo](https://jobanjps-Mental_Wellness.hf.space) or run locally
2. Enter your daily metrics:
   - **Screen Time**: Total hours spent on screens per day
   - **Sleep Hours**: Average hours of sleep per night
   - **Work Screen Time**: Hours spent on screens for work
3. Click "Predict Mental Wellness Score"
4. View your predicted wellness score

### API Usage

The Flask app accepts POST requests to the root endpoint:

```python
import requests

data = {
    'screen_time': 8.0,
    'sleep_hours': 7.5,
    'work_screen': 6.0
}

response = requests.post('https://jobanjps-Mental_Wellness.hf.space/', data=data)
```

## 🧠 Model Information

### Training Process

The machine learning model was developed using the following approach:

1. **Data Collection**: Gathered lifestyle and wellness data
2. **Feature Engineering**: Processed screen time, sleep, and work metrics
3. **Model Training**: Implemented regression algorithms for wellness prediction
4. **Validation**: Cross-validated model performance
5. **Deployment**: Serialized model using joblib

### Model Performance

- **Algorithm**: [Specify the algorithm used - e.g., Random Forest, Linear Regression]
- **Features**: 3 input features (screen_time, sleep_hours, work_screen)
- **Output**: Continuous mental wellness score
- **Validation**: [Include metrics like R², RMSE, MAE if available]

### Input Features

| Feature | Description | Unit | Range |
|---------|-------------|------|-------|
| `screen_time` | Total daily screen exposure | Hours | 0-24 |
| `sleep_hours` | Nightly sleep duration | Hours | 0-12 |
| `work_screen` | Work-related screen time | Hours | 0-16 |

## 🔍 Model Development Notebook

The complete model development process is documented in the [Google Colab notebook](https://colab.research.google.com/drive/mental_wellness.ipynb), which includes:

- Data exploration and visualization
- Feature engineering
- Model training and comparison
- Performance evaluation
- Model serialization

## 📈 Results & Insights

The model provides insights into how lifestyle factors affect mental wellness:

- **Sleep Quality**: Adequate sleep hours positively correlate with wellness
- **Screen Time Balance**: Excessive screen time may negatively impact wellness
- **Work-Life Balance**: Work screen exposure affects overall mental health

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/improvement
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -am 'Add new feature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/improvement
   ```
6. **Create a Pull Request**

## 🐛 Issues & Support

- **Bug Reports**: [Create an issue](https://github.com/Jobanjps089/Mental_Wellness/issues)
- **Feature Requests**: [Request a feature](https://github.com/Jobanjps089/Mental_Wellness/issues)
- **Questions**: Open a discussion in the repository

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This application is for educational and research purposes only. The predictions should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for mental health concerns.

## 👨‍💻 Author

**Joban Singh**
- GitHub: [@Jobanjps089](https://github.com/Jobanjps089)
- Project Link: [Mental_Wellness](https://github.com/Jobanjps089/Mental_Wellness)

## 🙏 Acknowledgments

- Machine learning techniques for mental health prediction research
- Flask framework for web development
- Hugging Face Spaces for deployment
- Google Colab for model development environment

## 🔮 Future Enhancements

- [ ] Add more lifestyle factors (exercise, diet, social interaction)
- [ ] Implement time-series analysis for trend tracking
- [ ] Add data visualization dashboard
- [ ] Include confidence intervals for predictions
- [ ] Mobile application development
- [ ] Multi-language support
- [ ] Integration with wearable devices

---

*Last Updated: September 2025*
