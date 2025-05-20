from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>CI/CD Pipeline Project</title>
        <style>
            body {
                background: linear-gradient(135deg, #f8f9fa, #d1f2eb);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }

            h1 {
                color: #2c3e50;
                font-size: 40px;
            }
            h2{
               color: #2c3e50;
               font-size: 20px;
            }
            p {
                color: #34495e;
                font-size: 20px;
            }

            .box {
                padding: 30px;
                background-color: #ffffffd9;
                border-radius: 12px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>CI/CD Pipeline for Flask Application</h1>
            <p>Powered by Docker, Jenkins & Kubernetes</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
