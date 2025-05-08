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

        stage('Deploy Model') {
            steps {
                sh 'uvicorn app:app --host 0.0.0.0 --port 8000 &'
                sleep(time: 5, unit: 'SECONDS') // Даем время сервису запуститься
            }
        }

        stage('Test Service') {
            steps {
                sh './venv/bin/python test_request.py'
            }
        }
    }

    post {
        always {
            sh 'pkill -f uvicorn' // Остановка сервиса после выполнения
        }
    }
}
