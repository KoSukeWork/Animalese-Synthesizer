# Animalese Synthesizer 《动物森友会》动物语合成器

受重轻老师[《集合啦！动物森友会》「狸语」语音制作小教程](https://www.gcores.com/articles/122542)2:50启发，自己捣鼓了这个可本机运行的“动物语合成器”，同时向机核官方在线版[“动森狸语生成器”](https://site.gcores.com/animal_crossing_voice)致敬。

## 简明使用指南

windows

1. 安装python 3，请确保pip也一并安装。
2. 运行install.bat安装依赖。
3. 前往[sox官方首页](http://sox.sourceforge.net/)，下载Windows版sox。安装完毕后将sox.exe所在目录加入环境变量。

ubuntu
运行install.sh安装依赖。

命令行键入`python3 main.py "玩儿游戏的都是朋友"`，当前目录下会生成合成的音频`synthesized.wav`。

## 算法思想

1. 利用[汉字转拼音(pypinyin)](https://github.com/mozillazg/python-pinyin)将中文转拼音，拆分出音素（声韵母）。
2. 用 sox 合成音效。

## 动物语音效要点

1. 速度加快
2. 音高提高一个八度以上
3. 随机化音高，造成抑扬顿挫感。

## 用到的工具

+ [sox](http://sox.sourceforge.net/)
+ [Audacity](https://www.audacityteam.org/)

## TODO

1. 动物语没有还原出重轻老师调制的效果，算法仍需修改。
2. 准备为所有村民调制声音特征，存储于`voice_features.json`。目前只有阿狸（Tom Nook）的特征参数。

## 参考资料

+ [Pinyin chart](https://resources.allsetlearning.com/chinese/pronunciation/pinyin_chart)
+ [音乐也有科学道理？Do、Re、Mi...都是如何确定的？李永乐老师讲音律](https://www.bilibili.com/video/BV124411e7Wk)
