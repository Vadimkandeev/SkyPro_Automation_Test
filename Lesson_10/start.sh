result=./results
rep_history=./final-report/rep_history
report=./final-report

rm -fr $results
pytest --alluredir=$results
mv $rep_history $results
rm -rf $report
allure generate $results -o $report
allure open $report
