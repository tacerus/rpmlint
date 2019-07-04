from rpmlint.rpmdiff import Rpmdiff

from Testing import testpath


def test_distribution_tags():
    oldpkg = testpath() / 'binary/mc-4.8.15-10.3.1.x86_64.rpm'
    newpkg = testpath() / 'binary/mc-4.8.21-2.1.x86_64.rpm'
    ignore = list()
    diff = Rpmdiff(oldpkg, newpkg, ignore)
    textdiff = diff.textdiff()
    print(textdiff)
    # the count always reports one less
    assert textdiff.count('\n') + 1 == 231

    ignore.append('T')
    ignore.append('5')
    ignore.append('S')
    diff = Rpmdiff(oldpkg, newpkg, ignore)
    textdiff = diff.textdiff()
    print('----\n' + textdiff)
    assert textdiff.count('\n') + 1 == 36

    assert 'added       /usr/share/mc/syntax/yaml.syntax' in textdiff
