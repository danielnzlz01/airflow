import streamlit as st
from helper_functions import download_from_blob
import os

st.set_page_config(layout="wide")

storage_conn_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = os.getenv('AZURE_CONTAINER_NAME')

st.title('Booking Curves Clustering with Various Mehtods')

tab1, tab2, tab3, tab4 = st.tabs(["K-Means Clustering", "Spectral K-Means Clustering", 'Hierarchical Clustering', 'Mapper'])

with tab1:
    st.title('K-Means Clustering')

    kmeans_pca = download_from_blob('clusters_pca_kmeans', storage_conn_str, container_name, folder='plots', subfolder='kmeans')

    st.components.v1.html(kmeans_pca, height=500)

    st.write("""
    **Descripción:**
    
    En esta visualización, se muestran los resultados del análisis de clustering realizado con KMeans, donde se utilizan los dos primeros componentes principales (PC1 y PC2) obtenidos a través de PCA. 
    Cada punto representa una observación y los diferentes colores indican los distintos clusters identificados por el modelo. Esta representación gráfica nos permite observar cómo se distribuyen las observaciones en un espacio reducido, 
    lo que ayuda a comprender las relaciones y la segmentación entre los diferentes grupos. Se puede observar que, en base al PCA, hay algunos clusters que están bien definidos y otros no tanto. 
    En base a esta gráfica, parece ser que los clusters mejor definidos son el cluster 0, el cluster 1, y el cluster 6. Por otro lado, en la parte inferior de la gráfica se puede observar que datos pertenecientes al cluster 2, 5, y 7 están muy compactos, 
    lo que puede sugerir que estos clusters no están tan bien definidos y comparten características entre ellos.
    """
    )

    kmeans_reservations = download_from_blob('reservations_date_cluster_kmeans', storage_conn_str, container_name, folder='plots', subfolder='kmeans')

    st.components.v1.html(kmeans_reservations, height=500)

    st.write("""
    **Descripción:**
    
    La gráfica de serie de tiempo con los clusters de K-Means muestra cómo se agrupan las observaciones a lo largo del tiempo según patrones similares. 
    Cada color representa un cluster diferente, lo que permite identificar comportamientos similares en distintos períodos. 
    Esta visualización ayuda a comprender cómo los datos evolucionan y cómo se agrupan en función de sus características, facilitando la detección de tendencias o patrones recurrentes.
    Esta figura busca mostrar que clusters (que en este caso representan las diferentes curvas de demanda) están presentes durante los días que se tiene. 
    Lo más interesante de esto es que, en si, los clusters se podrían dividir en dos conjuntos, 
    aquellos presentes antes del COVID (0, 3, y 6) y aquellos que están presentes durante el COVID (5, 2, 1, y 7); 
    el cluster 4 es el único que presenta instancias tanto antes como durante el COVID. Sabiendo esto, 
    se podría descartar el uso de los clusters presentes durante el COVID ya que esta fue una situación atípica, 
    y difícilmente estas curvas de demanda puedan llegar a ser útiles para poder afinar la predicción de demanda en un mundo post-pandemia.
    """
    )
    
    st.write("### Estadiscticas de los Clusters")

    cluster_means_kmeans = download_from_blob('cluster_means_kmeans', storage_conn_str, container_name, folder='parquets')

    st.write(cluster_means_kmeans)

    st.write("""
    **Descripción:**

    En la tabla presentada, se muestra el promedio de las características para cada cluster identificado mediante KMeans. Cada fila corresponde a un cluster, 
    y las columnas representan las medias de las variables numéricas dentro de ese cluster. Además, se ha agregado la columna "Count", 
    que muestra el número de observaciones en cada cluster. Esta información es útil para analizar las características promedio de cada grupo y su tamaño relativo.
    Algunas cosas interesantes que se pueden observar son que las columnas que parecen presentar mayor variabilidad son las de reservaciones y ventana de reservación, 
    y que existen dos clusters (1 y 7) con relativamente pocas instancias.
    """)
    
with tab2:
    st.title("Spectral K-Means Clustering")

    spectral_pca = download_from_blob('clusters_pca_spectral', storage_conn_str, container_name, folder='plots', subfolder='spectral')

    st.components.v1.html(spectral_pca, height=500)

    st.write("""
    **Descripción:**

    En esta gráfica podemos encontrar muchas similitudes con la de K-Means, como que hay ciertos clusters que están bien definidos y otros no tanto. 
    En esta ocasión, los clusters mejor definidos son el cluster 0, el cluster 4, y el cluster 6. Los cuales son similares a los de K-Means pero con diferente número.
    Por otro lado, los clusters que se encuentran muy agrupados y sin tanta claridad, son el 1, 2, y 3 están muy compactos.
    """)

    spectral_reservations = download_from_blob('reservations_date_cluster_spectral', storage_conn_str, container_name, folder='plots', subfolder='spectral')

    st.components.v1.html(spectral_reservations, height=500)

    st.write("""
    Nuevamente podemos observar similaridades entre el K-Means y Spectral Clustering, ya que aquí también podemos identificar que los clusters se podrían dividir en dos conjuntos, 
    aquellos presentes antes del COVID (0, 4 y 5) y aquellos que están presentes durante el COVID (4, 1, y 7); 
    el cluster 2 es el único que presenta instancias tanto antes como durante el COVID. Fue una división muy similar, pero si tiene sus pequeñas diferencias.
    """
    )

    st.write("### Estadiscticas de los Clusters")

    cluster_means_spectral = download_from_blob('cluster_means_spectral', storage_conn_str, container_name, folder='parquets')

    st.write(cluster_means_spectral)

    st.write("""
    **Descripción:**

    La tabla demuestra cosas diferentes a la de K-Means ya que se pueden observar que las columnas con mayor variabilidad son las de reservaciones, tarifa total 
    y ventana de reservación, sin embargo la cantidad de personas no varió mucho. Aquí solo hubo un cluster que tuvo que pocas instancias, siendo el Cluster 6.
    """)

