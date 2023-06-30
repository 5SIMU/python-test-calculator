pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from the repository
                // Replace the placeholder with your actual repository URL
                git 'https://github.com/5SIMU/python-test-calculator.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install required Python packages
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run pytest with Selenium tests
                sh 'pytest'
            }
        }
    }
}
