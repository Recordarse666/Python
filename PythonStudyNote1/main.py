 #数据类型/容器类型：列表和元组
 #序列：收纳各种数据对象，下标访问（相当于集合吗）
 #列表：可以删除，添加，替换，重排序列中元素（可变类型）
 #元组：不可变序列，更高性能
 #列表和元组的操作#####################################################
#创建列表:[],list()
alist=[1,2,3,4,5,6]
blist=list(["a","b","c","d","e","f"])
print(alist)
print(blist)

#创建元组:(),tuple()
atuple=(1,2,3,4,5,6)
btuple=tuple(["a","b","c","d","e","f"])
print(atuple)
print(btuple)

#列表/元组大小：len()
#f-string 在字符串前加 f，用 {变量/表达式} 嵌入值。
print(f"列表长度：{len(alist)}")
print(f"列表长度：{len(atuple)}")

#索引:alist[n]/atuple[n].注意：元组只能通过索引获取对应位置数据值，不可重新赋值
print(f"列表索引[0]:{alist[0]}")
print(f"元组索引[0]:{atuple[0]}")

#切片：alist[start:end:step];atuple[start:end:step]
print(f"列表切片[1:4]: {alist[1:4]}")#左闭右开，取的是alist[1],alist[2],alist[3]
print(f"列表切片[::2]: {alist[::2]}")
print(f"元组切片[1:4]: {atuple[1:4]}")

#查找：in查找元素是否在列表，index返回的是查找元素位置序列，count出现过几次
print(f"3在列表中吗? {3 in alist}")
print(f"7在列表中吗? {7 in alist}")
print(f"数字3的索引位置: {alist.index(3)}")
print(f"数字1出现次数: {alist.count(1)}")

#计算：sum累计求和，max/min
numbers = [10, 20, 30, 40, 50]
print(f"总和: {sum(numbers)}")
print(f"最大值: {max(numbers)}")
print(f"最小值: {min(numbers)}")

#列表操作###############################################################
#增长：append末尾添加/insert指定位置插入/extend合并，改变原列表
lst=[1,2,3]
lst.append(4)
print(lst)
lst.insert(1,99)#索引是从0开始的
print(lst)
lst.extend([5,6])
print(lst)

#缩减：pop(序号)，remove(对象本身)，clear整个变成空列表
removed=lst.pop(2)
print(lst)
lst.remove(99)
print(lst)
lst_copy=lst.copy()
lst_copy.clear()
print(lst_copy)

#重新组织：reverse头尾反转重新排列，sort按大小重排
nums=[3,4,1,5,7,2,6]
nums.reverse()
print(nums)

#sort对原列表重排
nums.sort()
print(nums)

#del删除第i个元素,index首次出现位置,count出现次数,remove将某个元素首次出现的删除
del nums[1]
print(nums)
print(nums.index(6))#6第一次出现的位置索引
print(nums.count(6))
nums.remove(6)
print(nums)

#合并+，连接两个列表/元组成一个新容器
#乘法*，赋值n次，新容器
list1=[1,2]
list2=[3,4]
print(list1+list2)
print(list1*2)

tuple1 = (1, 2)
tuple2 = (3, 4)
print(f"元组合并: {tuple1 + tuple2}")
print(f"元组重复: {tuple1 * 3}")


#数据类型/容器类型：字典
#字典：贴标签的数据“标签收纳盒”，通过标签获取数据；结构是Key(标签)-Value（数据值）,可变类型
#数据项，标签和数据项间用：连接

#批量添加，fromkeys() 会创建一个新字典，键来自可迭代对象，值统一为 None
a=dict.fromkeys(("name","age"))
print(a)

#创建字典：student={};student=dict()
bands={'Marxes':['Moe','Curly'],'KK':[True,'moon']}#value没有顺序，可以是任意类型，甚至可以是字典
print(bands['KK'][0])
poi={(100,100):'Zhongguancun',(123,23):'Pizza'}#()	创建元组，作为字典的 key，key只能是任意不可变类型，这里的元组是一个坐标
print(poi[(100,100)])#[]访问字典

#更新字典
#合并：update(新字典)，有相同标签更新Value值，无相同则把新的key-value值加进去
# 以下三种写法等价：
#b.update({"friends": ["Mike", "Alice"]})  # 方式1
#b.update(friends=["Mike", "Alice"])       # 方式2：关键字参数 + 等号
#b.update([("friends", ["Mike", "Alice"])]) # 方式3：可迭代对象,列表里可以有多个元组
#关联操作：
b={}
b["name"]="Tom"
b["age"]=10
print(b["name"])
print(b["age"])

bar={"course":["数学","英语"]}
b.update(bar)
print(b)
b.update(friends=["Mike","Alice"])
print(b)


#缩减字典，del删除指定数据项，pop删除指定标签的数据项并返回删除的数据值,popitem删除并返回一个数据项(默认删除最后一项，并返回),clear清除
del b["age"]
print(b)
remove=b.pop("name")
print(remove)
print(b)
remove1=b.popitem()
print(remove1)
print(b)
b.clear()
print(b)

#字典大小len()
print(len(b))

#访问字典的数据项
#标签索引 dict[key]，get方法，批量获取字典标签、数据值、数据项keys，values，items
c={"name":"Tom","age":10,"gender":"male"}
print(c["name"])
c["age"]=20#数据更新
print(c)

value=c.get('name')#无法做变量来用,也就是不能用get更改值
print(value)

print(c.keys())
print(c.values())
print(c.items())

#字典中查找in
d={"name":"Tom","age":10,"gender":"male"}
bool="name" in d
print(bool)
print("city" in d)
print(10 in d.values())#in与values结合判断某个数据值是否存在


########################################################