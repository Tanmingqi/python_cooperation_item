# python期末项目
### 题目：豆瓣电影相关信息数据可视化

一、**所含内容：**

* 一共有五个页面，分别是初始页，两个数据筛选页和两个数据整合页

1. 初始页背景包括：初始总表格，两个下拉跳转表单（一个靠“Do it！”键跳转，一个点击选项即可跳转），一个“返回上一页”键，初始总表格在导入“douban_movie.csv”后生成，“返回上一页”键可作用于所有五个页面



2. 靠“Do it！”键跳转的两个页面为数据筛选页，根据初始总表“concluding”属性，清洗筛选“TOP”和“世界”两大类并分别生成表格传输进flask网页中，下拉选单之后选择相应的选项，点击“Do it！”键即可跳转相应的表格查看豆瓣前250电影排行情况和世界范围内的电影产量情况



3. 初始页另外一个下拉选单也有两个选项，分别是Top250电影分析和世界电影评分分析，选择选项之后不需要点其他按键即可跳转，我和我的搭档将七张可视化图表分别整合了两个页面对应两个选项动作生成后跳转的URL，我整合了Top250电影分析的可视化图表的HTML文档，增加了全局的JavaScript粒子线条动画效果和返回上一页键实现页面内部跳转功能。



4.所含的URL：
、、、
http://chenzhouchi.pythonanywhere.com/

http://chenzhouchi.pythonanywhere.com/table_concluding

https://lephyant.gitee.io/experiment_sample/

https://lephyant.gitee.io/experiment_sample2/
、、、



---


二、**URL**


* **Github代码URL:**
[https://github.com/Tanmingqi/python_cooperation_item](https://github.com/Tanmingqi/python_cooperation_item)


* **PyhtonanywhereURL:**
[http://tanmingqi.pythonanywhere.com/](http://tanmingqi.pythonanywhere.com/)


---



三、**数据传递功能描述**

从名为douban_movie.csv中的excel表格中的提取数据，经df = pd.read_csv(‘douban_movie.csv’,encoding = ‘utf8’,delimiter = “\t”) 然后根据movie.py中的data_str = df.to_html和results.html 中的{{ the_res|safe }} ，在初始douban_movie.csv页面生成初始总表，根据douban_movie.csv的regions_available = list(df.concluding.dropna().unique())，从conclusing筛选出Top和世界两大类，将用户的选择作为了select
_region，将region_avaliable 定义为select _region，然后使用the_region = request.form["the_region_selected"]，根据form的字典属性，然后利用requests访问提交数据，并用the_region定义，之后在确认用户选择输入之后，使用movie.py中的dfs = df.query(“concluding=’{}’.format(the_region) )和result.html中{% for item in the_select_region %} &lt;option value="{{ item }}"&gt;{{ item }}</option>{% endfor %}然后循环迭代总表中conclusing属性下的top和世界两大类数据，并归类传到前台生成表单。当在初始页面第一个下拉表单选择top或者世界选项时，即可将动作传到后台，经代码运行后，将结果传递到results.html，响应到movie.py文件中，在前端即可跳转相对应的页面。

---



四、**文档描述**


* HTML档描述



前端HTML名称：top250.html/world.html
后端HTML名称：result.html

result.html响应页面描述：两队下拉表单组成：选择种类的top和世界选项，以及对于的“Do it！”按钮，第二个是跳转至可视化页面的下来表单，以及对于的返回上一页。下面粘连着从douban_movie.csv的提取出来的数据。

前端可视化图表页面描述：将七个图表整合成两个HTML可视化图表文档并调整图表的cs使其居中，在底部加入&lt;footer&gt;标签并设置css样式让底部栏呈现灰色，加入&lt;/br&gt;标签划分并在底部栏加入豆瓣电影相关数据故事；在全局加入JavaScript动画效果和返回上一页键作用页面全局。




* Python档描述

Python档名称：movie.py

movie.py引入html，flask，pandas模块。Flask作为web应用对象，通过pandas读取csv数据，传输到前端。运用‘ / ’和’/table_concluding ’和定义的函数关联，dropna().unique()清洗筛选数据，并用list列表归纳，然后用生成表格。



* Web App动作描述

（1）
类型下拉表单：点击后可以选择要了解的种类：top/世界；
对应的按键： ”Do it！“ 点击后跳转到对应的电影数据表格；



（2）
方向按键：点击后可以选择对于的分析：“Top250电影分析”和“世界电影评分分析”，直接点击后可以跳转到对应的可视化页面；




（3）
返回上一页按键：点击后可以放回至上一页的选择，实现内部跳转。
