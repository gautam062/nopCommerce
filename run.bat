pytest -v -m "sanity" --html=./Reports/reports.html .\testCases\ --browser chrome
pytest -v -m "regression" --html=./Reports/reports.html .\testCases\ --browser firefox
REM pytest -v -m "sanity and regression" --html=./Reports/reports.html .\testCases\ --browser chrome
REM pytest -v -m "sanity or regression" --html=./Reports/reports.html .\testCases\ --browser chrome