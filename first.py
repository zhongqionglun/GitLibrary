# -*- coding: utf-8 -*-


"""
The first script for TestLink
shows how to use the TestLinkAPI
change the DEFAULT_SERVER_URL and DEFAULT_DEVKEY in testlinkhelper.py
"""

from testlink import TestlinkAPIClient, TestLinkHelper,TestGenReporter
from testlink.testlinkerrors import TLResponseError
from platform import python_version
import os.path, sys

tl_helper = TestLinkHelper()
# tl_helper.setParamsFromArgs()
myTestLink = tl_helper.connect(TestlinkAPIClient)
# print(myTestLink.connectionInfo())
# print("")
myPyVersion = python_version()
myPyVersionShort = myPyVersion.replace('.', '')[:2]
print(myPyVersion)
myTLVersion = myTestLink.testLinkVersion()
# print(myTLVersion)

# use a valid account in  TestLink
myTestUserName="admin"
# myTestUserName2="tester01"
# get user information
response = myTestLink.getUserByLogin(myTestUserName)
print("getUserByLogin", response)
# myTestUserID=response[0]['dbID']
# print(myTestUserID)
# response = myTestLink.getUserByID(myTestUserID)
# print("getUserByID   ", response)

# example asking the api client about methods arguments
#print(myTestLink.whatArgs('assignTestCaseExecutionTask'))

# Creates the project
# myApiVersion='%s v%s' % (myTestLink.__class__.__name__ , myTestLink.__version__)
# NEWPROJECT="NEW_PROJECT_API-%s" % myPyVersionShort
NEWPREFIX="NPROAPI%s" % myPyVersionShort
# projInfo = 'Example created with Python %s API class %s in TL %s' % \
#             ( python_version(), myApiVersion, myTLVersion )
# newProject = myTestLink.createTestProject(NEWPROJECT, NEWPREFIX,
#     notes=projInfo, active=1, public=1,
# #    itsname=ITSNAME, itsenabled=1,
#     options={'requirementsEnabled' : 0, 'testPriorityEnabled' : 1,
#              'automationEnabled' : 1, 'inventoryEnabled' : 0})
# print("createTestProject", newProject)
# newProjectID = newProject[0]['id']
# print("New Project '%s' - id: %s" % (NEWPROJECT,newProjectID))
# print("getIssueTrackerSystem", aITS)
# Delete the project, if it already exists
# try:
#     response = myTestLink.deleteTestProject(NEWPREFIX)
#     print("deleteTestProject", response)
# except TLResponseError:
#     print("No project with prefix %s exists" % NEWPREFIX)

# # get IssueTrackerSystem
# aITS=myTestLink.getIssueTrackerSystem(aITSNAME)
