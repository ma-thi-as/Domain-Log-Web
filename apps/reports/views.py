from django.views.generic import TemplateView
from .models import DominioLog, EmailLog
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


class DominioLogChartView(TemplateView):
    template_name = 'dominio_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Query the data
        data = DominioLog.objects.all()

        # Create a DataFrame from the data
        df = pd.DataFrame(list(data.values()))

        # Convert the date field to a datetime object
        df['date'] = pd.to_datetime(df['date'])

        # Group the data by date and sum the metric values
        df_grouped = df.groupby(['date']).sum().reset_index()

        # Create the stacked bar chart with Plotly
        fig = go.Figure(data=[
            go.Bar(name='Sent', x=df_grouped['date'], y=df_grouped['sent']),
            go.Bar(name='Received', x=df_grouped['date'], y=df_grouped['received']),
            go.Bar(name='Renruted', x=df_grouped['date'], y=df_grouped['renruted']),
            go.Bar(name='Rejected', x=df_grouped['date'], y=df_grouped['rejected'])
        ])
        fig.update_layout(barmode='stack', xaxis_title='Date', yaxis_title='Count', title='Dominio Log Metrics')

        # Convert the plot to HTML
        domain_plot_html = fig.to_html(full_html=False)

        # Pass the plot HTML to the template
        context['domain_plot_html'] = domain_plot_html

        return context

class EmailLogChartView(TemplateView):
    template_name = 'email_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Query the data
        data = EmailLog.objects.all()

        # Create a DataFrame from the data
        df = pd.DataFrame(list(data.values()))

        # Convert the date field to a datetime object
        df['date'] = pd.to_datetime(df['date'])

        # Group the data by useremail and sum the metric values
        df_grouped = df.groupby(['useremail']).sum().reset_index()

        # Create the pie chart with Plotly
        fig = px.pie(df_grouped, values='sent', names='useremail', title='Email Metrics by User')

        # Update the layout of the plot


        # Convert the plot to HTML
        email_plot_html = fig.to_html(full_html=False)

        # Pass the plot HTML to the template
        context['email_plot_html'] = email_plot_html

        return context