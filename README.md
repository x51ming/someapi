## some restful api
### 运行方法：
```shell script
python manage.py runserver
```
### 依赖

- django == 2.2.12
- pillow == 7.2.0

### gif extract
提取gif的每一帧
使用方法：
```shell script
curl 127.0.0.1:8000/api/gifextract -T test.gif -o test.zip -X POST
```
使用POST方法上传gif文件，则会得到一个压缩包