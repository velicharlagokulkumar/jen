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
                cd C:\Users\velic\OneDrive\jen
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
