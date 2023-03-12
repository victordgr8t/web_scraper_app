pipeline {
    agent any
    environment {
        MONGO_DB_URL = 'mongodb://admin:Pacman111!@localhost:27017/web_scraper_db'
        MONGO_DB_COLLECTION = 'web_scraper_collection'
    }
    stages {
        stage('Build') {
            steps {
                // Clone the Git repository
                git url: 'https://github.com/victordgr8t/web_scraper_app.git', branch: 'main'
                // Install dependencies
                sh 'apt-get update'
                sh 'apt-get install -y python3-pip'
                sh 'pip3 install -r requirements.txt'
                // Run the Python script to scrape data from the website
                sh 'python3 web_scraper.py'
            }
        }
        stage('Performance Test') {
            steps {
                script {
                    def startTime = new Date().getTime()
                    sh 'python3 web_scraper.py'
                    def endTime = new Date().getTime()
                    def duration = (endTime - startTime) / 1000.0
                    echo "Web scraping took ${duration} seconds"
                }
            }
        }
        stage('Deploy') {
            steps {
                // Add deployment steps here (e.g., copy data to a website or database)
                sh 'mongo $MONGO_DB_URL --eval "db.$MONGO_DB_COLLECTION.find()"'
            }
        }
    }
    post {
        // Trigger another build if the pipeline fails
        failure {
            echo "Pipeline failed - sending email..."
            mail to: 'sparkmindconcepts@gmail.com',
                 subject: 'Pipeline failed Try again',
                 body: 'The pipeline for the Python web scraper project failed. Please investigate.'
            echo "Email sent"
            build job: 'Python Web Scraper', wait: false
        }
    }
}
