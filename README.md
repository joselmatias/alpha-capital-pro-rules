# Alpha Capital PRO — Matriz de Reglas Qualified Trader

Aplicación Streamlit con el análisis completo de reglas del plan **Alpha Capital PRO** para cuentas Qualified Trader, con fuente etiquetada en cada regla.

## Estructura del proyecto

```
alpha_capital_app/
├── app.py            # Aplicación principal Streamlit
├── data.py           # Base de datos de reglas con etiqueta de fuente
├── requirements.txt  # Dependencias
└── README.md
```

## Fuentes de cada regla

| Etiqueta | Descripción |
|----------|-------------|
| 📄 Contrato | Proviene exclusivamente del General Service Agreement firmado |
| 🌐 Web | Proviene exclusivamente del Help Center (help.alphacapitalgroup.uk) |
| 📄🌐 Ambos | Confirmada tanto en el contrato como en el sitio web |

## Deployment en Streamlit Cloud

1. Sube esta carpeta a un repositorio GitHub (público o privado).
2. Ve a [share.streamlit.io](https://share.streamlit.io) y conecta tu cuenta de GitHub.
3. Selecciona el repositorio y el archivo principal: `app.py`.
4. Haz clic en **Deploy**.

> No se requieren secrets ni variables de entorno. La app funciona con solo `streamlit`.

## Correr localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```
