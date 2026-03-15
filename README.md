# Schult Table - 视觉注意力训练

## 项目简介

Schult Table是一个基于Python和Tkinter开发的视觉注意力训练工具，通过按顺序点击数字的方式，帮助用户提高注意力集中能力和视觉搜索速度。

## 主要功能

- 支持3×3到7×7不同大小的网格
- 提供简单、普通、困难三种难度级别
- 实时计时功能，记录完成时间
- 视觉反馈，根据难度级别提供不同的点击反馈
- 响应式界面，自动调整按钮大小和字体

## 安装步骤

1. 确保你的系统已安装Python 3.6或更高版本
2. 克隆或下载本项目到本地
3. 进入项目目录

```bash
cd SchultTable
```

4. 运行应用程序

```bash
python schult_table.py
```

## 使用方法

1. 选择合适的网格大小（3×3到7×7）
2. 选择难度级别：
   - 简单：点击正确数字时会变为绿色，错误点击会变为红色
   - 普通：点击正确数字时会变为浅灰色
   - 困难：无视觉反馈，仅禁用已点击的数字
3. 按顺序点击数字，从1开始，依次点击到最大数字
4. 完成后，系统会显示完成时间
5. 点击"重新开始"按钮可以重新开始游戏

## 目录结构

```
SchultTable/
├── schult_table.py    # 主应用程序文件
├── .gitignore         # Git忽略文件
├── README.md          # 项目说明文档
└── LICENSE            # 许可证文件
```

## 贡献指南

1. Fork本项目
2. 创建新的分支
3. 提交你的更改
4. 发起Pull Request

## 许可证

本项目采用MIT许可证，详见LICENSE文件。

## 技术栈

- Python 3.6+
- Tkinter（Python标准库）
- random（Python标准库）
- time（Python标准库）

## 截图

![Schult Table截图](https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Schult%20Table%20game%20interface%20with%205x5%20grid%20of%20numbers%2C%20Python%20Tkinter%20application%2C%20clean%20UI%20with%20grid%20size%20and%20difficulty%20options&image_size=landscape_16_9)
