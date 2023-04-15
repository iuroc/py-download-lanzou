# 蓝奏云解析

- 开发日期：2023 年 4 月 15 日
- 作者：欧阳鹏

## 样本

- 会员版文件分享页：https://www.lanzoui.com/iXz3R0syjqwf
- 普通版文件分享页：https://www.lanzoui.com/icjultg

## 普通部署

1. 下载代码

    ```bash
    git clone https://kgithub.com/oyps/py-download-lanzou
    ```
2. 安装依赖
    
    ```bash
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    pip install requests
    pip install flask
    ```
3. 启动 HTTP 服务

    ```bash
    python app.py
    ```

## Docker 部署

  ```bash
  git clone https://kgithub.com/oyps/py-download-lanzou
  docker build -t py-download-lanzou py-download-lanzou
  docker run --name down-lanzou -p 5000:5000 py-download-lanzou
  rm -rf py-download-lanzou
  ```

## API 说明

- 下载文件
  - 请求地址：`/down`
  - 请求方式：GET
  - 请求参数
    - `id`：文件分享 ID
  - 请求示例：`/down?id=iMFpo00t1y1g`

## 拓展开发

```python
from lanzou import get_down_url  # 导入函数
down_url = get_down_url('iMFpo00t1y1g')  # 调用函数，获取下载地址
print(down_url)  # 输出下载地址
```