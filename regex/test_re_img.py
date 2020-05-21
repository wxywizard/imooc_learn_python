import re

# 1. 下载html
# 2. 写正则的规则
# 要找到img标签
# 找到src属性
# <img class="" style="" src="" xx="">
# <img.+src=\".+\".+>

def test_re_img():
    """ 使用正则表达式找到图片的地址 """
    # 1.读取html
    with open('img.html',encoding='utf-8') as f:
        html = f.read()
        #print(html)
        # 2.准备正则
        p = re.compile(r'<img.+?src=\"(?P<src>.+?)\".+?>',re.M|re.I)
        list_img = p.findall(html)
        print(len(list_img))
        for ls in list_img:
            print(ls.replace('&amp;','&'))
        # 使用urllib,requests将图片保存

if __name__ == '__main__':
    test_re_img()