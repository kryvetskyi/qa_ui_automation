pipeline {
    agent { docker { image 'python:3.9' }}

    stages {
        
        stage('Build') {
            steps {
                echo 'running the app'
            }
        }    
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
        stage('Finish') {
            steps {
                sh 'pip --version'
            }
        }
        
    }
}
