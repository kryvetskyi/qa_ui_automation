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
                ls -l
                pip install --upgrade -r requirements.txt
                echo 0
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                pwd
                ls -l
                сd pages
                pwd
                ls -l
                python3 test_jenkins.py
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
