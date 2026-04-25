import streamlit as st
from data import RULES

# ─────────────────────────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Alpha Capital PRO — Reglas Qualified Trader",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# ESTILOS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Fondo general */
    .stApp { background-color: #070b14; }
    section[data-testid="stSidebar"] { background-color: #0f172a; }

    /* Tipografía */
    html, body, [class*="css"] { font-family: 'DM Sans', 'Segoe UI', sans-serif; color: #e2e8f0; }

    /* Header principal */
    .main-header {
        background: linear-gradient(135deg, #0f0c29, #1a1033, #0f172a);
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 24px 28px;
        margin-bottom: 20px;
    }
    .main-header h1 { color: #f1f5f9; font-size: 26px; font-weight: 700; margin: 0 0 6px 0; }
    .main-header p  { color: #64748b; font-size: 13px; margin: 0; }
    .highlight      { color: #8b5cf6; }

    /* Alert crítico */
    .alert-critical {
        background: rgba(127,29,29,0.25);
        border: 1px solid rgba(239,68,68,0.35);
        border-left: 4px solid #ef4444;
        border-radius: 8px;
        padding: 14px 18px;
        margin-bottom: 20px;
        font-size: 13px;
        color: #fda4af;
        line-height: 1.7;
    }

    /* Cards de reglas */
    .rule-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 10px;
        padding: 16px 18px;
        margin-bottom: 12px;
        transition: border-color 0.2s;
    }
    .rule-card:hover { border-color: #334155; }

    /* Badges */
    .badge {
        display: inline-block;
        padding: 2px 9px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: 600;
        font-family: 'DM Mono', monospace;
        margin-right: 6px;
        margin-bottom: 2px;
    }
    .badge-critico    { background: rgba(127,29,29,0.4);  border:1px solid rgba(239,68,68,0.3);  color: #fca5a5; }
    .badge-moderado   { background: rgba(120,53,15,0.4);  border:1px solid rgba(245,158,11,0.3); color: #fcd34d; }
    .badge-operativo  { background: rgba(30,58,95,0.4);   border:1px solid rgba(59,130,246,0.3); color: #93c5fd; }
    .badge-informativo{ background: rgba(20,83,45,0.4);   border:1px solid rgba(16,185,129,0.3); color: #86efac; }

    /* Fuente badges */
    .badge-contract { background: rgba(139,92,246,0.2); border:1px solid rgba(139,92,246,0.35); color: #c4b5fd; }
    .badge-web      { background: rgba(6,182,212,0.2);  border:1px solid rgba(6,182,212,0.35);  color: #67e8f9; }
    .badge-both     { background: rgba(16,185,129,0.2); border:1px solid rgba(16,185,129,0.35); color: #6ee7b7; }

    /* Consecuencia */
    .consecuencia {
        background: rgba(15,23,42,0.8);
        border-left: 3px solid #334155;
        border-radius: 0 6px 6px 0;
        padding: 8px 12px;
        font-size: 12px;
        color: #94a3b8;
        margin-top: 10px;
        line-height: 1.6;
    }
    .consecuencia.critico  { border-left-color: #ef4444; color: #fca5a5; }
    .consecuencia.moderado { border-left-color: #f59e0b; color: #fcd34d; }

    /* Stats */
    .stat-box {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 10px;
        padding: 14px 16px;
        text-align: center;
    }
    .stat-val { font-size: 28px; font-weight: 700; font-family: 'DM Mono', monospace; }
    .stat-lbl { font-size: 11px; color: #475569; margin-top: 3px; }

    /* Referencia */
    .ref-tag {
        font-size: 10px;
        font-family: 'DM Mono', monospace;
        color: #475569;
        background: #080c18;
        border: 1px solid #1e293b;
        border-radius: 4px;
        padding: 2px 7px;
        margin-right: 5px;
        display: inline-block;
    }

    /* Sidebar labels */
    .stRadio > label { color: #94a3b8 !important; }
    .stMultiSelect > label { color: #94a3b8 !important; }
    .stSelectbox > label { color: #94a3b8 !important; }

    /* Ocultar footer Streamlit */
    footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# FUNCIONES AUXILIARES
# ─────────────────────────────────────────────────────────────────────────────
FUENTE_LABEL = {
    "CONTRACT": ("📄 Contrato",  "contract"),
    "WEB":      ("🌐 Web",       "web"),
    "BOTH":     ("📄🌐 Ambos",   "both"),
}
SEVERIDAD_ORDER = ["CRÍTICO", "MODERADO", "OPERATIVO", "INFORMATIVO"]

def severidad_badge(sev):
    cls = {"CRÍTICO": "critico", "MODERADO": "moderado",
           "OPERATIVO": "operativo", "INFORMATIVO": "informativo"}.get(sev, "informativo")
    icon = {"CRÍTICO": "🔴", "MODERADO": "🟡", "OPERATIVO": "🔵", "INFORMATIVO": "🟢"}.get(sev, "⚪")
    return f'<span class="badge badge-{cls}">{icon} {sev}</span>'

def fuente_badge(fuente):
    lbl, cls = FUENTE_LABEL.get(fuente, ("❓", "contract"))
    return f'<span class="badge badge-{cls}">{lbl}</span>'

def render_rule_card(rule):
    sev      = rule["severidad"]
    fuente   = rule["fuente"]
    cons_cls = {"CRÍTICO": "critico", "MODERADO": "moderado"}.get(sev, "")
    ref_cont = rule.get("referencia_contrato") or ""
    ref_web  = rule.get("referencia_web") or ""

    ref_html = ""
    if ref_cont:
        ref_html += f'<span class="ref-tag">📄 {ref_cont}</span>'
    if ref_web:
        short_ref = ref_web.replace("help.alphacapitalgroup.uk/en/articles/", "").replace("help.alphacapitalgroup.uk/en/", "")
        ref_html += f'<span class="ref-tag">🌐 {short_ref}</span>'

    st.markdown(f"""
    <div class="rule-card">
        <div style="margin-bottom:8px">
            {severidad_badge(sev)}{fuente_badge(fuente)}
        </div>
        <div style="font-size:14px;font-weight:600;color:#e2e8f0;line-height:1.4;margin-bottom:8px">
            {rule['regla']}
        </div>
        <div style="font-size:12.5px;color:#94a3b8;line-height:1.7">
            {rule['detalle']}
        </div>
        <div class="consecuencia {cons_cls}">
            <strong>⚡ Consecuencia:</strong> {rule['consecuencia']}
        </div>
        <div style="margin-top:10px">{ref_html}</div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR — FILTROS
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📊 Alpha Capital PRO")
    st.markdown("<small style='color:#475569'>Qualified Trader · Reglas vigentes</small>", unsafe_allow_html=True)
    st.divider()

    st.markdown("**Fuente**")
    fuente_sel = st.radio(
        "fuente",
        options=["Todas", "📄 Contrato", "🌐 Web", "📄🌐 Ambos"],
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown("**Severidad**")
    sev_sel = st.multiselect(
        "severidad",
        options=SEVERIDAD_ORDER,
        default=SEVERIDAD_ORDER,
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown("**Categoría**")
    all_cats = sorted(set(r["categoria"] for r in RULES))
    cat_sel = st.multiselect(
        "categorias",
        options=all_cats,
        default=all_cats,
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown("**Buscar**")
    search = st.text_input("buscar", placeholder="🔍 palabra clave...", label_visibility="collapsed")

    st.divider()
    st.markdown("<small style='color:#334155'>Basado en:<br>📄 General Service Agreement<br>🌐 help.alphacapitalgroup.uk</small>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# FILTRAR REGLAS
# ─────────────────────────────────────────────────────────────────────────────
FUENTE_MAP = {
    "Todas":        None,
    "📄 Contrato":  "CONTRACT",
    "🌐 Web":       "WEB",
    "📄🌐 Ambos":   "BOTH",
}
fuente_code = FUENTE_MAP[fuente_sel]

filtered = [
    r for r in RULES
    if (fuente_code is None or r["fuente"] == fuente_code)
    and r["severidad"] in sev_sel
    and r["categoria"] in cat_sel
    and (not search or search.lower() in r["regla"].lower() or search.lower() in r["detalle"].lower())
]

# ─────────────────────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>Reglas Qualified Trader — <span class="highlight">Alpha Capital PRO</span></h1>
    <p>Análisis unificado · Fuentes: 📄 Contrato (General Service Agreement) + 🌐 Help Center oficial</p>
</div>
""", unsafe_allow_html=True)

# ALERTA CRÍTICA
st.markdown("""
<div class="alert-critical">
    🔴 <strong>Cláusulas contractuales irrevocables que debes conocer:</strong><br>
    El sitio web tiene PRIORIDAD sobre el contrato firmado (Cláusula 1.4) ·
    Alpha puede terminar si <em>sospecha</em> incumplimiento (Cláusula 7.1) ·
    Non-Disparagement PERMANENTE — no puedes criticar a Alpha ni después de terminar (Cláusula 27.1) ·
    Tú pagas los costos legales de Alpha en cualquier disputa (Cláusula 27.2) ·
    Alpha NO está regulado por la FCA (Cláusula 28.4.1)
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# STATS
# ─────────────────────────────────────────────────────────────────────────────
total         = len(RULES)
total_critico = sum(1 for r in RULES if r["severidad"] == "CRÍTICO")
total_contract= sum(1 for r in RULES if r["fuente"] == "CONTRACT")
total_web     = sum(1 for r in RULES if r["fuente"] == "WEB")
total_both    = sum(1 for r in RULES if r["fuente"] == "BOTH")
showing       = len(filtered)

c1, c2, c3, c4, c5, c6 = st.columns(6)
for col, val, lbl, color in [
    (c1, showing,        "Mostrando",   "#8b5cf6"),
    (c2, total,          "Total Reglas","#3b82f6"),
    (c3, total_critico,  "🔴 Críticas", "#ef4444"),
    (c4, total_contract, "📄 Contrato", "#a78bfa"),
    (c5, total_web,      "🌐 Web",      "#67e8f9"),
    (c6, total_both,     "📄🌐 Ambos",  "#6ee7b7"),
]:
    col.markdown(f"""
    <div class="stat-box">
        <div class="stat-val" style="color:{color}">{val}</div>
        <div class="stat-lbl">{lbl}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# CONTENIDO PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────
if not filtered:
    st.warning("No se encontraron reglas con los filtros seleccionados.")
else:
    # Agrupar por categoría
    cats_in_filtered = []
    seen = set()
    for r in filtered:
        if r["categoria"] not in seen:
            cats_in_filtered.append(r["categoria"])
            seen.add(r["categoria"])

    for cat in cats_in_filtered:
        cat_rules = [r for r in filtered if r["categoria"] == cat]
        if not cat_rules:
            continue

        # Header de categoría con conteo de fuentes
        n_c = sum(1 for r in cat_rules if r["fuente"] == "CONTRACT")
        n_w = sum(1 for r in cat_rules if r["fuente"] == "WEB")
        n_b = sum(1 for r in cat_rules if r["fuente"] == "BOTH")

        source_info = ""
        if n_c: source_info += f'<span class="badge badge-contract">📄 {n_c}</span>'
        if n_w: source_info += f'<span class="badge badge-web">🌐 {n_w}</span>'
        if n_b: source_info += f'<span class="badge badge-both">📄🌐 {n_b}</span>'

        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:12px;margin:20px 0 12px 0;
                    padding:12px 18px;background:#080c18;border-radius:8px;
                    border-left:3px solid #334155">
            <span style="font-size:15px;font-weight:700;color:#e2e8f0">{cat}</span>
            <span style="font-size:11px;color:#475569">{len(cat_rules)} reglas</span>
            <div>{source_info}</div>
        </div>
        """, unsafe_allow_html=True)

        # Ordenar por severidad dentro de categoría
        order = {s: i for i, s in enumerate(SEVERIDAD_ORDER)}
        for rule in sorted(cat_rules, key=lambda r: order.get(r["severidad"], 99)):
            render_rule_card(rule)

# ─────────────────────────────────────────────────────────────────────────────
# LEYENDA FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.divider()
col_a, col_b, col_c, col_d = st.columns(4)
with col_a:
    st.markdown("<small style='color:#475569'>🔴 **CRÍTICO**: Cierre de cuenta o consecuencias legales graves</small>", unsafe_allow_html=True)
with col_b:
    st.markdown("<small style='color:#475569'>🟡 **MODERADO**: Restricciones o pérdida de ganancias</small>", unsafe_allow_html=True)
with col_c:
    st.markdown("<small style='color:#475569'>🔵 **OPERATIVO**: Parámetros de proceso que debes conocer</small>", unsafe_allow_html=True)
with col_d:
    st.markdown("<small style='color:#475569'>🟢 **INFORMATIVO**: Contexto legal sin consecuencia inmediata</small>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;margin-top:16px;font-size:11px;color:#334155">
    📄 General Service Agreement — Alpha Capital Group Limited · Company No. 13719951 · Harpenden, England
    &nbsp;·&nbsp; 🌐 help.alphacapitalgroup.uk
    &nbsp;·&nbsp; Análisis: José Matías Sánchez · Guayaquil, Ecuador
</div>
""", unsafe_allow_html=True)
