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
        def ceTask
        timeout(time: 1, unit: 'MINUTES') {
          waitUntil {
            sh 'curl -u $SONAR_AUTH_TOKEN $SONAR_CE_TASK_URL -o ceTask.json'
            ceTask = jsonParse(readFile('ceTask.json'))
            echo ceTask.toString()
            return "SUCCESS".equals(ceTask["task"]["status"])
          }
        }
        def qualityGateUrl = env.SONAR_HOST_URL + "/api/qualitygates/project_status?analysisId=" + ceTask["task"]["analysisId"]
        sh "curl -u $SONAR_AUTH_TOKEN $qualityGateUrl -o qualityGate.json"
        def qualitygate = jsonParse(readFile('qualityGate.json'))
        echo qualitygate.toString()
        if ("ERROR".equals(qualitygate["projectStatus"]["status"])) {
          error  "Quality Gate failure"
        }
        echo  "Quality Gate success"
    }
  }

    
stage('approve') {
    timeout(time: 1, unit: 'MINUTES') {
        input message: 'Do you want to continue?'
    }
}
   stage ('Deployment') {

  }
}
