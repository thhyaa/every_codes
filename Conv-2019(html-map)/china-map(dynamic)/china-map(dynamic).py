import pandas as pd
from pyecharts.charts import Map
from pyecharts import options
from pyecharts.charts import Timeline


# 修改读取数据后的格式
data = pd.read_excel('china_data.xlsx')
data = data.T  # 转置
data.columns = data.iloc[0].tolist()
data = data.drop(index=['Unnamed: 0'], axis=0)
attr = data.columns.tolist()


timeline = Timeline()

for i in range(len(data)):
    #取每日数据
    row = data.iloc[i,].tolist()
    #将数据转换为二元的列表
    sequence_temp = list(zip(attr,row))
    #对日期格式化以便显示
    time = data.index[i]
    #创建地图
    map_temp =(
        Map(options.InitOpts(width='2400px', height='1200px', bg_color="#ffffff",page_title='中国疫情地图'))
        .add(time, sequence_temp, maptype="china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="全国疫情动态地图"),
            visualmap_opts=opts.VisualMapOpts(max_=2000),
        )
    )
    #将地图加入时间轴对象
    timeline.add(map_temp,time).add_schema(play_interval=360)
    
# 地图创建完成后，通过render()方法可以将地图渲染为html 
timeline.render('全国疫情动态地图.html')