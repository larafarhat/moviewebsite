pipeline {
    agent any

    environment {
        // Define a unique image name to avoid conflicts in the Docker daemon
        DOCKER_IMAGE_NAME = "django-project/django-app"
    }

    stages {
        stage('Checkout') {
            steps {
                // Fetches the code from your GitHub repository
                checkout scm
            }
        }

        stage('Build Image for Minikube') {
            steps {
                script {
                    echo "Building Docker image for macOS..."
                    // This command configures the shell to use Minikube's internal Docker daemon.
                    // It's the crucial step for making the image available to Kubernetes without a remote registry.
                    sh 'eval $(/opt/homebrew/bin/minikube docker-env)'
                    
                    // Build the image and tag it with the unique Jenkins build number to ensure freshness
                    sh "docker build -t ${env.DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ."
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                script {
                    echo "Deploying to Minikube..."
                    // This command updates the deployment manifest with the new image tag.
                    // It uses the macOS/BSD compatible 'sed -i ""' syntax.
                    // This ensures Kubernetes pulls the new image version for the deployment.
                    sh "sed -i '' 's|image:.*|image: ${env.DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}|g' deployment.yaml"
                    
                    echo "Applying Kubernetes manifests..."
                    // Apply the updated deployment and the service configuration
                    sh 'kubectl apply -f deployment.yaml'
                    sh 'kubectl apply -f service.yaml'
                    
                    echo "Verifying deployment rollout..."
                    // This command waits for the deployment to complete and reports its status.
                    sh 'kubectl rollout status deployment/django-app-deployment'
                }
            }
        }
    }

    post {
        always {
            script {
                echo "Pipeline finished. To access the application, run: minikube service django-app-service"
                // This command cleans up the image tag in the YAML file, resetting it for the next run.
                // This prevents committing a build-specific tag back to source control.
                sh "sed -i '' 's|image:.*|image: django-project/django-app:placeholder|g' deployment.yaml"
            }
        }
    }
}
