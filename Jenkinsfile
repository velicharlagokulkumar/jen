pipeline  
{
    agent any
    stages 
    {
        stage('Build') 
        {
            steps 
            {
                echo 'Im Build'
                git branch: 'main', url: 'https://github.com/velicharlagokulkumar/jen.git'
                echo %python% 
            }
        }
        
        stage('Test') 
        {
            steps 
            {
                echo 'Im test'
            }
        }
        
        stage('Deploy') 
        {
            steps 
            {
                echo 'Im Deploy'
            }
        }
    }
      post 
       {
            always 
                {
                   bat 'echo "Completed"'
                }
       }
}
