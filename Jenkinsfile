pipeline {
    agent any
    stages {
        stage("Prepare") {
            steps {
                load "jenkins/config.groovy"
                dir(pwd(tmp: true)) {
                    git(
                        url: "$PROJECT_CI_CONFIG_GIT_URL",
                        branch: "$PROJECT_CI_CONFIG_GIT_BRANCH",
                        credentialsId: "$PROJECT_CI_CONFIG_GIT_CREDENTIALS",
                        changelog: true,
                        poll: true
                    )
                    load "config.groovy"
                }
            }
        }
        stage("Build") {
            steps {
                script {
                    gitBranch = sh(script: "git rev-parse --abbrev-ref HEAD", returnStdout: true).trim()
                    gitTag = sh(script: "git tag --points-at HEAD", returnStdout: true).trim()
                    gitCommit = sh(script: "git rev-parse HEAD", returnStdout: true).trim()
                    webImage = docker.build(
                        "${PROJECT_DOCKER_REGISTRY_ADDRESS}/${PROJECT_IMAGE_NAME}:jenkins-pipeline-${BUILD_ID}",
                        "--build-arg GIT_BRANCH=${gitBranch} --build-arg GIT_TAG=${gitTag} --build-arg GIT_COMMIT=${gitCommit} --build-arg BUILD_TAG=${BUILD_TAG} --build-arg BUILD_ID=${BUILD_ID} ."
                    )
                }
            }
        }
        stage("Test") {
            steps {
                script {
                    docker.image("${PROJECT_DB_IMAGE}").withRun("--name 0midnet-db-$BUILD_ID -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=mydb") {
                        mariadb ->
                        webImage.inside("--name 0midnet-web-$BUILD_ID --link ${mariadb.id} -e SITE_SECRET_KEY=testsecret -e SITE_DB_NAME=mydb -e SITE_DB_USER=root -e SITE_DB_PASSWORD=rootpass -e SITE_DB_HOST=0midnet-db-$BUILD_ID -e SITE_ENV=production --entrypoint '' ${PROJECT_CONTAINER_EXTRA_ARGS}") {
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
                            if ("${PROJECT_REPORT_UNIT_TEST_RESULTS}" == "true") {
                                junit "TEST-*.xml"
                            }
                            sh "coverage html"
                            sh "coverage xml"
                            if ("${PROJECT_REPORT_CODE_COVERAGE}" == "true") {
                                cobertura(
                                autoUpdateHealth: true,
                                autoUpdateStability: true,
                                coberturaReportFile: "coverage.xml"
                                )
                            }
                            if ("${PROJECT_ARCHIVE_ARTIFACTS}" == "true") {
                                archiveArtifacts(
                                artifacts: "*.xml,htmlcov/**/*",
                                fingerprint: true
                                )
                            }
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
                    if ("${PROJECT_LATEST_IMAGE_RELEASE}" == "true") {
                        webImage.push("latest")
                    }
                    if ("${PROJECT_BRANCH_IMAGE_RELEASE}" == "true") {
                        webImage.push(gitBranch)
                    }
                    if (gitTag != "") {
                        if (gitTag.startsWith("v")) {
                            gitTag = gitTag.minus("v")
                            webFullVersion = gitTag
                            version = gitTag.split("\\.")
                            webMajorVersion = version[0]
                            webMajorMinorVersion = version[0] + "." + version[1]
                            if ("${PROJECT_VERSION_IMAGE_RELEASE}" == "true") {
                                webImage.push(webMajorVersion)
                                webImage.push(webMajorMinorVersion)
                            }
                            if ("${PROJECT_TAG_IMAGE_RELEASE}" == "true") {
                                webImage.push(webFullVersion)
                            }
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