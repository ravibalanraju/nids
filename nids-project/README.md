<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Network Intrusion Detection System (NIDS)</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
            padding: 20px;
            background: white;
            margin-top: 30px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #333;
        }
        .badge {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            border-radius: 3px;
            color: white;
        }
        .badge-python {
            background-color: #3572A5;
        }
        .badge-license {
            background-color: #4CAF50;
        }
        nav {
            margin-bottom: 20px;
        }
        nav ul {
            list-style: none;
            padding: 0;
        }
        nav ul li {
            display: inline;
            margin-right: 10px;
        }
        .toc {
            list-style: none;
            padding-left: 20px;
        }
        .toc ul {
            padding-left: 20px;
        }
        .toc a {
            text-decoration: none;
            color: #333;
        }
        .toc a:hover {
            text-decoration: underline;
        }
        pre {
            background: #333;
            color: white;
            padding: 10px;
            border-radius: 5px;
        }
        .code {
            background: #f4f4f4;
            border-left: 5px solid #ccc;
            padding: 10px;
            margin: 10px 0;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Network Intrusion Detection System (NIDS)</h1>
        <span class="badge badge-python">Python 3.8+</span>
        <span class="badge badge-license">MIT License</span>

        <nav>
            <ul>
                <li><a href="#installation">Installation</a></li>
                <li><a href="#usage">Usage</a></li>
                <li><a href="#contributing">Contributing</a></li>
                <li><a href="#license">License</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>

        <h2>Table of Contents</h2>
        <ul class="toc">
            <li><a href="#project-structure">Project Structure</a></li>
            <li><a href="#installation">Installation</a></li>
            <li><a href="#usage">Usage</a>
                <ul>
                    <li><a href="#preprocess-data-and-train-model">Preprocess Data and Train Model</a></li>
                    <li><a href="#real-time-detection">Real-Time Detection</a></li>
                    <li><a href="#start-the-web-api">Start the Web API</a></li>
                </ul>
            </li>
            <li><a href="#contributing">Contributing</a></li>
            <li><a href="#license">License</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>

        <h2 id="project-structure">Project Structure</h2>
        <pre>
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
        </pre>

        <h2 id="installation">Installation</h2>
        <ol>
            <li>
                <strong>Clone the repository:</strong>
                <div class="code">git clone https://github.com/ravibalanraju/nids-project.git<br>cd nids-project</div>
            </li>
            <li>
                <strong>Set up a virtual environment</strong> (optional but recommended):
                <div class="code">
                    python -m venv venv<br>
                    source venv/bin/activate  <!-- On Windows use `venv\Scripts\activate` -->
                </div>
            </li>
            <li>
                <strong>Install the dependencies:</strong>
                <div class="code">pip install -r requirements.txt</div>
            </li>
            <li>
                <strong>Place your dataset in the `data` directory and name it `dataset.csv`.</strong>
            </li>
        </ol>

        <h2 id="usage">Usage</h2>
        <h3 id="preprocess-data-and-train-model">Preprocess Data and Train Model</h3>
        <ol>
            <li><strong>Run the preprocessing and training script:</strong>
                <div class="code">python src/train_model.py</div>
            </li>
            <li><strong>Output:</strong> This script will preprocess your data, train a Random Forest model, and save the trained model and scaler in the `models` directory.</li>
        </ol>

        <h3 id="real-time-detection">Real-Time Detection</h3>
        <ol>
            <li><strong>Run the real-time detection script:</strong>
                <div class="code">python src/real_time_detection.py</div>
            </li>
            <li><strong>Output:</strong> This script will capture live network traffic and use the trained model to detect intrusions in real-time.</li>
        </ol>

        <h3 id="start-the-web-api">Start the Web API</h3>
        <ol>
            <li><strong>Run the web API:</strong>
                <div class="code">python src/app.py</div>
            </li>
            <li><strong>Use the API:</strong> You can send POST requests to <code>http://127.0.0.1:5000/predict</code> with the network traffic features in JSON format:
                <div class="code">
                    {
                      "features": [0.5, 0.2, 0.1, 0.7, 0.4, ...]
                    }
                </div>
            </li>
            <li><strong>Response:</strong> The API will return a JSON response indicating whether the traffic is normal or an intrusion.</li>
        </ol>

        <h2 id="contributing">Contributing</h2>
        <p>Contributions are welcome! Please follow these steps:</p>
        <ol>
            <li>Fork the repository.</li>
            <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
            <li>Make your changes.</li>
            <li>Commit your changes (<code>git commit -m 'Add some feature'</code>).</li>
            <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
            <li>Open a pull request.</li>
        </ol>

        <h2 id="license">License</h2>
        <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

        <h2 id="contact">Contact</h2>
        <p>For any questions or suggestions, please feel free to contact me:</p>
        <ul>
            <li><strong>Email:</strong> <a href="mailto:your-email@example.com">your-email@example.com</a></li>
            <li><strong>GitHub:</strong> <a href="https://github.com/yourusername">yourusername</a></li>
        </ul>

        <footer>
            <p>Thank you for using the Network Intrusion Detection System (NIDS) project! If you find this project helpful, please star the repository and share it with others.</p>
        </footer>
    </div>
</body>
</html>

