## 基本功能
- 调用摄像头拍照并识别照片中的物体
- 加载本地图片或包含图片的文件夹逐张识别

## 环境依赖
项目基于python3.6开发，推荐使用pycharm打开。没有将venv依赖包目录加入git上传，请自行安装依赖。
- 安装依赖，在项目根目录下输入`pip install -r requirements.txt`

主要包含以下模块：
- opencv或cv2
- PySide2
- keras
- tensorflow

## 识别模型说明
模型脚本现有两个（Jupyter Notebook编写），`Keras_Cifar_CNN_Introduce.ipynb`是自行设计搭建的CNN网络，包含简单的3个卷积层、池化层和全连接层。`Keras_Cifar_ResNet.ipynb`是Kares官网上提供的ResNet程序，包含V1和V2两个版本，默认是V1。

当前得到的模型文件`cifar10_ResNet20v1_model.045.h5`，是`Keras_Cifar_ResNet.ipynb`脚本采用Cifar10数据集在Google Colab上进行训练（Python3&GPU加速），迭代50个epoch，择取验证集最佳的一次（第45次，val_acc=85.65%），训练过程约45分钟。、

**还！有！一！颗！练！了！4！个！钟！的！丹！test_acc！有！91%！但！是！colab！连！不！上！了！**
- 嘤嘤嘤嘤嘤

## 使用说明
- 运行根目录下的`main.py`

## 项目结构
```
IMG-REC
├── Core
│   ├── CameraMainWin.py                            #  主界面逻辑
│   ├── ImageRecognition.py                         #  图片识别类
│   ├── ResultWid.py                                #  多张图片识别结果页面逻辑
│   └── SingleResultWid.py                          #  单张图片识别结果页面逻辑
├── Models
│   └── cifar10_ResNet20v1_model.045.h5             #  训练好的模型
├── NetJupyterNotes
│   ├── Keras_Cifar_CNN_Introduce.ipynb             #  自行设计编写的模型脚本
│   └── Keras_Cifar_ResNet.ipynb                    #  Keras官网的ResNet示例脚本
├── Qt_Ui                                           #  QtDesigner生成的布局文件和py-uic转换后的布局脚本
│   ├── cameraWin.ui
│   ├── resultWid.ui
│   ├── singleResultWid.ui
│   ├── ui_cameraWin.py
│   ├── ui_resultWid.py
│   └── ui_singleResultWid.py
├── LICENSE
├── main.py                                         #  程序入口
├── README.md
└── requirement.txt
```

## 作者和版权声明
本项目采用[MIT协议](https://github.com/Jyunmau/IMG-REC/blob/master/LICENSE)。
项目程序主逻辑及打包发布和resnet的训练由@Jyunmau完成。
自建模型设计及训练由@cagaha完成。
