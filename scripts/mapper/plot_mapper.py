import sys
from helper_functions import download_from_blob, upload_to_blob
from gtda.mapper import make_mapper_pipeline, plot_static_mapper_graph
from gtda.mapper.filter import Projection
from gtda.mapper.cover import OneDimensionalCover

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

data_scaled = download_from_blob('scaled_df_mapper', storage_conn_str, container_name)

mapper = make_mapper_pipeline(
    filter_func=Projection(columns=[0]),
    cover=OneDimensionalCover(n_intervals=10, overlap_frac=0.1)
)

data_scaled = data_scaled.to_numpy()

fig = plot_static_mapper_graph(mapper, data_scaled, color_data=data_scaled[:, 1])
upload_to_blob(fig.to_html(), 'mapper_plot', storage_conn_str, container_name, folder='plots')