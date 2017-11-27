
import plotly.offline
from plotly.graph_objs import *
 
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline
from plotly.graph_objs import *
# Generate the figure
import plotly.plotly as py
import plotly.graph_objs as go
#32841
list_list_all_lable = [
#0
["孩子","死刑","幼儿园","老师","畜生","家长","社会","保护","枪毙","国家"],

]
list_list_all_value = [
[ 1811 , 1195 , 774 , 534 , 429 , 405 , 313 , 285 , 266 , 256 ]
]

list_articalClssfy= ['红蓝黄事件']

list_values = list_list_all_value[0]
list_lables = list_list_all_lable[0]
strName = list_articalClssfy[0]
myfilename = "hot_topic"
#

fig = {
	"data": [
	{
		"values": list_values,
		"labels": list_lables,
		"domain": {"x": [0, 1]},
		"name": strName,
		"hoverinfo": "label+percent+name",
		"hole": .4,
		"type": "pie"
	}],
	"layout": {
		"title": "'新浪全民话题'-'%s'"%strName,
		"annotations": [
			{
				"font": {
					"size": 30
				},
				"showarrow": False,
				"text": strName,
				"x": 0.50,
				"y": 0.5
			}
		]
	}
}



plotly.offline.plot(fig, filename='%s.html' % myfilename)
#py.iplot(fig, filename='grouped-bar')
print('Completed')