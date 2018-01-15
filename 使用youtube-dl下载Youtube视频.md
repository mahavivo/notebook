使用youtube-dl下载Youtube视频

via https://extremegtr.github.io/2017/10/06/Use_youtube-dl_download-Youtube-video/

## 前言

只要我们用百度或谷歌随便查找一下，那就能知道有挺多种方式可以下载Youtube视频的，不过挺多方式都有其的缺点，比如速度慢，又比如不能下载分辨率大于1080p的高清视频等等，当然你需求比较少，只有能下载视频就够了，很多下载方法都能够满足你。

下载Youtube视频翻墙是必要的，没有翻墙想下载Youtube的视频基本是没辙了，或者速度像乌龟那么慢，就算你下载的视频只是几百M的大小，那也是要到猴年马月。所以，无论如何，要先搞到一个好的翻墙方式，

## 常用的方式

以前我最常用的一招就是使用免费的翻墙软件XX-Net搭配以下的方法进行下载：

ClipConverter
这是一个在线媒体转码网站，只要你把Youtube视频地址复制过去，就有一个分辨率选择列表，你想要什么分辨率都行，4K也是没问题的。
选择完分辨率，等它转换完，那就可以下载了，不过有时候这个网站的服务器抽风那就没辙了。

Free YouTube Downloader
这个是要安装客户端的下载软件，以前免费可以下载2K的视频，现在是必须付费才能下载大于1080p的视频。
同样地，也是把视频地址粘上去，就会给一个列表你选，选后直接按下载就行了。

4K Video Downloader
这也是一个需要安装客户端得下载软件，功能和上面那个差不多。
而它甚至可以免费下载4K的视频，这是非常好的一点，但缺点也明显，与Free YouTube Downloader比起来，解析链接的速度可以说非常慢。

## 学习使用youtube-dl

youtube-dl这个工具的用法不像之前那些工具那么傻瓜式了，是需要输入命令里进行操作的，但通过各种参数进行配合，这会显得更加灵活，不过电脑小白用的话或许就会感到有些吃力，但用多几次就感觉还好。大部分用户用的都是Windows，并且我也是Linux系统的门外汉，所以这里只讲Windows下的使用过程。

### 把工具弄好

Python

要使用youtube-dl，那就得先安装Python。Python官网，到里面就可以找到下载地址，下载后安装即可，没啥好说的了。

youtube-dl

下载
之前所提供的的youtube-dl的链接里面就有下载链接，下载youtube-dl.exe这个工具就行了，其余不用多管。

放置
下载完之后，把它放到你所想的目录里（除了%SYSTEMROOT%\System32，任何地方你都可以放）。

配置系统环境变量Path
给系统环境变量Path的变量值最后加上youtube-dl.exe所在的路径。

设置配置文件
在Windows下，youtube-dl这个工具默认使用的配置文件是%APPDATA%\youtube-dl\config.txt或C:\Users\<user name>\youtube-dl.conf。

如果在那些目录里找不到配置文件，那你就自己在那些目录里自己创建一个。
这里，我也没找到相应的配置文件，所以就在自己的C盘的用户目录C:\Users\<user name>里创建一个youtube-dl.conf，并添加以下内容。
```
# Use this proxy
--proxy 127.0.0.1:8087
```
这是配置代理，只要把你自己的代理对应的IP以及端口配置上就行了。
如果不在配置文件配置代理，那么每次下载视频的视频都要在命令上加上这个代理参数。

就做以上这4步，就把youtube-dl工具给弄好了，之后我们就可以开始用它来下载Youtube视频了。

FFmpeg

因为Youtube的高清格式的视频都是音视频分开的，所以就算把1080p、2K、4K下载回来了，也是需要合成的，所以FFmpeg是必不可少的合成工具。

下载
到FFmpeg官网下载工具。

放置
下载后解压到你指定的位置。

配置系统环境变量Path
给系统环境变量Path的变量值最后加上解压后FFmpeg所在的路径。

### 下载视频

现在一切都搞好了，正式开始下载视频：打开控制台，输入一下命令就能够下载视频了。
这里你可以用这个视频地址自己尝试一下：https://www.youtube.com/watch?v=1La4QzGeaaQ。

