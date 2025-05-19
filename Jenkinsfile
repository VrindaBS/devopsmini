pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'vrindabs/flask-hello-world'
        CONTAINER_NAME = 'flask-hello-world'
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')

        // NEW: Use real kubectl path and kubeconfig
        KUBECTL_PATH = 'C:\\Users\\Vrinda\\kubectl\\kubectl.exe' // OR just 'kubectl' if in PATH
        KUBECONFIG = 'C:\\Users\\Vrinda\\.kube\\config'
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

        stage('Deploy to Kubernetes') {
            steps {
                echo '🚀 Deploying to Kubernetes...'
                bat """
                    set KUBECONFIG=%KUBECONFIG%
                    %KUBECTL_PATH% apply -f deployment.yaml
                    %KUBECTL_PATH% apply -f service.yaml
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
