pipeline{
    agent{
        node(label = 'agent1')
    }
    stages{
        stage('Checkout') {
            steps{
                echo 'step Git Checkout'
                checkout scm     
            }
        }
        stage('Build'){
            steps{
                sh 'make'
                sh 'make build'
            }
        }
        stage("Deploy"){
            steps{  
                sh 'docker image ls | grep flask-demo'
                
                sh 'kubectl apply -f kb8/deployment.yaml'
                sh 'kubectl apply -f kb8/service.yaml'
                
                sh 'kubectl get deployments'
                sh 'kubectl get service'

                sh 'kubectl get pods -o wide'
                sh 'kubectl describe pods'

                sh 'kubectl rollout status deployment/flask-deployment --timeout=120s'
            }          
        }
    }
}
