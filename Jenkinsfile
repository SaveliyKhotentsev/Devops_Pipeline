pipeline{
  agent any
  stages{
    stage('Checkout') {
      steps{
        echo 'step Git Checkout'
        checkout scm     
      }
    }
    //Собираем проект
    stage("Build"){
      steps{
        echo 'Building the project'
        sh "python3 -m venv venv"
        sh ". venv/bin/activate"
        sh "pip install --upgrade pip"
        sh "pip install -r requirements.txt"
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
    stage("Pytest"){
      steps{
        echo 'Testing the projects function...'
        sh 'make test'
      }
    }
    //запускаем докер? или нет?
    stage("BuildDocker"){
      steps{
        echo 'Bulidng test conteiner...'
        sh 'make build'
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
        sh 'make smoke'
      }
    }
    //Загружаем проект на сервер
    // Извлекаем проект из Bitbucket 
  }
}





