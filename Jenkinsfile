pipeline{
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
    //Проводим тесты проекта
    stage("Test"){
      echo 'Testing the project'
      sh 'make test'
    }
    //Загружаем проект на сервер
    stage("Deplopy"){

    }
  }
}






