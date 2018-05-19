import sys,importlib
from urllib import parse
import json

if len(sys.argv)!= 5:
    print(len(sys.argv))
    print("命令行参数长度不为5")
    sys.exit()
else:
    LabelCookie = parse.unquote(sys.argv[1])
    LabelUrl = parse.unquote(sys.argv[2])
    #PageType为List,Content,Pages分别代表列表页，内容页，多页http请求处理，Save代表内容处理
    PageType=sys.argv[3]
    SerializerStr = parse.unquote(sys.argv[4])
    if (SerializerStr[0:2] != '''{"'''):
        file_object = open(SerializerStr)
        try:
            SerializerStr = file_object.read()
            SerializerStr = parse.unquote(SerializerStr)
        finally:
            file_object.close()
    LabelArray = json.loads(SerializerStr)

#以下是用户编写代码区域
    if(PageType=="Save"):
        if(LabelArray['标题']):
            LabelArray['标题']='这是Python插件处理的标题'
    else:
        LabelArray['Html']='当前页面的网址为:'+ LabelUrl +"\r\n页面类型为:" + PageType + "\r\nCookies数据为:"+LabelCookie+"\r\n接收到的数据是:" + LabelArray['Html']
        

#以上是用户编写代码区域
    LabelArray = json.dumps(LabelArray)
    print(LabelArray)