import sdv

sdv.version.public

from sdv.datasets.demo import download_demo

real_data, metadata = download_demo(
    modality='single_table',
    dataset_name='fake_hotel_guests'
)

real_data.head()
metadata.visualize()

from sdv.single_table import GaussianCopulaSynthesizer

#synthesizer = GaussianCopulaSynthesizer(metadata)
#synthesizer.fit(real_data)
#synthesizer.save('my_synthesizer.pkl')
synthesizer = GaussianCopulaSynthesizer.load('my_synthesizer.pkl')
synthetic_data = synthesizer.sample(num_rows=500)
synthetic_data.head()

from sdv.evaluation.single_table import run_diagnostic

diagnostic = run_diagnostic(
    real_data=real_data,
    synthetic_data=synthetic_data,
    metadata=metadata
)

from sdv.evaluation.single_table import evaluate_quality

quality_report = evaluate_quality(
    real_data,
    synthetic_data,
    metadata
)

quality_report.get_details('Column Shapes')


from sdv.evaluation.single_table import get_column_plot

fig = get_column_plot(
    real_data=real_data,
    synthetic_data=synthetic_data,
    column_name='room_rate',
    metadata=metadata
)

#fig.show()

fig1 = get_column_plot(
    real_data=real_data,
    synthetic_data=synthetic_data,
    column_name='checkin_date',
    metadata=metadata
)

#fig1.show()

from sdv.evaluation.single_table import get_column_pair_plot

fig2 = get_column_pair_plot(
    real_data=real_data,
    synthetic_data=synthetic_data,
    column_names=['room_rate', 'room_type'],
    metadata=metadata
)

#fig2.show()

sensitive_column_names = ['guest_email', 'billing_address', 'credit_card_number']

real_data[sensitive_column_names].head(3)

synthetic_data[sensitive_column_names].head(3)



