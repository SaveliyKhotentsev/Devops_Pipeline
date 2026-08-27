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
                //sh 'docker image ls | grep flask-demo'
                //sh 'minikube image load flask-demo:latest'
                
                sh 'kubectl apply -f kb8/deployment.yaml'
                sh 'kubectl apply -f kb8/service.yaml'
                
                sh 'kubectl get deployments'
                sh 'kubectl get service'

                sh 'kubectl get pods -o wide'
                sh 'kubectl describe pods'

                sh 'kubectl rollout status deployment/flask-deployment --timeout=120s'
            }          
        }
        stage("SmokeTest"){
            steps{
                sh '''
                    echo "Checking Kubernetes pods..."
                    kubectl get pods

                    echo "Checking services..."
                    kubectl get svc

                    NODE_IP=$(kubectl get node minikube \
                        -o jsonpath='{.status.addresses[?(@.type=="InternalIP")].address}')
                    echo "Minikube IP: $NODE_IP"

                    NODE_PORT=$(kubectl get service flask-service \
                        -o jsonpath='{.spec.ports[0].nodePort}')
                    echo "NodePort: $NODE_PORT"

                    curl --fail http://$NODE_IP:$NODE_PORT/health
                '''
            }
        }
    }
}
