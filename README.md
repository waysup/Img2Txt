Img2Txt
-----

Img2Txt - A Dropzone 3 action which recognizes texts in images(jpg/png) using baidu OCR API

#### 实现功能
Dropzone 3 通过支持文件拖放来简化 Mac 上的很多操作,是提高工作效率的神器之一.识别图片中的文字是常见的需求,但貌似 Dropzone 3 上还没有通过拖放图片来获取其中文字的action插件. Img2Txt 实现的功能如下:

- **拖放图片实现文字识别**:调用[百度OCR API](https://cloud.baidu.com/doc/OCR/OCR-API.html#.EC.DF.48.27.9B.69.A4.2C.54.1B.DC.95.67.DB.1D.3C),识别图中的所有文字,识别出的内容将放置在粘贴板中,直接粘贴即可.

- **支持多张图片同时拖放**:多张图中的文字将依次存放在粘贴板中(以空行连接).

- **网页中的图片**也可以直接拖拽识别.

##### 其它说明
- 接口调用限制:使用的接口是通用文字识别（高精度版),**500次/天**以内免费,对个人来说完全够用.

- 图片类型限制:支持 **jpg/png** 格式的图片(百度接口限制).为减少使用依赖,暂不支持其它类型.

- 文件名:支持中文,但**不支持**包含空格.

- 默认识别图片中的**中英文**.

#### 安装配置

##### 安装

- 安装 Dropzone 3

	Dropzone 3 是 Mac 上提高效率的工具软件,最新版下载地址[戳这里](https://aptonic.com/dropzone3/latest).
	
- 安装 Img2Txt
	- 从网盘下载 .dzbundle 文件,地址: `https://pan.baidu.com/s/1AwnzZp41QsatQeRxCBjhKQ 密码: fgr6`

	- 从 GitHub 仓库下载 .dzbundle 文件,地址: `https://github.com/waysup/Img2Txt`

- API 申请与配置

	1.申请百度文字识别 API

	登录[百度云](https://console.bce.baidu.com),创建一个`文字识别`应用,取得 `API Key` 以及 `Secret Key`.
	[![baidu_api.jpg](https://i.loli.net/2018/05/28/5b0bac3636027.jpg)](https://i.loli.net/2018/05/28/5b0bac3636027.jpg)

	2.Img2Txt 配置

	下载完成后,双击 `.dzbundle` ,选择 `Add to Grid` ,在配置页面进行百度文字识别 API 的配置:
	[![img2conf.jpg](https://i.loli.net/2018/05/28/5b0badb05bdd3.jpg)](https://i.loli.net/2018/05/28/5b0badb05bdd3.jpg)
	
	其中 `API Key` 以及 `Secret Key` 来自前一步. 
	`Server` 以及 `Port` 分别填写 `https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic` 以及 `443`.其它项不填写.

##### 使用方法

将图片拖放到插件的位置,等待识别完成的提示,直接粘贴文字即可:
	
[![img2txt-demo.gif](https://i.loli.net/2018/05/30/5b0d84e1b1e9e.gif)](https://i.loli.net/2018/05/30/5b0d84e1b1e9e.gif)


#### TODO

- 支持点击动作,触发识别粘贴板图片中的文字
- 支持gif、bmp等更多图片格式

#### 参考资料

- [resizeup - Dropzone3's action plugin - markdown insert images solution](https://github.com/onvno/resizeup)
- [Add-on actions and API Docs for Dropzone 3](https://github.com/aptonic/dropzone3-actions)
- [通用文字识别（高精度版)](https://cloud.baidu.com/doc/OCR/OCR-API.html#.E8.AF.B7.E6.B1.82.E8.AF.B4.E6.98.8E)
- 图标来自[IconFinder](https://www.iconfinder.com/icons/2276086/document_extension_format_paper_txt_icon#size=512)