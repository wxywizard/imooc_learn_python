import re


def test_group():
    content = 'hello,world!'
    p = re.compile(r'world')
    rest = p.search(content)
    print(rest)
    if rest:
        print(rest.group())

        print(rest.groups())


def test_id_card():
    """ 身份证号码正则匹配 """
    #p = re.compile(r'(\d{6})(\d{4})((\d{2})(\d{2}))\d{2}\d{1}([0-9]|X)')
    p = re.compile(r'(\d{6})(?P<year>\d{4})((?P<month>\d{2})(?P<day>\d{2}))\d{2}\d{1}([0-9]|X)')
    id1 = '430656199610015493'
    id2 = '43065619961001548X'
    rest1 = p.search(id1)
    print(rest1.group())
    print(rest1.groups())
    print(rest1.groupdict())

if __name__ == '__main__':
    #test_group()
    test_id_card()
