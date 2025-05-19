pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'vrindabs/flask-hello-world'
        CONTAINER_NAME = 'flask-hello-world'
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')

        KUBECTL_PATH = 'C:\\Program Files\\Docker\\Docker\\resources\\bin\\kubectl.exe'
        KUBECONFIG = 'C:\\Users\\Vrinda\\.kube\\config'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    imageTag = "${DOCKER_HUB_REPO}:${env.BUILD_NUMBER}"
                    echo "🔧 Building Docker image with tag: ${imageTag}"
                    bat "docker build -t ${imageTag} ."
                }
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                bat """
                    docker stop %CONTAINER_NAME% || exit 0
                    docker rm %CONTAINER_NAME% || exit 0
                    docker run --rm --name %CONTAINER_NAME% ${imageTag} cmd /c "pytest test.py && flake8"
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo '📤 Pushing image to Docker Hub...'
                bat """
                    echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin
                    docker push ${imageTag}
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo '🚀 Deploying to Kubernetes with updated image...'
                bat """
                    set KUBECONFIG=%KUBECONFIG%
                    "${KUBECTL_PATH}" set image deployment/flask-hello-deployment flask-hello=${imageTag}
                    "${KUBECTL_PATH}" rollout status deployment flask-hello-deployment
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
