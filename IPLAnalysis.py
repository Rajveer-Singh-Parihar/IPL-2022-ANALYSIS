# Designing Data Requirement - Processing data - Performing Analytics over data - Visualizing data

# impoerting Libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects  as go

# READING THE CSV FILE
data = pd.read_csv(r"C:\Users\rajve\Downloads\IPL 2022.csv")
#print(data)

# Number of matches won by each team
figure = px.bar(data,x=data['match_winner'],title="Number Matches Won")
figure.show()

# Chasing and defending
data['won_by'] = data['won_by'].map({'Wickets':'Chasing','Runs':'Defending'})
won_by = data["won_by"].value_counts() # counts the occurence of each value
label = won_by.index  # unique names - what are we counting
counts = won_by.values # frequency of each category - how many of each
colors = ['red','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label,values=counts)])
fig.update_layout(title_text="Number of matches won by defending chasing")
fig.update_traces(hoverinfo= 'label+percent',textinfo='value',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()

# Best Bowler in ipl
figure=px.bar(data,x=data["best_bowling"],title="Best Bowler in IPL")
figure.show()

# Player of the match
figure = px.bar(data,x=data['player_of_the_match'],title='Most Player Of match Award')
figure.show()

# Top Scorer of the match
figure = px.bar(data,x=data['top_scorer'],y=data['highscore'],color=data['highscore'],title="Top Scorer in IPL")
figure.show()