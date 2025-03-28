# 代码配置

用 auto-cot 的环境应该也能跑, 不能的话再尝试下面配环境. 这个冲突太多了, 我注释了 `requirements.txt` 里的一些包. 如果还有冲突, 就手动下载关键包 torch transformers pandas pyarrow 这些, 不管包冲突

```
conda create --name nash_cot python=3.8
conda activate nash_cot
pip install -r requirements.txt
pip install pandas
pip install pyarrow
```

运行脚本 `run_nash_cot.sh`, 如果只跑单个数据集需要注释掉一些. 数据集我一起传上来了













# 代码配置 (废)

**以下不用看**

## 配环境


```
conda create --name nash_cot python=3.8
conda activate nash_cot
git clone https://github.com/stevezhangzA/nash-chain-of-thought.git
cd nash-chain-of-thought && pip install -r requirements.txt
```

这时候应该会报错, 然后输入

```
pip install setuptools==65.5.0 pip==21
pip install wheel==0.38.0
pip install -r requirements.txt
```

然后还会报错, 因为 PyGObject 在 PyPI 上已经没有3.26.1版本了, 装了3.28.3, 使用 `pip install PyGObject` 会自动降版本找到能装的版本, 直到3.30.5, 但是也安装失败了. 于是决定在 `requirements.txt` 注释掉这个包

```
pip install PyGObject==3.28.3
```

然后有包的冲突 PyOpenGL 和 dm-control

```
The conflict is caused by:
    The user requested PyOpenGL==3.1.0
    dm-control 1.0.13 depends on pyopengl>=3.1.4
```

输入指令, 并在 `requirements.txt` 注释掉该库

```
pip install pyopengl==3.1.4
```

还有包冲突 (后续有冲突都注释掉txt对应包)

```
The conflict is caused by:
    The user requested protobuf==3.20.0
    dm-control 1.0.13 depends on protobuf>=3.19.4
    google-api-core 2.11.1 depends on protobuf!=3.20.0, !=3.20.1, !=4.21.0, !=4.21.1, !=4.21.2, !=4.21.3, !=4.21.4, !=4.21.5, <5.0.0.dev0 and >=3.19.5
```

输入以下指令, 并在 `requirements.txt` 注释该库

```
pip install protobuf==3.19.5
```

包冲突

```
The conflict is caused by:
    The user requested cloudpickle==1.3.0
    gym 0.21.0 depends on cloudpickle>=1.2.0
    huggingface-sb3 2.2.4 depends on cloudpickle>=1.6
```

输入以下指令, 并在 `requirements.txt` 注释该库

```
pip install cloudpickle==1.6
```

依然有冲突

```
The conflict is caused by:
    gym 0.21.0 depends on cloudpickle>=1.2.0
    huggingface-sb3 2.2.4 depends on cloudpickle>=1.6
    jaynes 0.9.5 depends on cloudpickle==1.3.0
```

输入指令

```
pip install jaynes==0.9.9
```

依然有冲突, 

```
The conflict is caused by:
    gym 0.21.0 depends on cloudpickle>=1.2.0
    huggingface-sb3 2.2.4 depends on cloudpickle>=1.6
    ml-logger 0.10.15 depends on cloudpickle==1.3.0
```

安装

```
pip install ml-logger==0.10.21
```

安装 pandas

```
pip install pandas
pip install pyarrow
```


## 添加数据集

`utils.py` 添加数据集

`nash_cot.py` 添加数据集