#!/usr/bin/python
# -*- coding:utf-8 -*-
# author:zhongqionglun
# datetime:2019/3/23

'''
Testlink API Sample getProjects() - Client implementation
'''

import xmlrpc.client
from testlink import TestLinkHelper, TestlinkAPIClient


class MyTestlinkAPIClient:
    # substitute your server URL Here
    SERVER_URL = "http://localhost/testlink/lib/api/xmlrpc/v1/xmlrpc.php"

    def __init__(self, devKey):
        self.server = xmlrpc.client.ServerProxy(self.SERVER_URL)
        self.devKey = devKey

    def getInfo(self):
        return self.server.tl.about()

    def getProjects(self):
        return self.server.tl.getProjects(dict(devKey=self.devKey))


# substitute your Dev Key Here
client = MyTestlinkAPIClient("51a3030666be72e3aaaf8534ef97d530")

# get info about the server
print(client.getInfo())

projectnames = []
for x in client.getProjects():
    projectnames.append(x['name'])
    # print("The project is: %s" %  x['name'])
print(projectnames)
tl_helper = TestLinkHelper()
tl_helper.setParamsFromArgs('''Shows how to use the TestLinkAPI.
=> Counts and lists the Projects 
=> Create a new Project with the following structure:''')
myTestLink = tl_helper.connect(TestlinkAPIClient)

# get information - TestProject
for x in client.getProjects():
    response = myTestLink.getTestProjectByName(x['name'])
    print("getTestProjectByName", response)
    response = myTestLink.getProjectTestPlans(x['id'])
    print("getProjectTestPlans", response)
# response = myTestLink.getFirstLevelTestSuitesForTestProject(newProjectID)
# print("getFirstLevelTestSuitesForTestProject", response)
# response = myTestLink.getProjectPlatforms(newProjectID)
# print("getProjectPlatforms", response)
# response = myTestLink.getProjectKeywords(newProjectID)
# print("getProjectKeywords", response)
