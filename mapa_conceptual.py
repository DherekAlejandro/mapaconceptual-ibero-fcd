import streamlit as st
from pyvis.network import Network

# Configurar el título de la aplicación
st.set_page_config(page_title="Mapa Conceptual de Ciencia de Datos", layout="wide")

# Encabezado
st.title("📊 Mapa Conceptual de Ciencia de Datos")

st.markdown("""
### **Descripción**
Este mapa conceptual presenta una estructura clara sobre los fundamentos de la ciencia de datos, 
incluyendo términos clave como Big Data, Minería de Datos, Python, Machine Learning, y más. 
Cada nodo representa un concepto fundamental y su relación con otros elementos dentro del campo.
""")

# Crear el gráfico con pyvis
net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

# Agregar nodos principales
net.add_node("Ciencia de Datos", label="Ciencia de Datos", color="lightblue")

# Conexiones con Big Data y Estadística
net.add_node("Big Data", label="Big Data", color="orange")
net.add_node("Estadística", label="Estadística", color="orange")
net.add_edge("Ciencia de Datos", "Big Data", label="Gestión de Datos Masivos")
net.add_edge("Ciencia de Datos", "Estadística", label="Base Matemática")

# Subtemas de Big Data
big_data_subtopics = {
    "Volumen": ["Almacenamiento", "Escalabilidad"],
    "Velocidad": ["Procesamiento en Tiempo Real", "Baja Latencia"],
    "Variedad": ["Estructurados", "No Estructurados", "Semi-Estructurados"],
    "Veracidad": ["Calidad de Datos", "Fuentes Confiables"],
    "Valor": ["Análisis Predictivo", "Toma de Decisiones"]
}

for parent, children in big_data_subtopics.items():
    net.add_node(parent, label=parent, color="yellow")
    net.add_edge("Big Data", parent)
    for child in children:
        net.add_node(child, label=child, color="lightyellow")
        net.add_edge(parent, child)

# Subtemas de Estadística
for subtema in ["Inferencial", "Descriptiva"]:
    net.add_node(subtema, label=subtema, color="yellow")
    net.add_edge("Estadística", subtema)

# Relación con Python y Herramientas
net.add_node("Python", label="Python", color="green")
for herramienta in ["Pandas", "NumPy", "Scikit-Learn", "Matplotlib", "Seaborn"]:
    net.add_node(herramienta, label=herramienta, color="lightgreen")
    net.add_edge("Python", herramienta, label="Librerías")
net.add_edge("Ciencia de Datos", "Python", label="Lenguaje de Programación")

# Minería de Datos
net.add_node("Minería de Datos", label="Minería de Datos", color="purple")
for subtema in ["Clasificación", "Agrupación", "Regresión", "Asociación", "Reducción de Dimensionalidad"]:
    net.add_node(subtema, label=subtema, color="pink")
    net.add_edge("Minería de Datos", subtema)
net.add_edge("Ciencia de Datos", "Minería de Datos", label="Extracción de Conocimiento")

# Conectar Ciencia de Datos con más subtemas
subtemas_cd = {
    "Blockchain": ["Seguridad de Datos", "Contratos Inteligentes"],
    "Cloud Computing": ["IA en la Nube", "Almacenamiento Distribuido"],
    "Edge Computing": ["Procesamiento en el Borde", "Reducción de Latencia"],
    "Ética en Ciencia de Datos": ["Privacidad", "Sesgo en Datos"],
    "Procesamiento de Lenguaje Natural": ["Análisis de Sentimientos", "Traducción Automática"],
    "Ingeniería de Características": ["Selección de Características", "Transformación de Datos"],
    "Optimización": ["Algoritmos Genéticos", "Descenso de Gradiente"]
}

for parent, children in subtemas_cd.items():
    net.add_node(parent, label=parent, color="cyan")
    net.add_edge("Ciencia de Datos", parent)
    for child in children:
        net.add_node(child, label=child, color="lightblue")
        net.add_edge(parent, child)

# Guardar y mostrar el gráfico en Streamlit
net.save_graph("mapa_conceptual.html")
st.markdown("### **Mapa Conceptual Interactivo**")
st.components.v1.html(open("mapa_conceptual.html", "r").read(), height=750)

# Exportación del mapa conceptual
st.markdown("### **👅 Descarga tu Mapa Conceptual**")
st.markdown("Puedes hacer clic derecho sobre la imagen y guardarla como PNG o usar herramientas como Print Screen para capturarla.")
