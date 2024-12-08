# -*- coding: utf-8 -*-
import oss2
from oss2.credentials import StaticCredentialsProvider

# 从环境变量中获取访问凭证。运行本代码示例之前，请先配置环境变量。
auth = oss2.ProviderAuthV4(StaticCredentialsProvider(access_key_id="LTAI5tCcTXe8wHALSb44u9A3", access_key_secret="LUGNbSOSlQGrAn7aApd2oHSRYT96zA"))
# 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
endpoint = 'oss-cn-beijing.aliyuncs.com'
# 填写Endpoint对应的Region信息，例如cn-hangzhou。
region = 'cn-beijing'

# 填写Bucket名称。
bucket = oss2.Bucket(auth, endpoint, 'snail-prod', region=region)
print(
    bucket.put_object_from_file("a/b/c/d.jpg", "/home/will/桌面/projects/snail/ui/src/assets/thumbnail/OMG_7736.jpeg"))
