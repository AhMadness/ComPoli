import plotly.graph_objects as go
import plotly
import json
import os
from flask import Flask, render_template, send_from_directory, request
from data import data, data_usa, data_eu, data_g20, data_nato, countries, states, data_search
from PIL import Image

# PLOTLY
axis_range = [-10, 10]

fig = go.Figure()

fig.update_xaxes(range=axis_range, title='', tickmode='linear', showticklabels=False, side='top', gridcolor="rgb(224,224,224)", showgrid=False)
fig.update_yaxes(range=axis_range, title='', tickmode='linear', showticklabels=False, side='right', gridcolor="rgb(224,224,224)", showgrid=False)

fig.update_layout(plot_bgcolor='rgb(255,255,255)', height=800, width=800, margin=dict(l=125, r=125, t=125, b=125))
fig.update_layout(autosize=True)

# fig.add_vline(x=0, line_width=3)
# fig.add_hline(y=0, line_width=3)

# Adding X & Y Axis ~
fig.add_trace(go.Scatter(x=[-11, 11], y=[0, 0], marker=dict(color="black", opacity=1), showlegend=False))
fig.add_trace(go.Scatter(x=[0, 0], y=[-11, 11], marker=dict(color="black", opacity=1), showlegend=False))

# Add Axis Labels ~
font = dict(size=18, color='black', family="Montserrat")
fig.add_annotation(x=-10, y=0, text="Communism", xanchor='right', yanchor='middle', showarrow=False, font=font)
fig.add_annotation(x=10, y=0, text="Capitalism", xanchor='left', yanchor='middle', showarrow=False, font=font)
fig.add_annotation(x=0, y=10, text="Authoritarian", xanchor='center', yanchor='bottom', showarrow=False, font=font)
fig.add_annotation(x=0, y=-10, text="Libertarian", xanchor='center', yanchor='top', showarrow=False, font=font)

# Adding Color To Quadrants ~
fig.add_shape(type="rect", x0=-10, y0=-10, x1=0, y1=0, fillcolor="#C8E4BC", opacity=1, layer="below", line_width=0,)
fig.add_shape(type="rect", x0=0, y0=-10, x1=10, y1=0, fillcolor="#F5F5A7", opacity=1, layer="below", line_width=0,)
fig.add_shape(type="rect", x0=-10, y0=0, x1=0, y1=10, fillcolor="#F9BABA", opacity=1, layer="below", line_width=0,)
fig.add_shape(type="rect", x0=0, y0=0, x1=10, y1=10, fillcolor="#92D9F8", opacity=1, layer="below", line_width=0,)

# fig.show()


