
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
                bat 'if not exist index.html exit /b 1'
                bat 'if not exist tests\\test_registration.py exit /b 1'
                
bat '"C:\\Users\\khemr\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'

            }
        }

        stage('Run Automated Tests') {
            steps {
                
bat '"C:\\Users\\khemr\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m unittest discover -s tests -p "test_*.py" -v'

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
