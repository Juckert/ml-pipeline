pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Download data') {
            steps {
                sh './venv/bin/python download.py'
            }
        }

        stage('Train model') {
            steps {
                sh './venv/bin/python train_model.py'
            }
        }
    }
}
