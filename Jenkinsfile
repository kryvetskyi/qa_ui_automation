pipeline {
    agent { 
        node {
            label 'test-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd pages
                pip install requirements.txt
                echo 0
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                python test_jemkins.py
                echo 'Done'
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
