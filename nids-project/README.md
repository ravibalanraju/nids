# Network Intrusion Detection System (NIDS)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

This project uses machine learning to detect and classify network intrusions in real-time.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Preprocess Data and Train Model](#preprocess-data-and-train-model)
  - Run the preprocessing and training script:
  - python src/train_model.py
  - [Real-Time Detection](#real-time-detection)
  - Run the real-time detection script:
  - python src/real_time_detection.py
  - Output: This script will capture live network traffic and use the trained model to detect intrusions in real-time.
  - [Start the Web API](#start-the-web-api)
  - Run the web API:
  - python src/app.py
  - Use the API: You can send POST requests to http://127.0.0.1:5000/predict with the network traffic features in JSON format:

{
  "features": [0.5, 0.2, 0.1, 0.7, 0.4, ...]
}
Response: The API will return a JSON response indicating whether the traffic is normal or an intrusion.
-
- [Contributing](#contributing)
- Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
-
- [Contact](#contact)
- For any questions or suggestions, please feel free to contact me:

Email: ravibalan79@gmail.com   <br>
GitHub: ravibalanraju

## Project Structure

```plaintext
nids-project/
├── data/
│   └── dataset.csv
├── models/
│   ├── trained_model.pkl
│   └── scaler.pkl
├── src/
│   ├── preprocess.py
│   ├── train_model.py
│   ├── real_time_detection.py
│   └── app.py
├── requirements.txt
└── README.md
