pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'vrindabs/flask-hello-world'
        CONTAINER_NAME = 'flask-hello-world'
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        MINIKUBE_PATH = 'C:\\path\\to\\minikube.exe'  // <- Change this!
    }

    stages {
        stage('Build') {
            steps {
                echo '🔧 Building Docker image...'
                bat "docker build -t %DOCKER_HUB_REPO%:latest ."
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                bat '''
                    docker stop %CONTAINER_NAME% || exit 0
                    docker rm %CONTAINER_NAME% || exit 0
                    docker run --rm --name %CONTAINER_NAME% %DOCKER_HUB_REPO%:latest cmd /c "pytest test.py && flake8"
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo '📤 Pushing image to Docker Hub...'
                bat '''
                    echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin
                    docker push %DOCKER_HUB_REPO%:latest
                '''
            }
        }

        stage('Deploy to Kubernetes (Minikube)') {
            steps {
                echo '🚀 Deploying to Kubernetes...'
                bat """
                    \"%MINIKUBE_PATH%\" kubectl -- apply -f deployment.yaml
                    \"%MINIKUBE_PATH%\" kubectl -- apply -f service.yaml
                """
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check the logs.'
        }
    }
}
