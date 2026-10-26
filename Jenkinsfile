
pipeline {
    agent any

    stages {
        stage('Checkout from GitHub') {
            steps {
                checkout scm
            }
        }

        stage('Verify Project Files') {
            steps {
                bat 'python --version'
                bat 'if not exist index.html exit /b 1'
                bat 'if not exist tests\\test_registration.py exit /b 1'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat 'python -m unittest discover -s tests -p "test_*.py" -v'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Student registration form tests passed.'
        }
        failure {
            echo 'FAILURE: Check the console output for errors.'
        }
    }
}
