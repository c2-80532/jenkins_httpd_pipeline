pipeline {
    agent any

    stages {
        stage ('SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/c2-80532/jenkins_httpd_pipeline.git'
            }
        }
        stage ('docker login') {
            steps {
                sh 'echo dckr_pat_3a6jflttElXRXFZGMK4pYLi2eK4 | /usr/bin/docker login -u shubhamchau --password-stdin'
            }
        }
        stage ('docker build image') {
            steps {
                sh '/usr/bin/docker build -t shubhamchau/flask:1.0 .'
            }
        }
        stage ('docker push image') {
            steps {
                sh '/usr/bin/docker image push shubhamchau/flask:1.0'
            }
        }
        stage ('docker remove service') {
            steps {
                sh '/usr/bin/docker service rm mybuildsrv'
            }
        }
        stage ('docker create service') {
            steps {
                sh '/usr/bin/docker service create --name myflask -p 9000:80 --replicas 5  shubhamchau/flask:1.0'
            }
        }
    }
}

