# PKUAutoSubmit
PKU一键出入校备案小工具 (2022.7.22)

### 需要gecko-driver支持, 请自行查找安装办法



此为作者的一个 `selenium` 练手小项目，完善程度较低，欢迎任意类型的使用与开发改进


## 说明

- 本工具采用 Python3 搭配 `selenium` 完成自动化操作，实现全自动填报学生出入校备案，为频繁出入校的 PKU 学子（不频繁也行）提供较为便捷的解决方案
- 支持多个配置文件，可在一个进程内同时进行多人填报
- 采用定时任务可实现定期（如每日）免打扰填报
- 第三方依赖包几乎只有 `selenium` 一个，从下到用贼jr快

## 安装与需求

### Python 3

本项目需要 Python 3，可以从[Python 官网](https://www.python.org/)下载安装

本项目采用 Python 3.7.4 开发，由于含有 `f-string` ，请至少使用 Python 3.6 及以上版本，建议使用 Python 3.7 及以上版本

### Packages


```
pip3 install selenium pyyaml
```


## 基本用法

1. 将 `config.yml` 文件移动到config目录下 ，请不要新建文件，不然自己搞定编码问题

2. 用文本编辑器（建议vscode）打开 `config.yml` 文件

3. 配置变量，在 `config.yml` 文件内有详细注释

4. 若需要多人同时填报，可将 `config.yml` 文件复制若干份，分别重命名为 `config+序号.yml` 例如 `config1.yml`,  `config2.yml`...并配置对应变量

   **Note:** 序号仅作匹配用，具体数值不重要，但是非法命名格式可能导致检测失败

5. 进入项目根目录，以命令 `python pkusubmit.py` 运行主程序


## 责任须知

- 本项目仅供参考学习，造成的一切后果由使用者自行承担
- 本项目敏感性不比 skj，利人利己，私以为还是可以合理扩散一下的，吧？

## 证书

[GPL-3](https://www.gnu.org/licenses/gpl-3.0.en.html)

## 相关项目

本项目参考了 https://github.com/Bruuuuuuce/PKUAutoSubmit 在此致谢

