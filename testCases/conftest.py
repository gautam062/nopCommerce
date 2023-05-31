import os
from selenium import webdriver
import pytest
import pytest_html


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("*******Launching Chrome*********")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("*******Launching Firefox*********")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("*******Launching Edge*********")
    else:
        driver = webdriver.Chrome()
        print("*******Default Launching Chrome*********")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


################# PyTest HTML Report ###################

# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata["Project Name"] = "nop Commerce"
#     config._metadata["Module Name"] = "Customers"
#     config._metadata["Tester"] = "Gautam Kumar"
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#     if report.when == "call":
#         # always add url to report
#         extras.append(pytest_html.extras.url("https://admin-demo.nopcommerce.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure+
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             destFile = os.path.join(report_directory, file_name)
#             driver.save_screenshot(destFile)
#             if file_name:
#                 html= '<div><img src=%s" alt="screenshot" style = "width:300ox;height=200px"'\
#                 'onlick="window.open(this.src" align="right"/></div>'%file_name
#             extras.append(pytest_html.extras.html(html))
#         report.extras = extras

def pytest_html_report_title(report):
    report.title = "Nop Commerce Automation Report"