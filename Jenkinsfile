pipeline {
    agent any
    
    tools {
        // Asegúrate de que en 'Global Tool Configuration' instalaste el scanner
        // y le pusiste EXACTAMENTE este nombre:
        org.sonarsource.scanner.jenkins.runner.SonarScannerBuildWrapper 'sonar-scanner' 
        // Si te da error en la línea de arriba, prueba simplemente con:
        // sonarScanner 'sonar-scanner'
        // (Depende de la versión del plugin, lo explico abajo en notas)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
         
        stage('Build Image') {
            steps {
                sh 'docker build -t fase1:latest .'
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Limpieza: Si existe el contenedor, lo borra. Si no, no pasa nada (|| true)
                    sh 'docker rm -f test-container || true'
                    // Arranca el nuevo
                    sh 'docker run --name test-container -d fase1:latest'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Obtenemos la herramienta configurada en Jenkins (Tools)
                    // Nombre debe coincidir con el que pusiste en Jenkins (ej: 'sonar-scanner')
                    def scannerHome = tool 'sonar-scanner' 
                    
                    // Nombre debe coincidir con el que pusiste en System -> SonarQube servers (ej: 'sonar-server')
                    withSonarQubeEnv('sonar-server') {
                        sh """
                        ${scannerHome}/bin/sonar-scanner \
                        -Dsonar.projectKey=proyecto-python \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://localhost:9000
                        """
                    }
                }
            }
        }
    }
}
