node('229') {

   stage('Preparation') {
       git credentialsId: '6a944868-6bf7-445e-aa78-94b233e043e4', url: 'http://gitlab.caibaopay.com/dengmingyao/testcase_PCCashier_APITest.git'
       git pull
    }

   stage('Build') {
       sh '''#!/bin/bash

cd ..

source httpruner_venv/bin/activate

cd PCCashier_APITest

hrun --dot-env-path devlop.env --html-report-name index_dev.html tests/testcases/'''
   }

   stage('Results') {
       publishHTML([allowMissing: true, alwaysLinkToLastBuild: false, includes: '**/*.html', keepAll: true, reportDir: '/home/jenkins/work/workspace/PCCashier_APITest/reports', reportFiles: 'index_dev.html', reportName: '接口测试报告', reportTitles: 'PC收银台接口测试报告'])
   }
}