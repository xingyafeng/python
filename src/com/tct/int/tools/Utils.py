#!/usr/bin/python
import re
import os
import sys
# import ldap
import smtplib
import pexpect
import tempfile
from email.mime.text import MIMEText

__defaultLogFile = '/data/nishome/td/yafeng.xing/workspace/date/0724/aa.log'
__notifyList = []
__dirStack = []


def setDefaultLogFile(fileName):
    global __defaultLogFile
    __defaultLogFile = fileName


def getDefaultLogFile():
    global __defaultLogFile
    return __defaultLogFile


def addNotifyInfo(strNotify, addHead=False):
    global __notifyList
    if addHead:
        __notifyList.insert(0, strNotify)
    else:
        __notifyList.append(strNotify)


def getNotifyInfo():
    global __notifyList
    return '\n==========================================================================\n\n'.join(__notifyList)


class __bothLog(file):
    def __init__(self, filename, mode):
        self.notify = []
        self.filename = filename
        if len(self.filename) > 0:
            file.__init__(self, self.filename, mode)

    def write(self, s):
        if len(self.filename) > 0:
            file.write(self, s)
        sys.stdout.write(s)
        self.notify.append(s)
        if len(self.notify) > 200:
            self.notify = self.notify[-200:]

    def flush(self):
        if len(self.filename) > 0:
            file.flush(self)

    def close(self):
        if len(self.filename) > 0:
            file.close(self)

    def getNotify(self):
        return ''.join(self.notify)


def chdir(path, log=''):
    oldDir = os.getcwd()
    if len(log) == 0:
        log = getDefaultLogFile()
    logFile = __bothLog(log, 'a')
    logFile.write('chdir: %s => %s\n' % (oldDir, path))
    os.chdir(path)
    return oldDir


def pushdir(path, log=''):
    global __dirStack
    __dirStack.insert(0, chdir(path, log))


def popdir(log=''):
    global __dirStack
    if len(__dirStack) > 0:
        chdir(__dirStack[0], log)
        __dirStack = __dirStack[1:]


def checkDir(path):
    if not os.path.isdir(path):
        docmd('rm -rf ' + path)
        docmd('mkdir -p ' + path)


def getToolPath():
    return re.sub('lib$', '', os.path.dirname(__file__), 1)


def docmd(cmd, log=''):
    if len(log) == 0:
        log = getDefaultLogFile()
    logFile = __bothLog(log, 'a')
    logFile.write('docmd:' + os.getcwd() + '$ ' + cmd + '\n')
    proc = pexpect.spawn('/bin/bash', ['-c', cmd], timeout=None, logfile=logFile)
    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        logFile.close()
    else:
        logFile.write("Error: docmd:%s$ %s <Return %d>\n" % (os.getcwd(), cmd, proc.exitstatus))
        logFile.close()
        addNotifyInfo(logFile.getNotify())
        sys.exit(1)


def docmd_noexit(cmd, log=''):
    if len(log) == 0:
        log = getDefaultLogFile()
    logFile = __bothLog(log, 'a')
    logFile.write('docmd_noexit:' + os.getcwd() + '$ ' + cmd + '\n')
    proc = pexpect.spawn('/bin/bash', ['-c', cmd], timeout=None, logfile=logFile)
    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        logFile.close()
    else:
        logFile.write("Error: docmd_noexit:%s$ %s <Return %d>\n" % (os.getcwd(), cmd, proc.exitstatus))
        logFile.close()
        addNotifyInfo(logFile.getNotify())
    return proc.exitstatus


def docmd_forever(cmd, log=''):
    if len(log) == 0:
        log = getDefaultLogFile()
    logFile = __bothLog(log, 'a')
    logFile.write('docmd_forever:' + os.getcwd() + '$ ' + cmd + '\n')
    while True:
        proc = pexpect.spawn('/bin/bash', ['-c', cmd], timeout=None, logfile=logFile)
        proc.expect(pexpect.EOF)
        proc.close()
        if proc.exitstatus == 0:
            logFile.close()
            break
        else:
            logFile.write("Error: docmd_forever:%s$ %s <Return %d>, try again\n" % (os.getcwd(), cmd, proc.exitstatus))


