pipeline {
 agent none 
 stages {
  stage('SCM') {
   steps{
    git 'https://github.com/bala151187/python_flask.git'
   }
  }
  stage ('Unit test using coverage') {
   steps{
    bat'coverage run test_webs.py'
    bat'coverage xml -i'
   }
  }
  stage('SonarQube analysis') {
    environment { 
     scannerHome = tool 'GSonar';
    }
   steps{
    // requires SonarQube Scanner 2.8+  
    withSonarQubeEnv('My SonarQube Server') {
      bat "\"${scannerHome}\"\\bin\\sonar-scanner"
    }
   }
  }
stage("Quality Gate"){
 steps{
    withSonarQubeEnv('My SonarQube Server') {
      timeout(time: 1, unit: 'MINUTES') {
       environment {
       qualitygate = waitForQualityGate()
       }
      if (qualitygate.status != "OK") {
         error "Pipeline aborted due to quality gate coverage failure: ${qualitygate.status}"
      }
      }
    }      
  }
}
    
stage('Aprove') {
 steps{
    timeout(time: 1, unit: 'MINUTES') {
    emailext (
      to: 'balamurugan151187@gmail.com',
      subject: 'Job status',
      body: 'Approve'
    )
   }
 }
}
 }
}
