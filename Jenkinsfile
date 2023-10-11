pipeline {
        agent any
        stages {

        stage('Récupération du code source') {
            steps {
                git branch: 'master',
                url : 'https://github.com/salemhadd/Flask-API.git';
               /* git 'https://github.com/votre-utilisateur/votre-depot.git' */
            }
        }
    stage('Affichage de la date système') {
            steps {
                // Afficher la date système
                script {
                    def date = new Date()
                    echo "Date systeme est : ${date}"
                }
            }
        }

    }
    triggers {
        // Déclencher le pipeline lorsqu'un push est détecté dans Git
        cron('*/1 * * * *') // Vérification toutes les 5 minutes
    }

}