from datadog import initialize, api

from gardnr import constants, drivers


class DataDogAPI(drivers.Exporter):
    blacklist = [constants.Metrics.IMAGE]

    def setup(self):
        options = {
            'api_key': self.api_key,
            'app_key': self.app_key
        }

        initialize(**options)

    def export(self, logs):
        api.Metric.send([{
            'metric': log.metric.name,
            'points': log.value} for log in logs])
