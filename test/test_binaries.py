import os
import sys

# rpmlint's Testing needs TESTPATH
os.environ['TESTPATH'] = os.path.dirname(__file__)


import Testing
import BinariesCheck


class Tools(object):
    '''Class providing basic tools for other classes'''

    def _rpm_test_output(self, rpm):
        '''Wrapper that checks RPM package and returns output'''
        pkg = Testing.getTestedPackage(rpm)
        Testing.startTest()
        BinariesCheck.check.check(pkg)
        return Testing.getOutput()


class TestForbiddenCCalls(Tools):

    def test_forbidden_c_calls(self):
        for package in ['cyrus-imapd', 'dovecot']:
            out = self._rpm_test_output(os.path.join('binary', package))
            assert 'crypto-policy-non-compliance' in "\n".join(out)

    def test_waived_forbidden_c_calls(self):
        for package in ['ngircd']:
            out = self._rpm_test_output(os.path.join('binary', package))
            assert 'crypto-policy-non-compliance' not in "\n".join(out)

# Local variables:
# indent-tabs-mode: nil
# py-indent-offset: 4
# End:
# ex: ts=4 sw=4 et