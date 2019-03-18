# -*-coding:UTF-8-*-


from bs4 import BeautifulSoup
import testlink


class ReportTestLink(object):
    def __init__(self):
        self.tls = None

    def connect_testlink(self, TESTLINK_API_PYTHON_SERVER_URL, TESTLINK_API_PYTHON_DEVKEY):
        '''
        :param TESTLINK_API_PYTHON_SERVER_URL: testlink的接口地址 如：http://IP:PORT/lib/api/xmlrpc/v1/xmlrpc.php
        :param TESTLINK_API_PYTHON_DEVKEY: 2e9685efd7d2589b50987f00dc9d10d7 接口秘钥
        :return:
        '''
        try:
            self.tls = testlink.TestlinkAPIClient(TESTLINK_API_PYTHON_SERVER_URL, TESTLINK_API_PYTHON_DEVKEY)
        except Exception as e:
            print("连接Testlink失败：%s" % e)

    def get_information_test_project(self):
        print("Number of Projects      in TestLink: %s " % self.tls.countProjects())
        print("Number of Platforms  (in TestPlans): %s " % self.tls.countPlatforms())
        print("Number of Builds                   : %s " % self.tls.countBuilds())
        print("Number of TestPlans                : %s " % self.tls.countTestPlans())
        print("Number of TestSuites               : %s " % self.tls.countTestSuites())
        print("Number of TestCases (in TestSuites): %s " % self.tls.countTestCasesTS())
        print("Number of TestCases (in TestPlans) : %s " % self.tls.countTestCasesTP())
        print(self.tls.countProjects())

    def get_testcaseid(self, testcasename):
        caseid = self.tls.getTestCaseIDByName(testcasename)
        return(caseid)


    def report(self, report_xml_path, testplanid, buildname, testcaseid,  user, platformname="0"):
        '''
        :param report_xml_path: rf测试报告xml文件路径
        :param testplanid: 测试计划id
        :param buildname: 测试计划的name
        :param user: 执行用例人，要和秘钥对应 或者测试计划设置为公共
        :param platformname: 平台 默认为0
        :return:
        '''
        caseoutlist = self._parse_reportxml(report_xml_path)
        for i in caseoutlist:
            self.tls.reportTCResult(testplanid=testplanid, testcaseid=testcaseid, buildname=buildname,
                                            status=i.get("status", ""),
                                            notes=i.get("notes", ""),
                                            user=user, platformname=platformname)

    def _parse_reportxml(self, report_xml_path):
        try:
            f = open(report_xml_path, "r")
        except Exception as e:
            print(u"打开robot output.xml出现异常:%s" % e)
            exit()

        body = f.read()
        soup = BeautifulSoup(body, "lxml")
        caselist = soup.findAll("test")
        a = []
        for i in caselist:
            case = {}
            case['casename'] = i.attrs['name']
            case['caseid'] = i.attrs['id']
            status = i.find('status', attrs={'critical': 'yes'}).attrs['status']
            if status == 'PASS':
                status = 'p'
            if status == "FAIL":
                status = 'f'
            if status == '':
                continue
            case['status'] = status
            case['endtime'] = i.status.attrs['endtime']
            case['starttime'] = i.status.attrs['starttime']
            case['notes'] = i.find('status', attrs={'critical': 'yes'}).text
            a.append(case)
            print(a)
        return a


if __name__ == "__main__":
    URL = "http://172.29.1.114/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
    KEY = "52065db013e6aa01f5685455e0133a85"
    OUTXML = u"C:\\Users\钟琼伦\AppData\Local\Temp\RIDEmodi5tl7.d\output.xml"
    rtl = ReportTestLink()
    rtl.connect_testlink(URL, KEY)
    testcaseid = rtl.get_testcaseid(u"web登录-2")
    for i in range(len(testcaseid)):
        testcaseiddic = testcaseid[i]
        print(testcaseiddic['id'])
        try:
            rtl.report(OUTXML, '7501', testcaseiddic['id'], '1.0', 'admin', '')
        except Exception as e:
            print("回写Testlink失败：%s" % e)


