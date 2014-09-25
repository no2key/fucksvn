#fucksvn
回溯SVN仓库, 根据关键字在指定文件里找出该关键字第一作者和版本号. 想象这么个场景, 你看到A.php文件里有个叫`fuckyou`的函数, 该A.php有1000次提交记录. 你想知道谁是`fuckyou`的第一作者, 版本是多少. 这样就方便鄙视某人或者崇拜某人, 或者找出第一作者咨询某代码的含义以及存在的作用. 总之, 方便你维护以`svn`作版本控制的项目.

#使用方式
把`TortoiseSVN`的`bin`目录加入到系统的`PATH`里

##使用打包后的`fucksvn.exe`
下载`fucksvn.exe`到项目主目录里, 执行(例子):
`fucksvn.exe application/index.php fuckyou`

##使用源代码`fucksvn.py`
1. 下载安装`Python2.7`
2. 把`Python`加入到系统的`PATH`里
2. 拷贝`fucksvn.py`到项目主目录
3. 执行`python fucksvn.py application/index.php fuckyou`

#返回结果例子:
`version: r11237, author: laotaitai`
