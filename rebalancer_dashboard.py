import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import pandas as pd

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Apex Rebalancer | Product Overview",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# APEX BRAND COLORS
# ============================================================

APEX_COLORS = {
    'navy': '#002060',
    'blue': '#0066CC',
    'bright_blue': '#3B82F6',
    'sky_blue': '#00B0F0',
    'light_blue': '#87CEFA',
    'charcoal': '#2D3748',
    'gray': '#6B7280',
    'light_gray': '#F0F0F0',
    'lighter_gray': '#F8F9FA',
    'green': '#28A745',
    'red': '#EF4444',
    'gold': '#FBBF24',
    'purple': '#7030A0',
    'amethyst': '#802CC0',
    'amethyst_pink': '#EC0075'
}

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(f"""
<style>
    /* Main container */
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: #FFFFFF;
    }}

    /* Overall app background */
    .stApp {{
        background-color: #FFFFFF;
    }}

    /* Headers */
    h1 {{
        color: {APEX_COLORS['navy']};
        font-family: 'Calibri', sans-serif;
        border-bottom: 4px solid {APEX_COLORS['blue']};
        padding-bottom: 10px;
        margin-top: 30px;
    }}

    h2 {{
        color: {APEX_COLORS['blue']};
        font-family: 'Calibri', sans-serif;
        padding-left: 10px;
        border-left: 5px solid {APEX_COLORS['sky_blue']};
        margin-top: 25px;
    }}

    h3 {{
        color: {APEX_COLORS['navy']};
        font-family: 'Calibri', sans-serif;
        margin-top: 20px;
    }}

    /* Sidebar styling */
    section[data-testid="stSidebar"] {{
        background-color: #FFFFFF;
        border-right: 2px solid {APEX_COLORS['light_gray']};
    }}

    section[data-testid="stSidebar"] > div {{
        background-color: #FFFFFF;
    }}

    /* Metric cards */
    [data-testid="stMetricValue"] {{
        font-size: 36px;
        color: {APEX_COLORS['blue']};
    }}

    /* Metric labels */
    [data-testid="stMetricLabel"] {{
        color: {APEX_COLORS['charcoal']};
        font-size: 16px;
        font-weight: 600;
    }}

    /* Success/Info/Warning boxes */
    .stAlert {{
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }}

    /* Buttons */
    .stButton>button {{
        background-color: {APEX_COLORS['blue']};
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: 600;
        border: none;
        transition: all 0.3s;
    }}

    .stButton>button:hover {{
        background-color: {APEX_COLORS['navy']};
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }}

    /* Expander styling with 3D hover effects - Force override */
    div[data-testid="stExpander"] details summary {{
        background: linear-gradient(135deg, #E7F3FF 0%, #F3E7FF 100%) !important;
        border-radius: 10px !important;
        padding: 15px !important;
        font-weight: 600 !important;
        color: {APEX_COLORS['navy']} !important;
        border-left: 5px solid {APEX_COLORS['blue']} !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
        margin-bottom: 10px !important;
    }}

    div[data-testid="stExpander"] details summary:hover {{
        background: linear-gradient(135deg, #E7F3FF 0%, #F3E7FF 100%) !important;
        color: {APEX_COLORS['navy']} !important;
        border-left: 5px solid {APEX_COLORS['blue']} !important;
        transform: translateY(-5px) scale(1.01) !important;
        box-shadow: 0 8px 16px rgba(0, 102, 204, 0.2) !important;
    }}

    /* Tables */
    .dataframe {{
        border: 1px solid {APEX_COLORS['light_gray']};
        border-radius: 5px;
    }}

    /* Links */
    a {{
        color: {APEX_COLORS['blue']};
        text-decoration: none;
    }}

    a:hover {{
        color: {APEX_COLORS['navy']};
        text-decoration: underline;
    }}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def create_provider_status_chart():
    """Create model provider pie chart with hover shine effect"""
    providers = ['State Street', 'Aptus', 'Franklin Templeton', 'PIMCO', 'Zacks']
    model_counts = [38, 5, 16, 6, 13]  # Actual model counts per provider

    # Color coding for each provider
    colors = [
        '#7030A0',  # State Street: Purple
        '#0066CC',  # Aptus: Blue
        '#00B0F0',  # Franklin Templeton: Sky Blue
        '#28A745',  # PIMCO: Green
        '#FBBF24'   # Zacks: Gold
    ]

    fig = go.Figure(data=[
        go.Pie(
            labels=providers,
            values=model_counts,
            hole=0.5,
            marker=dict(
                colors=colors,
                line=dict(color='white', width=4)
            ),
            textfont=dict(size=14, color='white', family='Calibri', weight='bold'),
            hovertemplate='<b style="font-size:18px">%{label}</b><br><span style="font-size:16px">%{value} Models</span><br><i style="color:#0066CC">👆 Click to explore</i><extra></extra>',
            hoverlabel=dict(
                bgcolor='rgba(255, 255, 255, 0.95)',
                font_size=15,
                font_family='Calibri',
                font_color='#002060',
                bordercolor='#0066CC',
                align='left'
            ),
            insidetextorientation='radial'
        )
    ])

    fig.update_layout(
        title=dict(
            text="5 Model Providers",
            x=0.5,
            xanchor='center'
        ),
        title_font=dict(size=18, color=APEX_COLORS['navy'], family='Calibri'),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.1,
            xanchor="center",
            x=0.5,
            font=dict(size=12, family='Calibri'),
        ),
        height=500,
        autosize=True,
        margin=dict(l=80, r=80, t=80, b=100)
    )

    return fig

def get_provider_models():
    """Return dictionary of models by provider"""
    return {
        'Aptus Capital Advisors': [
            'Aptus Impact Agg Growth',
            'Aptus Impact Conservative',
            'Aptus Impact Growth',
            'Aptus Impact Moderate',
            'Aptus Impact Preserve'
        ],
        'Franklin Templeton': [
            'Core Multi Manager 10 EQ/90 FI ETF Model',
            'Core Multi Manager 100 Equity ETF Model',
            'Core Multi Manager 20 EQ/80 FI ETF Model',
            'Core Multi Manager 30 EQ/70 FI ETF Model',
            'Core Multi Manager 40 EQ/60 FI ETF Model',
            'Core Multi Manager 50 EQ/50 FI ETF Model',
            'Core Multi Manager 60 EQ/40 FI ETF Model',
            'Core Multi Manager 70 EQ/30 FI ETF Model',
            'Core Multi Manager 80 EQ/20 FI ETF Model',
            'Core Multi Manager 90 EQ/10 FI ETF Model',
            'Core Multi-Manager All Equity + Digital Assets ETF',
            'Core Multi-Manager Balanced + Digital Assets ETF',
            'Core Multi-Manager Conservative Growth + Digital Assets ETF',
            'Core Multi-Manager Growth + Digital Assets ETF',
            'Core Multi-Manager Moderate Growth + Digital Assets ETF',
            'Core Plus ETF Model'
        ],
        'PIMCO': [
            'Tax Aware Fixed Income ETF Portfolio - Capital Preservation Model',
            'Tax Aware Fixed Income ETF Portfolio - Enhanced Core Model',
            'Tax Aware Fixed Income ETF Portfolio - Income Focus ETF Model',
            'Taxable Fixed Income ETF Portfolio - Capital Preservation Model',
            'Taxable Fixed Income ETF Portfolio - Enhanced Core Model',
            'Taxable Fixed Income ETF Portfolio - Income Focus ETF Model'
        ],
        'State Street Investment Management': [
            'Active Asset Allocation ETF Model Portfolio: Conservative',
            'Active Asset Allocation ETF Model Portfolio: Growth',
            'Active Asset Allocation ETF Model Portfolio: Maximum Growth',
            'Active Asset Allocation ETF Model Portfolio: Moderate',
            'Active Asset Allocation ETF Model Portfolio: Moderate Conservative',
            'Active Asset Allocation ETF Model Portfolio: Moderate Growth',
            'Active Multi-Asset Income ETF Portfolio',
            'Enhanced Strategic Asset Allocation ETF Model Portfolio: Conservative',
            'Enhanced Strategic Asset Allocation ETF Model Portfolio: Growth',
            'Enhanced Strategic Asset Allocation ETF Model Portfolio: Maximum Growth',
            'Enhanced Strategic Asset Allocation ETF Model Portfolio: Moderate',
            'Enhanced Strategic Asset Allocation ETF Model Portfolio: Moderate Conservative',
            'Enhanced Strategic Asset Allocation ETF Model Portfolio: Moderate Growth',
            'Fixed income Sector Rotation ETF Portfolio',
            'Multi-Asset Real Return ETF Portfolio',
            'Quarterly Asset Allocation ETF Portfolio: Conservative',
            'Quarterly Asset Allocation ETF Portfolio: Growth',
            'Quarterly Asset Allocation ETF Portfolio: Maximum Growth',
            'Quarterly Asset Allocation ETF Portfolio: Moderate',
            'Quarterly Asset Allocation ETF Portfolio: Moderate Conservative',
            'Quarterly Asset Allocation ETF Portfolio: Moderate Growth',
            'Strategic Asset Allocation ETF Model Portfolio: Conservative',
            'Strategic Asset Allocation ETF Model Portfolio: Growth',
            'Strategic Asset Allocation ETF Model Portfolio: Maximum Growth',
            'Strategic Asset Allocation ETF Model Portfolio: Moderate',
            'Strategic Asset Allocation ETF Model Portfolio: Moderate Conservative',
            'Strategic Asset Allocation ETF Model Portfolio: Moderate Growth',
            'Strategic Multi-Asset Income ETF Portfolio',
            'Tax-Sensitive Strategic Asset Allocation ETF Model Portfolio: Conservative',
            'Tax-Sensitive Strategic Asset Allocation ETF Model Portfolio: Growth',
            'Tax-Sensitive Strategic Asset Allocation ETF Model Portfolio: Moderate',
            'Tax-Sensitive Strategic Asset Allocation ETF Model Portfolio: Moderate Conservative',
            'Tax-Sensitive Strategic Asset Allocation ETF Model Portfolio: Moderate Growth',
            'U.S Equity Sector Rotation ETF Portfolio',
            'US-Focused Quarterly Asset Allocation ETF Portfolio: Conservative',
            'US-Focused Quarterly Asset Allocation ETF Portfolio: Growth',
            'US-Focused Quarterly Asset Allocation ETF Portfolio: Maximum Growth',
            'US-Focused Quarterly Asset Allocation ETF Portfolio: Moderate'
        ],
        'Zacks Investment Management': [
            'Zacks Active ETF Model Aggressive',
            'Zacks Active ETF Model Conservative',
            'Zacks Active ETF Model Moderate',
            'Zacks Active ETF Model Moderate Aggressive',
            'Zacks Active ETF Model Moderate Conservative',
            'Zacks Active ETF Model Ultra Aggressive',
            'Zacks+ Aggressive',
            'Zacks+ All Equity',
            'Zacks+ Balanced',
            'Zacks+ Income',
            'Zacks+ Moderate Aggressive',
            'Zacks+ Moderate Growth',
            'Zacks+ Moderate Value'
        ]
    }

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, {APEX_COLORS['navy']} 0%, {APEX_COLORS['blue']} 100%); border-radius: 10px; margin-bottom: 20px;'>
        <h1 style='color: white; margin: 0; border: none; padding: 0; font-size: 32px;'>⚖️</h1>
        <h2 style='color: white; margin: 5px 0 0 0; border: none; padding: 0; font-size: 20px;'>Apex Rebalancer</h2>
        <p style='color: {APEX_COLORS['sky_blue']}; margin: 5px 0 0 0; font-size: 14px;'>Portfolio Rebalancing Platform</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📋 Navigation")
    section = st.radio(
        "",
        ["🏠 Overview", "✨ Features", "🔄 How It Works", "🔧 Process Flow", "❓ Q&A"],
        label_visibility="collapsed"
    )


# ============================================================
# MAIN CONTENT
# ============================================================

if section == "🏠 Overview":
    st.title("⚖️ Apex Rebalancer: Portfolio Rebalancing Platform")

    # CSS animations
    st.markdown("""
    <style>
        @keyframes gradientFlow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes floatUp {
            0%, 100% { transform: translateY(0px); opacity: 0.3; }
            50% { transform: translateY(-20px); opacity: 0.6; }
        }

        @keyframes floatDown {
            0%, 100% { transform: translateY(0px); opacity: 0.4; }
            50% { transform: translateY(15px); opacity: 0.7; }
        }

        .hero-container {
            position: relative;
            background: linear-gradient(135deg, #0066CC, #7030A0, #EC0075, #0066CC);
            background-size: 400% 400%;
            animation: gradientFlow 8s ease infinite;
            padding: 40px;
            border-radius: 20px;
            margin-bottom: 30px;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0,0,0,0.15);
        }

        .floating-shape {
            position: absolute;
            border-radius: 50%;
            background: rgba(255,255,255,0.1);
        }

        .shape1 {
            width: 100px;
            height: 100px;
            top: 20%;
            left: 10%;
            animation: floatUp 4s ease-in-out infinite;
        }

        .shape2 {
            width: 150px;
            height: 150px;
            top: 60%;
            right: 15%;
            animation: floatDown 5s ease-in-out infinite;
        }

        .shape3 {
            width: 80px;
            height: 80px;
            bottom: 20%;
            left: 70%;
            animation: floatUp 6s ease-in-out infinite 1s;
        }
    </style>
    """, unsafe_allow_html=True)

    # Animated hero section
    st.markdown("""
    <div class='hero-container'>
        <div class='floating-shape shape1'></div>
        <div class='floating-shape shape2'></div>
        <div class='floating-shape shape3'></div>
        <div style='position: relative; z-index: 10;'>
            <h2 style='color: white; margin: 0; border: none; padding: 0; font-size: 32px; text-shadow: 0 2px 10px rgba(0,0,0,0.2);'>
                Automated Portfolio Rebalancing for Wealth Management
            </h2>
            <h3 style='color: rgba(255,255,255,0.95); margin: 20px 0 15px 0; border: none; padding: 0; font-size: 22px;'>
                What is Apex Rebalancer?
            </h3>
            <p style='font-size: 18px; margin-top: 10px; line-height: 1.7; color: rgba(255,255,255,0.95);'>
                Rebalancing is the process of adjusting a portfolio's asset allocations to align with levels advisors specify in an investment plan. Apex's Rebalancer allows advisors to manage portfolios based on asset types, expected returns, and risk levels. The rebalancer creates trade proposals that realign investment portfolios to targets and ranges that match the desired portfolio models as markets move and asset values shift. Within the rebalancer, advisors can submit trade proposals to the market and seamlessly manage their investor's portfolios.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Key Value Propositions
    st.markdown("## 🎯 Key Value Propositions")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div style='background-color: {APEX_COLORS['lighter_gray']}; padding: 20px; border-radius: 10px; height: 200px; border-left: 5px solid {APEX_COLORS['green']};'>
            <h3 style='color: {APEX_COLORS['navy']}; margin-top: 0;'>⚡ Efficiency</h3>
            <p>Automate portfolio rebalancing across hundreds or thousands of accounts simultaneously, saving hours of manual work.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='background-color: {APEX_COLORS['lighter_gray']}; padding: 20px; border-radius: 10px; height: 200px; border-left: 5px solid {APEX_COLORS['blue']};'>
            <h3 style='color: {APEX_COLORS['navy']}; margin-top: 0;'>🎯 Precision</h3>
            <p>Maintain target allocations with configurable drift thresholds and optimize for tax efficiency and trade costs.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style='background-color: {APEX_COLORS['lighter_gray']}; padding: 20px; border-radius: 10px; height: 200px; border-left: 5px solid {APEX_COLORS['purple']};'>
            <h3 style='color: {APEX_COLORS['navy']}; margin-top: 0;'>📈 Scale</h3>
            <p>Manage complex portfolios at scale with support for custom models, tax-loss harvesting, and direct indexing.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Who Is It For?
    st.markdown("## 👥 Who Is Rebalancer For?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        ### ✅ **Ideal For:**
        - **RIAs** managing discretionary portfolios
        - **Family Offices** with complex multi-account structures
        - **Asset Managers** running model-based strategies
        - **Robo-Advisors** requiring automated rebalancing
        - Firms with **>50 accounts** needing systematic rebalancing
        """)

    with col2:
        st.markdown(f"""
        ### ⚠️ **Requirements:**
        - **Ascend platform** (not available on Classic)
        - **Discretionary trading authority** over client accounts
        - **Model-based investment approach** (pre-defined allocations)
        - Willingness to adopt **goal-based portfolio management**
        """)

    st.markdown("---")

    # Bottom Stats Section
    st.markdown("## 📊 Platform Analysis")

    bottom_col1, bottom_col2, bottom_col3, bottom_col4 = st.columns(4)

    # Add custom CSS for 3D hover effects
    st.markdown("""
    <style>
        .stat-card {
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .stat-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.25);
        }
    </style>
    """, unsafe_allow_html=True)

    with bottom_col1:
        st.markdown(f"""
        <div class='stat-card' style='background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['bright_blue']} 100%);'>
            <div style='font-size: 42px; font-weight: bold;'>44</div>
            <div style='font-size: 16px; margin-top: 8px; opacity: 0.95;'>Total Clients</div>
            <div style='font-size: 14px; margin-top: 5px; opacity: 0.85;'>Active on Platform</div>
        </div>
        """, unsafe_allow_html=True)

    with bottom_col2:
        st.markdown(f"""
        <div class='stat-card' style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);'>
            <div style='font-size: 42px; font-weight: bold;'>$2.95B</div>
            <div style='font-size: 16px; margin-top: 8px; opacity: 0.95;'>Total AUM</div>
            <div style='font-size: 14px; margin-top: 5px; opacity: 0.85;'>Assets Under Management</div>
        </div>
        """, unsafe_allow_html=True)

    with bottom_col3:
        st.markdown(f"""
        <div class='stat-card' style='background: linear-gradient(135deg, {APEX_COLORS['green']} 0%, {APEX_COLORS['sky_blue']} 100%);'>
            <div style='font-size: 42px; font-weight: bold;'>$67M</div>
            <div style='font-size: 16px; margin-top: 8px; opacity: 0.95;'>Avg. Client Size</div>
            <div style='font-size: 14px; margin-top: 5px; opacity: 0.85;'>Mean AUM per Client</div>
        </div>
        """, unsafe_allow_html=True)

    with bottom_col4:
        st.markdown(f"""
        <div class='stat-card' style='background: linear-gradient(135deg, {APEX_COLORS['gold']} 0%, {APEX_COLORS['green']} 100%);'>
            <div style='font-size: 42px; font-weight: bold;'>$1.87B</div>
            <div style='font-size: 16px; margin-top: 8px; opacity: 0.95;'>Largest Client</div>
            <div style='font-size: 14px; margin-top: 5px; opacity: 0.85;'>Public.com</div>
        </div>
        """, unsafe_allow_html=True)

elif section == "✨ Features":
    st.title("✨ Rebalancer Features")

    st.markdown("## Core Capabilities")

    # Feature categories
    features = {
        "Portfolio Management": {
            "icon": "📊",
            "items": [
                "**Goal-Based Portfolios**: Assign multiple investment goals to each account with separate allocations",
                "**Model Management**: Create and maintain investment models with target allocations for taxable and tax-advantaged accounts",
                "**Frameworks**: Three types - Glidepath (target-date based), Risk-Based (2 models, 0-100 risk score), Risk-Tier (2-10 tiers)",
                "**Drift Monitoring**: Automatic tracking of portfolio drift from target allocations",
                "**Multi-Account Support**: Rebalance hundreds or thousands of accounts simultaneously",
                "**Asset Class Mapping**: Flexible security-to-asset-class mapping for accurate tracking",
                "**Model Marketplace**: Subscribe to professionally managed models with automatic updates from providers"
            ]
        },
        "Rebalancing & Optimization": {
            "icon": "⚖️",
            "items": [
                "**Smart Rebalancing**: Optimize trade recommendations to minimize costs and tax impact",
                "**Threshold Management**: Configurable drift thresholds for securities, asset classes, and cash (firm-level or account-level)",
                "**Tax-Loss Harvesting**: Automatically identify and execute tax-loss harvesting opportunities",
                "**Wash Sale Restrictions**: Automatic restrictions to prevent wash sale violations",
                "**Cash Management**: Generate cash positions with minimum cash parameter",
                "**Trade Blotter Analysis**: Review and modify proposed trades before execution",
                "**Basket Trading**: Execute bulk orders across multiple securities"
            ]
        },
        "Advanced Features": {
            "icon": "🚀",
            "items": [
                "**Direct Indexing**: Build custom index portfolios with tracking error constraints, security bands, and tax optimization",
                "**Capital Gains Budget**: Set annual dollar limits on short-term and long-term gains with automatic restrictions",
                "**Ticker Restrictions**: Create buy/sell restrictions on specific securities at client or account level",
                "**Liquidate Positions**: Sell all holdings in an account with automatic restriction removal",
                "**Quarantine Accounts**: Prevent trade proposals for specific accounts (automatic or manual)",
                "**API Access**: Programmatic access for automated rebalancing workflows",
                "**Completion Portfolio**: Reduce drift for portfolios holding restricted securities"
            ]
        },
        "Security & Administration": {
            "icon": "🔐",
            "items": [
                "**Multi-Factor Authentication (MFA)**: Secure access via phone or authenticator app",
                "**Organization Settings**: Add users, create API keys (max 5 per firm)",
                "**Firm Settings**: Configure minimum trade size, trading limits, and tax-loss harvesting defaults",
                "**Client Settings**: Customize preferences per client, override firm-wide settings",
                "**Investor Settings**: Account-level customization and preferences"
            ]
        },
        "Reporting & Analytics": {
            "icon": "📈",
            "items": [
                "**Performance Tracking**: Monitor portfolio performance vs. targets",
                "**Drift Reports**: Visualize current portfolio drift by account or asset class",
                "**Historical Trades**: Navigate, filter, and download past trades with advanced search",
                "**Tax Reports**: Tax-loss harvesting summary and realized gains/losses",
                "**Client Statements**: White-label reporting for end clients",
                "**Compliance Controls**: Pre-trade compliance checks and reporting"
            ]
        }
    }

    for category, details in features.items():
        with st.expander(f"{details['icon']} {category}", expanded=False):
            for item in details['items']:
                st.markdown(f"- {item}")

    st.markdown("---")

    # Integration with Model Marketplace
    st.markdown("## 🔗 Model Marketplace Integration")

    st.info("""
    **NEW:** Rebalancer now integrates with **Model Marketplace**, giving you access to institutional investment
    models from providers like State Street, PIMCO, Aptus, Franklin Templeton, and Zacks Investment Management.

    Subscribe to professionally-managed models and Rebalancer will automatically incorporate them into your
    rebalancing workflows with provider updates applied seamlessly.
    """)

    # Show provider ecosystem chart with click interaction
    st.markdown("<h3 style='text-align: center;'>📊 Provider Ecosystem</h3>", unsafe_allow_html=True)

    # Add blinking "CLICK ME" indicator - centered
    st.markdown("""
    <div style='text-align: center; margin: 15px 0;'>
        <span style='background: linear-gradient(135deg, #7030A0 0%, #0066CC 25%, #00B0F0 50%, #28A745 75%, #FBBF24 100%);
                     background-size: 200% 200%;
                     animation: gradientShift 3s ease infinite;
                     color: white;
                     padding: 8px 20px;
                     border-radius: 25px;
                     font-weight: bold;
                     font-size: 14px;
                     box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                     display: inline-block;'>
            👆 CLICK ANY SLICE TO VIEW MODELS
        </span>
    </div>
    <style>
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        /* Center the entire plotly chart */
        div[data-testid="stPlotlyChart"] {
            display: flex;
            justify-content: center;
        }
    </style>
    """, unsafe_allow_html=True)

    from streamlit_plotly_events import plotly_events

    fig = create_provider_status_chart()

    # Update figure to be more clickable
    fig.update_traces(
        hoverinfo='label+percent',
        textposition='inside',
        marker=dict(line=dict(color='white', width=3))
    )

    # Display chart with use_container_width for responsive centering
    selected_points = plotly_events(
        fig,
        click_event=True,
        hover_event=False,
        select_event=False,
        override_height=500,
        key='provider_pie_chart'
    )

    provider_models = get_provider_models()

    # Color mapping
    color_map = {
        'State Street Investment Management': '#7030A0',
        'Aptus Capital Advisors': '#0066CC',
        'Franklin Templeton': '#00B0F0',
        'PIMCO': '#28A745',
        'Zacks Investment Management': '#FBBF24'
    }

    # Show popup if a slice was clicked
    if selected_points and len(selected_points) > 0:
        point_data = selected_points[0]
        point_number = point_data.get('pointNumber', -1)

        # Map pointNumber to provider names
        provider_list = [
            'State Street Investment Management',
            'Aptus Capital Advisors',
            'Franklin Templeton',
            'PIMCO',
            'Zacks Investment Management'
        ]

        if 0 <= point_number < len(provider_list):
            provider = provider_list[point_number]
            models = provider_models[provider]

            # Use Streamlit dialog
            @st.dialog(f"✨ {provider}", width="large")
            def show_provider_models():
                st.markdown(f"**📊 {len(models)} Investment Models**")
                st.markdown("---")

                for i, model in enumerate(models, 1):
                    st.markdown(f"""
                    <div style='padding: 12px; margin: 6px 0;
                                background: linear-gradient(135deg, {color_map[provider]}15 0%, {color_map[provider]}25 100%);
                                border-left: 5px solid {color_map[provider]};
                                border-radius: 8px;'>
                        <span style='color: {color_map[provider]}; font-weight: bold; font-size: 16px;'>{i}.</span>
                        <span style='color: #002060; font-size: 15px;'> {model}</span>
                    </div>
                    """, unsafe_allow_html=True)

            show_provider_models()

    st.markdown("---")

    # MMP Guide PDF Section
    st.markdown("## 📄 Model Marketplace Full Guide")

    import os
    pdf_path = os.path.join(os.path.dirname(__file__), 'MMP1.pdf')

    # Download button
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(
            label="⬇️ Download Complete MMP Guide (PDF)",
            data=pdf_bytes,
            file_name="Model_Marketplace_Guide.pdf",
            mime="application/pdf",
            use_container_width=True
        )

elif section == "🔄 How It Works":
    st.title("🔄 How Rebalancer Works")

    st.markdown("## The Rebalancing Workflow")

    # Step-by-step process with modern card design
    steps = [
        {
            "number": "1",
            "icon": "📊",
            "title": "Define Investment Models",
            "description": "Create investment models with target asset allocations (e.g., 60% Stocks, 40% Bonds). Subscribe to Model Marketplace models or build custom allocations.",
            "color": APEX_COLORS['blue']
        },
        {
            "number": "2",
            "icon": "🎯",
            "title": "Assign Goals to Accounts",
            "description": "Assign investment goals (linked to models) to client accounts. Each account can have multiple goals with different allocations.",
            "color": APEX_COLORS['green']
        },
        {
            "number": "3",
            "icon": "📈",
            "title": "Monitor Portfolio Drift",
            "description": "Rebalancer continuously monitors accounts and flags those exceeding drift thresholds (e.g., >5% drift from target).",
            "color": APEX_COLORS['purple']
        },
        {
            "number": "4",
            "icon": "⚡",
            "title": "Generate Trade Proposals",
            "description": "Click 'Rebalance' to generate optimized trade recommendations that bring portfolios back to target allocations.",
            "color": APEX_COLORS['gold']
        },
        {
            "number": "5",
            "icon": "✏️",
            "title": "Review & Modify",
            "description": "Review proposed trades in the trade blotter. Modify quantities, add/remove trades, or adjust allocations as needed.",
            "color": APEX_COLORS['amethyst']
        },
        {
            "number": "6",
            "icon": "✅",
            "title": "Accept & Submit",
            "description": "Accept proposals and submit trades to Apex clearing. All trades execute through standard Apex trade processing.",
            "color": APEX_COLORS['navy']
        },
        {
            "number": "7",
            "icon": "📋",
            "title": "Track & Report",
            "description": "Monitor trade execution, track portfolio performance, and generate client reports showing portfolio status.",
            "color": APEX_COLORS['sky_blue']
        }
    ]

    # Display steps in interactive gradient cards with 3D hover effects
    for i, step in enumerate(steps):
        # Arrow connector between steps
        if i > 0:
            st.markdown(f"""
            <div style='text-align: center; margin: -5px 0;'>
                <span style='font-size: 30px; color: {step['color']}; font-weight: bold;'>↓</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class='workflow-card' style='background: linear-gradient(135deg, {step['color']}15 0%, {step['color']}30 100%);
                    padding: 25px;
                    border-radius: 15px;
                    border-left: 6px solid {step['color']};
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                    margin: 15px 0;
                    transition: all 0.3s ease;
                    cursor: pointer;'>
            <div style='display: flex; align-items: center; gap: 20px;'>
                <div style='background: {step['color']};
                            color: white;
                            width: 70px;
                            height: 70px;
                            border-radius: 15px;
                            display: flex;
                            flex-direction: column;
                            align-items: center;
                            justify-content: center;
                            font-size: 28px;
                            font-weight: bold;
                            box-shadow: 0 4px 12px {step['color']}50;
                            flex-shrink: 0;'>
                    <div style='font-size: 30px;'>{step['icon']}</div>
                    <div style='font-size: 14px; margin-top: -5px;'>STEP {step['number']}</div>
                </div>
                <div style='flex: 1;'>
                    <h3 style='color: {step['color']}; margin: 0 0 10px 0; font-size: 22px;'>{step['title']}</h3>
                    <p style='color: #002060; margin: 0; font-size: 15px; line-height: 1.6;'>{step['description']}</p>
                </div>
            </div>
        </div>
        <style>
            .workflow-card:hover {{
                transform: translateY(-5px) scale(1.01);
                box-shadow: 0 12px 25px rgba(0,0,0,0.15) !important;
            }}
        </style>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Key Concepts
    st.markdown("## 🔑 Key Concepts")

    concept_col1, concept_col2 = st.columns(2)

    with concept_col1:
        st.markdown("### Goals vs. Models")
        st.markdown("""
        - **Model**: A template allocation (e.g., "Conservative Growth" = 40% stocks, 60% bonds)
        - **Goal**: An instance of a model assigned to an account (e.g., "Retirement" goal for John Doe)
        - One model can be used by many goals across many accounts
        """)

        st.markdown("### Drift Thresholds")
        st.markdown("""
        - **Drift**: How far a portfolio has moved from its target allocation
        - **Threshold**: The % drift that triggers rebalancing (typically 5-10%)
        - **Example**: If target is 60% stocks but current is 66%, drift = +6%
        """)

    with concept_col2:
        st.markdown("### Asset Classes")
        st.markdown("""
        - Securities are mapped to asset classes (Equity, Fixed Income, Cash, etc.)
        - Rebalancer tracks allocation by asset class, not individual securities
        - You control the mapping: assign each holding to its appropriate class
        """)

        st.markdown("### Tax-Loss Harvesting")
        st.markdown("""
        - Automatically identify securities with unrealized losses
        - Sell losers to realize tax losses while maintaining asset allocation
        - Replace with similar securities to stay invested
        """)

