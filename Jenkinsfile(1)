pipeline {
    agent any
    stages {
        // Quitamos la etapa 'Checkout' manual porque Jenkins ya la hace al principio
        
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube Scanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner \
                        -Dsonar.projectKey=agenda-goles \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://sonarqube:9000"
                    }
                }
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t fase1:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f test-container || true'
                sh 'docker run --name test-container -d fase1:latest'
            }
        }
    }
}
