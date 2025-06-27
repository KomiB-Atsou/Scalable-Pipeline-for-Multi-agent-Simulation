import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from beam_pipeline.transforms import CleanAndTransform

def run():
    options = PipelineOptions(
        streaming=False,
        runner='DirectRunner'  # Change to 'DataflowRunner' if running on GCP
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | "Read raw inflation data" >> beam.io.ReadFromText("data/inflation_data.json")
            | "Clean and enrich data" >> beam.ParDo(CleanAndTransform())
            | "Write transformed output" >> beam.io.WriteToText("output/inflation_output", file_name_suffix=".json")
        )

if __name__ == "__main__":
    run()