elif section == "🔧 Process Flow":
    st.title("🔧 Rebalancing Process Flow")

    st.markdown("## The Rebalancing Journey")

    # Create HTML table with gradient backgrounds (like MMP dashboard)
    st.markdown(f"""
    <style>
        .process-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-radius: 10px;
            overflow: hidden;
        }}
        .process-table th {{
            background: linear-gradient(135deg, {APEX_COLORS['navy']} 0%, {APEX_COLORS['blue']} 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
            font-size: 16px;
        }}
        .process-table td {{
            padding: 15px;
            border-bottom: 1px solid {APEX_COLORS['light_gray']};
            font-size: 15px;
        }}
        .process-table tr:nth-child(odd) td {{
            background: linear-gradient(135deg, rgba(0,102,204,0.08) 0%, rgba(0,32,96,0.05) 100%);
        }}
        .process-table tr:nth-child(even) td {{
            background: linear-gradient(135deg, rgba(128,44,192,0.08) 0%, rgba(236,0,117,0.05) 100%);
        }}
        .process-table tr:hover td {{
            background: linear-gradient(135deg, rgba(0,102,204,0.15) 0%, rgba(128,44,192,0.1) 100%);
        }}
        .step-number {{
            font-weight: bold;
            color: {APEX_COLORS['blue']};
            font-size: 18px;
        }}
        .action-name {{
            font-weight: 600;
            color: {APEX_COLORS['navy']};
        }}
        .owner-badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 600;
        }}
        .owner-automated {{
            background-color: {APEX_COLORS['sky_blue']};
            color: white;
        }}
        .owner-advisor {{
            background-color: {APEX_COLORS['amethyst']};
            color: white;
        }}
        .owner-system {{
            background-color: {APEX_COLORS['blue']};
            color: white;
        }}
        .owner-apex {{
            background-color: {APEX_COLORS['navy']};
            color: white;
        }}
    </style>

    <table class="process-table">
        <thead>
            <tr>
                <th>Step</th>
                <th>Action</th>
                <th>Description</th>
                <th>Owner</th>
                <th>Duration</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><span class="step-number">1</span></td>
                <td><span class="action-name">Monitor Portfolios</span></td>
                <td>System continuously tracks portfolio allocations vs. targets</td>
                <td><span class="owner-badge owner-automated">Automated</span></td>
                <td>Continuous</td>
            </tr>
            <tr>
                <td><span class="step-number">2</span></td>
                <td><span class="action-name">Detect Drift</span></td>
                <td>Identify accounts exceeding drift thresholds (e.g., >5%)</td>
                <td><span class="owner-badge owner-automated">Automated</span></td>
                <td>Instant</td>
            </tr>
            <tr>
                <td><span class="step-number">3</span></td>
                <td><span class="action-name">Generate Trades</span></td>
                <td>Click 'Rebalance' to create optimized trade recommendations</td>
                <td><span class="owner-badge owner-system">System</span></td>
                <td>&lt; 5 sec</td>
            </tr>
            <tr>
                <td><span class="step-number">4</span></td>
                <td><span class="action-name">Review & Modify</span></td>
                <td>Review proposed trades in blotter, modify as needed</td>
                <td><span class="owner-badge owner-advisor">Advisor</span></td>
                <td>5-30 min</td>
            </tr>
            <tr>
                <td><span class="step-number">5</span></td>
                <td><span class="action-name">Accept Proposals</span></td>
                <td>Approve trade proposals and compliance disclosures</td>
                <td><span class="owner-badge owner-advisor">Advisor</span></td>
                <td>1-5 min</td>
            </tr>
            <tr>
                <td><span class="step-number">6</span></td>
                <td><span class="action-name">Submit Orders</span></td>
                <td>Submit trades to Apex clearing for processing</td>
                <td><span class="owner-badge owner-system">System</span></td>
                <td>Instant</td>
            </tr>
            <tr>
                <td><span class="step-number">7</span></td>
                <td><span class="action-name">Execute & Settle</span></td>
                <td>Trades execute and settle in 1-3 business days</td>
                <td><span class="owner-badge owner-apex">Apex Clearing</span></td>
                <td>1-3 days</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Key roles
    st.markdown("## 👥 Key Roles in the Process")

    # Add 3D hover effect styling
    st.markdown("""
    <style>
        .role-card {
            background-color: #F8F9FA;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            cursor: pointer;
        }
        .role-card:hover {
            transform: translateY(-10px) scale(1.05);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            background: linear-gradient(135deg, #E7F3FF 0%, #F3E7FF 100%);
        }
        .role-icon {
            font-size: 48px;
            margin-bottom: 10px;
            transition: all 0.3s ease;
        }
        .role-card:hover .role-icon {
            transform: scale(1.2) rotate(5deg);
        }
    </style>
    """, unsafe_allow_html=True)

    role_col1, role_col2, role_col3 = st.columns(3)

    with role_col1:
        st.markdown(f"""
        <div class='role-card'>
            <div class='role-icon'>🤖</div>
            <h4 style='color: {APEX_COLORS['navy']}; margin: 10px 0;'>Automated</h4>
            <p style='font-size: 14px; color: {APEX_COLORS['gray']};'>System monitors drift continuously and generates trade proposals</p>
        </div>
        """, unsafe_allow_html=True)

    with role_col2:
        st.markdown(f"""
        <div class='role-card'>
            <div class='role-icon'>👨‍💼</div>
            <h4 style='color: {APEX_COLORS['navy']}; margin: 10px 0;'>Advisor</h4>
            <p style='font-size: 14px; color: {APEX_COLORS['gray']};'>Reviews, modifies, and approves all trades before execution</p>
        </div>
        """, unsafe_allow_html=True)

    with role_col3:
        st.markdown(f"""
        <div class='role-card'>
            <div class='role-icon'>🏢</div>
            <h4 style='color: {APEX_COLORS['navy']}; margin: 10px 0;'>Apex Clearing</h4>
            <p style='font-size: 14px; color: {APEX_COLORS['gray']};'>Executes trades and handles settlement through standard processing</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Manual vs. Automated
    st.markdown("## ⚙️ Automation Options")

    tab1, tab2 = st.tabs(["🖐️ Manual Rebalancing", "🤖 Automated Rebalancing (API)"])

    with tab1:
        st.markdown("### Manual Workflow (Current State)")
        st.markdown("""
        **Advisor-Initiated:**
        1. Log into Apex Rebalancer UI
        2. Navigate to Clients → Select accounts to rebalance
        3. Click "Rebalance" button
        4. Review proposed trades in trade blotter
        5. Modify if needed (adjust quantities, remove trades)
        6. Accept proposals
        7. Submit trades to Apex clearing
        8. Monitor execution in trade history

        **Frequency:** On-demand (advisor decides when to rebalance)

        **Best For:** Firms that want full control over timing and trade decisions
        """)

    with tab2:
        st.markdown("### Automated Workflow (API-Driven)")
        st.markdown("""
        **System-Initiated:**
        1. Your system calls Rebalancer API on a schedule (e.g., daily, weekly)
        2. API identifies accounts exceeding drift thresholds
        3. API generates trade proposals automatically
        4. Trades auto-submit to Apex (if configured) OR queue for review
        5. Your system receives confirmation and trade details
        6. Monitor via API or Rebalancer UI

        **Frequency:** Scheduled (daily, weekly, monthly, or event-driven)

        **Best For:** Robo-advisors, firms managing 500+ accounts, systematic strategies

        **API Documentation:** Available through Apex Developer Portal
        """)

    st.markdown("---")

    # Common Scenarios - as expandable dropdowns
    st.markdown("## 📋 Common Rebalancing Scenarios")

    with st.expander("📈 Scenario 1: Market Drift", expanded=False):
        st.markdown("""
        **Situation:** Stock market rallies 20%, bonds flat

        **Impact:** 60/40 portfolio becomes 67/33 (7% drift)

        **Rebalancer Action:**
        - Sell stocks (capture gains)
        - Buy bonds (return to 60/40)
        - Optional: harvest tax losses if any positions are down
        """)

    with st.expander("💵 Scenario 2: Cash Deposit", expanded=False):
        st.markdown("""
        **Situation:** Client deposits $50K into account

        **Impact:** Cash allocation increases, other assets underweight

        **Rebalancer Action:**
        - Invest $50K according to target allocation
        - Buy securities to bring portfolio back to target
        - Minimize trades by prioritizing underweight positions
        """)

    with st.expander("🔄 Scenario 3: Model Update", expanded=False):
        st.markdown("""
        **Situation:** Provider updates Model Marketplace model allocation

        **Impact:** Target allocation changes (e.g., 60/40 → 55/45)

        **Rebalancer Action:**
        - Update all accounts assigned to that model
        - Generate trades to move to new target allocation
        - Advisor reviews and submits trades
        """)

    with st.expander("📉 Scenario 4: Tax-Loss Harvesting", expanded=False):
        st.markdown("""
        **Situation:** Individual stock position down 15%

        **Impact:** Unrealized loss available for harvesting

        **Rebalancer Action:**
        - Identify losing position
        - Sell to realize tax loss
        - Buy similar security to maintain allocation
        - Avoid wash sale violations
        """)

elif section == "❓ Q&A":
    st.title("❓ Common Questions & Objections")

    # Gradient styling for expander titles
    st.markdown(f"""
    <style>
        div[data-testid="stExpander"] details summary p {{
            background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
            font-size: 15px;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Search functionality
    search_query = st.text_input("🔍 Search questions:", placeholder="Type keywords to find answers...")

    qa_data = [
        ("Does the system automatically calculate what trades are needed to rebalance back to the model?", "Yes. When a portfolio drifts from its target allocation, advisors click \"Rebalance\" and the system automatically calculates the exact trades needed across all funds. For example, if a 60/40 stock/bond portfolio drifts to 65/35, the system calculates \"Sell $5,000 stocks, buy $5,000 bonds\" and breaks it down by individual fund. Advisors review the proposals and submit to trading—no manual math required. Note: Rebalancing must be manually initiated and approved by advisors; it is not fully automated."),
        ("Does Apex automatically rebalance our accounts?", "Not currently. You must manually initiate rebalancing via the UI or call our API to trigger automated rebalancing workflows."),
        ("Can we use Model Marketplace models in Rebalancer?", "Yes! Model Marketplace is fully integrated. Subscribe to models from State Street, PIMCO, Aptus, Franklin Templeton, and Zacks, and assign them to client accounts through Rebalancer goals."),
        ("How often should we rebalance?", "Best practice varies by strategy. Common approaches: quarterly calendar rebalancing, threshold-based (when drift exceeds 5-10%), or event-driven (deposits/withdrawals). Tax considerations may favor annual rebalancing."),
        ("What happens if a trade fails?", "Failed trades appear in your trade history with error details. Common causes: insufficient cash, restricted securities, market closed. Apex Support can help resolve issues via Service Center ticket."),
        ("Can we customize drift thresholds per account?", "Yes, you can set firm-level defaults and override at the account level. For example: conservative accounts might use 5% threshold, aggressive accounts 10%."),
        ("Does Rebalancer support tax-loss harvesting?", "Yes, Rebalancer identifies securities with unrealized losses and can automatically execute tax-loss harvesting while maintaining target allocations. You control the wash sale rules and replacement securities."),
        ("What if we want to exclude certain securities?", "You can create exclusion lists at the firm or account level. Common uses: exclude employer stock, restricted securities, or low-liquidity positions from rebalancing."),
        ("Can we test Rebalancer before committing?", "Yes, we can enable Rebalancer access in UAT (test environment) where you can create models, assign goals, and generate test trades without affecting live accounts."),
        ("How do we get support for Rebalancer issues?", "Open an Apex Service Center ticket under the Rebalancer category. Provide account details, screenshots, and error messages. Support is handled by Park (primary) with engineering escalation available."),
        ("What Rebalancer features work with Model Marketplace?", "All standard Rebalancer features apply: firm settings, thresholds, tax-loss harvesting, optimization between drift reduction and tax sensitivity, direct indexing, asset class management, and trade blotter analysis."),
        ("Can we rebalance across multiple account types?", "Yes, Rebalancer supports taxable, IRA, Roth IRA, 401k, 529, UTMA/UGMA, trusts, and more. Tax-loss harvesting only applies to taxable accounts."),
        ("How long does rebalancing take?", "Trade generation is typically instant (seconds for 100s of accounts). Review time varies based on your workflow. Trade execution follows standard Apex clearing timelines (1-3 days for settlement)."),
        ("Can we white-label Rebalancer reports?", "Yes, client-facing reports can be customized with your firm branding. Work with your RM to configure report templates and logos."),
        ("How much does Rebalancer cost?", "Rebalancer fees: 3 BPS of AUM assigned to rebalancing goals OR $0.20 per funded account per month (whichever is greater), billed monthly. Direct indexing features have additional fees. Contact your RM for detailed pricing.")
    ]

    # Filter Q&A based on search
    if search_query:
        filtered_qa = [(q, a) for q, a in qa_data if search_query.lower() in q.lower() or search_query.lower() in a.lower()]
    else:
        filtered_qa = qa_data

    st.markdown(f"**Showing {len(filtered_qa)} of {len(qa_data)} questions**")

    # Display Q&A
    for i, (question, answer) in enumerate(filtered_qa):
        with st.expander(f"Q: {question}"):
            st.markdown(f"**A:** {answer}")

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: {APEX_COLORS['gray']}; padding: 20px;'>
    <p><strong>Document Version:</strong> 1.0 | <strong>Last Updated:</strong> June 17, 2026</p>
    <p><strong>Owner:</strong> Apex Wealth</p>
</div>
""", unsafe_allow_html=True)
