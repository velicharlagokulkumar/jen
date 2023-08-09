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
                echoo 'Im Deploy'
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
