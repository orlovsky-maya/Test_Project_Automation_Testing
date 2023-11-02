#!/bin/sh

while [ "$(curl -s "http://firefox_grid:4444/status" | jq -r .value.ready)" != "true" ]; do
    sleep 1
done

pytest -v --alluredir=allure_test_results

# Prompt:
# pytest -rxXs  # show extra info on xfailed, xpassed, and skipped tests
# Run test with mark -m login_guest
# Run test --tb=line - only one line per failure

# Commands with allure attribute:
#pytest -v -s --alluredir=allure_test_results ./Tests/test_buy_product.py
#pytest -v -s --alluredir=allure_test_results ./Tests/test_link_about.py
#pytest -v --alluredir=allure_test_results ./Tests/test_buy_product.py
#pytest -v --alluredir=allure_test_results ./Tests/test_link_about.py


