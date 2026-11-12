
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\sanja\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Check Python') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '"%PYTHON%" -m unittest -v test_game.py'
            }
        }

        stage('Launch Tic Tac Toe') {
            steps {
                bat 'start "" "%PYTHON%" tic_tac_toe.py'
            }
        }
    }

    post {
        success {
            echo 'All stages completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}
