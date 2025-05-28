import streamlit as st

def generar_comandos_ma3(grupo, preset_tipo, preset_num, cue_base, num_cues, tiempo_fade):
    comandos = []
    for i in range(num_cues):
        comandos.append(f"Store Preset {preset_tipo} {preset_num + i} /g={grupo} /o")

    comandos.append(f"Store Sequence {cue_base}")
    for i in range(num_cues):
        comandos.append(f"Store Sequence {cue_base} Cue {i + 1} Preset {preset_tipo} {preset_num + i}")
        comandos.append(f"Fade Sequence {cue_base} Cue {i + 1} {tiempo_fade}")

    return "\n".join(comandos)

st.title("Generador de Código MA3 🚨")
st.write("Automatiza tu programación básica de presets y cues.")

grupo = st.number_input("Número de Grupo", min_value=1, value=1)
preset_tipo = st.selectbox("Tipo de Preset", [2, 3, 4, 5], format_func=lambda x: f"{x} ({['Dimmer','Position','Color','Gobo'][x-2]})")
preset_num = st.number_input("Preset Inicial", min_value=1, value=1)
cue_base = st.number_input("Número de Secuencia", min_value=1, value=101)
num_cues = st.slider("Número de Cues", 1, 20, 5)
tiempo_fade = st.text_input("Tiempo de Fade", value="1s")

if st.button("Generar Código"):
    resultado = generar_comandos_ma3(grupo, preset_tipo, preset_num, cue_base, num_cues, tiempo_fade)
    st.code(resultado, language='bash')
