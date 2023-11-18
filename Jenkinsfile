pipeline {
    agent any
    stages {
        stage("Prepare") {
            steps {
                sh "true"
            }
        }
        stage("Build") {
            steps {
                script {
                    gitBranch = sh(script: "git rev-parse --abbrev-ref HEAD", returnStdout: true).trim()
                    gitTag = sh(script: "git tag --points-at HEAD", returnStdout: true).trim()
                    gitCommit = sh(script: "git rev-parse HEAD", returnStdout: true).trim()
                    webImage = docker.build(
                        "192.168.1.14/0mid-net:jenkins-pipeline-$BUILD_ID",
                        "--build-arg GIT_BRANCH=${gitBranch} --build-arg GIT_TAG=${gitTag} --build-arg GIT_COMMIT=${gitCommit} --build-arg BUILD_TAG=${BUILD_TAG} --build-arg BUILD_ID=${BUILD_ID} ."
                    )
                }
            }
        }
        stage("Test") {
            steps {
                script {
                    docker.image("mariadb:11").withRun("--name 0midnet-mariadb-$BUILD_ID -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=mydb") {
                        mariadb ->
                        webImage.inside("--name 0midnet-web-$BUILD_ID --link ${mariadb.id} -e SITE_SECRET_KEY=testsecret -e SITE_DB_NAME=mydb -e SITE_DB_USER=root -e SITE_DB_PASSWORD=rootpass -e SITE_DB_HOST=0midnet-mariadb-$BUILD_ID -e SITE_ENV=production --entrypoint '' ") {
                            i = 1
                            retry(5) {
                                sh "sleep $i"
                                i *= 2
                                sh "python manage.py test --noinput --settings=config.settings.production 2> /dev/null"
                            }
                            coverageStatus = sh (
                                script: "coverage run --source='.' manage.py test --noinput --settings config.settings.production --testrunner xmlrunner.extra.djangotestrunner.XMLTestRunner",
                                returnStatus: true
                            )
                            junit "TEST-*.xml"
                            sh "coverage html"
                            sh "coverage xml"
                            cobertura(
                                autoUpdateHealth: true,
                                autoUpdateStability: true,
                                coberturaReportFile: "coverage.xml"
                            )
                            archiveArtifacts(
                                artifacts: "*.xml,htmlcov/**/*",
                                fingerprint: true
                            )
                            if (coverageStatus != 0) {
                                sh "false"
                            }
                        }
                    }
                }
            }
        }
        stage("Release") {
            steps {
                script {
                    webImage.push("latest")
                    if (gitTag != "") {
                        if (gitTag.startsWith("v")) {
                            gitTag = gitTag.minus("v")
                            webFullVersion = gitTag
                            version = gitTag.split("\\.")
                            webMajorVersion = version[0]
                            webMajorMinorVersion = version[0] + "." + version[1]
                            webImage.push(webFullVersion)
                            webImage.push(webMajorVersion)
                            webImage.push(webMajorMinorVersion)
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            deleteDir()
        }
    }
}