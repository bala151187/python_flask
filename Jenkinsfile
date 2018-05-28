 
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
       timeout(time: 1, unit: 'MINUTES') {
        def qualitygate = waitForQualityGate()       
         if (qualitygate.status != "OK") {
           error "Pipeline aborted due to quality gate coverage failure: ${qualitygate.status}"
      }
    }
  }
}
    
stage('Notifying Jenkin Job') {
    timeout(time: 1, unit: 'MINUTES') {
    emailext (
      to: 'balamurugan151187@gmail.com',
      subject: 'Job Details',
      body: ' http://jenkins/job/job_name_being_promoted/77'
    )
   }
}
   stage ('Deployment') {

  }
}