# FLASK ~
app = Flask(__name__, template_folder=os.path.abspath(".")+"/templates",
            static_folder=os.path.abspath(".")+"/static")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        country = request.form.get("country", None)
        reset = request.form.get('reset', None)
        quiz = request.form.get('quiz', None)

        if quiz:
            # Quiz form was submitted
            name = request.form.get("name", '')
            if name == '':
                name = "Unidentified"
            y = request.form.get('Q1')
            x = request.form.get('Q2')
            fig.add_scatter(x=[x], y=[y], name=name, text=[name], mode="markers+text", hoverinfo='name',
                            showlegend=False, marker=dict(size=15, color='red', line=dict(color='black', width=3)),
                            textfont=dict(size=14, family='Montserrat', color='black'), textposition='bottom center',
                            hoverlabel=dict(bgcolor='white', font=dict(color='black')))

        elif reset or country.lower() == "reset" or country.lower() == "clear":
            fig.data = []
            fig.layout.images = []
            fig.add_trace(go.Scatter(x=[-11, 11], y=[0, 0], marker=dict(color="black", opacity=1), showlegend=False))
            fig.add_trace(go.Scatter(x=[0, 0], y=[-11, 11], marker=dict(color="black", opacity=1), showlegend=False))

        elif country.lower() == 'all':
            for key, value in data.items():
                x, y = value
                flag_url = f"flags/{key.lower()}.png"
                img = Image.open(flag_url)
                existing_image_objects = list(fig.layout.images) if fig.layout.images else []
                image_object = go.layout.Image(source=img, xref="x", yref="y", x=x, y=y, sizex=1, sizey=1,
                                               xanchor="center", yanchor="middle")
                existing_image_objects.append(image_object)
                fig.update_layout(images=existing_image_objects, showlegend=False)
                fig.add_scatter(x=[x], y=[y], name=key, mode='markers', hoverinfo='name')

        elif country.lower() == 'eu':
            for key, value in data_eu.items():
                x, y = value
                flag_url = f"flags/{key.lower()}.png"
                img = Image.open(flag_url)
                existing_image_objects = list(fig.layout.images) if fig.layout.images else []
                image_object = go.layout.Image(source=img, xref="x", yref="y", x=x, y=y, sizex=1, sizey=1,
                                               xanchor="center", yanchor="middle")
                existing_image_objects.append(image_object)
                fig.update_layout(images=existing_image_objects, showlegend=False)
                fig.add_scatter(x=[x], y=[y], name=key, mode='markers', hoverinfo='name', hoverlabel=dict(bgcolor='white', font=dict(color='black')))

        elif country.lower() == 'g20':
            for key, value in data_g20.items():
                x, y = value
                flag_url = f"flags/{key.lower()}.png"
                img = Image.open(flag_url)
                existing_image_objects = list(fig.layout.images) if fig.layout.images else []
                image_object = go.layout.Image(source=img, xref="x", yref="y", x=x, y=y, sizex=1, sizey=1,
                                               xanchor="center", yanchor="middle")
                existing_image_objects.append(image_object)
                fig.update_layout(images=existing_image_objects, showlegend=False)
                fig.add_scatter(x=[x], y=[y], name=key, mode='markers', hoverinfo='name', hoverlabel=dict(bgcolor='white', font=dict(color='black')))

        elif country.lower() == 'nato':
            for key, value in data_nato.items():
                x, y = value
                flag_url = f"flags/{key.lower()}.png"
                img = Image.open(flag_url)
                existing_image_objects = list(fig.layout.images) if fig.layout.images else []
                image_object = go.layout.Image(source=img, xref="x", yref="y", x=x, y=y, sizex=1, sizey=1,
                                               xanchor="center", yanchor="middle")
                existing_image_objects.append(image_object)
                fig.update_layout(images=existing_image_objects, showlegend=False)
                fig.add_scatter(x=[x], y=[y], name=key, mode='markers', hoverinfo='name', hoverlabel=dict(bgcolor='white', font=dict(color='black')))

        elif country.lower() == 'real':
            for key, value in data_usa["Real"].items():
                x, y = value
                flag_url = f"flags_usa/{key.lower()}.png"
                img = Image.open(flag_url)
                existing_image_objects = list(fig.layout.images) if fig.layout.images else []
                image_object = go.layout.Image(source=img, xref="x", yref="y", x=x, y=y, sizex=1, sizey=1,
                                               xanchor="center", yanchor="middle")
                existing_image_objects.append(image_object)
                fig.update_layout(images=existing_image_objects, showlegend=False)
                fig.add_scatter(x=[x], y=[y], name=key, mode='markers', hoverinfo='name', hoverlabel=dict(bgcolor='white', font=dict(color='black')))

        elif country.lower() == 'relative':
            for key, value in data_usa["Relative"].items():
                x, y = value
                flag_url = f"flags_usa/{key.lower()}.png"
                img = Image.open(flag_url)
                existing_image_objects = list(fig.layout.images) if fig.layout.images else []
                image_object = go.layout.Image(source=img, xref="x", yref="y", x=x, y=y, sizex=1, sizey=1,
                                               xanchor="center", yanchor="middle")
                existing_image_objects.append(image_object)
                fig.update_layout(images=existing_image_objects, showlegend=False)
                fig.add_scatter(x=[x], y=[y], name=key, mode='markers', hoverinfo='name', hoverlabel=dict(bgcolor='white', font=dict(color='black')))

        elif country.rstrip("-USA") in data_usa["Real"]:
            country = country.rstrip("-USA")
            x, y = data_usa["Real"][country]
            flag_url = f"flags_usa/{country.lower()}.png"
            existing_image_objects = list(fig.layout.images) if fig.layout.images else []
            image_object = go.layout.Image(source=Image.open(flag_url), xref="x", yref="y", x=x, y=y, sizex=1, sizey=1, xanchor="center", yanchor="middle")
            existing_image_objects.append(image_object)
            fig.update_layout(images=existing_image_objects, showlegend=False)
            if country not in [scatter.name for scatter in fig.data]:
                fig.add_scatter(x=[x], y=[y], name=country, mode='markers', hoverinfo='name', hoverlabel=dict(bgcolor='white', font=dict(color='black')))

        elif country in data:
            x, y = data[country]
            flag_url = f"flags/{country.lower()}.png"
            existing_image_objects = list(fig.layout.images) if fig.layout.images else []
            image_object = go.layout.Image(source=Image.open(flag_url), xref="x", yref="y", x=x, y=y, sizex=1, sizey=1, xanchor="center", yanchor="middle")
            existing_image_objects.append(image_object)
            fig.update_layout(images=existing_image_objects, showlegend=False)
            if country not in [scatter.name for scatter in fig.data]:
                fig.add_scatter(x=[x], y=[y], name=country, mode='markers', hoverinfo='name', hoverlabel=dict(bgcolor='white', font=dict(color='black')))
    plot = json.dumps(fig.to_dict(), cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", plot=plot, countries=countries, states=states, data_search=data_search)


if __name__ == "__main__":
    app.run()
