import numpy as np

arr=[
[
"儿童姓名",
"性别",
"村名",
"出生日期",
"接种疫苗",
"剂次",
"最后修改单位",
"最后修改日期",
"标识"
],
[
"李如全",
"男",
"盐客树村",
"1949-09-27",
"新冠疫苗（Vero细胞）",
"3",
"六神乡卫生院",
"2022-03-27",
"李如全1949-09-27"
],
[
"沈回春",
"女",
"造册桥村",
"1980-10-21",
"新冠疫苗（Vero细胞）",
"3",
"六神乡卫生院",
"2022-03-27",
"沈回春1980-10-21"
],
[
"袁月华",
"女",
"延寿庵村",
"1959-05-18",
"新冠疫苗（Vero细胞）",
"3",
"六神乡卫生院",
"2022-03-27",
"袁月华1959-05-18"
],
[
"严利来",
"男",
"延寿庵村",
"1947-04-13",
"新冠疫苗（Vero细胞）",
"3",
"六神乡卫生院",
"2022-03-27",
"严利来1947-04-13"
],
[
"李斯腊",
"男",
"延寿庵村",
"1944-12-11",
"新冠疫苗（Vero细胞）",
"3",
"六神乡卫生院",
"2022-03-27",
"李斯腊1944-12-11"
],
[
"李选民",
"女",
"延寿庵村",
"1945-08-29",
"新冠疫苗（Vero细胞）",
"3",
"六神乡卫生院",
"2022-03-27",
"李选民1945-08-29"
],
[
"董静",
"女",
"造册桥村",
"1983-05-01",
"新冠疫苗（Vero细胞）",
"3",
"六神乡卫生院",
"2022-03-27",
"董静1983-05-01"
]
]
arr=np.array(arr)
print(type(arr))
def arrToDict(arr):
	head=arr[0]
	data=arr[1:]
	return {r[-1]:dict(zip(head,r)) for r in data}
ret=arrToDict(arr)	
print(ret)
# print(ret["董静"]["村名"])
