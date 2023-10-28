pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            echo 'Im Build'
          }
        }

        stage('jhgf') {
          steps {
            sh 'echo sdasdhh'
          }
        }

        stage('asdfjhyt') {
          steps {
            sh 'echo sabi'
          }
        }

      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            echo 'Im test'
          }
        }

        stage('qewt') {
          steps {
            sh 'echo sasdf'
          }
        }

        stage('asdfas') {
          steps {
            sh 'echo asdf'
          }
        }

      }
    }

    stage('Deploy') {
      parallel {
        stage('Deploy') {
          steps {
            echo 'Im Deploy'
          }
        }

        stage('asdhhh') {
          steps {
            sh 'echo hwllo'
          }
        }

        stage('stage33') {
          steps {
            sh 'echo \'hellow\''
          }
        }

      }
    }

  }
}