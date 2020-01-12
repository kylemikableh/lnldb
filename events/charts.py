import datetime

from django.db.models import Avg, Q
from django.utils import timezone
from jchart import Chart
from jchart.config import Axes, DataSet

from events.models import BaseEvent

class SurveyVpChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],
    }

    def get_datasets(self, *args, **kwargs):
        year_ago = timezone.now() - datetime.timedelta(days=365)
        events = BaseEvent.objects \
            .filter(datetime_start__gte=year_ago) \
            .filter(Q(billings__isnull=False) | Q(multibillings__isnull=False)) \
            .filter(surveys__isnull=False) \
            .distinct()
        data_communication_responsiveness = []
        data_bill_as_expected = []
        for event in events:
            data = event.surveys.aggregate(
                Avg('communication_responsiveness'),
                Avg('bill_as_expected'),
            )
            data_communication_responsiveness.append({'x': event.datetime_start.isoformat(), 'y': data['communication_responsiveness__avg']})
            data_bill_as_expected.append({'x': event.datetime_start.isoformat(), 'y': data['bill_as_expected__avg']})
        options = {'type': 'line', 'fill': False, 'lineTension': 0}
        return [
            DataSet(label='Communication responsiveness', data=data_communication_responsiveness, borderColor='#8B0000', backgroundColor='#8B0000', **options),
            DataSet(label='Bill as expected', data=data_bill_as_expected, borderColor='#66CDAA', backgroundColor='#66CDAA', **options),
        ]


class SurveyCrewChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],
    }

    def get_datasets(self, *args, **kwargs):
        year_ago = timezone.now() - datetime.timedelta(days=365)
        events = BaseEvent.objects \
            .filter(datetime_start__gte=year_ago) \
            .filter(Q(billings__isnull=False) | Q(multibillings__isnull=False)) \
            .filter(surveys__isnull=False) \
            .distinct()
        data_lighting_quality = []
        data_sound_quality = []
        data_setup_on_time = []
        data_crew_respectfulness = []
        data_crew_preparedness = []
        data_crew_knowledgeability = []
        for event in events:
            data = event.surveys.aggregate(
                Avg('lighting_quality'),
                Avg('sound_quality'),
                Avg('setup_on_time'),
                Avg('crew_respectfulness'),
                Avg('crew_preparedness'),
                Avg('crew_knowledgeability'),
            )
            data_lighting_quality.append({'x': event.datetime_start.isoformat(), 'y': data['lighting_quality__avg']})
            data_sound_quality.append({'x': event.datetime_start.isoformat(), 'y': data['sound_quality__avg']})
            data_setup_on_time.append({'x': event.datetime_start.isoformat(), 'y': data['setup_on_time__avg']})
            data_crew_respectfulness.append({'x': event.datetime_start.isoformat(), 'y': data['crew_respectfulness__avg']})
            data_crew_preparedness.append({'x': event.datetime_start.isoformat(), 'y': data['crew_preparedness__avg']})
            data_crew_knowledgeability.append({'x': event.datetime_start.isoformat(), 'y': data['crew_knowledgeability__avg']})
        options = {'type': 'line', 'fill': False, 'lineTension': 0}
        return [
            DataSet(label='Lighting quality', data=data_lighting_quality, borderColor='#F4A460', backgroundColor='#F4A460', **options),
            DataSet(label='Sound quality', data=data_sound_quality, borderColor='#006400', backgroundColor='#006400', **options),
            DataSet(label='Setup on time', data=data_setup_on_time, borderColor='#DB7093', backgroundColor='#DB7093', **options),
            DataSet(label='Crew respectfulness', data=data_crew_respectfulness, borderColor='#FFE4B5', backgroundColor='#FFE4B5', **options),
            DataSet(label='Crew preparedness', data=data_crew_preparedness, borderColor='#00008B', backgroundColor='#00008B', **options),
            DataSet(label='Crew knowledgeability', data=data_crew_knowledgeability, borderColor='#9932CC', backgroundColor='#9932CC', **options),
        ]


class SurveyPricelistChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],
    }

    def get_datasets(self, *args, **kwargs):
        year_ago = timezone.now() - datetime.timedelta(days=365)
        events = BaseEvent.objects \
            .filter(datetime_start__gte=year_ago) \
            .filter(Q(billings__isnull=False) | Q(multibillings__isnull=False)) \
            .filter(surveys__isnull=False) \
            .distinct()
        data_pricelist_ux = []
        data_quote_as_expected = []
        data_price_appropriate = []
        for event in events:
            data = event.surveys.aggregate(
                Avg('pricelist_ux'),
                Avg('quote_as_expected'),
                Avg('price_appropriate'),
            )
            data_pricelist_ux.append({'x': event.datetime_start.isoformat(), 'y': data['pricelist_ux__avg']})
            data_quote_as_expected.append({'x': event.datetime_start.isoformat(), 'y': data['quote_as_expected__avg']})
            data_price_appropriate.append({'x': event.datetime_start.isoformat(), 'y': data['price_appropriate__avg']})
        options = {'type': 'line', 'fill': False, 'lineTension': 0}
        return [
            DataSet(label='Pricelist UX', data=data_pricelist_ux, borderColor='#D8BFD8', backgroundColor='#D8BFD8', **options),
            DataSet(label='Quote as expected', data=data_quote_as_expected, borderColor='#696969', backgroundColor='#696969', **options),
            DataSet(label='Price appropriate', data=data_price_appropriate, borderColor='#FF4500', backgroundColor='#FF4500', **options),
        ]


class SurveyLnlChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],
    }

    def get_datasets(self, *args, **kwargs):
        year_ago = timezone.now() - datetime.timedelta(days=365)
        events = BaseEvent.objects \
            .filter(datetime_start__gte=year_ago) \
            .filter(Q(billings__isnull=False) | Q(multibillings__isnull=False)) \
            .filter(surveys__isnull=False) \
            .distinct()
        data_services_quality = []
        data_customer_would_return = []
        for event in events:
            data = event.surveys.aggregate(
                Avg('services_quality'),
                Avg('customer_would_return'),
            )
            data_services_quality.append({'x': event.datetime_start.isoformat(), 'y': data['services_quality__avg']})
            data_customer_would_return.append({'x': event.datetime_start.isoformat(), 'y': data['customer_would_return__avg']})
        options = {'type': 'line', 'fill': False, 'lineTension': 0}
        return [
            DataSet(label='Services quality', data=data_services_quality, borderColor='#4682B4', backgroundColor='#4682B4', **options),
            DataSet(label='Customer would return', data=data_customer_would_return, borderColor='#1E90FF', backgroundColor='#1E90FF', **options),
        ]
