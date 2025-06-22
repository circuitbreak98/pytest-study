pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Python') {
      steps {
        sh 'python3 -m venv .venv'
        sh '. .venv/bin/activate && pip install -r requirements.txt'
      }
    }

    stage('Run Pytest') {
      steps {
        sh '. .venv/bin/activate && pytest --junitxml=results.xml'
      }
      post {
        always {
          junit 'results.xml'
        }
      }
    }
  }

  post {
    success { echo "✅ Tests passed!" }
    failure { echo "❌ Some tests failed." }
  }
}

