from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# List of DevOps-related words and definitions
flashcards = [
    {"word": "Containerization", "definition": "A lightweight virtualization method to run applications in isolated environments."},
    {"word": "CI/CD", "definition": "Continuous Integration and Continuous Deployment – automating software delivery."},
    {"word": "Kubernetes", "definition": "An open-source system for automating deployment, scaling, and management of containerized applications."},
    {"word": "Infrastructure as Code", "definition": "Managing and provisioning infrastructure using code instead of manual processes."},
    {"word": "Load Balancer", "definition": "Distributes network traffic across multiple servers to ensure high availability."},
    {"word": "Monitoring", "definition": "Tracking and analyzing system performance using tools like Prometheus and Grafana."},
    {"word": "Version Control", "definition": "A system that tracks changes in code, commonly using Git."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flashcard')
def get_flashcard():
    return jsonify(random.choice(flashcards))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

