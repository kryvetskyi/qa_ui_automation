docker run -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS=3 -e KEEP_HISTORY=1 \
                 -v /data/allure-results:/app/reports/allure-results \
                 -v /data/allure-results/:/app/default-reports \
                 frankescobar/allure-docker-service
