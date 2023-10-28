pipeline {
  agent any
  stages {
          parallel {
    stage('agfb014') {
   agent any
        stage('Setup_f') {
          steps {
            echo 'setup_f'
          }
        }

        stage('qsys_f') {
          steps {
            echo 'qsys_F'
          }
        }

        stage('sof_f') {
          steps {
            echo 'sof_f'
          }
        }

        stage('build_f') {
          steps {
            echo 'build_f'
          }
        }

        stage('Deploy_f') {
          steps {
            echo 'Deploy_f'
          }
        }
    }

    stage('agib027') {
  agent any
        stage('Setup_i') {
          steps {
            echo 'setup_i'
          }
        }

        stage('qsys_i') {
          steps {
            echo 'qsys_i'
          }
        }

        stage('sof_i') {
          steps {
            echo 'sof_i'
          }
        }

        stage('build_i') {
          steps {
            echo 'build_i'
          }
        }

        stage('Deploy_i') {
          steps {
            echo 'Deploy_i'
          }
        }
    }

    stage('hitek') {
  agent any
        stage('Setup_h') {
          steps {
            echo 'setup_h'
          }
        }

        stage('qsys_h') {
          steps {
            echo 'qsys_h'
          }
        }

        stage('sof_h') {
          steps {
            echo 'sof_h'
          }
        }

        stage('build_h') {
          steps {
            echo 'build_h'
          }
        }

        stage('Deploy_h') {
          steps {
            echo 'Deploy_h'
          }
        }
    }
   }
  }
}
