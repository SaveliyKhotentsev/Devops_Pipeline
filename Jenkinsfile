pipeline{
  agent {
    node { label 'agent1' }
  }
  stages{
    stage('Checkout') {
      steps{
        echo 'step Git Checkout'
        checkout scm     
      }
    }
    //Проверяем синтексис
    stage("Build"){
      steps{
        echo 'Building...'
        sh 'make'
      }
    }
    //Проверяем синтексис
    stage("SyntaxTest"){
      steps{
        echo 'Checking syntax'
        sh 'make lint'
      }
    }
    //Проводим тест функций проекта
    stage("UnitTests"){
      steps{
        echo 'Testing the projects function...'
        sh 'make unit_test'
      }
    }
    stage("Docker-compose"){
      steps{
        echo 'Testing the projects function...'
        sh 'make build'
        sh 'make doc-com'
      }
    }
    stage("IntegrationTests"){
      steps{
        echo 'Testing the projects function...'
        sh 'make integration_test'
      }
    }
    //Сканируем образ на уязвимости
    stage("TrivyTest"){
      steps{
        echo 'Finding CVE vulnerabilities...'
        sh 'make scan'
      }
    }
    //Проводим тест докера (запустится ли он, заработает ли на нем приложение)
    stage("SmokeTest"){
      steps{
        echo 'Testing the conteiner...'
        sh 'make smoke2'
      }
    }
    stage("ImageUpload"){
      steps{
        sh '''
        VERSION=$(python3 -c \
          'import tomllib; print(tomllib.load(open("pyproject.toml", "rb"))["project"]["version"])')
        echo "Application version: $VERSION"
        docker tag flask-demo:latest \
          melidicr2/flask-demo:$VERSION
        docker push melidicr2/flask-demo:$VERSION
        '''
      }
    }
  }
  post {
    always {
      junit 'reports/junit-report.xml'
      archiveArtifacts artifacts: 'reports/**', fingerprint: true
      sh 'make stop_compose'
      cleanWs()
    }
  }
  //Загружаем проект на сервер
  // Извлекаем проект из Bitbucket 
}