最普通的下载命令
```
youtube-dl 视频地址
```
这样直接下载的是指定视频地址的最高质量视频，并且已经是音视频合成好的视频。

配置代理参数

```
youtube-dl --proxy 127.0.0.1:8087 视频地址
```
没有在配置文件设置代理的情况下，在配置文件配置了就不用加上这个参数--proxy参数。

查看所能下载的所有格式
```
youtube-dl -F或--list-formats 视频地址
```
其中-F的F必须是大写，不能是小写的f，如果你写成小写，那就会报错。
输入该命令后，那在控制台上就会显示该视频地址所能下载到的所有格式。

比如输入以下命令：
```
youtube-dl -F https://www.youtube.com/watch?v=1La4QzGeaaQ
或
youtube-dl --list-formats https://www.youtube.com/watch?v=1La4QzGeaaQ
```
得到的结果就是：
```
format code  extension  resolution note
139          m4a        audio only DASH audio   48k , m4a_dash container, mp4a.40.5@ 48k (22050Hz), 1.92MiB
249          webm       audio only DASH audio   58k , opus @ 50k, 2.01MiB
250          webm       audio only DASH audio   78k , opus @ 70k, 2.68MiB
171          webm       audio only DASH audio  125k , vorbis@128k, 4.64MiB
140          m4a        audio only DASH audio  128k , m4a_dash container, mp4a.40.2@128k (44100Hz), 5.12MiB
251          webm       audio only DASH audio  150k , opus @160k, 5.29MiB
160          mp4        256x144    DASH video  118k , avc1.4d400c, 30fps, video only, 4.49MiB
278          webm       256x144    144p  119k , webm container, vp9, 30fps, video only, 3.92MiB
330          webm       256x144    144p60 HDR  199k , vp9.2, 60fps, video only,5.97MiB
133          mp4        426x240    DASH video  260k , avc1.4d4015, 30fps, video only, 9.92MiB
331          webm       426x240    240p60 HDR  271k , vp9.2, 60fps, video only, 9.16MiB
242          webm       426x240    240p  281k , vp9, 30fps, video only, 8.51MiB
243          webm       640x360    360p  491k , vp9, 30fps, video only, 15.83MiB
332          webm       640x360    360p60 HDR  583k , vp9.2, 60fps, video only, 19.51MiB
134          mp4        640x360    DASH video  645k , avc1.4d401e, 30fps, videoonly, 21.83MiB
244          webm       854x480    480p  905k , vp9, 30fps, video only, 29.17MiB
333          webm       854x480    480p60 HDR 1090k , vp9.2, 60fps, video only, 36.77MiB
135          mp4        854x480    DASH video 1178k , avc1.4d401f, 30fps, video only, 42.40MiB
247          webm       1280x720   720p 2088k , vp9, 30fps, video only, 59.14MiB
136          mp4        1280x720   720p 2357k , avc1.4d401f, 30fps, video only, 84.20MiB
334          webm       1280x720   720p60 HDR 2496k , vp9.2, 60fps, video only, 82.87MiB
302          webm       1280x720   720p60 3061k , vp9, 60fps, video only, 97.24MiB
298          mp4        1280x720   DASH video 3585k , avc1.4d4020, 60fps, video only, 115.60MiB
248          webm       1920x1080  1080p 3694k , vp9, 30fps, video only, 104.08MiB
335          webm       1920x1080  1080p60 HDR 4305k , vp9.2, 60fps, video only, 140.18MiB
137          mp4        1920x1080  1080p 4591k , avc1.640028, 30fps, video only, 157.97MiB
303          webm       1920x1080  1080p60 5564k , vp9, 60fps, video only, 166.17MiB
299          mp4        1920x1080  DASH video 5915k , avc1.64002a, 60fps, video only, 205.13MiB
264          mp4        2560x1440  DASH video 10757k , avc1.640032, 30fps, video only, 365.34MiB
336          webm       2560x1440  1440p60 HDR 11180k , vp9.2, 60fps, video only, 379.99MiB
271          webm       2560x1440  1440p 11533k , vp9, 30fps, video only, 329.39MiB
308          webm       2560x1440  1440p60 16424k , vp9, 60fps, video only, 489.65MiB
337          webm       3840x2160  2160p60 HDR 23026k , vp9.2, 60fps, video only, 762.28MiB
266          mp4        3840x2160  DASH video 23442k , avc1.640033, 30fps, video only, 679.31MiB
313          webm       3840x2160  2160p 24334k , vp9, 30fps, video only, 700.74MiB
315          webm       3840x2160  2160p60 32601k , vp9, 60fps, video only, 1.01GiB
138          mp4        7680x4320  DASH video 78931k , avc1.640033, 30fps, video only, 2.33GiB
272          webm       7680x4320  4320p60 92526k , vp9, 60fps, video only, 2.70GiB
17           3gp        176x144    small , mp4v.20.3, mp4a.40.2@ 24k
36           3gp        320x180    small , mp4v.20.3, mp4a.40.2
43           webm       640x360    medium , vp8.0, vorbis@128k
18           mp4        640x360    medium , avc1.42001E, mp4a.40.2@ 96k
22           mp4        1280x720   hd720 , avc1.64001F, mp4a.40.2@192k (best)
```

