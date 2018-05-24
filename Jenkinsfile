node {
  stage('SCM') {
    git 'https://github.com/bala151187/python_flask.git'
  }
  stage ('Unit test using coverage') {
    bat'coverage run test_webs.py'
    bat'coverage xml -i'
  }
  stage('SonarQube analysis') {
    // requires SonarQube Scanner 2.8+
    def scannerHome = tool 'GSonar';
    withSonarQubeEnv('My SonarQube Server') {
      bat "\"${scannerHome}\"\\bin\\sonar-scanner"
    }
  }
stage("Quality Gate"){
  
    withSonarQubeEnv('My SonarQube Server') {
       def qualitygate = waitForQualityGate()
      if (qualitygate.status != "OK") {
         error "Pipeline aborted due to quality gate coverage failure: ${qualitygate.status}"
      }
    }      
  }

    
stage('approve') {
    timeout(time: 1, unit: 'MINUTES') {
      step([$class: 'Mailer', notifyEveryUnstableBuild: false, recipients: 'balamurugan151187@gmail.com', sendToIndividuals: true])
    }
}
  
   stage ('Deployment') {

  }
}
