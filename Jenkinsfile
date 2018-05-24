node {
  stage('SCM') {
    git 'https://github.com/bala151187/python_flask.git'
  }
  stage ('Unit test') {
    bat'python test\\test_app.py'
  }
  stage('SonarQube analysis') {
    // requires SonarQube Scanner 2.8+
    def scannerHome = tool 'GSonar';
    withSonarQubeEnv('My SonarQube Server') {
      bat "\"${scannerHome}\"\\bin\\sonar-scanner"
    }
  }
 
}
