#!/bin/sh

while [ "$(curl -s "http://firefox_grid:4444/status" | jq -r .value.ready)" != "true" ]; do
    sleep 1
done

pytest --browser_name=firefox --run_tests=docker -v -s --alluredir=allure_test_results/firefox

while [ "$(curl -s "http://chrome_grid:4444/status" | jq -r .value.ready)" != "true" ];
do
    sleep 1
done

pytest --browser_name=chrome --run_tests=docker -v -s --alluredir=allure_test_results/chrome
