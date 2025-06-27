import json
import apache_beam as beam

class CleanAndTransform(beam.DoFn):
    def process(self, element):
        try:
            record = json.loads(element)
            # Basic cleaning and typing
            record['cpi'] = float(record.get('cpi', 0.0))
            record['wage'] = float(record.get('wage', 0.0))
            record['country'] = record.get('country', '').strip().upper()
            # Example enrichment
            record['inflation_risk'] = 'HIGH' if record['cpi'] > 6.0 else 'MODERATE'
            yield json.dumps(record)
        except Exception as e:
            print(f"Error processing record: {e}")
