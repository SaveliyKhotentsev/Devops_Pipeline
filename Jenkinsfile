pipeline{
  stages{
    // Извлекаем проект из Bitbucket 
    stage('Checkout') {
      echo 'step Git Checkout'
      checkout scm
    }
    //Собираем проект
    stage("Build"){
      sh 'pip install -r requirements.txt'
    }    
    //Проводим тесты проекта
    stage("Test"){

    }
    //Загружаем проект на сервер
    stage("Deplopy"){

    }
  }
}






