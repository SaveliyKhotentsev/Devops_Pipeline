pipeline{
    agents any
    stages{
        // Извлекаем проект из Bitbucket 
    stage('Checkout') {
      echo 'step Git Checkout'
      checkout scm
    }
    //Собираем проект
    stage("Build"){
      echo 'Building the project'
      sh 'make'
    }
    //Проверяем синтексис
    stage("SyntaxTest"){
      echo 'Checking syntax'
      sh 'make lint'
    }
    //Проводим тест функций проекта
    stage("Pytest"){
      echo 'Testing the projects function...'
      sh 'make test'
    }
    //запускаем докер? или нет?
    stage("BuildDocker"){
      echo 'Bulidng test conteiner...'
      sh 'make build'
    }
    //Сканируем образ на уязвимости
    stage("TrivyTest"){
      echo 'Finding CVE vulnerabilities...'
      sh 'make scan'
    }
    //Проводим тест докера (запустится ли он, заработает ли на нем приложение)
    stage("SmokeTest"){
      echo 'Testing the conteiner...'
      sh 'make smoke'
    }
    //Загружаем проект на сервер
    stage("Deplopy"){

    }
  }
}





