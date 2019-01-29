# -*- coding: utf-8 -*-

from testlink import TestlinkAPIClient, TestLinkHelper, TestGenReporter
from testlink.testlinkerrors import TLResponseError
from xml.etree import ElementTree

"""
to parse xml testcases
to create testcases
"""


def str_replace(string):
    string.replace('<p>', '')
    string.replace('</p>', '')


if __name__ == "__main__":
    tl_helper = TestLinkHelper()
    myTestLink = tl_helper.connect(TestlinkAPIClient)
    dic_temp = {}
    RootProjectId = 1
    tree = ElementTree.parse("./Web测试用例_登录测试.xml")
    dic_temp['FirstSuitename'] = "Base"
    dic_temp['new_testsuite'] = tree._root.attrib['name']
    dic_temp['parent_testsuite'] = "testsuitea"
    response = myTestLink.getFirstLevelTestSuitesForTestProject(RootProjectId)
    print("getFirstLevelTestSuitesForTestProject", response)
    FirstLevelID = ""
    for suites in response:
        if suites['name'] == "Base":
            print("the suite name Base is exist")
            FirstLevelID = suites['id']
        else:
            continue
    if not FirstLevelID:
        newTestSuite = myTestLink.createTestSuite(RootProjectId, response['name'],
                                                  "crteate firstlevelsuite by python")
    else:
        # Creates the test Suite A
        newTestSuite = myTestLink.createTestSuite(RootProjectId, dic_temp['new_testsuite'],
                                                  "crteate form python", parentid=FirstLevelID)
        print("createTestSuite", newTestSuite)
    list_node = tree.getiterator("testcase")
    casenum = len(list_node)
    for case in range(0, casenum):
        steps = list_node[case].find("steps")
        step_num = len(steps)
        keywords = list_node[case].find("keywords")
        if keywords is not None:
            dic_temp['keyword'] = keywords[0].attrib['name']
        else:
            dic_temp['keyword'] = None
        for step in steps:
            list_temp = []
            action = str_replace(step[1].text)
            list_temp.append(action)
            expresult = str_replace(step[2].text)
            list_temp.append(expresult)
            dic_temp[step[0].text] = list_temp
        print("the dic is: \n")
        print(dic_temp)

    # # Creates the test Suite A
    # newTestSuite = myTestLink.createTestSuite(newProjectID, NEWTESTSUITE_A,
    #                                           "Details of the Test Suite A")
    # print("createTestSuite", newTestSuite)
    # newTestSuiteID_A = newTestSuite[0]['id']
    # print("New Test Suite '%s' - id: %s" % (NEWTESTSUITE_A, newTestSuiteID_A))
    #
    # FirstLevelID = newTestSuiteID_A
    #
    # # Creates the test Suite AA
    # newTestSuite = myTestLink.createTestSuite(newProjectID, NEWTESTSUITE_AA,
    #                                           "Details of the Test Suite AA", parentid=FirstLevelID)
    # print("createTestSuite", newTestSuite)
    # newTestSuiteID_AA = newTestSuite[0]['id']
    # print("New Test Suite '%s' - id: %s" % (NEWTESTSUITE_AA, newTestSuiteID_AA))
    # # Creates the test case TC_AA  with state ready for review
    # myTestLink.initStep("Step action 1", "Step result 1", MANUAL)
    # myTestLink.appendStep("Step action 2", "Step result 2", MANUAL)
    # myTestLink.appendStep("Step action 3", "Step result 3", MANUAL)
    # myTestLink.appendStep("Step action 4", "Step result 4", MANUAL)
    # myTestLink.appendStep("Step action 5", "Step result 5", MANUAL)
    # myTestLink.appendStep("Dummy step for delete tests",
    #                       "should be delete with deleteTestCaseSteps", MANUAL)
    #
    # newTestCase = myTestLink.createTestCase(NEWTESTCASE_AA, newTestSuiteID_AA,
    #                                         newProjectID, myTestUserName, "This is the summary of the Test Case AA",
    #                                         preconditions='these are the preconditions',
    #                                         importance=LOW, state=READFORREVIEW, estimatedexecduration=10.1)
    # print("createTestCase", newTestCase)
    # newTestCaseID_AA = newTestCase[0]['id']
    # print("New Test Case '%s' - id: %s" % (NEWTESTCASE_AA, newTestCaseID_AA))
