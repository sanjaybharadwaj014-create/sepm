
pipeline {
    agent any

    stages {

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python -m unittest -v test_game.py'
            }
        }

        stage('Launch Tic Tac Toe') {
            steps {
                powershell '''
                    Start-Process -FilePath "python" `
                        -ArgumentList "tic_tac_toe.py" `
                        -WorkingDirectory "$env:WORKSPACE"
                '''
            }
        }
    }

    post {
        success {
            echo 'Tic Tac Toe pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
