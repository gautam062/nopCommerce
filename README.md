# nopCommerce
Selenium Hybrid Framework
(Python, Selenium, PyTest, Page Object Model, HTML Report)
Step 1: Create new Project and Install Required Packages/Plugins
•	Selenium: Selenium Libraries
•	PyTest: Python Unit Test Framework
•	Pytest-html: PyTest HTML Reports
•	Pytest-xdist: Run Tests Parallel
•	Openpyxl: Excel Support
•	Allure-pytest: for generating allure reports
Step 2: Create Folder Structure
Project Name
		|
		pageObjects(Package) 
 	| 
 	testCases(Package)
 	| 
 	utilities(Package)
 	|
 	TestData(Folder)
 	|
		Configurations(Folder) 
 	| 
 	logs(Folder)
 	| 
 	screenshots(Folder)
 	|
 	Reports(Folder)
 	|
 	Run.bat
Step 3: Automating Login Test Case
	3.1: Create LoginPage Object class under pageObjects
	3.2: Create LoginTest under testCases
	3.3: Create conftest.py under testCases
Step 4: Capture Screenshots on failure
	4.1: Update LoginTest with screenshot under testCases


Step 5: Read common values from ini file
	5.1: Add config.ini file in Configurations folder
	5.2: Create readProperties.py utility file under utilities package to read concern data
	5.3: Replace hard coded values in Login Test case
Step 6: Adding logs to test case
6.1: Add customLogger.py under utilities package
6.2: Add logs to Login Test case 
Step 7: Run Tests on Desired Browser/Cross Browser/Parallel
	7.1: Update conftest.py with required fixture which will accept command line argument (browser)
	7.2: Pass browser name as argument in command line
To run tests on desired browser 
pytest –s –v testCases/test_login.py --browser chrome
pytest –s –v testCases/test_login.py --browser firefox
To run tests parallel
pytest –s –v –n=2 testCases/test_login.py --browser chrome
pytest –s –v –n=3 testCases/test_login.py --browser firefox
Step 8: Generate pytest HTML Reports
	8.1: Update conftest.py with pytest hooks
	8.2: To generate HTML report run below command
pytest –s –v –n=3 –html=Reports\report.html testCases/test_login.py --browser firefox 
Step 9: Automating Data Driven Test Case 
	9.1: Prepare test data in Excel sheet, place the excel file inside TestData folder
	9.2: Create ExcelUtils.py utility class under utilities package
	9.3: Create LoginDataDrivenTest under testCases
	9.4: Run the test case 
Step 10: Adding new testcases
Step 11: Grouping Tests
	11.1: Grouping markers (Add markers to every test method)
	@pytest.mark.sanity
	@pytest.mark.regression
 
11.2: Add Marker entries in pytest.ini file
pytest.ini
-------------
[pytest]
markers = 
		sanity
		regression
	11.3: Select groups at run time
	-m ”sanity”
	-m ”regression”
	-m ”sanity and regression”
	-m ”sanity or regression”
Step 12: Run Tests in Command Prompt and run.bat file
	12.1: Create run.bat file 
pytest –s –v –m “sanity” --html=Reports\report.html testCases/test_login.py --browser firefox 
	12.2: Open command prompt as Administrator and then run run.bat file 
Step 13: Push the code to Git and GitHub Repository 
Initial Steps (only one time)
	1) git init  Create an Empty git repository (Local repository)
	2) git remote add origin gitRepositoryURL
Before doing commit first time we need to execute these below commands
	git config –global user.name “Gautam Kumar”
	git config –global user.email “Gautam.kumar062@gmail.com”

	3) git status 
	4) git add .  add all the files in to staging/indexing area
	5) git commit –m “comment”
	6) git push –u origin master
Day to day commands
	1) git status 
	2) git add . 
	3) git commit –m “comment”
	4) git push –u origin master
     git pull  pull all the files from github to local
Step 14: Run Tests using Jenkins
