# WeChat_Article    
爬取微信公众号文章    

## exe文件试用：WeChat_Article-master\Py\dist\main.exe；真正的代码在py文件夹里
**注意，除非你要断点续传，否则删除目录下conf.ini和url.json再启动！！！！**

爬取微信公众号有三种方法：      
第一种：用搜狗微信公众号搜过，这个只能收到前10条；    
第二种：用fiddler或手机抓包，从访问链接去获得appmsg_token，发现虽然这个值就在html页面里，但只有抓包的数据里含有效值，直接访问的是空的，而且还有时效性。这样，每次都要抓包获取，就很麻烦。   
第三种：就是这种用公众号搜公众号的，虽然速度慢点，但便捷了不少。    

exe文件试用：  
WeChat_Article-master\Py\dist\main.exe

****************************************************************************************************    
* 程序原理:     
通过selenium登录获取token和cookie，再自动爬取和下载   
* 使用前提：   
1、电脑已装Firefox、Chrome、Opera、Edge等浏览器（默认使用火狐驱动）   
2、下载selenium驱动放入python安装目录，将目录添加至环境变量(https://www.seleniumhq.org/download/)   
3、申请一个微信公众号(https://mp.weixin.qq.com)   
****************************************************************************************************    
* 更新记录：
1. 下载文章文字内容到txt
2. 下载文章图片
3. 保存HTML文件，并将图片链接指向本地  
4. 添加按时间范围下载  
5. 添加cookie登陆，不成功才selenium浏览器登陆  
6. 增加记住密码功能  
7. 修复一些问题，如requests卡死  
8. 添加按关键词下载  
9. 多线程优化下载速度  
10. 增加断点续传功能（可能存在bug，欢迎提issue）  
11. 拟增加备用公众号功能（暂未完成）  
**************************************************************************************************** 
建议主程序放到./Py文件夹里运行。若运行仍报错，可：  
1. 可以把这个exe文件拷贝到qt的安装目录下的bin目录下运行即可；  
2. 把bin目录下的Qt5Core.dll, Qt5Gui.dll, Qt5Widgets.dll以及C:\Qt\Qt5.8.0\5.8\msvc2015\plugins\platforms拷贝到exe同级目录。platforms文件夹下有qminimal.dll, qoffscreen.dll, qwindows.dll.  再次运行exe或重新用pyinstaller -F -W -i main.py生成exe。
.    


