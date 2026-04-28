# data.py — Alpha Capital Group · Reglas Plan PRO (Qualified Trader)
# Fuente etiquetada: CONTRACT | WEB | BOTH

RULES = [
    # ─────────────────────────────────────────────────────────────
    # CATEGORÍA: DRAWDOWN Y PÉRDIDAS
    # ─────────────────────────────────────────────────────────────
    {
        "categoria": "📉 Drawdown y Pérdidas",
        "regla": "Pérdida diaria máxima: 3% (PRO 6%) / 4% (PRO 8%) / 5% (PRO 10%)",
        "detalle": (
            "Se calcula sobre el balance o equity al cierre de la vela diaria (00:00 broker time GMT+2/GMT+3). "
            "PRO 6%: se usa el mayor entre equity y balance del día. "
            "PRO 8% y 10%: solo balance-based. "
            "Una breach se aplica en base al equity actual (incluyendo trades abiertos no realizados)."
        ),
        "consecuencia": "Cierre automático de todos los trades + cierre permanente de la cuenta. Sin advertencia previa.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 1 y Schedule 3",
        "referencia_web": "help.alphacapitalgroup.uk — Daily Risk Limits",
    },
    {
        "categoria": "📉 Drawdown y Pérdidas",
        "regla": "Pérdida total máxima estática: 6% (PRO 6%) / 8% (PRO 8%) / 10% (PRO 10%)",
        "detalle": (
            "El drawdown total nunca puede superar el porcentaje según la variante PRO. "
            "Es ESTÁTICO: se calcula siempre sobre el balance inicial de la cuenta fondeada, no sigue el balance actual."
        ),
        "consecuencia": "Cierre permanente de la cuenta fondeada.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 1 (Max Sim Drawdown) y Schedule 3",
        "referencia_web": "help.alphacapitalgroup.uk — Alpha Pro Plan",
    },
    {
        "categoria": "📉 Drawdown y Pérdidas",
        "regla": "Breach se aplica con trades ABIERTOS (equity, no solo balance)",
        "detalle": (
            "Independientemente de si el cálculo base es equity o balance, las violaciones se aplican "
            "en función del equity actual de la cuenta (incluyendo pérdidas no realizadas en trades abiertos). "
            "Si tu equity cae por debajo del límite diario, el sistema cierra todo automáticamente."
        ),
        "consecuencia": "Hard breach automático. Todos los trades se cierran por el sistema.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 1 — Notas importantes",
        "referencia_web": "help.alphacapitalgroup.uk — Daily Risk Limits",
    },

    # ─────────────────────────────────────────────────────────────
    # CATEGORÍA: NIVEL DE RIESGO Y CONSISTENCIA
    # ─────────────────────────────────────────────────────────────
    {
        "categoria": "📐 Nivel de Riesgo y Consistencia",
        "regla": "Debes mantener el mismo nivel de riesgo que usaste en el Challenge",
        "detalle": (
            "El contrato establece que el Qualified Analyst debe mantener el mismo nivel de exposición "
            "que tenía en la cuenta de evaluación. Ejemplo: si en el challenge operabas con $100k de exposición, "
            "debes mantener eso en la cuenta fondeada. Reducir drásticamente el tamaño es violación contractual."
        ),
        "consecuencia": "Terminación INSTANTÁNEA del servicio y cierre de cuenta. Sin advertencia.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 28.3.2",
        "referencia_web": None,
    },
    {
        "categoria": "📐 Nivel de Riesgo y Consistencia",
        "regla": "Regla de Consistencia 40% Best Day (On-Demand)",
        "detalle": (
            "Ningún día de trading puede representar ≥40% del total de ganancias netas acumuladas. "
            "Fórmula: Mejor día / Ganancias totales < 0.40. "
            "Ejemplo: si ganas $1,000 en un día, debes tener al menos $2,500 en ganancias totales para retirar. "
            "Solo aplica al payout On-Demand. El bi-weekly no tiene esta regla."
        ),
        "consecuencia": "Payout bloqueado hasta que el score baje de 40%. No hay violación de cuenta, solo bloqueo de retiro.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Performance Fees On-Demand",
        "referencia_web": "help.alphacapitalgroup.uk — Performance Fee On-Demand",
    },
    {
        "categoria": "📐 Nivel de Riesgo y Consistencia",
        "regla": "Mínimo 5 días de trading — 1er payout Bi-Weekly",
        "detalle": (
            "Para el primer payout bi-weekly se requieren al menos 5 días con operaciones abiertas Y cerradas "
            "en el mismo día, usando la misma estrategia de trading de forma consistente. "
            "No se permiten lotes mínimos solo para 'completar' días. "
            "Si normalmente operas 20 lots, usar 0.02 lots no cuenta; reducir a 5 lots con duración similar sí."
        ),
        "consecuencia": "Primer payout rechazado. Días con lotes simbólicos no se contabilizan.",
        "severidad": "CRÍTICO",
        "fuente": "WEB",
        "referencia_contrato": None,
        "referencia_web": "help.alphacapitalgroup.uk — Performance Fee Bi-Weekly",
    },
    {
        "categoria": "📐 Nivel de Riesgo y Consistencia",
        "regla": "Alpha evalúa la consistencia del trading vs. el historial del challenge",
        "detalle": (
            "Alpha revisa el historial completo de tu trading en cada solicitud de payout. "
            "Un cambio drástico de estrategia, tamaño de posición o estilo entre el challenge y la cuenta "
            "fondeada puede derivar en rechazo del payout o revisión por el Risk Team."
        ),
        "consecuencia": "Payout rechazado o movimiento al Risk Management Group.",
        "severidad": "MODERADO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 28.2.6 (sole discretion)",
        "referencia_web": "help.alphacapitalgroup.uk — Risk Management Group PRO",
    },

    # ─────────────────────────────────────────────────────────────
    # CATEGORÍA: TAMAÑO DE POSICIÓN (LOTS)
    # ─────────────────────────────────────────────────────────────
    {
        "categoria": "📊 Tamaño de Posición (Lots)",
        "regla": "Límite de lotes por tamaño de cuenta (PRO Normal)",
        "detalle": (
            "$5k=2.5L | $10k=5L | $25k=10L | $50k=20L | $100k=40L | $200k=80L | $300k=120L. "
            "Es la exposición combinada simultánea, no por trade individual."
        ),
        "consecuencia": "1ra violación: ganancias no elegibles para payout. 2da violación: cuenta desactivada.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Leverage & Lot Exposure (Alpha PRO)",
        "referencia_web": "help.alphacapitalgroup.uk — Lot Size Limit Qualified",
    },
    {
        "categoria": "📊 Tamaño de Posición (Lots)",
        "regla": "Las violaciones de lots se evalúan POR POSICIÓN, no por idea de trade",
        "detalle": (
            "Una secuencia de trades puede generar múltiples violaciones. "
            "Ejemplo: límite = 10 lots. Abres trade de 11 lots (violación #1). "
            "Mientras ese trade está abierto, abres otro de 1 lot (violación #2 porque 11+1=12). "
            "Dos violaciones = cierre de cuenta."
        ),
        "consecuencia": "Dos violaciones simultáneas pueden cerrar la cuenta en un solo movimiento.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Alpha PRO Plan (nota sobre violaciones)",
        "referencia_web": "help.alphacapitalgroup.uk — Lot Size Limit Qualified",
    },
    {
        "categoria": "📊 Tamaño de Posición (Lots)",
        "regla": "Límite de lotes reducido en Risk Management Group",
        "detalle": (
            "Si entras al Risk Group PRO: $5k=1.25L | $10k=2.5L | $25k=5L | $50k=10L | $100k=20L | $200k=40L. "
            "Apalancamiento reducido: FX 1:30, Metales 1:9, Índices 1:10, Oil 1:10."
        ),
        "consecuencia": "Restricción vigente hasta completar 2 payouts exitosos consecutivos.",
        "severidad": "MODERADO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 28.3.4 (a)",
        "referencia_web": "help.alphacapitalgroup.uk — Risk Management Group PRO",
    },

    # ─────────────────────────────────────────────────────────────
    # CATEGORÍA: TRADING EN NOTICIAS
    # ─────────────────────────────────────────────────────────────
    {
        "categoria": "📰 Trading en Noticias",
        "regla": "PRO 8%/10%: ventana prohibida ±2 min — Soft Breach",
        "detalle": (
            "Prohibido ABRIR o CERRAR (incluyendo TP, SL y pending orders) en el instrumento afectado "
            "dentro de 2 min antes y 2 min después del evento (ventana total 4 min). "
            "Si un Take Profit o Stop Gain se activa automáticamente dentro de la ventana = violación. "
            "SÍ puedes holdear un trade que fue abierto MÁS de 2 min antes del evento. "
            "Discursos/conferencias: la ventana cubre TODA su duración + 2 min antes de que empiece + 2 min después de que termine."
        ),
        "consecuencia": "Soft Breach: ganancias de ese trade NO elegibles para payout. La cuenta NO se cierra.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — News Trading Pro 8% y 10%",
        "referencia_web": "help.alphacapitalgroup.uk/en/articles/9293522-can-i-trade-news-pro-one-three-plans",
    },
    {
        "categoria": "📰 Trading en Noticias",
        "regla": "PRO 6% / Alpha One / Alpha Three: ventana prohibida ±5 min — Soft Breach",
        "detalle": (
            "Prohibido ABRIR o CERRAR (incluyendo TP, SL y pending orders) en el instrumento afectado "
            "dentro de 5 min antes y 5 min después del evento (ventana total 10 min). "
            "Si un Take Profit o Stop Gain se activa automáticamente dentro de la ventana = violación. "
            "SÍ puedes holdear un trade que fue abierto MÁS de 5 min antes del evento. "
            "Discursos/conferencias: la ventana cubre TODA su duración + 5 min antes de que empiece + 5 min después de que termine."
        ),
        "consecuencia": "Soft Breach: ganancias de ese trade NO elegibles para payout. La cuenta NO se cierra.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — News Trading Pro 6%, Alpha One, Alpha Three",
        "referencia_web": "help.alphacapitalgroup.uk/en/articles/9293522-can-i-trade-news-pro-one-three-plans",
    },
    {
        "categoria": "📰 Trading en Noticias",
        "regla": "Alpha Swing: trade abierto en ventana de 4 min debe durar más de 2 min",
        "detalle": (
            "En Swing el trading durante noticias está PERMITIDO, pero con condición: "
            "si un trade se INICIA dentro de los 2 min antes o 2 min después de una noticia (ventana 4 min), "
            "su duración debe ser MAYOR a 2 minutos para que sea válido. "
            "Ejemplo: trade abierto a 14:29 y cerrado a 14:30 durante una noticia a las 14:30 = inválido. "
            "Las cuentas Swing también están sujetas a las reglas de gambling."
        ),
        "consecuencia": "Trade inválido: ganancias anuladas si fue abierto en la ventana y cerrado antes de 2 min.",
        "severidad": "MODERADO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — News Trading Alpha Swing",
        "referencia_web": "help.alphacapitalgroup.uk/en/articles/9789907-alpha-swing",
    },
    {
        "categoria": "📰 Trading en Noticias",
        "regla": "Instrumentos afectados — TODOS: 3 eventos USD universales sin excepción",
        "detalle": (
            "Para ABSOLUTAMENTE TODOS los instrumentos (FX, metales, índices, oil) sin excepción, "
            "los siguientes 3 eventos activan la restricción:<br>"
            "• <strong>USD CPI / Inflation Rate</strong><br>"
            "• <strong>Federal Funds Rate + Statements + Press Conference</strong><br>"
            "• <strong>Non-Farm Employment Change (NFP)</strong><br>"
            "Estos 3 son los únicos que aplican para instrumentos no listados en el resto de la tabla."
        ),
        "consecuencia": "Soft Breach si se opera en la ventana prohibida en CUALQUIER instrumento durante estos 3 eventos.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Tabla de instrumentos y noticias",
        "referencia_web": "help.alphacapitalgroup.uk/en/articles/9293522-can-i-trade-news-pro-one-three-plans",
    },
    {
        "categoria": "📰 Trading en Noticias",
        "regla": "Instrumentos afectados — XAUUSD / XAGUSD: cobertura máxima de noticias",
        "detalle": (
            "Para XAUUSD.pro/.raw y XAGUSD.pro/.raw aplica CUALQUIER noticia high-impact de:<br>"
            "• Todos los <strong>USD</strong> high-impact news/speeches<br>"
            "• Todos los <strong>AUD</strong> high-impact news/speeches<br>"
            "• Todos los <strong>CAD</strong> high-impact news/speeches<br>"
            "• Todos los <strong>EUR</strong> high-impact speeches<br>"
            "• Todos los <strong>GBP</strong> high-impact speeches<br>"
            "• TODAS las divisas: Interest Rate Decision + Press Conference<br>"
            "• TODAS las divisas: CPI/Inflation Rate · GDP Growth Rate · PCE · PMI<br>"
            "• TODAS las divisas: Unemployment Change/Rate · Employment Change/Rate<br>"
            "Es el instrumento con la lista de restricciones de noticias más amplia de la plataforma."
        ),
        "consecuencia": "Soft Breach. Prácticamente cualquier noticia high-impact de las principales divisas activa la restricción en oro/plata.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Tabla XAUUSD/XAGUSD",
        "referencia_web": "help.alphacapitalgroup.uk/en/articles/9293522-can-i-trade-news-pro-one-three-plans",
    },
    {
        "categoria": "📰 Trading en Noticias",
        "regla": "Instrumentos afectados — USD Forex / Commodities / US Indices (US30, US100, US500)",
        "detalle": (
            "Además de los 3 universales, para pares USD e índices americanos aplican:<br>"
            "Employment Change/Rate · Unemployment Change/Rate · Non-Farm Payrolls · PMI · ISM · "
            "CPI/Inflation Rate · PPI · GDP · Balance of Trade · Jobless Claims · "
            "Consumer Confidence/Sentiment · JOLTs Job Openings · Average Hourly Earnings · "
            "10Y Note Auction · 30Y Bond Auction · Existing &amp; New Home Sales · Durable Goods Orders · "
            "Speeches · Empire State Manufacturing Index · Retail Sales · Core PCE"
        ),
        "consecuencia": "Soft Breach si se opera en la ventana durante cualquiera de estos eventos en pares USD o índices americanos.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Tabla USD (Forex, Commodities & US Indices)",
        "referencia_web": "help.alphacapitalgroup.uk/en/articles/9293522-can-i-trade-news-pro-one-three-plans",
    },
    {
        "categoria": "📰 Trading en Noticias",
        "regla": "Instrumentos afectados — EUR, GBP, CAD, AUD, NZD, CHF, JPY y Oil por divisa",
        "detalle": (
            "<strong>EUR</strong> (Forex, EU Indices): PMI · CPI · GDP · Employment/Unemployment · Retail Sales · "
            "Balance of Trade · ECB Rates + conf. · Deposit Facility Rate · Sentiment · Business Climate · Consumer Confidence · Speeches · ALL GBP HIGH-IMPACT<br>"
            "<strong>GBP</strong> (Forex): PMI · CPI · GDP · House Prices · Mortgage Approvals · Retail Sales · "
            "BoE Rates + conf. · Trade Balances · Claimant Count Change · Speeches · ALL EUR HIGH-IMPACT<br>"
            "<strong>CAD</strong> (Forex, Oil): BoC Rates + conf. · PMI · CPI · GDP · Employment/Unemployment · "
            "Retail Sales · Housing Starts · Balance of Trade · Speeches<br>"
            "<strong>AUD</strong> (Forex): RBA Rate + conf. · Employment/Unemployment · CPI · GDP · Retail Sales · Speeches<br>"
            "<strong>NZD</strong> (Forex): RBNZ Rate + conf. · Employment/Unemployment · CPI · GDP · Speeches<br>"
            "<strong>CHF</strong> (Forex): CPI · GDP · SNB Policy Rate + conf. · Speeches<br>"
            "<strong>JPY</strong> (Forex, Asian Indices): BoJ Rates + conf. · PMI · CPI · GDP · Industrial Production · Merchandise Trade Balance · Speeches<br>"
            "<strong>OIL</strong> (USOIL/UKOIL): All CAD High Impact News + Crude Oil Inventories"
        ),
        "consecuencia": "Soft Breach si se opera en la ventana durante los eventos listados para cada divisa/instrumento.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Tabla EUR/GBP/CAD/AUD/NZD/CHF/JPY/Oil",
        "referencia_web": "help.alphacapitalgroup.uk/en/articles/9293522-can-i-trade-news-pro-one-three-plans",
    },
    {
        "categoria": "📰 Trading en Noticias",
        "regla": "Calendario de referencia: Myfxbook + Forex Factory — basta 'rojo' en uno de los dos",
        "detalle": (
            "Para determinar si aplica la restricción, consulta Myfxbook Forex Economic Calendar "
            "y Forex Factory Calendar. Lo que importa: que el evento esté listado en la tabla Y que "
            "al menos UNO de los dos calendarios lo clasifique como high-impact (rojo). "
            "Si un calendario lo marca 'naranja' (medium) y el otro 'rojo' (high), aplica la restricción. "
            "Discursos y conferencias: la ventana cubre toda su duración (no solo el momento de inicio)."
        ),
        "consecuencia": "Ignorar este criterio puede resultar en soft breach aunque el evento parezca menor en un calendario.",
        "severidad": "MODERADO",
        "fuente": "WEB",
        "referencia_contrato": None,
        "referencia_web": "help.alphacapitalgroup.uk — What Happens if a Rule is Broken (nota de calendarios)",
    },

    # ─────────────────────────────────────────────────────────────
    # CATEGORÍA: FIN DE SEMANA Y HORARIOS
    # ─────────────────────────────────────────────────────────────
    {
        "categoria": "📅 Fin de Semana y Horarios",
        "regla": "PRO Qualified: NO se puede holdear trades el fin de semana",
        "detalle": (
            "En la cuenta fondeada (Qualified Analyst) PRO, está PROHIBIDO mantener posiciones abiertas "
            "durante el fin de semana. Debes cerrar TODOS los trades antes del cierre del mercado del viernes. "
            "Nota: durante las fases de evaluación (Phase 1 y 2) SÍ podías holdear. Eso cambia al fondear."
        ),
        "consecuencia": "Violación de las Additional Virtual Trading Rules. Puede resultar en breach de cuenta.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Weekend Hold (Alpha PRO Qualified)",
        "referencia_web": "help.alphacapitalgroup.uk — Alpha Pro Plan",
    },
    {
        "categoria": "📅 Fin de Semana y Horarios",
        "regla": "Horario diario reset: 00:00 broker time (GMT+2, GMT+3 en DST USA)",
        "detalle": (
            "El 'día de trading' se resetea a las 00:00 broker time. "
            "Durante el horario de verano de EE.UU. (Daylight Saving Time), el broker opera en GMT+3. "
            "El cálculo de la pérdida diaria máxima usa el balance/equity al inicio de esa vela diaria."
        ),
        "consecuencia": "Calcular mal el horario puede hacerte pensar que estás en un día nuevo cuando no lo estás.",
        "severidad": "OPERATIVO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 1 — Notas sobre Max Daily Drawdown",
        "referencia_web": "help.alphacapitalgroup.uk — Daily Risk Limits",
    },
    {
        "categoria": "📅 Fin de Semana y Horarios",
        "regla": "Inactividad de 30 días = cierre permanente irreversible",
        "detalle": (
            "Si no realizas ninguna operación durante 30 días consecutivos, la cuenta se desactiva "
            "de forma permanente. No hay proceso de recuperación ni reactivación. "
            "Si planeas una ausencia mayor a 30 días, debes contactar a support@alphacapitalgroup.uk ANTES."
        ),
        "consecuencia": "Pérdida permanente de la cuenta fondeada. Sin posibilidad de apelación ni recuperación.",
        "severidad": "CRÍTICO",
        "fuente": "WEB",
        "referencia_contrato": None,
        "referencia_web": "help.alphacapitalgroup.uk — Qualified Trader FAQ",
    },

    # ─────────────────────────────────────────────────────────────
    # CATEGORÍA: PERFORMANCE FEES Y PAGOS
    # ─────────────────────────────────────────────────────────────
    {
        "categoria": "💰 Performance Fees y Pagos",
        "regla": "Performance Fee: 80% trader / 20% Alpha Capital",
        "detalle": (
            "Recibes el 80% de las ganancias virtuales generadas. "
            "Este pago NO proviene de tu trading virtual directamente, sino de los fondos propios de Alpha "
            "como resultado de trades reales que ELLOS ejecutan usando tu análisis como señal."
        ),
        "consecuencia": "N/A — es el beneficio base contractual.",
        "severidad": "INFORMATIVO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 2 — Cláusula 28.2.1",
        "referencia_web": "help.alphacapitalgroup.uk — How Do I Get Paid",
    },
    {
        "categoria": "💰 Performance Fees y Pagos",
        "regla": "Mínimo payout Bi-Weekly: $100 ganancia bruta",
        "detalle": (
            "Para el método bi-weekly, necesitas un mínimo de $100 de ganancia bruta en la cuenta. "
            "El pago neto sería $80 (80% de $100). Se calcula sobre ganancia BRUTA antes de aplicar el split."
        ),
        "consecuencia": "Solicitud de payout rechazada si no se alcanza el mínimo.",
        "severidad": "OPERATIVO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 28.3.1",
        "referencia_web": "help.alphacapitalgroup.uk — Performance Fee Bi-Weekly",
    },
    {
        "categoria": "💰 Performance Fees y Pagos",
        "regla": "Mínimo payout On-Demand: 2% de ganancia bruta sobre balance inicial",
        "detalle": (
            "Para On-Demand necesitas al menos 2% del balance de la cuenta como ganancia bruta. "
            "Ejemplo en $100k: mínimo $2,000 de ganancia bruta. Además la regla del 40% Best Day debe cumplirse."
        ),
        "consecuencia": "Solicitud bloqueada hasta cumplir ambas condiciones: 2% Y regla 40%.",
        "severidad": "OPERATIVO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 28.3.1",
        "referencia_web": "help.alphacapitalgroup.uk — Performance Fee On-Demand",
    },
    {
        "categoria": "💰 Performance Fees y Pagos",
        "regla": "Todos los trades deben estar CERRADOS al solicitar el payout",
        "detalle": (
            "Absolutamente todas las posiciones virtuales deben cerrarse antes de hacer la solicitud. "
            "El trading queda PAUSADO desde que se envía la solicitud hasta que el monto sea retirado del balance. "
            "Solo puedes reanudar después de que el balance sea reseteado."
        ),
        "consecuencia": "Solicitud rechazada si hay trades abiertos. Cuenta congelada durante la revisión.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 28.2.5",
        "referencia_web": "help.alphacapitalgroup.uk — Performance Fee Bi-Weekly y On-Demand",
    },
    {
        "categoria": "💰 Performance Fees y Pagos",
        "regla": "Tiempo de procesamiento: 3 días hábiles (hasta 14 con verificación adicional)",
        "detalle": (
            "Los pagos se procesan dentro de 3 Business Days (días hábiles de Londres, UK). "
            "Si Alpha requiere verificación adicional, puede extenderse hasta 14 Business Days. "
            "Business Days = lunes a viernes excluyendo feriados públicos en Inglaterra."
        ),
        "consecuencia": "Planifica con margen: feriados UK pueden alargar el plazo aunque en Ecuador sea día normal.",
        "severidad": "OPERATIVO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 28.2.7",
        "referencia_web": None,
    },
    {
        "categoria": "💰 Performance Fees y Pagos",
        "regla": "Alpha puede retener el pago a su SOLA discreción si detecta violaciones",
        "detalle": (
            "La cláusula establece que el Performance Fee no se pagará cuando Alpha determine, "
            "A SU SOLA DISCRECIÓN ('sole discretion'), que algún trade fue ejecutado en violación de las reglas. "
            "No hay proceso de apelación explícito en el contrato."
        ),
        "consecuencia": "Pérdida total del payout correspondiente al período en cuestión.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 28.2.6",
        "referencia_web": None,
    },
    {
        "categoria": "💰 Performance Fees y Pagos",
        "regla": "Bono 4to payout: 0.25% del balance inicial (NO es automático)",
        "detalle": (
            "Al 4to retiro exitoso consecutivo, Alpha otorga un bono de 0.25% del balance inicial. "
            "NO es automático. Debes solicitarlo EXPLÍCITAMENTE en el campo 'Reason/Notes' de la solicitud. "
            "Si no lo mencionas, no lo recibes."
        ),
        "consecuencia": "Pérdida del bono si no se solicita manualmente en el campo correcto.",
        "severidad": "OPERATIVO",
        "fuente": "WEB",
        "referencia_contrato": None,
        "referencia_web": "help.alphacapitalgroup.uk — Performance Fee Bi-Weekly (bonus section)",
    },
    {
        "categoria": "💰 Performance Fees y Pagos",
        "regla": "Métodos de cobro disponibles",
        "detalle": (
            "Rise (Riseworks), Checkout.com, CoinPayments, Nuvei, wire transfer. "
            "Criptomonedas solo a través de Riseworks. "
            "Si recibes en tu moneda doméstica (no USD), se aplica tarifa de cambio del proveedor, no de Alpha."
        ),
        "consecuencia": "N/A — información operativa de proceso.",
        "severidad": "INFORMATIVO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusulas 11 y 28.2.4",
        "referencia_web": "help.alphacapitalgroup.uk — How Do I Get Paid",
    },

    # ─────────────────────────────────────────────────────────────
    # CATEGORÍA: ASIGNACIÓN Y MÚLTIPLES CUENTAS
    # ─────────────────────────────────────────────────────────────
    {
        "categoria": "🏦 Asignación y Múltiples Cuentas",
        "regla": "Máximo $400,000 por hogar (todos los planes combinados)",
        "detalle": (
            "El límite de $400,000 aplica por household (hogar/unidad familiar) y se comparte entre "
            "todos los planes: PRO + Swing + One + Three. "
            "Cuentas dentro del mismo hogar deben operar activos diferentes para cumplir la regla."
        ),
        "consecuencia": "Cuentas que excedan el límite serán reembolsadas. Posible revisión y cierre.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 9.1.3",
        "referencia_web": "help.alphacapitalgroup.uk — How Many Accounts Can I Have",
    },
    {
        "categoria": "🏦 Asignación y Múltiples Cuentas",
        "regla": "Máximo $300,000 por estrategia (definida por activo específico)",
        "detalle": (
            "No puedes operar el mismo activo en dos cuentas fondeadas si la suma supera $300k. "
            "Si tienes XAUUSD en cuenta #1 activa, NUNCA puedes operar XAUUSD en cuenta #2, "
            "aunque sea en un día o semana diferente. "
            "Activos correlacionados con mismo timing de entrada/salida también se consideran misma estrategia."
        ),
        "consecuencia": "Violación del máximo por estrategia. Cuentas excedentes son reembolsadas.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 9.1.3 y Schedule 3",
        "referencia_web": "help.alphacapitalgroup.uk — Maximum Allocation Per Strategy",
    },

    # ─────────────────────────────────────────────────────────────
    # CATEGORÍA: ESTRATEGIAS PROHIBIDAS Y RISK GROUP
    # ─────────────────────────────────────────────────────────────
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Arbitrage, latency y front-running: explotación de precios irreales",
        "detalle": (
            "Está prohibido operar sobre cualquier precio u oportunidad de trading irreal. El contrato lista explícitamente:<br>"
            "• <strong>Arbitrage:</strong> explotar diferencias de precio entre plataformas, brokers o feeds<br>"
            "• <strong>Latency trading:</strong> aprovecharse del delay temporal entre el feed real y el feed de la plataforma<br>"
            "• <strong>Front-running:</strong> anticiparse artificialmente al movimiento del price feed<br>"
            "• <strong>Exploiting mispricing:</strong> operar sobre precios erróneos o anómalos del sistema<br>"
            "Alpha revisa el historial completo de entradas/salidas en cada solicitud de payout. "
            "Patrones de entradas a precios imposibles en condiciones normales de mercado activan la revisión."
        ),
        "consecuencia": "Terminación inmediata del contrato + ban potencial de todos los servicios de Alpha. Ganancias del período anuladas. Evaluaciones aprobadas sujetas a revisión retroactiva.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Prohibited Trading Strategies",
        "referencia_web": "help.alphacapitalgroup.uk — Prohibited Strategies",
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "High Frequency Trading (HFT): prohibido en todas sus formas",
        "detalle": (
            "El HFT está prohibido sin excepción. Alpha lo evalúa comparando la frecuencia de trades "
            "contra el historial COMPLETO de la cuenta — no solo la sesión actual. "
            "Un día de muchos trades no es HFT; un patrón sistemático de trades ultra-cortos a lo largo del tiempo sí lo es. "
            "El scalping extremo recurrente (alta frecuencia + duraciones muy cortas como patrón consistente) "
            "cae en zona HFT y puede derivar en Risk Management Group. "
            "Si tienes dudas sobre si tu estrategia califica como HFT, Alpha ofrece revisión previa "
            "mediante cuenta de prueba gratuita antes de comprar una evaluación."
        ),
        "consecuencia": "HFT confirmado: terminación + posible ban permanente. Scalping extremo recurrente: Risk Management Group (leverage y lotes reducidos).",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Prohibited Trading Strategies + Cláusula 28.3.4(b)",
        "referencia_web": "help.alphacapitalgroup.uk — Prohibited Strategies",
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Reverse trading y group hedging coordinado entre usuarios de Alpha",
        "detalle": (
            "Prohibido el reverse trading y el group hedging entre múltiples usuarios. "
            "Esto incluye cualquier coordinación donde distintos traders de Alpha toman posiciones opuestas "
            "en los mismos instrumentos al mismo tiempo para cubrir riesgo colectivo o manipular resultados. "
            "Alpha analiza correlaciones entre cuentas para detectar este patrón. "
            "No confundir con hedging personal dentro de una misma cuenta, que puede estar permitido dependiendo del plan."
        ),
        "consecuencia": "Terminación inmediata + posible ban de servicios. Ganancias anuladas en todos los períodos afectados.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Schedule 3 — Reverse Trading/Group Hedging",
        "referencia_web": None,
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Order Book Spamming: múltiples órdenes pequeñas en lugar de una sola",
        "detalle": (
            "Prohibido colocar múltiples órdenes pequeñas en lugar de una sola orden equivalente. "
            "El contrato define esto como crear una impresión engañosa de actividad del mercado.<br>"
            "<strong>Ejemplo prohibido (literal del contrato):</strong> ingresar 10 órdenes de 0.1 lots "
            "en un período corto en vez de 1 orden de 1 lot.<br>"
            "<strong>Por qué está prohibido:</strong><br>"
            "• Ventaja injusta: en el entorno simulado las consecuencias son menores que en live<br>"
            "• Sobrecarga del sistema: puede causar delays y afectar a todos los usuarios de la plataforma<br>"
            "Alpha detecta este patrón en el historial de órdenes colocadas, incluyendo las canceladas, "
            "no solo en las ejecutadas."
        ),
        "consecuencia": "Terminación inmediata del contrato. Todas las evaluaciones aprobadas quedan sujetas a revisión retroactiva. Ganancias anuladas.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Spamming Order Book",
        "referencia_web": "help.alphacapitalgroup.uk — Prohibited Strategies",
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Group trading y signal following: coordinación con otros usuarios de Alpha",
        "detalle": (
            "Prohibida cualquier forma de trading coordinado con otros usuarios de Alpha Capital:<br>"
            "• Seguir señales de terceros de forma sincronizada con otros Analysts/Qualified Analysts de Alpha<br>"
            "• Participar en grupos (Telegram, Discord, etc.) donde múltiples usuarios de Alpha toman las mismas entradas/salidas al mismo tiempo<br>"
            "• Servicios de account management: cualquier persona que opere la cuenta distinta al titular del contrato<br>"
            "• Copiar trades de otros Analysts de Alpha (aunque sean señales públicas)<br>"
            "El contrato exige que TODAS las cuentas sean operadas exclusivamente por el trader "
            "cuyo nombre y firma aparecen en el contrato firmado."
        ),
        "consecuencia": "Revisión + terminación instantánea si se confirma. Ganancias anuladas. No avanza a Qualified Analyst en evaluaciones.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Group Trading/Signal Following",
        "referencia_web": "help.alphacapitalgroup.uk — Prohibited Strategies",
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Gambling All-or-Nothing: riesgo desproporcionado por trade — el contrato mide el MAX LOSS, no el profit",
        "detalle": (
            "Alpha prohíbe estrategias donde el riesgo máximo por trade es desproporcionado respecto al objetivo. "
            "<strong>Criterio clave:</strong> Alpha evalúa el MÁXIMO DRAWDOWN del trade (peor punto del precio), "
            "no el resultado final. Un trade que bajó 4% pero cerró en ganancia sigue siendo catalogado como all-or-nothing.<br>"
            "<strong>PROHIBIDO (literal del contrato):</strong> arriesgar 4% para ganar 8%<br>"
            "<strong>PERMITIDO (literal del contrato):</strong> arriesgar 2% para ganar 8%<br>"
            "El umbral orientativo es: max risk ≥ 2% del balance en un trade o secuencia de trades "
            "cerrados en el mismo momento (criterio (a) del Risk Management Group)."
        ),
        "consecuencia": "Eliminación de ganancias del período + posible terminación del contrato y cierre de cuenta. Si es patrón recurrente: Risk Management Group.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 28.3.4(c) y Schedule 3 — Gambling Policy",
        "referencia_web": "help.alphacapitalgroup.uk — Policy Against Gambling",
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Gambling por desviación de estilo: cambio de lot size o duración vs. historial de la cuenta",
        "detalle": (
            "Alpha compara cada trade contra el historial COMPLETO de la cuenta para detectar desviaciones. "
            "Tres señales de alerta concretas que menciona el contrato:<br>"
            "• <strong>Cambio de lot size:</strong> operar un tamaño significativamente mayor o menor al promedio histórico "
            "sin justificación estratégica se considera gambling<br>"
            "• <strong>Cambio de duración:</strong> si tu promedio histórico es 2-6h por trade pero un trade dura "
            "pocos minutos (especialmente alrededor de noticias), se interpreta como especulación pura<br>"
            "• <strong>News-hunting:</strong> abrir trades justo antes del evento y cerrarlos justo después de "
            "que pase la ventana restringida (sin intención real de holdear) se considera gambling, "
            "tanto en cuentas Pro/One/Three como en Swing<br>"
            "Este análisis aplica durante el assessment Y en la cuenta fondeada al momento del payout."
        ),
        "consecuencia": "En assessment: no avanza a Qualified Analyst. En cuenta fondeada: eliminación de ganancias + posible terminación.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Gambling Policy",
        "referencia_web": "help.alphacapitalgroup.uk — Policy Against Gambling",
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Copy trading solo desde TU PROPIA cuenta externa — no de terceros",
        "detalle": (
            "El único copy trading permitido es desde tu propia cuenta externa hacia tu Alpha Account. "
            "El contrato (Cláusula 9.1.5) es explícito: cualquier Analyst encontrado copiando trades "
            "de otros traders será revisado y, si se confirma, resultará en terminación instantánea. "
            "Quedan prohibidos:<br>"
            "• Copiar señales de servicios de señales externos coordinados con otros usuarios de Alpha<br>"
            "• Usar EAs o bots que repliquen estrategias de terceros<br>"
            "• Delegar la cuenta a un gestor o account manager externo"
        ),
        "consecuencia": "Revisión inmediata + terminación instantánea si se confirma. Sin proceso de apelación explícito en el contrato.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 9.1.5 y Schedule 3",
        "referencia_web": None,
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Account rolling: pasar y fallar muchas cuentas en poco tiempo",
        "detalle": (
            "Alpha lleva un historial de TODAS tus cuentas anteriores (aprobadas y falladas). "
            "El account rolling se define como: operar a riesgo máximo en cada cuenta para pasar o fallar rápido, "
            "combinado con un volumen alto de cuentas abiertas y cerradas en poco tiempo. "
            "Consecuencias posibles:<br>"
            "• Movimiento al Risk Management Group (leverage y lotes reducidos)<br>"
            "• <strong>Pausa de 30 días</strong> del servicio completo para prevenir el abuso sistemático<br>"
            "El historial de cuentas previas se toma en cuenta en cada revisión, incluyendo evaluaciones falladas."
        ),
        "consecuencia": "Risk Management Group + posible pausa de 30 días del servicio. El historial negativo se acumula y afecta futuras cuentas.",
        "severidad": "MODERADO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 28.3.4(f)",
        "referencia_web": "help.alphacapitalgroup.uk — Risk Management Group PRO",
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Criterios completos del Risk Management Group — 6 causas contractuales",
        "detalle": (
            "El contrato lista 6 categorías que activan el Risk Management Group (Cláusula 28.3.4):<br>"
            "• <strong>(a)</strong> Riesgo ≥2% en un trade individual o secuencia de trades cerrados al mismo tiempo<br>"
            "• <strong>(b)</strong> Scalping extremo: alta frecuencia de trades cortos vs. historial completo<br>"
            "• <strong>(c)</strong> Estilo all-or-nothing: max risk ≥ 4% para ganar 8% (alpha evalúa el max loss del trade)<br>"
            "• <strong>(d)</strong> Uso excesivo de margen o max lots de forma reiterada<br>"
            "• <strong>(e)</strong> Gambling en noticias — tanto durante assessment como soft breach en cuenta fondeada<br>"
            "• <strong>(f)</strong> Account rolling — historial de cuentas previas se considera<br>"
            "Tras entrar al Risk Group se requieren <strong>2 payouts exitosos consecutivos</strong> para solicitar revisión "
            "de regreso al leverage normal. La revisión es DISCRECIONAL del Risk Team (no automática)."
        ),
        "consecuencia": "Leverage reducido (Pro/One/Three: FX 1:30, Metales 1:9, Índices 1:10, Oil 1:10 | Swing: FX 1:15, Metales 1:4, Índices 1:5, Oil 1:5). Lotes a la mitad.",
        "severidad": "MODERADO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 28.3.4",
        "referencia_web": "help.alphacapitalgroup.uk — Risk Management Group PRO",
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Contacto directo con el broker de Alpha: PROHIBIDO bajo cualquier circunstancia",
        "detalle": (
            "Los Qualified Analysts reciben credenciales y derechos de ejecución virtual, pero operan "
            "<strong>en nombre del Account Owner (Alpha)</strong>. La Cláusula 9.1.2 prohíbe explícitamente:<br>"
            "• Cualquier contacto directo con el broker o intermediario de Alpha<br>"
            "• Instrucciones directas al broker sin autorización previa de Alpha<br>"
            "• Comunicación con cualquier contraparte de la cadena de ejecución<br>"
            "Fundamento legal: todas las cuentas y todos los fondos virtuales dentro de ellas son "
            "propiedad exclusiva de Alpha (Cláusula 9.1.1). El trader solo tiene derechos de ejecución virtual."
        ),
        "consecuencia": "Terminación INSTANTÁNEA del servicio y cierre de la cuenta. Sin advertencia previa. Sin proceso de apelación.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 9.1.1 y 9.1.2",
        "referencia_web": None,
    },

    # ─────────────────────────────────────────────────────────────
    # CATEGORÍA: SCALING
    # ─────────────────────────────────────────────────────────────
    {
        "categoria": "📈 Scaling Plan",
        "regla": "Requisito de 10% de ganancia para escalar",
        "detalle": (
            "Para solicitar scaling: debes tener el 10% de ganancia sobre el balance al momento de la solicitud "
            "presente en la cuenta (los retiros previos NO cuentan). "
            "El scaling se hace en incrementos del 10% del balance inicial. Capital máximo: $2,000,000. "
            "Planes elegibles: Alpha Pro, Alpha Swing, Alpha Three."
        ),
        "consecuencia": "Solicitud rechazada si no se cumple el requisito de ganancia presente en cuenta.",
        "severidad": "OPERATIVO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 1 — Max Sim Capital Growth (notas)",
        "referencia_web": "help.alphacapitalgroup.uk — Scaling Plan",
    },
    {
        "categoria": "📈 Scaling Plan",
        "regla": "Proceso de scaling: solicitud dual (dashboard + email a payments@alphacapitalgroup.uk)",
        "detalle": (
            "Para escalar debes: (1) indicarlo en el campo 'Reason/Notes' de la solicitud de payout, "
            "Y (2) enviar email a payments@alphacapitalgroup.uk solicitando el scale-up. "
            "El proceso tarda 24-48 horas hábiles. "
            "Tras el scaling, se requieren mínimo 5 días de trading antes del próximo payout."
        ),
        "consecuencia": "Sin el email, el scaling no se procesa aunque lo indiques en el dashboard.",
        "severidad": "OPERATIVO",
        "fuente": "WEB",
        "referencia_contrato": None,
        "referencia_web": "help.alphacapitalgroup.uk — Requesting a Scale-up",
    },

    # ─────────────────────────────────────────────────────────────
    # CATEGORÍA: CLÁUSULAS LEGALES CRÍTICAS
    # ─────────────────────────────────────────────────────────────
    {
        "categoria": "⚖️ Cláusulas Legales Críticas",
        "regla": "El sitio web SIEMPRE tiene prioridad sobre el contrato escrito",
        "detalle": (
            "En caso de discrepancia entre los Schedules del contrato y el sitio web de Alpha, "
            "el sitio web toma PRECEDENCIA. Las reglas publicadas en alphacapitalgroup.uk son las vigentes, "
            "no el PDF firmado. Alpha puede modificar reglas operativas actualizando solo la web."
        ),
        "consecuencia": "Lo que firmaste puede quedar desactualizado. Siempre revisa el sitio web antes de operar.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 1.4",
        "referencia_web": None,
    },
    {
        "categoria": "⚖️ Cláusulas Legales Críticas",
        "regla": "Alpha puede terminar el contrato si SOSPECHA incumplimiento (sin prueba)",
        "detalle": (
            "La Cláusula 7.1 permite a Alpha terminar o suspender acceso si un usuario 'falla, "
            "o Alpha SOSPECHA que ha fallado' en cumplir cualquier término. "
            "No requiere prueba demostrada. La sospecha es suficiente para actuar. "
            "Seguirás siendo responsable de montos adeudados hasta la fecha de terminación."
        ),
        "consecuencia": "Cierre de cuenta sin recurso de apelación explícito en el contrato.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 7.1",
        "referencia_web": None,
    },
    {
        "categoria": "⚖️ Cláusulas Legales Críticas",
        "regla": "Non-Disparagement PERMANENTE: no puedes criticar a Alpha públicamente",
        "detalle": (
            "Está prohibido denigrar a Alpha en cualquier plataforma (redes sociales, foros, reseñas, "
            "TrustPilot, Forex Peace Army, comentarios a terceros) de forma negativa o despectiva. "
            "Esta cláusula aplica DURANTE y DESPUÉS de que termine el contrato (indefinida). "
            "Alpha es el ÚNICO árbitro de qué constituye una violación."
        ),
        "consecuencia": "Terminación del acceso + posible acción legal bajo Defamation Act 2013 (UK) con costas a tu cargo.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 27.1",
        "referencia_web": None,
    },
    {
        "categoria": "⚖️ Cláusulas Legales Críticas",
        "regla": "TÚ pagas los costos legales de Alpha en cualquier disputa",
        "detalle": (
            "Si Alpha incurre en costos legales para hacer cumplir sus derechos contra ti, "
            "o para defenderse de tus reclamaciones, TÚ pagas TODOS los costos: honorarios de abogados, "
            "costas del tribunal, disbursements — independientemente del resultado del proceso legal. "
            "Esta obligación sobrevive a la terminación del contrato."
        ),
        "consecuencia": "Exposición financiera ilimitada a costos legales en caso de disputa, independientemente del resultado.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 27.2",
        "referencia_web": None,
    },
    {
        "categoria": "⚖️ Cláusulas Legales Críticas",
        "regla": "Alpha NO está regulado por la FCA — sin cobertura del Financial Ombudsman",
        "detalle": (
            "Alpha declara explícitamente que no realiza negocio de inversión regulado ni emite "
            "promociones financieras, por lo tanto no está obligado a estar autorizado por la FCA. "
            "Los usuarios NO tienen cobertura del Financial Ombudsman Service. "
            "En caso de disputa sobre pagos, solo tienes recursos legales civiles ordinarios."
        ),
        "consecuencia": "Sin protección regulatoria. El único recurso ante disputas son los tribunales civiles.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 28.4.1",
        "referencia_web": None,
    },
    {
        "categoria": "⚖️ Cláusulas Legales Críticas",
        "regla": "Confidencialidad de 5 años post-terminación",
        "detalle": (
            "No puedes revelar información confidencial sobre Alpha (negocio, clientes, estrategias, "
            "metodologías internas) durante la vigencia del contrato ni por 5 años después de su terminación. "
            "Aplica también a personal de Alpha sobre tu información personal."
        ),
        "consecuencia": "Exposición a acciones legales por divulgación de información confidencial.",
        "severidad": "MODERADO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 14",
        "referencia_web": None,
    },
    {
        "categoria": "⚖️ Cláusulas Legales Críticas",
        "regla": "Tu trading es VIRTUAL — Alpha usa tu análisis para su propio trading real",
        "detalle": (
            "El Performance Fee que recibes NO es ganancia de tu trading virtual directo. "
            "Es un pago que Alpha hace desde SUS PROPIOS FONDOS, resultado de trades reales que "
            "ELLOS ejecutan usando tu análisis virtual como señal de entrada. "
            "Nunca tienes acceso a mercados reales ni controlas fondos reales. "
            "Por esto Alpha no necesita regulación FCA."
        ),
        "consecuencia": "Implicación legal: sin regulación. Sin cobertura de protección al inversor.",
        "severidad": "INFORMATIVO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusulas 8.1, 28.2.1 y 28.4.1",
        "referencia_web": None,
    },
    {
        "categoria": "⚖️ Cláusulas Legales Críticas",
        "regla": "Ley aplicable: Derecho Inglés — Alpha puede demandarte en tu país de residencia",
        "detalle": (
            "El contrato se rige por la ley inglesa. Disputas en tribunales ingleses (o del país donde resides). "
            "Alpha puede iniciar acciones legales en los tribunales del país donde TÚ resides. "
            "Para ti: Ecuador. Esto significa que podrías enfrentar litigios bajo ley inglesa aplicada en Ecuador."
        ),
        "consecuencia": "Complejidad legal y costos elevados en caso de disputa transnacional.",
        "severidad": "INFORMATIVO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 28",
        "referencia_web": None,
    },
]