with tab3:
    st.title("Hierarchical Clustering")

    hierarchical_dendogram = download_from_blob('dendrogram_hierarchical', storage_conn_str, container_name, folder='plots', subfolder='hierarchical')

    st.components.v1.html(hierarchical_dendogram, height=500)

    st.write("""
    El dendrograma que se encuentra anteriormente demuestra cómo los datos se organizan de manera jerárquica. En este diagrama, cada combinación entre puntos o conjuntos de puntos se ilustra con una rama. 
    La altura de las ramas representa la separación entre los puntos que se agrupan. Este diagrama permite visualizar la estructura de los datos.
    y seleccionar un número apropiado de agrupaciones, identificando el punto en el que las fusiones se estancan. Para este caso, se decidió elegir el punto 10 como punto de corte,
    lo cual representó 8 clusters, similar a lo que se hizo en K-Means.
    """)

    hierarchical_pca = download_from_blob('clusters_pca_hierarchical', storage_conn_str, container_name, folder='plots', subfolder='hierarchical')

    st.components.v1.html(hierarchical_pca, height=500)

    st.write("""
     **Descripción:**

    En esta gráfica podemos notar un poco más de diferencias a las anteriores de PCA. 
    En esta ocasión, los clusters mejor definidos son el cluster 1, cluster 3, el cluster 4, y el cluster 6. Algunos son similares a los de K-Means pero con diferente número,
    sin embargo, en este caso podemos observar una separación más clara en la parte izquierda de la gráfica para el cluster 3.
    Por otro lado, los clusters que se encuentran muy agrupados y sin tanta claridad siguen siendo los mismos que se encuentran en la parte baja de la gráfica,
    estos son el 0, 2, y 5.
    """)

    hierarchical_reservations = download_from_blob('reservations_date_cluster_hierarchical', storage_conn_str, container_name, folder='plots', subfolder='hierarchical')

    st.components.v1.html(hierarchical_reservations, height=500)

    st.write("""
    En esta gráfica podemos observar como el cluster 1 esta muy presente antes del COVID, completamente absorbiendo otros clusters que se observaban en las gráficas de los otros modelos.
    De igual manera hay clusters antes (1, 3 y 4) y después (0, 2, 6 y 7) del COVID. En este caso no hubo ningún cluster que estuviera en ambas épocas lo cual indica una mejor separación
    en las diferentes epocas. 
    """
    )

    st.write("### Estadiscticas de los Clusters")

    cluster_means_hierarchical = download_from_blob('cluster_means_hierarchical', storage_conn_str, container_name, folder='parquets')

    st.write(cluster_means_hierarchical)

    st.write("""
    **Descripción:**

    La tabla demuestra cosas similares a la de K-Means ya que se pueden observar que las columnas con mayor variabilidad son las de reservaciones, tarifa total 
    y ventana de reservación, la cantidad de personas solo fue afectada para el cluster 7 pero porque tiene pocas instancias, lo cual indica que creó un cluster
    únicamente para los outliers. El cluster 6 también tuvo pocas instancias pero no tuvo ninguna variable fuera de lo normal para indicar una separación significativa.
    """)

with tab4:
    st.title("Mapper Pipeline Visualization")

    mapper = download_from_blob('mapper_plot', storage_conn_str, container_name, folder='plots', subfolder='mapper')

    st.components.v1.html(mapper, height=500)

    st.write("""
    **Descripción:**

    El gráfico generado con Mapper representa una simplificación topológica de los datos de reservas hoteleras, 
    donde cada nodo agrupa reservas con características similares en función de un filtrado y clustering aplicados a los datos. 
    Las conexiones entre nodos indican solapamientos entre intervalos definidos por el filtro.
    En este caso, los nodos están coloreados según los valores escalados de ID_Reserva (Número de reservaciones), 
    lo que permite identificar cómo se distribuyen los identificadores de reservas en el espacio de características. 
    El gráfico muestra una estructura central densa, que representa el comportamiento típico de las reservas 
    (con similitudes en variables como días de estancia, precios o número de personas). 
    Las regiones desconectadas o menos densas sugieren patrones de comportamiento menos comunes o posibles outliers en las reservas.
    """)