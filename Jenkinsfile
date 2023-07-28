pipeline {
    agent any

    stages {
        stage('Check out') {
            steps {
                checkout([$class: 'GitSCM', 
                branches: [[name: '*/jenkins_job']],
                userRemoteConfigs: [[url: 'https://github.com/kryvetskyi/qa_ui_automation.git']]])
            }
        }
        
        stage('Build and Test') {
            steps {
                // Remove previous test results
                sh "rm -r reports/allure-results/*"

                // Build the custom Docker image using the Dockerfile in the project directory
                script {
                    docker.build("my_custom_image:${env.BUILD_NUMBER}", "-f Dockerfile .")
                }

                // Run the build and test steps inside the custom Docker container
                script {
                    docker.image("my_custom_image:${env.BUILD_NUMBER}").inside {
                        // The working directory is automatically set to /app inside the container
                        sh 'pytest --alluredir=reports/allure-results tests/test_alerts.py'
                    }
                }
            }
        }
    }
    
    post {
        always {
            // Clean up after the build
            script {
                sh "docker rmi my_custom_image:${env.BUILD_NUMBER}"
            }
            allure([
            reportBuildPolicy: "ALWAYS",
            results: [[path: "reports/allure-results"]]
            ])
        }
    }
}