下载指定格式的文件

关于这一块，重点关注的是命令中的参数，这里参数变化就会多一点点。
```
youtube-dl -f 或 --format 格式代号 视频地址
```
与之前的相反，这里的-f只能是小写，不能是大写。
前面我们查看了指定视频地址的所有能够下载到的格式，其中format code这一列就是格式代号，比如就拿之前所看到的数据来说：

137是1080p 30fps、299是1080p 60fps
并且这两个都是只有视频画面的mp4文件，它们都是不带音频的视频。
266是2160p 30fps不带音频的mp4视频
315是2160p 60fps不带音频的webm视频
138是4320p 30fps不带音频的mp4视频
140是128k 44100Hz的m4a音频
你想下载什么样的格式，就在下载命令里填什么样的格式代号。

又比如我想下载之前所提供的那个链接的4K且视频格式为mp4的视频，那么下载命令就是：
```
youtube-dl -f 266 https://www.youtube.com/watch?v=1La4QzGeaaQ
或
youtube-dl --format 266 https://www.youtube.com/watch?v=1La4QzGeaaQ
```
我们下载视频当然想要的是即是高清又带声音的，所以不能只是单纯地下载不带声音的视频，必须要把音频也搞下来，然后利用FFmpeg合成即可。

但使用FFmpeg进行合成又要使用命令了，这显得很繁琐，但还好有一种更简单的方式：
只要你安装配置好了FFmpeg，在youtube-dl命令里同时指定视频与音频两者的格式代号进行下载，那youtube-dl就会自动调用FFmpeg进行合成。
```
youtube-dl -f 视频格式代号+音频格式代号 视频地址
```
这里两个格式代号，前面必须是视频，后面必须是音频，不能搞反了。
现在还是拿之前那个Youtube视频链接作为案例。

现在想下载它对应的质量最佳的视频以及质量最佳的音频以合成一个完整的视频
```
youtube-dl -f bestvideo+bestaudio https://www.youtube.com/watch?v=1La4QzGeaaQ
```
其实这条命令就相当于最开始那条普通的下载命令
```
youtube-dl https://www.youtube.com/watch?v=1La4QzGeaaQ
```
下载4K30帧的mp4视频

那就得首先查询音频视频的格式代号，再进行下载。4K30帧mp4视频的格式代号是266，对应的m4a音频代号是140
```
youtube-dl -f 266+140 https://www.youtube.com/watch?v=1La4QzGeaaQ
```
有时候，我们不一定要想最佳质量的，反而是想根据自己的需要来下载的，想下载其他分辨率或其他格式的如法炮制就行

指定下载的路径

如果你已经试过前面的命令了，那就会发现：所下载的视频对应的文件都被放在执行该下载命令的路径下，要修改下载路径很简单：使用参数-o。
```
youtube-dl -o "绝对路径\%(title)s.%(ext)s"
```
其中，前半部分的绝对路径是你指定的，后半部分最好是固定的，使用原来的标题作为文件名以及使用原扩展名。

比如把之前的4K30帧的mp4视频下载到H:\youtube_videos内，那么命令就是这样：
```
youtube-dl -o "H:\youtube_videos\%(title)s.%(ext)s" -f 266+140 https://www.youtube.com/watch?v=1La4QzGeaaQ
```
