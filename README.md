# CNN 混凝土裂缝识别

上传目标：https://github.com/luguannan90-sketch/concretecrack-CNN

## 运行入口

在 VS Code 打开本仓库目录，使用 `CNN混凝土裂缝识别复现.ipynb`，选择安装过 PyTorch 的内核，按章节运行。
Notebook 使用 PyTorch/torchvision 做图像分类，不输出裂缝位置或宽度。
具体参数以当前 Notebook 为准，两份说明记录此前的实验方案与结果。

## 数据与模型

本仓库只上传代码、说明和必要配置，Notebook 输出已清空。
数据集放在 `SDNET2018/SDNET2018/`，训练结果与模型放在 `artifacts/`。
这些文件保留在原电脑本地，不随 Git 克隆；新电脑需要准备数据并训练，或提供兼容的已有模型。
第 21 节默认图片为 `inputs/your_image.jpg`，使用时改为实际图片路径。
模型、样本图片与全部运行结果均被 Git 忽略。

## 环境与上传

已有可运行环境无需重复安装。新环境需按自己的 GPU 安装兼容的 PyTorch 和 torchvision，其他所需库列在 requirements.txt。
本地已启用上传目标检查与提交检查；重新克隆后运行 `git config core.hooksPath .githooks`。

在本仓库终端执行：

```powershell
python scripts/clean_notebooks.py
git add .
git commit -m "Update CNN code"
git push origin main
```

提交检查要求只包含代码与说明，并清除 Notebook 输出。上传检查只允许 concretecrack-CNN 仓库。
旧提交中已有的大文件仍可能存在于 Git 历史，本次不重写历史。
