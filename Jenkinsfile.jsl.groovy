pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Error') {
            steps {
                sh 'error.exe'
            }
        }
        stage('Source') {
            steps {
                git 'https://github.com/Anselm82/unir-cicd.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('Api tests') {
            steps {
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('E2E tests') {
            steps {
                sh 'make test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }

    }
    post {
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }
        failure {  
            emailext body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}",
                subject: "ERROR CI: Project name -> ${env.JOB_NAME}",
                from: 'juanjose.hernandez886@comunidadunir.net',
                recipientProviders: [requestor()]
        }  
    }
}
