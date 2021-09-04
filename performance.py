import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

data=[]
for index in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    data.append(dice1+dice2)

mean=sum(data)/len(data)
std_deviation=statistics.stdev(data)
median=statistics.median(data)
mode=statistics.mode(data)
first_std_deviation_start,first_std_deviation_end=mean.std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
fig=ff.create_distplot([data],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="startsd1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="endsd1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="startsd2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="endsd2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_end],y=[0,0.17],mode="lines",name="startsd3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="endsd3"))
fig.show()
listofdatasd1=[result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
listofdatasd2=[result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
listofdatasd3=[result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]
print("mean of this data is {}".format(mean))
print("median of the data is {}".format(median))
print("mode od the data is {}".format(mode))
print("{}% of data lies within one standard deviation".format(len(listofdatasd1)*100.0/len(data)))
print("{}% of data lies within two standard deviation".format(len(listofdatasd2)*100.0/len(data)))
print("{}% of data lies within three standard deviation".format(len(listofdatasd3)*100.0/len(data)))