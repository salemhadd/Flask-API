pipeline {
        agent any
        stages {

        stage('Récupération du code source') {
            steps {
                echo 'Pulling';
                git branch: 'master',
                url : 'https://github.com/mhassini/avec-maven.git';
                git 'https://github.com/votre-utilisateur/votre-depot.git'
            }
        }
    stage('Affichage de la date système') {
            steps {
                // Afficher la date système
                script {
                    def date = new Date()
                    echo "Date système : ${date}"
                }
            }
        }

    }
    triggers {
        // Déclencher le pipeline lorsqu'un push est détecté dans Git
        scm('*/5 * * * *') // Vérification toutes les 5 minutes
    }

}