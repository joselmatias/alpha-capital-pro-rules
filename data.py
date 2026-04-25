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
        "regla": "PRO 8%/10%: ventana restringida de ±2 min (4 min total)",
        "detalle": (
            "Prohibido abrir O cerrar trades en instrumentos afectados dentro de 2 min antes "
            "y 2 min después de noticias de alto impacto. "
            "Un Take Profit o Stop Loss activado por el sistema dentro de esa ventana también es violación. "
            "Discursos y conferencias: la ventana cubre toda su duración + 2 min antes de empezar y 2 min después de terminar."
        ),
        "consecuencia": "Soft Breach: ganancias de ese trade no elegibles para payout. No cierra la cuenta.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — News Trading Pro 8% y 10%",
        "referencia_web": "help.alphacapitalgroup.uk — Can I Trade News (Pro/One/Three)",
    },
    {
        "categoria": "📰 Trading en Noticias",
        "regla": "PRO 6%: ventana restringida de ±5 min (10 min total)",
        "detalle": (
            "Prohibido abrir O cerrar trades en instrumentos afectados dentro de 5 min antes "
            "y 5 min después de noticias de alto impacto. Ventana más amplia que el PRO 8/10. "
            "Mantener trades abiertos que fueron iniciados ANTES de la ventana: SÍ está permitido."
        ),
        "consecuencia": "Soft Breach: ganancias de ese trade no elegibles para payout.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — News Trading Pro 6%",
        "referencia_web": "help.alphacapitalgroup.uk — Can I Trade News (Pro/One/Three)",
    },
    {
        "categoria": "📰 Trading en Noticias",
        "regla": "Instrumentos afectados: TODOS por USD CPI, Fed Funds Rate + conf., NFP",
        "detalle": (
            "Para TODOS los instrumentos: USD CPI/Inflation Rate, Federal Funds Rate + Statements + Press Conference, "
            "Non-Farm Employment Change. "
            "Para XAUUSD/XAGUSD: aplican también todos los high-impact news de USD, AUD, CAD, EUR, GBP, "
            "Interest Rate Decisions, CPI, GDP, PCE, PMI, Unemployment de TODAS las monedas."
        ),
        "consecuencia": "Soft Breach por operar en ventana prohibida. Ganancias anuladas para ese trade.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Tabla de instrumentos y noticias",
        "referencia_web": "help.alphacapitalgroup.uk — Can I Trade News",
    },
    {
        "categoria": "📰 Trading en Noticias",
        "regla": "Calendario recomendado: Myfxbook y Forex Factory (al menos en uno debe ser 'high impact')",
        "detalle": (
            "Lo que importa es si la noticia está listada en los calendarios de referencia Y es considerada "
            "high-impact en al menos uno de ellos. Aunque un calendario la clasifique como 'naranja' (medium), "
            "si el otro la clasifica como 'rojo' (high), aplica la restricción."
        ),
        "consecuencia": "Ignorar este criterio puede resultar en soft breach aunque el evento parezca menor.",
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
        "regla": "Prohibición absoluta: arbitrage, latency, HFT, reverse trading, order book spamming",
        "detalle": (
            "Prohibido: explotar precios no realistas (arbitraje, latency, front-running), "
            "High Frequency Trading, reverse trading/group hedging, spamming del order book "
            "(múltiples órdenes pequeñas en lugar de una grande), group trading/signal following coordinado."
        ),
        "consecuencia": "Terminación inmediata de la cuenta + posible ban permanente de todos los servicios de Alpha. Ganancias anuladas.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Schedule 3 — Prohibited Trading Strategies",
        "referencia_web": "help.alphacapitalgroup.uk — Prohibited Strategies",
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Gambling / All-or-Nothing: política estricta",
        "detalle": (
            "Prohibido: estrategias all-or-nothing, cambio drástico de lot size vs. promedio de la cuenta, "
            "duración de trades significativamente distinta al promedio histórico, "
            "trades abiertos justo antes de noticias y cerrados justo después de la ventana restringida. "
            "Ejemplo permitido: arriesgar 2% para ganar 8% (no es all-or-nothing). "
            "Ejemplo prohibido: arriesgar 4% para ganar 8%."
        ),
        "consecuencia": "Eliminación de ganancias + posible terminación del contrato y cierre de cuenta.",
        "severidad": "CRÍTICO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 28.3.4 y Schedule 3 — Gambling Policy",
        "referencia_web": "help.alphacapitalgroup.uk — Policy Against Gambling",
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Copy trading solo desde TU PROPIA cuenta externa",
        "detalle": (
            "El único copy trading permitido es desde tu propia cuenta externa hacia tu Alpha Account. "
            "Está prohibido copiar trades de otros traders, seguir señales de terceros de forma coordinada "
            "con otros usuarios de Alpha, o usar servicios de gestión de cuentas por terceros."
        ),
        "consecuencia": "Revisión + terminación instantánea si se confirma la violación.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 9.1.5 y Schedule 3",
        "referencia_web": None,
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Criterios del Risk Management Group",
        "detalle": (
            "Tu cuenta puede ser movida al Risk Group si: (a) arriesgas ≥2% en un trade o secuencia, "
            "(b) scalping extremo en relación al historial completo, (c) estilo all-or-nothing, "
            "(d) uso excesivo de margen, (e) gambling en noticias, (f) account rolling "
            "(pasar y fallar muchas cuentas en poco tiempo — historial de cuentas previas se considera)."
        ),
        "consecuencia": "Reducción de apalancamiento y lotes. Restricción mínima hasta 2 payouts exitosos.",
        "severidad": "MODERADO",
        "fuente": "BOTH",
        "referencia_contrato": "Cláusula 28.3.4",
        "referencia_web": "help.alphacapitalgroup.uk — Risk Management Group PRO",
    },
    {
        "categoria": "🚫 Estrategias Prohibidas",
        "regla": "Contacto directo con el broker de Alpha: PROHIBIDO",
        "detalle": (
            "Los Qualified Analysts pueden recibir credenciales y ejecutar trades virtualmente, "
            "pero tienen PROHIBIDO cualquier contacto directo con el broker o intermediario de Alpha "
            "sin autorización del Account Owner (Alpha). "
            "Todas las cuentas y activos dentro de ellas son propiedad de Alpha."
        ),
        "consecuencia": "Terminación INSTANTÁNEA del servicio y cierre de la cuenta. Sin excepción.",
        "severidad": "CRÍTICO",
        "fuente": "CONTRACT",
        "referencia_contrato": "Cláusula 9.1.2",
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
