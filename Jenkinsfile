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
                echo 1
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo 2
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
