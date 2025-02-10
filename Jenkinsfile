pipeline {
   agent any
 
   environment {
       AWS_REGION = 'us-east-1'  
       FUNCTION_NAME = 'CI-CD-Test-Function'
   }
 
   stages {
       stage('Checkout Code') {
           steps {
               git branch: 'main', url: 'https://github.com/Navikenz-testing/CI-CD-Test-Function-Public.git'
           }
       }
 
       stage('Install Dependencies & Package Code') {
           steps {
               sh '''
               cp -r * package/
               cd package && zip -r ../lambda_package.zip .
               '''
           }
       }
 
       stage('Deploy to AWS Lambda') {
           steps {
               withAWS(credentials: 'aws-credentials', region: "${AWS_REGION}") {
                   sh '''
                   aws lambda update-function-code --function-name ${FUNCTION_NAME} --zip-file fileb://lambda_package.zip
                   '''
               }
           }
       }
   }
}
 