# def getADUser(user, key):
#     # Set debugging level
#     hostip = '172.24.63.212'
#     hostuser = 'CN=Rongbin XUE,OU=SDD,OU=SHANGHAI,DC=cn,DC=ta-mp,DC=com'
#     hostpwd = 'Aa123456'
#     base = "OU=SHANGHAI,DC=cn,DC=ta-mp,DC=com"
#     res = []
#     scope = ldap.SCOPE_SUBTREE
#     # Set debugging level
#     ldap.set_option(ldap.OPT_DEBUG_LEVEL, 0)
#     ldapmodule_trace_level = 1
#     ldapmodule_trace_file = sys.stderr
#     filter = '(&(objectClass=person)(sAMAccountName=%s))' % user
#
#     # Create LDAPObject instance
#     ldapobj = ldap.initialize('ldap://%s' % hostip)
#
#     # Set LDAP protocol version used
#     ldapobj.protocol_version = ldap.VERSION3
#     # Try a bind to provoke failure if protocol version is not supported
#     ldapobj.simple_bind_s(hostuser, hostpwd)
#
#     # get the ldap infomation user the user and key
#     if cmp('', key) == 0:
#         res = ldapobj.search_ext_s(base, scope, filter)
#     else:
#         tempres = ldapobj.search_ext_s(base, scope, filter, attrlist=[key])
#         if len(tempres) == 0:
#             return res
#         res = return_result(tempres)
#     # print_result(res)
#
#     # Close connection
#     ldapobj.unbind_s()
#
#     return res


# def getADUserByMail(mail, key=''):
#     # Set debugging level
#     hostip = '172.24.63.212'
#     hostuser = 'CN=Rongbin XUE,OU=SDD,OU=SHANGHAI,DC=cn,DC=ta-mp,DC=com'
#     hostpwd = 'Aa123456'
#     base = "OU=SHANGHAI,DC=cn,DC=ta-mp,DC=com"
#     res = []
#     scope = ldap.SCOPE_SUBTREE
#     # Set debugging level
#     ldap.set_option(ldap.OPT_DEBUG_LEVEL, 0)
#     ldapmodule_trace_level = 1
#     ldapmodule_trace_file = sys.stderr
#     filter = '(&(objectClass=person)(mail=%s))' % mail
#
#     # Create LDAPObject instance
#     ldapobj = ldap.initialize('ldap://%s' % hostip)
#
#     # Set LDAP protocol version used
#     ldapobj.protocol_version = ldap.VERSION3
#     # Try a bind to provoke failure if protocol version is not supported
#     ldapobj.simple_bind_s(hostuser, hostpwd)
#
#     # get the ldap infomation user the user and key
#     if cmp('', key) == 0:
#         res = ldapobj.search_ext_s(base, scope, filter)
#     else:
#         tempres = ldapobj.search_ext_s(base, scope, filter, attrlist=[key])
#         if len(tempres) == 0:
#             return res
#         res = return_result(tempres)
#     # print_result(res)
#
#     # Close connection
#     ldapobj.unbind_s()
#
#     return res


def return_result(search_result):
    for n in range(len(search_result)):
        for attr in search_result[n][1].keys():
            for i in range(len(search_result[n][1][attr])):
                # print repr(search_result[n][1][attr][0])
                # print search_result[n][1][attr]

                # the passwd infomation repr()
                # print "%s: %s" % (attr, repr(search_result[n][1][attr][i]))

                # temppm="%s: %s" % (attr, search_result[n][1][attr][i])
                returnval = [attr, search_result[n][1][attr][i]]
                return returnval


# def getADUserProf(user, key):
#     return getADUser(user, key)[1]


# def textMail(sender, tolist, subject, content):
#     msg = MIMEText(content)
#     msg['Subject'] = subject
#     fromAdd = getADUserProf(sender, 'mail')
#     msg['From'] = getADUserProf(sender, 'displayName') + ' <' + fromAdd + '>'
#     tos = []
#     for to in tolist:
#         match = re.search('<([^<>@]+@[^<>@]+)>', to)
#         if match:
#             msg['To'] = to.strip()
#             tos.append(match.group(1))
#         else:
#             toAdd = getADUserProf(to, 'mail')
#             msg['To'] = getADUserProf(to, 'displayName') + ' <' + toAdd + '>'
#             tos.append(toAdd)
#     s = smtplib.SMTP('mail.tcl.com')
#     s.sendmail(fromAdd, tos, msg.as_string())
#     s.quit()


def clone(path, server):
    chdir(path)
    docmd('rm -rf .repo .git')
    tmpstr = tempfile.mkdtemp('HAPPYBUILD', 'temp', '/tmp/')
    tmpstr = tmpstr + '/'
    chdir(tmpstr)
    docmd('git clone ' + server)
    return os.getcwd()


def push(path):
    chdir(path)
    docmd('git pull')
    docmd('git push')


if __name__ == '__main__':
    username = sys.argv[1]
    keyval = sys.argv[2]
    # listmap = getADUser(username, keyval)
    # print type(listmap)
    # for x in listmap:
    #     print x
