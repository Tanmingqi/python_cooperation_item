import html

from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go

app = Flask(__name__)

# 准备工作
df = pd.read_csv('douban_movie.csv', encoding='utf-8', delimiter="\t")
cf.set_config_file(offline=True, theme="ggplot")
regions_available = list(df.concluding.dropna().unique())



print(regions_available) # 读取数据确认


@app.route('/',methods=['GET'])
def douban_2019():
    data_str = df.to_html()
    return render_template('results.html',
                           the_res = data_str,
                           the_select_region=regions_available,

                           )
    # 初始表格置入选择



@app.route('/table_concluding',methods=['POST'])
def table_1() -> 'html':
   the_region = request.form["the_region_selected"]
   print(the_region)  # 检查用户输入
   dfs = df.query("concluding=='{}'".format(the_region))   # 表格生成传输 评分
   data_str = dfs.to_html()
   return render_template('results.html',
                           the_res=data_str,
                           the_select_region=regions_available,
                          )




@app.route('/table_base')
def entry_page() -> 'html':
    # the_region = request.form["the_region_selected"]
    # print(the_region)




    return render_template('layout_form.html')


# 左边部分开始
@app.route('/production',methods=['POST'])
def tran_page3() -> 'html':


    return render_template('total_productions_of_countries.html',

                           )





@app.route('/score',methods=['POST'])
def tran_page5() -> 'html':
    return render_template('total_movie_rates.html',)

@app.route('/Proportion',methods=['POST'])
def tran_page7() -> 'html':
    return render_template('rates_of_douban_proportion.html')
#左边部分结束





#右边部分开始
@app.route('/source')
def tran_page2() -> 'html':
    return render_template('top_proportion_of_production.html')

@app.route('/place')
def tran_page6() -> 'html':
    return render_template('top.html')

@app.route('/director')
def tran_page1() -> 'html':
    return render_template('top_ten_directors.html')

@app.route('/artor')
def tran_page4() -> 'html':
    return render_template('actors.html')
#右边部分结束


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
