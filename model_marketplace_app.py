import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import base64
from pathlib import Path
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import pandas as pd

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Model Marketplace | Apex Fintech Solutions",
    page_icon="📊",
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
    }}

    /* Buttons */
    .stButton>button {{
        background-color: {APEX_COLORS['blue']};
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: bold;
        border: none;
    }}

    .stButton>button:hover {{
        background-color: {APEX_COLORS['navy']};
    }}

    /* Text elements */
    p, li, span {{
        color: {APEX_COLORS['charcoal']};
    }}

    /* Success/Info/Warning boxes */
    .stSuccess {{
        background-color: #E8F5E9;
        border-left: 5px solid {APEX_COLORS['green']};
    }}

    .stInfo {{
        background-color: #E3F2FD;
        border-left: 5px solid {APEX_COLORS['blue']};
    }}

    .stWarning {{
        background-color: #FFF3E0;
        border-left: 5px solid {APEX_COLORS['gold']};
    }}

    /* Expander styling */
    .streamlit-expanderHeader {{
        background-color: {APEX_COLORS['lighter_gray']};
        border-radius: 5px;
        font-weight: bold;
        color: {APEX_COLORS['navy']};
    }}

    .streamlit-expanderHeader:hover {{
        background-color: #E3F2FD;
    }}

    /* Tables */
    .dataframe {{
        font-family: 'Calibri', sans-serif;
        background-color: white;
    }}

    /* Radio buttons */
    .stRadio > label {{
        color: {APEX_COLORS['charcoal']};
    }}

    /* Selectbox */
    .stSelectbox > label {{
        color: {APEX_COLORS['charcoal']};
    }}

    /* Text input */
    .stTextInput > label {{
        color: {APEX_COLORS['charcoal']};
    }}

    /* Custom stat card */
    .stat-card {{
        background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['bright_blue']} 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }}

    .stat-number {{
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 10px;
    }}

    .stat-label {{
        font-size: 14px;
        opacity: 0.9;
    }}

    /* Provider card */
    .provider-card {{
        border: 2px solid {APEX_COLORS['light_gray']};
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        background: white;
        transition: all 0.3s ease;
    }}

    .provider-card:hover {{
        border-color: {APEX_COLORS['blue']};
        box-shadow: 0 4px 12px rgba(0,102,204,0.2);
    }}

    .provider-name {{
        font-size: 18px;
        font-weight: bold;
        color: {APEX_COLORS['navy']};
        margin-bottom: 10px;
    }}

    .status-live {{
        background: #E8F5E9;
        color: {APEX_COLORS['green']};
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
    }}

    .status-pending {{
        background: #F3E5F5;
        color: {APEX_COLORS['purple']};
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
    }}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def create_metric_chart(value, label, color='blue'):
    """Create a visual metric card"""
    fig = go.Figure(go.Indicator(
        mode="number",
        value=value if isinstance(value, (int, float)) else 0,
        title={'text': label, 'font': {'size': 14, 'color': APEX_COLORS['charcoal']}},
        number={'font': {'size': 48, 'color': APEX_COLORS[color]}},
    ))
    fig.update_layout(
        height=150,
        margin=dict(l=20, r=20, t=30, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def create_provider_status_chart():
    """Create provider status visualization as a donut chart"""
    providers = ['Aptis', 'Franklin Templeton', 'Timco and Sachs', 'State Street']
    status = ['Live', 'Live', 'Live', 'Coming Soon']

    # Aptis uses a teal color from the green-to-blue gradient (like $0 FREE! card)
    # Others keep their original blue gradient colors
    colors = [
        '#1BAA7E',  # Aptis: Teal from the green→blue gradient
        '#3B82F6',  # Franklin Templeton: Bright Blue (original)
        '#00B0F0',  # Timco and Sachs: Sky Blue (original)
        '#7030A0'   # State Street: Purple (Coming Soon)
    ]

    # Create labels with provider name and status
    labels = [f"{provider}<br>({stat})" for provider, stat in zip(providers, status)]

    fig = go.Figure(data=[
        go.Pie(
            labels=labels,
            values=[1, 1, 1, 1],  # Equal sizes for all providers - balanced!
            hole=0.5,  # Creates donut effect (0.5 = 50% hole)
            marker=dict(
                colors=colors,
                line=dict(color='white', width=4)
            ),
            textfont=dict(size=14, color='white', family='Calibri', weight='bold'),
            hovertemplate='<b>%{label}</b><br>Provider in Marketplace<extra></extra>',
            pull=[0, 0, 0, 0]  # All balanced - no pull
        )
    ])

    fig.update_layout(
        title="Model Provider Ecosystem",
        title_font=dict(size=22, color=APEX_COLORS['navy'], family='Calibri'),
        showlegend=True,
        legend=dict(
            orientation="v",  # Vertical legend on the side
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.05,  # Position to the right of the chart
            font=dict(size=14, family='Calibri'),
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor=APEX_COLORS['light_gray'],
            borderwidth=2,
            itemsizing='constant',
            itemwidth=40  # Bigger legend boxes
        ),
        height=500,  # Bigger chart
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=200, t=60, b=40)  # More right margin for legend
    )

    return fig

def create_timeline_chart():
    """Create roadmap timeline visualization"""
    quarters = ['Q2 2026', 'Coming Soon', 'Future']
    milestones = [
        'Marketing Launch & Press Release',
        'Enhanced Model Analytics',
        'Provider Expansion & Features'
    ]

    fig = go.Figure()

    for i, (quarter, milestone) in enumerate(zip(quarters, milestones)):
        fig.add_trace(go.Scatter(
            x=[i],
            y=[0],
            mode='markers+text',
            marker=dict(size=30, color=APEX_COLORS['blue']),
            text=quarter,
            textposition='top center',
            textfont=dict(size=14, color=APEX_COLORS['navy']),
            hovertemplate=f'<b>{quarter}</b><br>{milestone}<extra></extra>',
            showlegend=False
        ))

        fig.add_annotation(
            x=i,
            y=-0.1,
            text=milestone,
            showarrow=False,
            font=dict(size=11, color=APEX_COLORS['charcoal']),
            align='center'
        )

    fig.update_layout(
        title="Product Roadmap Timeline",
        title_font=dict(size=20, color=APEX_COLORS['navy']),
        height=250,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.3, 0.3]),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=60, b=100)
    )

    return fig

def create_adoption_funnel():
    """Create adoption metrics visualization as custom bar chart with gradients"""
    # Using st.markdown directly in the section instead of returning HTML
    pass

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.image("APEX_LOGO_AFS_Color_Wide_RGB.png", use_container_width=True)
st.sidebar.markdown("---")

st.sidebar.title("📋 Navigation")

section = st.sidebar.radio(
    "Jump to Section:",
    [
        "🏠 Home",
        "📊 Executive Summary",
        "📰 Press Release Brief",
        "📊 Why Model Marketplace",
        "🔄 Process Flow",
        "👥 Roles & Responsibilities",
        "🏢 Model Providers",
        "🎯 Strategic Partner: State Street",
        "💰 Revenue Model",
        "📢 Marketing Strategy",
        "💼 Use Cases",
        "🔧 Rebalancer Integration",
        "📝 Onboarding Checklist",
        "❓ Q&A",
        "📈 Success Metrics",
        "🗺️ Roadmap",
        "📞 Contact Directory"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Version:** 1.1")
st.sidebar.markdown(f"**Last Updated:** March 24, 2026")

# Download button
st.sidebar.markdown("---")
st.sidebar.markdown("### 📥 Downloads")
if st.sidebar.button("📊 Download Metrics Excel"):
    st.sidebar.info("Metrics export feature coming soon!")

# ============================================================
# MAIN CONTENT
# ============================================================

if section == "🏠 Home":
    # Hero Section with Gradient Background
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {APEX_COLORS['navy']} 0%, {APEX_COLORS['blue']} 50%, {APEX_COLORS['sky_blue']} 100%);
                padding: 60px 40px;
                border-radius: 20px;
                text-align: center;
                margin-bottom: 40px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.15);'>
        <h1 style='font-size: 64px; color: white; border: none; margin: 0; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);'>
            Model Marketplace
        </h1>
        <h2 style='font-size: 32px; color: white; border: none; padding: 0; margin: 20px 0; font-weight: 400;'>
            Business Framework for Client Engagement
        </h2>
        <p style='font-size: 22px;
                  margin-top: 30px;
                  background: linear-gradient(135deg, white 0%, {APEX_COLORS['light_blue']} 100%);
                  -webkit-background-clip: text;
                  -webkit-text-fill-color: transparent;
                  background-clip: text;
                  font-weight: 500;'>
            Investment Model Distribution Platform<br>
            Integrated with Apex Rebalancer
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Quick Stats with Enhanced Cards
    st.markdown("### 📊 Key Metrics at a Glance")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['navy']} 0%, {APEX_COLORS['blue']} 100%);
                    padding: 30px 20px;
                    border-radius: 15px;
                    text-align: center;
                    box-shadow: 0 4px 12px rgba(0,102,204,0.3);'>
            <div style='font-size: 48px; font-weight: bold; margin-bottom: 10px;
                        background: linear-gradient(135deg, white 0%, {APEX_COLORS['light_blue']} 100%);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        background-clip: text;'>41</div>
            <div style='color: {APEX_COLORS['light_blue']}; font-size: 16px; font-weight: 500;'>Active Rebalancer Clients</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['bright_blue']} 100%);
                    padding: 30px 20px;
                    border-radius: 15px;
                    text-align: center;
                    box-shadow: 0 4px 12px rgba(59,130,246,0.3);'>
            <div style='font-size: 48px; font-weight: bold; margin-bottom: 10px;
                        background: linear-gradient(135deg, white 0%, {APEX_COLORS['light_blue']} 100%);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        background-clip: text;'>33,080</div>
            <div style='color: white; font-size: 16px; font-weight: 500; opacity: 0.9;'>Accounts on Platform</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['bright_blue']} 0%, {APEX_COLORS['sky_blue']} 100%);
                    padding: 30px 20px;
                    border-radius: 15px;
                    text-align: center;
                    box-shadow: 0 4px 12px rgba(0,176,240,0.3);'>
            <div style='font-size: 48px; font-weight: bold; margin-bottom: 10px;
                        background: linear-gradient(135deg, white 0%, {APEX_COLORS['light_blue']} 100%);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        background-clip: text;'>4</div>
            <div style='color: white; font-size: 16px; font-weight: 500; opacity: 0.9;'>Model Providers Live</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['green']} 0%, {APEX_COLORS['sky_blue']} 100%);
                    padding: 30px 20px;
                    border-radius: 15px;
                    text-align: center;
                    box-shadow: 0 4px 12px rgba(40,167,69,0.3);'>
            <div style='font-size: 48px; font-weight: bold; margin-bottom: 10px;
                        background: linear-gradient(135deg, white 0%, {APEX_COLORS['light_blue']} 100%);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        background-clip: text;'>3 BPS</div>
            <div style='color: white; font-size: 16px; font-weight: 500; opacity: 0.9;'>Starting Fee (AUM-based)</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Value Proposition Highlights
    st.markdown("### 🎯 Why Choose Model Marketplace?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div style='background: white;
                    border-left: 5px solid {APEX_COLORS['blue']};
                    padding: 25px;
                    border-radius: 10px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    height: 100%;'>
            <div style='font-size: 40px; margin-bottom: 15px;'>🎯</div>
            <h4 style='color: {APEX_COLORS['navy']}; margin-top: 0;'>Institutional Quality</h4>
            <p style='color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                Access professionally managed models from Franklin Templeton, Aptis, Timco and Sachs, and State Street
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='background: white;
                    border-left: 5px solid {APEX_COLORS['green']};
                    padding: 25px;
                    border-radius: 10px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    height: 100%;'>
            <div style='font-size: 40px; margin-bottom: 15px;'>🔄</div>
            <h4 style='color: {APEX_COLORS['navy']}; margin-top: 0;'>Automatic Updates</h4>
            <p style='color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                Models automatically update when providers rebalance—no manual intervention required
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style='background: white;
                    border-left: 5px solid {APEX_COLORS['purple']};
                    padding: 25px;
                    border-radius: 10px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    height: 100%;'>
            <div style='font-size: 40px; margin-bottom: 15px;'>⚡</div>
            <h4 style='color: {APEX_COLORS['navy']}; margin-top: 0;'>Seamless Integration</h4>
            <p style='color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                Fully integrated with Apex Rebalancer for efficient portfolio management and rebalancing
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Provider Status Chart
    st.plotly_chart(create_provider_status_chart(), use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # What's New Section - Side by Side
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['green']} 0%, {APEX_COLORS['sky_blue']} 100%);
                    padding: 30px;
                    border-radius: 15px;
                    color: white;
                    box-shadow: 0 4px 12px rgba(40,167,69,0.3);
                    height: 280px;
                    display: flex;
                    flex-direction: column;'>
            <h3 style='margin-top: 0; color: white; border: none;'>✅ Recently Completed</h3>
            <ul style='line-height: 2; font-size: 17px; margin: 0; padding-left: 20px; flex: 1;'>
                <li>Franklin Templeton SFTP integration (daily ETF reporting)</li>
                <li>Correspondent-scoped API endpoints</li>
                <li>Feature flag implementation</li>
                <li>Documentation published to Service Center</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['bright_blue']} 100%);
                    padding: 30px;
                    border-radius: 15px;
                    color: white;
                    box-shadow: 0 4px 12px rgba(0,102,204,0.3);
                    height: 280px;
                    display: flex;
                    flex-direction: column;'>
            <h3 style='margin-top: 0; color: white; border: none;'>🚀 Coming Soon</h3>
            <ul style='line-height: 2; font-size: 17px; margin: 0; padding-left: 20px; flex: 1;'>
                <li><strong>Enhanced Model Analytics</strong></li>
                <li>Dedicated BD resource for provider acquisition</li>
                <li>Enhanced provider onboarding process</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Quick Navigation CTA
    st.markdown(f"""
    <div style='background: {APEX_COLORS['lighter_gray']};
                padding: 40px;
                border-radius: 15px;
                text-align: center;
                border: 2px solid {APEX_COLORS['light_gray']};'>
        <h3 style='color: {APEX_COLORS['navy']}; margin-top: 0;'>📚 Explore the Framework</h3>
        <p style='color: {APEX_COLORS['charcoal']}; font-size: 16px; margin-bottom: 25px;'>
            Use the sidebar navigation to dive into specific sections
        </p>
        <div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;'>
            <div style='background: white; padding: 15px 25px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <strong style='color: {APEX_COLORS['blue']};'>📋 Process Flow</strong>
            </div>
            <div style='background: white; padding: 15px 25px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <strong style='color: {APEX_COLORS['blue']};'>💼 Use Cases</strong>
            </div>
            <div style='background: white; padding: 15px 25px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <strong style='color: {APEX_COLORS['blue']};'>❓ Q&A</strong>
            </div>
            <div style='background: white; padding: 15px 25px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <strong style='color: {APEX_COLORS['blue']};'>🗺️ Roadmap</strong>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif section == "📊 Executive Summary":
    # What is Model Marketplace - Large Definition Box with Left Border
    st.markdown(f"""
    <div style='background: linear-gradient(to right, {APEX_COLORS['lighter_gray']} 0%, white 100%);
                border-left: 8px solid {APEX_COLORS['blue']};
                padding: 40px 50px;
                border-radius: 12px;
                margin-bottom: 50px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.08);'>
        <div style='display: flex; align-items: center; margin-bottom: 20px;'>
            <div style='font-size: 60px; margin-right: 20px;'>💡</div>
            <h2 style='color: {APEX_COLORS['navy']}; margin: 0; font-size: 36px; border: none; padding: 0;'>
                What is Model Marketplace?
            </h2>
        </div>
        <p style='color: {APEX_COLORS['charcoal']}; font-size: 18px; line-height: 1.9; margin: 0;'>
            Model Marketplace is Apex's <strong style='color: {APEX_COLORS['blue']};'>investment model distribution platform</strong> integrated within Ascend Rebalancer,
            allowing advisors to subscribe to professionally managed models from leading investment management providers.
            Models generate trade proposals based on market activity that realign investment portfolios according to a
            defined set of holdings and their weight. Subscribed models receive <strong style='color: {APEX_COLORS['blue']};'>automatic updates and adjustments</strong>
            from the provider, enabling efficient model updates, allocation changes, and compliance monitoring.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Key Value Proposition - Horizontal List Format
    st.markdown(f"""
    <div style='margin-bottom: 30px;'>
        <h3 style='color: {APEX_COLORS['navy']}; font-size: 28px; margin-bottom: 30px;'>
            🎯 Key Value Proposition
        </h3>
    </div>
    """, unsafe_allow_html=True)

    # Feature 1
    st.markdown(f"""
    <div style='display: flex; align-items: start; gap: 25px; padding: 25px;
                background: white; border-radius: 10px; margin-bottom: 20px;
                border: 2px solid {APEX_COLORS['light_gray']};
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);'>
        <div style='flex-shrink: 0;'>
            <div style='width: 80px; height: 80px; background: {APEX_COLORS['blue']};
                        border-radius: 12px; display: flex; align-items: center;
                        justify-content: center; font-size: 40px;'>
                🎯
            </div>
        </div>
        <div style='flex-grow: 1;'>
            <h4 style='color: {APEX_COLORS['navy']}; margin: 0 0 10px 0; font-size: 20px;'>
                Institutional-Grade Investment Models
            </h4>
            <p style='color: {APEX_COLORS['charcoal']}; margin: 0; line-height: 1.7; font-size: 16px;'>
                Access professionally managed models from Franklin Templeton, Aptis, Timco and Sachs, and State Street—
                the same institutional-quality strategies used by large wealth managers
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Feature 2
    st.markdown(f"""
    <div style='display: flex; align-items: start; gap: 25px; padding: 25px;
                background: white; border-radius: 10px; margin-bottom: 20px;
                border: 2px solid {APEX_COLORS['light_gray']};
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);'>
        <div style='flex-shrink: 0;'>
            <div style='width: 80px; height: 80px; background: {APEX_COLORS['green']};
                        border-radius: 12px; display: flex; align-items: center;
                        justify-content: center; font-size: 40px;'>
                🔄
            </div>
        </div>
        <div style='flex-grow: 1;'>
            <h4 style='color: {APEX_COLORS['navy']}; margin: 0 0 10px 0; font-size: 20px;'>
                Automatic Model Updates from Providers
            </h4>
            <p style='color: {APEX_COLORS['charcoal']}; margin: 0; line-height: 1.7; font-size: 16px;'>
                When providers rebalance or adjust their models, your subscriptions automatically receive the updates—
                no manual data entry or model reconstruction required
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Feature 3
    st.markdown(f"""
    <div style='display: flex; align-items: start; gap: 25px; padding: 25px;
                background: white; border-radius: 10px; margin-bottom: 20px;
                border: 2px solid {APEX_COLORS['light_gray']};
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);'>
        <div style='flex-shrink: 0;'>
            <div style='width: 80px; height: 80px; background: {APEX_COLORS['bright_blue']};
                        border-radius: 12px; display: flex; align-items: center;
                        justify-content: center; font-size: 40px;'>
                ⚡
            </div>
        </div>
        <div style='flex-grow: 1;'>
            <h4 style='color: {APEX_COLORS['navy']}; margin: 0 0 10px 0; font-size: 20px;'>
                Seamless Rebalancer Integration
            </h4>
            <p style='color: {APEX_COLORS['charcoal']}; margin: 0; line-height: 1.7; font-size: 16px;'>
                Marketplace models integrate directly into your existing Apex Rebalancer workflow—
                use with tax-loss harvesting, optimization, thresholds, and all Rebalancer features
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Feature 4 & 5 in Two Columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style='display: flex; align-items: start; gap: 15px; padding: 20px;
                    background: white; border-radius: 10px;
                    border: 2px solid {APEX_COLORS['green']};
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05); height: 100%;'>
            <div style='flex-shrink: 0; font-size: 32px;'>💰</div>
            <div>
                <h4 style='color: {APEX_COLORS['navy']}; margin: 0 0 8px 0; font-size: 18px;'>
                    No Subscription Fees
                </h4>
                <p style='color: {APEX_COLORS['charcoal']}; margin: 0; line-height: 1.6; font-size: 15px;'>
                    Free access to the entire marketplace for all Rebalancer clients
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='display: flex; align-items: start; gap: 15px; padding: 20px;
                    background: white; border-radius: 10px;
                    border: 2px solid {APEX_COLORS['purple']};
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05); height: 100%;'>
            <div style='flex-shrink: 0; font-size: 32px;'>📊</div>
            <div>
                <h4 style='color: {APEX_COLORS['navy']}; margin: 0 0 8px 0; font-size: 18px;'>
                    Simplified Implementation
                </h4>
                <p style='color: {APEX_COLORS['charcoal']}; margin: 0; line-height: 1.6; font-size: 15px;'>
                    Quick subscription process with streamlined portfolio setup
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Providers
    st.markdown("### 🏢 Current Model Providers")

    col1, col2, col3, col4 = st.columns(4)

    providers_info = [
        ("Aptis", "LIVE", col1),
        ("Franklin Templeton", "LIVE", col2),
        ("Timco and Sachs", "LIVE", col3),
        ("State Street", "COMING SOON", col4)
    ]

    for provider, status, col in providers_info:
        with col:
            status_class = "status-live" if status == "LIVE" else "status-pending"
            st.markdown(f"""
            <div class='provider-card'>
                <div class='provider-name'>{provider}</div>
                <span class='{status_class}'>{status}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Market Size Metrics
    st.markdown("### 📊 Current Market Size")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.plotly_chart(create_metric_chart(41, "Active Rebalancer Clients", 'navy'), use_container_width=True)

    with col2:
        st.markdown(f"""
        <div class='stat-card'>
            <div class='stat-number'>33,080</div>
            <div class='stat-label'>Accounts on Rebalancer</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.plotly_chart(create_metric_chart(4, "Model Providers Live", 'blue'), use_container_width=True)

elif section == "📰 Press Release Brief":
    st.title("📰 Press Release Brief")

    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {APEX_COLORS['navy']} 0%, {APEX_COLORS['blue']} 100%);
                padding: 40px; border-radius: 15px; margin-bottom: 30px;'>
        <h2 style='margin: 0 0 15px 0; font-size: 28px; border: none; font-weight: bold;'>
            <span style='filter: none;'>📢</span>
            <span style='background: linear-gradient(135deg, white 0%, {APEX_COLORS['light_blue']} 100%);
                         -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;'>
                Apex Launches Model Marketplace
            </span>
        </h2>
        <p style='color: white; font-size: 18px; margin: 0; opacity: 0.95;'>
            Premier custody platform partners with State Street and leading asset managers to deliver
            institutional-quality investment models to RIAs and digital advisors
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Key Announcement Points
    st.subheader("📋 Key Announcement Points")

    st.markdown(f"""
    <div style='text-align: center; margin: 40px 0;'>
        <span style='font-size: 100px;'>🎯</span>
        <h2 style='color: {APEX_COLORS['blue']}; font-size: 60px; font-weight: 900; margin: 10px 0;'>01</h2>
        <h3 style='color: {APEX_COLORS['navy']}; margin: 15px 0;'>What We're Launching</h3>
        <p style='font-size: 16px; line-height: 2.0; max-width: 600px; margin: 0 auto;'>
            Model Marketplace platform • Institutional-quality models • Aptis, Franklin Templeton, Timco & Sachs • <strong style='color: {APEX_COLORS['blue']};'>State Street Partnership</strong>
        </p>
    </div>

    <div style='text-align: center; margin: 40px 0;'>
        <span style='font-size: 100px;'>✨</span>
        <h2 style='color: {APEX_COLORS['amethyst']}; font-size: 60px; font-weight: 900; margin: 10px 0;'>02</h2>
        <h3 style='color: {APEX_COLORS['amethyst']}; margin: 15px 0;'>Key Benefits</h3>
        <p style='font-size: 16px; line-height: 2.0; max-width: 600px; margin: 0 auto;'>
            <strong style='color: {APEX_COLORS['amethyst']};'>70% time reduction</strong> • Automatic model updates • Seamless workflow integration • Tax optimization ready
        </p>
    </div>

    <div style='text-align: center; margin: 40px 0;'>
        <span style='font-size: 100px;'>💰</span>
        <h2 style='color: {APEX_COLORS['green']}; font-size: 60px; font-weight: 900; margin: 10px 0;'>03</h2>
        <h3 style='color: {APEX_COLORS['green']}; margin: 15px 0;'>Market Opportunity</h3>
        <p style='font-size: 16px; line-height: 2.0; max-width: 600px; margin: 0 auto;'>
            <strong style='color: {APEX_COLORS['green']};'>41 Rebalancer clients</strong> • <strong style='color: {APEX_COLORS['green']};'>33,080 accounts</strong> • Growing demand for models • Democratizing strategies
        </p>
    </div>

    <div style='text-align: center; margin: 40px 0;'>
        <span style='font-size: 100px;'>🚀</span>
        <h2 style='color: {APEX_COLORS['gold']}; font-size: 60px; font-weight: 900; margin: 10px 0;'>04</h2>
        <h3 style='color: {APEX_COLORS['gold']}; margin: 15px 0;'>Future Vision</h3>
        <p style='font-size: 16px; line-height: 2.0; max-width: 600px; margin: 0 auto;'>
            Expanding provider network • Enhanced analytics • Growing advisor ecosystem • Dedicated BD resources
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Sample Messaging
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 24px; margin-bottom: 20px; margin-top: 30px;'>
        💬 Sample Messaging & Quotes
    </h3>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(0,102,204,0.08) 0%, rgba(0,32,96,0.05) 100%);
                padding: 30px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['blue']}; margin-bottom: 20px;'>
        <h4 style='color: {APEX_COLORS['navy']}; margin-top: 0; font-size: 18px;'>🎙️ Executive Quote (Sample)</h4>
        <p style='font-style: italic; font-size: 16px; line-height: 1.8; color: {APEX_COLORS['charcoal']}; margin: 15px 0;'>
            "Model Marketplace represents a significant milestone in democratizing institutional-quality investment strategies.
            By partnering with industry leaders like State Street, we're enabling RIAs of all sizes to offer the same sophisticated
            portfolio solutions previously available only to the largest wealth managers."
        </p>
        <p style='margin: 0; font-weight: 600; color: {APEX_COLORS['navy']};'>— [Executive Name], [Title], Apex Fintech Solutions</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(128,44,192,0.08) 0%, rgba(236,0,117,0.05) 100%);
                padding: 30px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['amethyst']}; margin-bottom: 20px;'>
        <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                   margin-top: 0; font-size: 18px; font-weight: 600;'>🏦 State Street Quote (Sample)</h4>
        <p style='font-style: italic; font-size: 16px; line-height: 1.8; color: {APEX_COLORS['charcoal']}; margin: 15px 0;'>
            "Our partnership with Apex opens new distribution channels for State Street's investment strategies,
            allowing us to serve a broader range of advisors and their clients through a best-in-class technology platform."
        </p>
        <p style='margin: 0; font-weight: 600;'><span style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>— [Executive Name], [Title], State Street</span></p>
    </div>
    """, unsafe_allow_html=True)

    # Quick Stats Box
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 24px; margin-bottom: 20px; margin-top: 30px;'>
        📊 Press Release Stats
    </h3>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['navy']} 0%, {APEX_COLORS['blue']} 100%);
                    padding: 25px; border-radius: 12px; text-align: center;'>
            <div style='font-size: 36px; font-weight: bold; color: white;'>41</div>
            <div style='color: white; font-size: 14px; opacity: 0.9; margin-top: 8px;'>Rebalancer Clients</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['bright_blue']} 100%);
                    padding: 25px; border-radius: 12px; text-align: center;'>
            <div style='font-size: 36px; font-weight: bold; color: white;'>33K+</div>
            <div style='color: white; font-size: 14px; opacity: 0.9; margin-top: 8px;'>Accounts on Platform</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                    padding: 25px; border-radius: 12px; text-align: center;'>
            <div style='font-size: 36px; font-weight: bold; color: white;'>4</div>
            <div style='color: white; font-size: 14px; opacity: 0.9; margin-top: 8px;'>Model Providers</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['green']} 0%, {APEX_COLORS['sky_blue']} 100%);
                    padding: 25px; border-radius: 12px; text-align: center;'>
            <div style='font-size: 36px; font-weight: bold; color: white;'>70%</div>
            <div style='color: white; font-size: 14px; opacity: 0.9; margin-top: 8px;'>Time Savings</div>
        </div>
        """, unsafe_allow_html=True)

elif section == "📊 Why Model Marketplace":
    st.title("📊 Why Model Marketplace?")

    st.markdown(f"""
    <div style='background: linear-gradient(to right, {APEX_COLORS['lighter_gray']} 0%, white 100%);
                border-left: 8px solid {APEX_COLORS['blue']};
                padding: 40px 50px;
                border-radius: 12px;
                margin-bottom: 40px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.08);'>
        <h3 style='color: {APEX_COLORS['navy']}; margin: 0 0 15px 0; font-size: 28px;'>
            Three Approaches to Portfolio Management
        </h3>
        <p style='color: {APEX_COLORS['charcoal']}; font-size: 16px; line-height: 1.8; margin: 0;'>
            Most Apex Rebalancer clients currently manage their own proprietary models. Model Marketplace offers
            a complementary approach—allowing firms to blend custom strategies with institutional models or
            offer clients choice between proprietary and third-party solutions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Comparison Table
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 24px; margin-bottom: 20px;'>
        🔄 Comparison: Custom vs Marketplace vs Hybrid
    </h3>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <table style='width: 100%; border-collapse: collapse; margin: 20px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
        <thead>
            <tr style='background: {APEX_COLORS['navy']}; color: white;'>
                <th style='padding: 15px; text-align: left; border: 1px solid #ddd;'>Aspect</th>
                <th style='padding: 15px; text-align: left; border: 1px solid #ddd;'>Custom Models Only</th>
                <th style='padding: 15px; text-align: left; border: 1px solid #ddd;'>Marketplace Only</th>
                <th style='padding: 15px; text-align: left; border: 1px solid #ddd;'>Hybrid Approach</th>
            </tr>
        </thead>
        <tbody>
            <tr style='background: white;'>
                <td style='padding: 15px; border: 1px solid #ddd; font-weight: 600; color: {APEX_COLORS['blue']};'>Investment Philosophy</td>
                <td style='padding: 15px; border: 1px solid #ddd;'>100% proprietary</td>
                <td style='padding: 15px; border: 1px solid #ddd;'>100% third-party institutional</td>
                <td style='padding: 15px; border: 1px solid #ddd; background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.02) 100%);'>
                    Mix of proprietary + institutional ✨
                </td>
            </tr>
            <tr style='background: #f9f9f9;'>
                <td style='padding: 15px; border: 1px solid #ddd; font-weight: 600; color: {APEX_COLORS['blue']};'>Research Overhead</td>
                <td style='padding: 15px; border: 1px solid #ddd;'>High - in-house team required</td>
                <td style='padding: 15px; border: 1px solid #ddd; background: linear-gradient(135deg, rgba(40,167,69,0.05) 0%, rgba(40,167,69,0.02) 100%);'>
                    None - provider manages ✅
                </td>
                <td style='padding: 15px; border: 1px solid #ddd;'>Moderate - focus on strategic allocation</td>
            </tr>
            <tr style='background: white;'>
                <td style='padding: 15px; border: 1px solid #ddd; font-weight: 600; color: {APEX_COLORS['blue']};'>Client Options</td>
                <td style='padding: 15px; border: 1px solid #ddd;'>Firm strategies only</td>
                <td style='padding: 15px; border: 1px solid #ddd;'>Institutional strategies only</td>
                <td style='padding: 15px; border: 1px solid #ddd; background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.02) 100%);'>
                    Full menu - client choice ✨
                </td>
            </tr>
            <tr style='background: #f9f9f9;'>
                <td style='padding: 15px; border: 1px solid #ddd; font-weight: 600; color: {APEX_COLORS['blue']};'>Time to Market</td>
                <td style='padding: 15px; border: 1px solid #ddd;'>Months to build</td>
                <td style='padding: 15px; border: 1px solid #ddd; background: linear-gradient(135deg, rgba(40,167,69,0.05) 0%, rgba(40,167,69,0.02) 100%);'>
                    Weeks to subscribe ✅
                </td>
                <td style='padding: 15px; border: 1px solid #ddd;'>Immediate expansion</td>
            </tr>
            <tr style='background: white;'>
                <td style='padding: 15px; border: 1px solid #ddd; font-weight: 600; color: {APEX_COLORS['blue']};'>Scalability</td>
                <td style='padding: 15px; border: 1px solid #ddd;'>Limited by team capacity</td>
                <td style='padding: 15px; border: 1px solid #ddd; background: linear-gradient(135deg, rgba(40,167,69,0.05) 0%, rgba(40,167,69,0.02) 100%);'>
                    Unlimited with automation ✅
                </td>
                <td style='padding: 15px; border: 1px solid #ddd; background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.02) 100%);'>
                    Best of both worlds ✨
                </td>
            </tr>
            <tr style='background: #f9f9f9;'>
                <td style='padding: 15px; border: 1px solid #ddd; font-weight: 600; color: {APEX_COLORS['blue']};'>Brand Control</td>
                <td style='padding: 15px; border: 1px solid #ddd; background: linear-gradient(135deg, rgba(40,167,69,0.05) 0%, rgba(40,167,69,0.02) 100%);'>
                    Full branding control ✅
                </td>
                <td style='padding: 15px; border: 1px solid #ddd;'>Provider-branded</td>
                <td style='padding: 15px; border: 1px solid #ddd; background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.02) 100%);'>
                    Selective white-labeling ✨
                </td>
            </tr>
            <tr style='background: white;'>
                <td style='padding: 15px; border: 1px solid #ddd; font-weight: 600; color: {APEX_COLORS['blue']};'>Best For</td>
                <td style='padding: 15px; border: 1px solid #ddd;'>Large RIAs with research teams</td>
                <td style='padding: 15px; border: 1px solid #ddd;'>Digital advisors, new entrants</td>
                <td style='padding: 15px; border: 1px solid #ddd; background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.02) 100%);'>
                    Growing RIAs seeking flexibility ✨
                </td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Use Case Examples
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 24px; margin-top: 40px; margin-bottom: 20px;'>
        💡 Real-World Scenarios
    </h3>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div style='background: white; padding: 25px; border-radius: 12px; border: 2px solid {APEX_COLORS['blue']}; height: 100%; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
            <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0;'>🏢 Scenario 1</h4>
            <p style='font-weight: 600; color: {APEX_COLORS['navy']};'>Custom Only</p>
            <p style='font-size: 14px; line-height: 1.6; color: {APEX_COLORS['charcoal']};'>
                Large wealth manager with 10-person investment committee. Built proprietary models over years.
                Uses Rebalancer for portfolio management but doesn't need external models.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='background: white; padding: 25px; border-radius: 12px; border: 2px solid {APEX_COLORS['green']}; height: 100%; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
            <h4 style='color: {APEX_COLORS['green']}; margin-top: 0;'>📱 Scenario 2</h4>
            <p style='font-weight: 600; color: {APEX_COLORS['navy']};'>Marketplace Only</p>
            <p style='font-size: 14px; line-height: 1.6; color: {APEX_COLORS['charcoal']};'>
                Digital advisor launching managed portfolios. No in-house research team. Subscribes to
                Franklin Templeton and Aptis models. Scales to 10,000+ accounts quickly.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style='background: white; padding: 25px; border-radius: 12px; border: 2px solid {APEX_COLORS['amethyst']}; height: 100%; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
            <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                       margin-top: 0; font-weight: 600;'>🌟 Scenario 3</h4>
            <p style='font-weight: 600; color: {APEX_COLORS['navy']};'>Hybrid Approach</p>
            <p style='font-size: 14px; line-height: 1.6; color: {APEX_COLORS['charcoal']};'>
                Mid-sized RIA with custom value-oriented models. Clients request ESG and thematic exposure.
                Adds State Street ESG models to complement proprietary strategies.
            </p>
        </div>
        """, unsafe_allow_html=True)

elif section == "🎯 Strategic Partner: State Street":
    st.title("🎯 Strategic Partner: State Street")

    # Hero Section
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                padding: 50px 40px;
                border-radius: 20px;
                text-align: center;
                margin-bottom: 40px;
                box-shadow: 0 8px 24px rgba(128,44,192,0.2);'>
        <h1 style='font-size: 48px; color: white; margin: 0; font-weight: bold; border: none;'>
            State Street Partnership
        </h1>
        <h3 style='font-size: 24px; color: white; margin: 20px 0 0 0; font-weight: 400; border: none; padding: 0; opacity: 0.95;'>
            Top Strategic Partner for Model Marketplace Launch
        </h3>
    </div>
    """, unsafe_allow_html=True)

    # Why State Street
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 24px; margin-bottom: 20px;'>
        🌟 Why State Street?
    </h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style='background: white; padding: 30px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['amethyst']};
                    margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); height: 100%;'>
            <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                       margin-top: 0; font-weight: 600;'>🏦 Industry Leadership</h4>
            <ul style='line-height: 1.8; color: {APEX_COLORS['charcoal']};'>
                <li>Global financial services leader</li>
                <li>$4+ trillion in AUM</li>
                <li>Trusted institutional brand</li>
                <li>Deep expertise in asset management</li>
                <li>Proven track record in model portfolios</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='background: white; padding: 30px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['blue']};
                    margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); height: 100%;'>
            <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0;'>🤝 Strategic Alignment</h4>
            <ul style='line-height: 1.8; color: {APEX_COLORS['charcoal']};'>
                <li>Shared vision for democratizing institutional strategies</li>
                <li>Commitment to technology-enabled distribution</li>
                <li>Focus on RIA and digital advisor markets</li>
                <li>Long-term partnership approach</li>
                <li>Aligned incentives for mutual growth</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Partnership Value
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 24px; margin-bottom: 20px; margin-top: 30px;'>
        💎 Partnership Value Proposition
    </h3>
    """, unsafe_allow_html=True)

    # Value for Apex
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(0,102,204,0.08) 0%, rgba(0,32,96,0.05) 100%);
                padding: 30px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['blue']}; margin-bottom: 20px;'>
        <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0; font-size: 20px;'>📈 Value for Apex</h4>
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;'>
            <div>
                <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                    ✅ <strong>Credibility:</strong> Premier brand validates Model Marketplace
                </p>
            </div>
            <div>
                <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                    ✅ <strong>Quality:</strong> Institutional-grade models attract sophisticated clients
                </p>
            </div>
            <div>
                <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                    ✅ <strong>Scale:</strong> State Street's brand draws client interest
                </p>
            </div>
            <div>
                <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                    ✅ <strong>Differentiation:</strong> Competitive advantage in custody market
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Value for State Street
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(128,44,192,0.08) 0%, rgba(236,0,117,0.05) 100%);
                padding: 30px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['amethyst']}; margin-bottom: 20px;'>
        <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                   margin-top: 0; font-size: 20px; font-weight: 600;'>🚀 Value for State Street</h4>
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;'>
            <div>
                <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                    ✅ <strong>Distribution:</strong> Access to 41 RIA firms and 33,080 accounts
                </p>
            </div>
            <div>
                <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                    ✅ <strong>Automation:</strong> Scalable platform for model delivery
                </p>
            </div>
            <div>
                <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                    ✅ <strong>Market Access:</strong> Reach emerging digital advisor segment
                </p>
            </div>
            <div>
                <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                    ✅ <strong>Efficiency:</strong> One integration reaches multiple advisors
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Current Status
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 24px; margin-bottom: 20px; margin-top: 30px;'>
        📊 Current Status & Next Steps
    </h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(251,191,36,0.1) 0%, rgba(245,158,11,0.05) 100%);
                    padding: 30px; border-radius: 12px; border: 2px solid {APEX_COLORS['gold']}; height: 100%;'>
            <h4 style='color: {APEX_COLORS['gold']}; margin-top: 0;'>📋 Status: Coming Soon</h4>
            <p style='color: {APEX_COLORS['charcoal']}; line-height: 1.8; margin-bottom: 15px;'>
                State Street models are in final stages of onboarding and will be available on Model Marketplace shortly.
            </p>
            <p style='margin: 0; font-size: 14px;'>
                <strong style='color: {APEX_COLORS['navy']};'>Awaiting:</strong> Final model holdings data submission
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(40,167,69,0.1) 0%, rgba(40,167,69,0.05) 100%);
                    padding: 30px; border-radius: 12px; border: 2px solid {APEX_COLORS['green']}; height: 100%;'>
            <h4 style='color: {APEX_COLORS['green']}; margin-top: 0;'>🎯 Next Steps</h4>
            <ol style='color: {APEX_COLORS['charcoal']}; line-height: 1.8; margin: 0; padding-left: 20px;'>
                <li>Receive holdings data from State Street</li>
                <li>Upload models to production</li>
                <li>Internal testing and validation</li>
                <li>Launch announcement and press release</li>
                <li>Client enablement and training</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Press Release Angle
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 24px; margin-bottom: 20px; margin-top: 30px;'>
        📰 Press Release Messaging
    </h3>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.02) 100%);
                padding: 35px; border-radius: 12px; border: 2px solid {APEX_COLORS['amethyst']};'>
        <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                   margin-top: 0; font-size: 20px; font-weight: 600;'>🎤 Recommended Headline</h4>
        <p style='font-size: 18px; font-weight: 600; color: {APEX_COLORS['navy']}; margin: 15px 0; line-height: 1.6;'>
            "Apex Fintech Solutions Partners with State Street to Launch Model Marketplace,
            Bringing Institutional Investment Strategies to RIAs and Digital Advisors"
        </p>
        <hr style='border: none; border-top: 1px solid #ddd; margin: 20px 0;'>
        <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                   margin: 20px 0 10px 0; font-size: 18px; font-weight: 600;'>Key Message Points:</h4>
        <ul style='color: {APEX_COLORS['charcoal']}; line-height: 1.8; margin: 10px 0;'>
            <li>First-of-its-kind partnership between premier custody platform and global asset manager</li>
            <li>State Street models available alongside Aptis, Franklin Templeton, and Timco and Sachs</li>
            <li>Enables firms of all sizes to compete with institutional-quality investment solutions</li>
            <li>Seamless integration with Apex Rebalancer platform serving 41 firms</li>
            <li>Foundation for expanding provider network and model selection</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif section == "🔄 Process Flow":
    st.title("🔄 Model Marketplace Process Flow")

    # Client Journey Map Section
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(128,44,192,0.08) 0%, rgba(236,0,117,0.05) 100%);
                padding: 30px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['amethyst']}; margin-bottom: 30px;'>
        <h3 style='color: {APEX_COLORS['amethyst']}; margin: 0 0 10px 0;'>End-to-End Client Journey</h3>
        <p style='color: {APEX_COLORS['charcoal']}; margin: 0; font-size: 16px;'>
            Visual overview of how clients go from existing Rebalancer users to actively delivering
            institutional models to their advisors and end clients.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Journey Stages
    st.markdown(f"""
    <h3 style='font-weight: 700; font-size: 24px; margin-bottom: 30px;'>
        <span style='filter: none;'>🛤️</span>
        <span style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                     -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;'>
            Five-Stage Journey
        </span>
    </h3>
    """, unsafe_allow_html=True)

    # Stage 1
    st.markdown(f"""
    <div style='display: flex; align-items: center; margin-bottom: 25px;'>
        <div style='background: {APEX_COLORS['blue']}; color: white; width: 60px; height: 60px; border-radius: 50%;
                    display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold;
                    flex-shrink: 0; margin-right: 20px; box-shadow: 0 4px 12px rgba(0,102,204,0.3);'>1</div>
        <div style='flex-grow: 1; background: linear-gradient(135deg, rgba(0,102,204,0.1) 0%, rgba(59,130,246,0.05) 100%);
                    padding: 20px; border-radius: 12px; border-left: 4px solid {APEX_COLORS['blue']};'>
            <h4 style='color: {APEX_COLORS['blue']}; margin: 0 0 10px 0;'>Discovery & Enablement</h4>
            <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                <strong>Who:</strong> Apex Sales/RM + Client<br>
                <strong>What:</strong> Client learns about Model Marketplace, evaluates fit, decides to enable<br>
                <strong>Output:</strong> Feature enabled in Client Configurator
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Arrow 1->2
    st.markdown(f"""
    <div style='text-align: center; margin: 20px 0;'>
        <div style='width: 3px; height: 30px; background: linear-gradient(180deg, {APEX_COLORS['blue']}, {APEX_COLORS['sky_blue']}); margin: 0 auto;'></div>
        <div style='width: 0; height: 0; margin: 0 auto;
                    border-left: 10px solid transparent;
                    border-right: 10px solid transparent;
                    border-top: 12px solid {APEX_COLORS['sky_blue']};'></div>
    </div>
    """, unsafe_allow_html=True)

    # Stage 2
    st.markdown(f"""
    <div style='display: flex; align-items: center; margin-bottom: 25px;'>
        <div style='background: {APEX_COLORS['sky_blue']}; color: white; width: 60px; height: 60px; border-radius: 50%;
                    display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold;
                    flex-shrink: 0; margin-right: 20px; box-shadow: 0 4px 12px rgba(0,176,240,0.3);'>2</div>
        <div style='flex-grow: 1; background: linear-gradient(135deg, rgba(0,176,240,0.1) 0%, rgba(0,176,240,0.05) 100%);
                    padding: 20px; border-radius: 12px; border-left: 4px solid {APEX_COLORS['sky_blue']};'>
            <h4 style='color: {APEX_COLORS['sky_blue']}; margin: 0 0 10px 0;'>Access & Permissions</h4>
            <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                <strong>Who:</strong> Client Administrator + Apex Onboarding<br>
                <strong>What:</strong> Grant subscribe permissions to authorized users, configure access<br>
                <strong>Output:</strong> Users can access Model Marketplace in Ascend
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Arrow 2->3
    st.markdown(f"""
    <div style='text-align: center; margin: 20px 0;'>
        <div style='width: 3px; height: 30px; background: linear-gradient(180deg, {APEX_COLORS['sky_blue']}, {APEX_COLORS['green']}); margin: 0 auto;'></div>
        <div style='width: 0; height: 0; margin: 0 auto;
                    border-left: 10px solid transparent;
                    border-right: 10px solid transparent;
                    border-top: 12px solid {APEX_COLORS['green']};'></div>
    </div>
    """, unsafe_allow_html=True)

    # Stage 3
    st.markdown(f"""
    <div style='display: flex; align-items: center; margin-bottom: 25px;'>
        <div style='background: {APEX_COLORS['green']}; color: white; width: 60px; height: 60px; border-radius: 50%;
                    display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold;
                    flex-shrink: 0; margin-right: 20px; box-shadow: 0 4px 12px rgba(40,167,69,0.3);'>3</div>
        <div style='flex-grow: 1; background: linear-gradient(135deg, rgba(40,167,69,0.1) 0%, rgba(40,167,69,0.05) 100%);
                    padding: 20px; border-radius: 12px; border-left: 4px solid {APEX_COLORS['green']};'>
            <h4 style='color: {APEX_COLORS['green']}; margin: 0 0 10px 0;'>Browse & Subscribe</h4>
            <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                <strong>Who:</strong> End Client/Advisor<br>
                <strong>What:</strong> Browse models, review holdings/weights, subscribe to selected models, accept T&Cs<br>
                <strong>Output:</strong> Subscribed models available in Rebalancer
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Arrow 3->4
    st.markdown(f"""
    <div style='text-align: center; margin: 20px 0;'>
        <div style='width: 3px; height: 30px; background: linear-gradient(180deg, {APEX_COLORS['green']}, {APEX_COLORS['amethyst']}); margin: 0 auto;'></div>
        <div style='width: 0; height: 0; margin: 0 auto;
                    border-left: 10px solid transparent;
                    border-right: 10px solid transparent;
                    border-top: 12px solid {APEX_COLORS['amethyst']};'></div>
    </div>
    """, unsafe_allow_html=True)

    # Stage 4
    st.markdown(f"""
    <div style='display: flex; align-items: center; margin-bottom: 25px;'>
        <div style='background: {APEX_COLORS['amethyst']}; color: white; width: 60px; height: 60px; border-radius: 50%;
                    display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold;
                    flex-shrink: 0; margin-right: 20px; box-shadow: 0 4px 12px rgba(128,44,192,0.3);'>4</div>
        <div style='flex-grow: 1; background: linear-gradient(135deg, rgba(128,44,192,0.1) 0%, rgba(236,0,117,0.05) 100%);
                    padding: 20px; border-radius: 12px; border-left: 4px solid {APEX_COLORS['amethyst']};'>
            <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                       margin: 0 0 10px 0; font-weight: 600;'>Configure & Assign</h4>
            <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                <strong>Who:</strong> Client/Advisor<br>
                <strong>What:</strong> Verify asset class mappings, create goals, assign models to client accounts, set thresholds<br>
                <strong>Output:</strong> Accounts ready for rebalancing with marketplace models
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Arrow 4->5
    st.markdown(f"""
    <div style='text-align: center; margin: 20px 0;'>
        <div style='width: 3px; height: 30px; background: linear-gradient(180deg, {APEX_COLORS['amethyst']}, {APEX_COLORS['gold']}); margin: 0 auto;'></div>
        <div style='width: 0; height: 0; margin: 0 auto;
                    border-left: 10px solid transparent;
                    border-right: 10px solid transparent;
                    border-top: 12px solid {APEX_COLORS['gold']};'></div>
    </div>
    """, unsafe_allow_html=True)

    # Stage 5
    st.markdown(f"""
    <div style='display: flex; align-items: center; margin-bottom: 25px;'>
        <div style='background: {APEX_COLORS['gold']}; color: white; width: 60px; height: 60px; border-radius: 50%;
                    display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold;
                    flex-shrink: 0; margin-right: 20px; box-shadow: 0 4px 12px rgba(251,191,36,0.3);'>5</div>
        <div style='flex-grow: 1; background: linear-gradient(135deg, rgba(251,191,36,0.1) 0%, rgba(245,158,11,0.05) 100%);
                    padding: 20px; border-radius: 12px; border-left: 4px solid {APEX_COLORS['gold']};'>
            <h4 style='color: {APEX_COLORS['gold']}; margin: 0 0 10px 0;'>Rebalance & Deliver</h4>
            <p style='margin: 0; color: {APEX_COLORS['charcoal']}; line-height: 1.6;'>
                <strong>Who:</strong> Client/Advisor<br>
                <strong>What:</strong> Initiate rebalance, review proposals, accept proposals, submit trades, deliver models to end clients<br>
                <strong>Output:</strong> Institutional models actively managed for client accounts
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Key Touchpoints
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 24px; margin-top: 40px; margin-bottom: 20px;'>
        🎯 Key Touchpoints & Timeline
    </h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style='background: white; padding: 25px; border-radius: 12px; border: 2px solid {APEX_COLORS['blue']}; height: 100%;'>
            <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0;'>⏱️ Typical Timeline</h4>
            <ul style='line-height: 1.8; color: {APEX_COLORS['charcoal']};'>
                <li><strong>Stage 1-2:</strong> 1-2 weeks (enablement + permissions)</li>
                <li><strong>Stage 3:</strong> 5-10 minutes (browse + subscribe)</li>
                <li><strong>Stage 4:</strong> 15-30 minutes (first-time configuration)</li>
                <li><strong>Stage 5:</strong> Variable (ongoing rebalancing)</li>
                <li><strong>Total Time to First Rebalance:</strong> ~2-3 weeks</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='background: white; padding: 25px; border-radius: 12px; border: 2px solid {APEX_COLORS['green']}; height: 100%;'>
            <h4 style='color: {APEX_COLORS['green']}; margin-top: 0;'>✅ Success Criteria</h4>
            <ul style='line-height: 1.8; color: {APEX_COLORS['charcoal']};'>
                <li>Client successfully subscribed to at least 1 model</li>
                <li>Asset class mappings verified</li>
                <li>Models assigned to test accounts</li>
                <li>First rebalance executed successfully</li>
                <li>Client understands ongoing workflow</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 8-Step Implementation Process")

    # Progress indicator
    st.markdown("**Drag to view step:**")
    step_progress = st.slider("", 1, 8, 1, label_visibility="collapsed")

    steps = [
        {
            "title": "Step 1: Initial Access Setup",
            "who": "Apex Onboarding Team / Client Configurator Team",
            "what": "Enable Model Marketplace at correspondent level",
            "where": "Client Configurator → Experience Settings → Enable Model Marketplace",
            "timeline": "Completed during client onboarding",
            "color": APEX_COLORS['blue']
        },
        {
            "title": "Step 2: User Permission Configuration",
            "who": "Client Administrator / Apex Client Services",
            "what": "Grant subscribe permissions to specific users",
            "where": "User management interface",
            "timeline": "Before first use",
            "color": APEX_COLORS['bright_blue']
        },
        {
            "title": "Step 3: Client Acceptance & Discovery",
            "who": "End Client/Advisor",
            "what": "Sign in to Ascend Workstation → Trading → Model Marketplace",
            "where": "Accept Apex Terms & Conditions (one-time, all providers)",
            "timeline": "5-10 minutes (one-time setup)",
            "color": APEX_COLORS['sky_blue']
        },
        {
            "title": "Step 4: Model Evaluation",
            "who": "Client/Advisor",
            "what": "Review model details: Holdings, Target Weights, Summary, Resources",
            "where": "Columns: Provider | Model | Investment Vehicle | Status",
            "timeline": "Variable - depends on research depth",
            "color": APEX_COLORS['navy']
        },
        {
            "title": "Step 5: Model Subscription",
            "who": "Authorized Client User (with subscribe permission)",
            "what": "Click Subscribe → Accept Provider-Specific T&Cs",
            "where": "Status changes: AVAILABLE → SUBSCRIBED, Button: Green → Red",
            "timeline": "2-3 minutes per model",
            "color": APEX_COLORS['green']
        },
        {
            "title": "Step 6: Post-Subscription Configuration in Rebalancer",
            "who": "Client/Advisor",
            "what": "CRITICAL: Verify asset class assignments for each security",
            "where": "Rebalancer → Settings → Models → Create Goals → Assign to Accounts",
            "timeline": "15-30 minutes for first model",
            "color": APEX_COLORS['gold']
        },
        {
            "title": "Step 7: Portfolio Rebalancing",
            "who": "Client/Advisor",
            "what": "Initiate rebalance → Review proposals → Accept proposals → Review in Accepted Proposals tab → Submit trades",
            "where": "Review compliance disclosures before submission",
            "timeline": "Variable based on portfolio size",
            "color": APEX_COLORS['purple']
        },
        {
            "title": "Step 8: Unsubscribe (Optional)",
            "who": "Client/Advisor",
            "what": "Stops automatic updates but retains last subscribed weights",
            "where": "To fully discontinue: Delete model from Rebalancer",
            "timeline": "Immediate",
            "color": APEX_COLORS['amethyst'],
            "color2": APEX_COLORS['amethyst_pink']
        }
    ]

    # Display selected step
    selected_step = steps[step_progress - 1]

    # Handle gradient for Step 8 (amethyst gradient)
    if 'color2' in selected_step:
        gradient = f"linear-gradient(135deg, {selected_step['color']} 0%, {selected_step['color2']} 100%)"
    else:
        gradient = f"linear-gradient(135deg, {selected_step['color']} 0%, {APEX_COLORS['lighter_gray']} 100%)"

    # Use white gradient text for dark backgrounds (navy)
    if selected_step['color'] == APEX_COLORS['navy']:
        text_style = f"""background: linear-gradient(135deg, white 0%, {APEX_COLORS['light_blue']} 100%);
                         -webkit-background-clip: text;
                         -webkit-text-fill-color: transparent;
                         background-clip: text;"""
    else:
        text_style = "color: white;"

    st.markdown(f"""
    <div style='background: {gradient};
                padding: 30px; border-radius: 15px; margin: 20px 0;'>
        <h2 style='{text_style} border: none; padding: 0; margin: 0;'>{selected_step['title']}</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"**👤 WHO:** {selected_step['who']}")
        st.markdown(f"**📋 WHAT:** {selected_step['what']}")

    with col2:
        st.markdown(f"**📍 WHERE:** {selected_step['where']}")
        st.markdown(f"**⏱️ TIMELINE:** {selected_step['timeline']}")

    # Show all steps expandable
    st.markdown("---")
    st.markdown("### View All Steps")

    # Add gradient styling to expander labels
    st.markdown(f"""
    <style>
        div[data-testid="stExpander"] summary p {{
            background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
        }}
    </style>
    """, unsafe_allow_html=True)

    for i, step in enumerate(steps, 1):
        with st.expander(f"{step['title']}"):
            st.markdown(f"**👤 WHO:** {step['who']}")
            st.markdown(f"**📋 WHAT:** {step['what']}")
            st.markdown(f"**📍 WHERE:** {step['where']}")
            st.markdown(f"**⏱️ TIMELINE:** {step['timeline']}")

    # Key limitation warning
    st.warning("⚠️ **KEY LIMITATION:** Apex does NOT automatically execute trades. Clients must currently review and submit all trade orders manually.")

elif section == "👥 Roles & Responsibilities":
    st.title("👥 Roles & Responsibilities Matrix")

    # Client Eligibility Section
    st.markdown("### ✅ Client Eligibility Checker")

    st.markdown(f"""
    <p style='font-size: 16px; margin-bottom: 20px;'>
        <strong>Requirements:</strong>
        <span style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                     -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                     font-weight: 600;'>
            Client must be on Ascend platform and have an active Rebalancer subscription.
        </span>
    </p>
    """, unsafe_allow_html=True)

    with st.form("eligibility_form"):
        st.markdown("Check if a client is eligible for Model Marketplace:")

        col1, col2 = st.columns(2)

        with col1:
            on_ascend = st.radio("Is the client on Ascend platform?", ["Yes", "No"], horizontal=True)
            is_rebalancer = st.radio("Is the client a Rebalancer customer?", ["Yes", "No"], horizontal=True)

        with col2:
            migration_status = st.selectbox("Migration Status:", ["Fully on Ascend", "Mid-migration", "Classic only"])

        submitted = st.form_submit_button("Check Eligibility")

        if submitted:
            if on_ascend == "Yes" and is_rebalancer == "Yes" and migration_status == "Fully on Ascend":
                st.success("✅ **ELIGIBLE!** This client can use Model Marketplace immediately after onboarding team enables access.")
            elif on_ascend == "Yes" and is_rebalancer == "Yes" and migration_status == "Mid-migration":
                st.warning("⚠️ **PARTIALLY ELIGIBLE** - Client can use Model Marketplace but only for migrated accounts.")
            else:
                reasons = []
                if on_ascend == "No":
                    reasons.append("Must be on Ascend platform")
                if is_rebalancer == "No":
                    reasons.append("Must be a Rebalancer client")
                st.error(f"❌ **NOT ELIGIBLE** - Client needs: {', '.join(reasons)}")

    st.markdown("---")

    st.markdown("### Who Does What?")

    # Custom styling for multiselect label and selected items
    st.markdown(f"""
    <style>
        div[data-testid="stMultiSelect"] label {{
            color: {APEX_COLORS['blue']} !important;
            font-weight: 600 !important;
            font-size: 16px !important;
        }}

        /* Style the selected role chips/tags */
        div[data-testid="stMultiSelect"] span[data-baseweb="tag"] {{
            background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['bright_blue']} 100%) !important;
        }}

        div[data-testid="stMultiSelect"] span[data-baseweb="tag"] span {{
            background: linear-gradient(135deg, white 0%, {APEX_COLORS['light_blue']} 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            font-weight: 600 !important;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Interactive role filter
    role_filter = st.multiselect(
        "Filter by role:",
        ["Client", "Apex RM/Sales", "Apex Onboarding", "Client Services", "Engineering/PM"],
        default=["Client", "Apex RM/Sales", "Apex Onboarding"]
    )

    # Roles matrix data
    matrix_data = {
        "Activity": [
            "Identify Rebalancer prospects",
            "Present Model Marketplace value",
            "Validate Ascend migration status",
            "Enable Model Marketplace (Client Configurator)",
            "Configure user subscribe permissions",
            "Provide training/documentation",
            "Accept Apex T&Cs",
            "Browse and evaluate models",
            "Subscribe to models",
            "Assign models to accounts",
            "Initiate rebalancing",
            "Submit trade orders",
            "Handle usage questions",
            "Troubleshoot technical issues",
            "Bug fixes and enhancements"
        ],
        "Client": ["○", "", "", "", "●", "", "●", "●", "●", "●", "●", "●", "", "", ""],
        "Apex RM/Sales": ["●", "●", "●", "", "", "○", "", "", "", "", "", "", "", "", ""],
        "Apex Onboarding": ["○", "●", "●", "●", "●", "●", "", "", "", "", "", "", "", "", ""],
        "Client Services": ["", "", "", "", "○", "○", "", "", "", "", "", "", "●", "●", ""],
        "Engineering/PM": ["", "", "", "", "", "", "", "", "", "", "", "", "○", "●", "●"]
    }

    # Create dataframe and filter by selected roles
    import pandas as pd
    df = pd.DataFrame(matrix_data)

    # Filter columns: always show Activity + selected roles
    if role_filter:
        columns_to_show = ["Activity"] + role_filter
        filtered_df = df[columns_to_show]
    else:
        filtered_df = df[["Activity"]]  # Show only Activity if nothing selected

    # Style the dataframe with better colors
    def style_matrix(val):
        if val == "●":
            return f'color: {APEX_COLORS["blue"]}; font-weight: bold; font-size: 20px;'
        elif val == "○":
            return f'color: {APEX_COLORS["sky_blue"]}; font-weight: bold; font-size: 20px;'
        else:
            return f'color: {APEX_COLORS["charcoal"]};'

    def style_activity(val):
        # Apply gradient to Activity column text
        return f'background: linear-gradient(135deg, {APEX_COLORS["amethyst"]}, {APEX_COLORS["amethyst_pink"]}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'

    styled_df = filtered_df.style.map(style_matrix).apply(
        lambda x: [style_activity(v) for v in x], subset=['Activity']
    ).set_properties(**{
        'text-align': 'center'
    }, subset=filtered_df.columns[1:])  # Center all columns except Activity

    # Display filtered table
    st.dataframe(styled_df, use_container_width=True, hide_index=True)

    st.markdown("**Legend:** ● = Primary Owner | ○ = Supporting Role")

    st.markdown("---")

    # Phase breakdown
    st.markdown("### Breakdown by Phase")

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Pre-Sales", "🚀 Onboarding", "⚡ Ongoing Usage", "🛟 Support"])

    with tab1:
        st.markdown(f"<div style='background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['bright_blue']} 100%); padding: 10px 25px; border-radius: 12px;'><h4 style='color: white; margin: 0; font-size: 17px;'>📊 Pre-Sales & Discovery</h4></div>", unsafe_allow_html=True)
        st.markdown("- **Apex RM/Sales (Primary):** Identify prospects, present value proposition")
        st.markdown("- **Apex Onboarding (Primary):** Present value, validate migration status")
        st.markdown("- **Client (Supporting):** Provide requirements, evaluate fit")

    with tab2:
        st.markdown(f"<div style='background: linear-gradient(135deg, {APEX_COLORS['green']} 0%, {APEX_COLORS['sky_blue']} 100%); padding: 10px 25px; border-radius: 12px;'><h4 style='color: white; margin: 0; font-size: 17px;'>🚀 Onboarding</h4></div>", unsafe_allow_html=True)
        st.markdown("- **Apex Onboarding (Primary):** Enable in Client Configurator, configure permissions, provide training")
        st.markdown("- **Client (Primary):** Identify which users need subscribe permissions")
        st.markdown("- **Client Services (Supporting):** Assist with configuration if needed")

    with tab3:
        st.markdown(f"<div style='background: linear-gradient(135deg, {APEX_COLORS['sky_blue']} 0%, {APEX_COLORS['bright_blue']} 100%); padding: 10px 25px; border-radius: 12px;'><h4 style='color: white; margin: 0; font-size: 17px;'>⚡ Ongoing Usage</h4></div>", unsafe_allow_html=True)
        st.markdown("**Client (Primary):** All day-to-day activities:")
        st.markdown("- Accept T&Cs")
        st.markdown("- Browse and evaluate models")
        st.markdown("- Subscribe to models")
        st.markdown("- Assign models to accounts")
        st.markdown("- Initiate rebalancing")
        st.markdown("- Submit trade orders")

    with tab4:
        st.markdown(f"<div style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%); padding: 10px 25px; border-radius: 12px;'><h4 style='color: white; margin: 0; font-size: 17px;'>🛟 Support</h4></div>", unsafe_allow_html=True)
        st.markdown("- **Client Services (Primary):** Handle usage questions, troubleshoot issues")
        st.markdown("- **Engineering/PM (Primary):** Troubleshoot technical issues, bug fixes, enhancements")
        st.markdown("- **Engineering/PM (Supporting):** Support on usage questions when technical")

elif section == "🏢 Model Providers":
    st.title("🏢 Model Provider Information")

    st.markdown("### Current Providers")

    # Provider selection
    provider = st.selectbox(
        "Select a provider to learn more:",
        ["Overview", "Aptis", "Franklin Templeton", "Timco and Sachs", "State Street"]
    )

    if provider == "Overview":
        st.plotly_chart(create_provider_status_chart(), use_container_width=True)

        st.markdown("---")

        st.markdown("### Provider Onboarding Process")

        # Custom CSS for expander headers with gradient text
        st.markdown(f"""
        <style>
            div[data-testid="stExpander"] details summary p {{
                background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-weight: 600;
            }}
        </style>
        """, unsafe_allow_html=True)

        timeline_steps = [
            ("1. Sourcing & Outreach", "Identify potential providers, initial discussions, validate credibility"),
            ("2. Legal & Compliance", "Contract negotiation, T&C review, compliance approval ⚠️ BOTTLENECK: No dedicated resource"),
            ("3. Technical Integration", "Holdings data submission, SFTP setup (e.g., Franklin Templeton daily feeds)"),
            ("4. Testing & Validation", "UAT environment testing, data accuracy verification"),
            ("5. Go-Live", "Upload to production, internal announcement to sales team")
        ]

        for step, desc in timeline_steps:
            with st.expander(step):
                st.markdown(desc)

        st.info("**Current Contact:** Rich or Larry (Business Development)")

    elif provider == "Franklin Templeton":
        st.markdown("### Franklin Templeton")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
            <div class='provider-card' style='text-align: left;'>
                <div class='provider-name'>Franklin Templeton</div>
                <span class='status-live'>LIVE</span>
                <hr>
                <p><strong>Integration Type:</strong> SFTP</p>
                <p><strong>Update Frequency:</strong> Daily</p>
                <p><strong>Data Feed:</strong> ETF performance reporting</p>
                <p><strong>UAT Status:</strong> Completed</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("**Contact Information:**")
            st.markdown("""
            - **Primary Contact:** Jennifer Zmarzly
            - **Email:** Jennifer.Zmarzly@franklintempleton.com
            - **SFTP Directory:** apex-part-frtn-prod-reporting
            """)

        st.success("✅ **Status:** Live in production with daily data feeds")

    elif provider == "State Street":
        st.markdown("### State Street")

        st.markdown(f"""
        <div class='provider-card' style='text-align: left;'>
            <div class='provider-name'>State Street</div>
            <span class='status-pending'>COMING SOON</span>
            <hr>
            <p><strong>Status:</strong> Awaiting holdings data</p>
            <p><strong>Timeline:</strong> TBD</p>
        </div>
        """, unsafe_allow_html=True)

        st.info("📋 **Next Steps:** Waiting for State Street to submit model holdings data for upload to production")

    else:  # Aptis or Timco and Sachs
        st.markdown(f"### {provider}")

        st.markdown(f"""
        <div class='provider-card' style='text-align: left;'>
            <div class='provider-name'>{provider}</div>
            <span class='status-live'>LIVE</span>
            <hr>
            <p><strong>Status:</strong> Live in production</p>
            <p><strong>Models Available:</strong> Multiple investment strategies</p>
        </div>
        """, unsafe_allow_html=True)

        st.success(f"✅ **{provider}** models are live and available to all Rebalancer clients")

elif section == "💰 Revenue Model":
    st.title("💰 Revenue Model & Pricing Strategy")

    st.markdown("### Current State (2026)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['green']} 0%, {APEX_COLORS['sky_blue']} 100%);
                    padding: 30px; border-radius: 10px; text-align: center; color: white;'>
            <div style='font-size: 48px; font-weight: bold;'>3 BPS</div>
            <div style='font-size: 18px; margin-top: 10px; font-weight: 600;'>Rebalancer Fee</div>
            <div style='font-size: 15px; opacity: 0.9;'>+ $0.20/account/month</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['bright_blue']} 100%);
                    padding: 30px; border-radius: 10px; text-align: center; color: white;'>
            <div style='font-size: 40px; font-weight: bold;'>Varies</div>
            <div style='font-size: 18px; margin-top: 10px; font-weight: 600;'>Direct Indexing</div>
            <div style='font-size: 15px; opacity: 0.9;'>3-6 BPS additional</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {APEX_COLORS['navy']} 0%, {APEX_COLORS['charcoal']} 100%);
                    padding: 30px; border-radius: 10px; text-align: center; color: white;'>
            <div style='font-size: 48px; font-weight: bold;'>Indirect</div>
            <div style='font-size: 18px; margin-top: 10px; font-weight: 600;'>Revenue Source</div>
            <div style='font-size: 15px; opacity: 0.9;'>Custody + Rebalancer fees</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Future State Recommendations")

    # Custom CSS for tab gradient text - apply to all tabs
    st.markdown(f"""
    <style>
        button[data-baseweb="tab"] div {{
            background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            font-weight: 600 !important;
        }}
        button[data-baseweb="tab"][aria-selected="true"] div {{
            font-weight: 700 !important;
        }}
    </style>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Option A: Charge Providers", "Option B: Tiered Pricing", "Option C: Hybrid Model"])

    with tab1:
        st.markdown("#### Option A: Charge Model Providers")

        st.success("✅ **Recommended Approach**")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Approach:**")
            st.markdown("""
            - Marketplace listing fees
            - Distribution platform value
            - Based on Etsy/Facebook model
            - Charge per model or flat monthly fee
            """)

        with col2:
            st.markdown("**Rationale:**")
            st.markdown("""
            - ✅ Once adoption grows, providers gain value
            - ✅ Access to 41 firms, 33,080 accounts
            - ✅ Automated distribution
            - ✅ Standard marketplace model
            """)

        st.info("**Timeline:** Implement Q4 2026+ once marketplace adoption is proven")

    with tab2:
        st.markdown("#### Option B: Tiered Client Pricing")

        st.warning("⚠️ **Challenge:** Limited current adoption")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Tiers:**")
            st.markdown("""
            - **Free Tier:** Limited provider access
            - **Premium Tier:** Full catalog
            - **Enterprise Tier:** Custom solutions
            """)

        with col2:
            st.markdown("**Challenges:**")
            st.markdown("""
            - ❌ May slow adoption
            - ❌ Complex to implement
            - ❌ Client pushback expected
            """)

    with tab3:
        st.markdown("#### Option C: Hybrid Model")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Structure:**")
            st.markdown("""
            - Free for clients
            - Revenue share with providers on AUM
            - Platform fees for premium providers
            - Performance-based pricing
            """)

        with col2:
            st.markdown("**Considerations:**")
            st.markdown("""
            - Complex to implement
            - Requires AUM tracking
            - Alignment of incentives
            - Future consideration
            """)

elif section == "📢 Marketing Strategy":
    st.title("📢 Client Communication & Marketing Strategy")

    st.markdown("### Target Audience Priority")

    # Priority table with gradient styling
    st.markdown(f"""
    <table style='width: 100%; border-collapse: collapse; margin: 20px 0;'>
        <thead>
            <tr style='background: {APEX_COLORS['navy']}; color: white;'>
                <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>Priority</th>
                <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>Audience</th>
                <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>Size</th>
                <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>Rationale</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style='padding: 12px; border: 1px solid #ddd;'>🥇 1</td>
                <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                    Existing Rebalancer Clients on Ascend
                </td>
                <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                    41 firms
                </td>
                <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                    Already using platform, easiest adoption
                </td>
            </tr>
            <tr style='background: #f9f9f9;'>
                <td style='padding: 12px; border: 1px solid #ddd;'>🥈 2</td>
                <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                    Classic Clients Post-Migration
                </td>
                <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                    TBD
                </td>
                <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                    Will have Rebalancer access after conversion
                </td>
            </tr>
            <tr>
                <td style='padding: 12px; border: 1px solid #ddd;'>🥉 3</td>
                <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                    New Rebalancer Prospects
                </td>
                <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                    Market
                </td>
                <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                    Model Marketplace as differentiator
                </td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Key Messaging")

    messaging_type = st.radio("Select audience:", ["For Advisors", "For Firms", "For Model Providers"], horizontal=True)

    if messaging_type == "For Advisors":
        st.markdown(f"""
        <div style='background-color: #E3F2FD; padding: 20px; border-radius: 10px;'>
        <h4 style='color: {APEX_COLORS['blue']};'>Messaging for Advisors</h4>
        <ul>
            <li>Access institutional-quality models from Franklin Templeton, Aptis, Timco and Sachs, and State Street</li>
            <li><strong>Models automatically update</strong> when providers rebalance—no manual intervention</li>
            <li>Reduce time on portfolio construction by 70%</li>
            <li>Seamlessly integrates with existing Rebalancer workflow</li>
            <li>Combine marketplace + proprietary strategies</li>
            <li>Full tax-loss harvesting and optimization</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    elif messaging_type == "For Firms":
        st.markdown(f"""
        <div style='background-color: #E8F5E9; padding: 20px; border-radius: 10px;'>
        <h4 style='color: {APEX_COLORS['green']};'>Messaging for Firms</h4>
        <ul>
            <li>Launch managed portfolios without hiring investment team</li>
            <li>Scale to thousands of accounts with automated updates</li>
            <li><strong>Competitive pricing</strong> - 3 BPS + $0.20/account/month</li>
            <li>Compete with larger firms using institutional models</li>
            <li>Choose from multiple providers</li>
            <li>Maintain compliance with automatic updates</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    else:  # For Model Providers
        st.markdown(f"""
        <div style='background-color: #F3E5F5; padding: 20px; border-radius: 10px;'>
        <h4 style='color: {APEX_COLORS['purple']};'>Messaging for Model Providers</h4>
        <ul>
            <li><strong>Distribution reach:</strong> 41 RIA firms managing 33,080 accounts</li>
            <li><strong>Automated platform:</strong> Upload once, updates propagate automatically</li>
            <li><strong>Growing ecosystem:</strong> Reach Apex's digital advisors and wealth managers</li>
            <li><strong>Partnership opportunity</strong> with premier fintech custody platform</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Communication Channels")

    # Custom HTML for expanders with gradient text (excluding emojis)
    st.markdown(f"""
    <style>
        .custom-expander {{
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            margin-bottom: 10px;
            padding: 15px;
            background-color: white;
        }}
        .custom-expander summary {{
            cursor: pointer;
            font-weight: 600;
            font-size: 16px;
            list-style: none;
        }}
        .custom-expander summary::-webkit-details-marker {{
            display: none;
        }}
        .gradient-text {{
            background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['navy']} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .custom-expander ul {{
            margin-top: 10px;
            padding-left: 20px;
        }}
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <details class="custom-expander">
            <summary>📧 <span class="gradient-text">1. Direct Outreach</span></summary>
            <ul>
                <li>RM/Sales team → existing Rebalancer clients</li>
                <li>Email campaign highlighting providers</li>
                <li>One-on-one demos</li>
                <li>Personalized value propositions</li>
            </ul>
        </details>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <details class="custom-expander">
            <summary>📚 <span class="gradient-text">2. Documentation & Resources</span></summary>
            <ul>
                <li>Developer portal documentation</li>
                <li>This framework document</li>
                <li>Video tutorials (recommended)</li>
                <li>Provider fact sheets</li>
            </ul>
        </details>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <details class="custom-expander">
            <summary>📰 <span class="gradient-text">3. Press Release</span></summary>
            <ul>
                <li>Announce Model Marketplace availability</li>
                <li>Highlight provider partnerships</li>
                <li>Include client testimonials</li>
                <li>Coordinate with marketing team</li>
            </ul>
        </details>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <details class="custom-expander">
            <summary>🎓 <span class="gradient-text">4. Internal Enablement</span></summary>
            <ul>
                <li>Sales team training</li>
                <li>RM playbook for conversations</li>
                <li>FAQ document for objections</li>
                <li>Demo environment access</li>
            </ul>
        </details>
        """, unsafe_allow_html=True)

elif section == "💼 Use Cases":
    st.title("💼 Client Use Cases & Value Stories")

    # Large custom heading for use case selection
    st.markdown(f"""
    <h3 style='color: {APEX_COLORS['navy']}; font-size: 24px; margin-bottom: 10px; margin-top: 20px;'>
        📋 Select a use case scenario:
    </h3>
    """, unsafe_allow_html=True)

    use_case = st.selectbox(
        "Choose scenario:",
        [
            "RIA Scaling Portfolio Management",
            "Digital Advisor Launching New Product",
            "Existing Client Enhancing Offering",
            "Sub-Advisory Relationship (Provider View)"
        ],
        label_visibility="collapsed"
    )

    if use_case == "RIA Scaling Portfolio Management":
        st.markdown("### 🏢 Use Case 1: RIA Scaling Portfolio Management")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(0,102,204,0.1) 0%, rgba(59,130,246,0.1) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['blue']}; margin-bottom: 15px;'>
                <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0; font-size: 18px;'>👤 Client Profile</h4>
                <p style='margin: 0;'>Mid-sized RIA with 500 client accounts, limited in-house investment research team</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(251,191,36,0.1) 0%, rgba(245,158,11,0.1) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['gold']}; margin-bottom: 15px;'>
                <h4 style='color: {APEX_COLORS['gold']}; margin-top: 0; font-size: 18px;'>⚡ Challenge</h4>
                <p style='margin: 0;'>Advisors spend 15+ hours weekly constructing and maintaining custom portfolios, limiting client acquisition capacity</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.05) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['amethyst']}; margin-bottom: 15px;'>
                <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                           -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                           margin-top: 0; font-size: 18px; font-weight: 700;'>💡 Solution with Model Marketplace</h4>
                <ol style='margin: 5px 0 0 0; padding-left: 20px;'>
                    <li>Subscribe to Franklin Templeton and Aptis ETF models aligned with firm's investment philosophy</li>
                    <li>Create goal-based frameworks using marketplace models (conservative, balanced, growth)</li>
                    <li>Assign models to client segments based on risk tolerance</li>
                    <li>Rebalancer generates trade proposals automatically as markets drift</li>
                    <li>Marketplace models receive automatic provider updates</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("**Results:**")
            st.metric("Time Savings", "70%", delta="Construction time reduction")
            st.metric("Scalability", "1000+", delta="accounts without new staff")

            st.success("✅ Consistent investment quality across all accounts")
            st.success("✅ Tax-loss harvesting built-in")

    elif use_case == "Digital Advisor Launching New Product":
        st.markdown("### 📱 Use Case 2: Digital Advisor Launching New Product")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(0,102,204,0.1) 0%, rgba(59,130,246,0.1) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['blue']}; margin-bottom: 15px;'>
                <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0; font-size: 18px;'>👤 Client Profile</h4>
                <p style='margin: 0;'>Digital investment platform adding managed portfolios to self-directed offering</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(251,191,36,0.1) 0%, rgba(245,158,11,0.1) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['gold']}; margin-bottom: 15px;'>
                <h4 style='color: {APEX_COLORS['gold']}; margin-top: 0; font-size: 18px;'>⚡ Challenge</h4>
                <p style='margin: 0;'>Need institutional-quality models quickly without building in-house model management team</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.05) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['amethyst']}; margin-bottom: 15px;'>
                <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                           -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                           margin-top: 0; font-size: 18px; font-weight: 700;'>💡 Solution with Model Marketplace</h4>
                <ol style='margin: 5px 0 0 0; padding-left: 20px;'>
                    <li>Subscribe to multiple provider models across risk spectrums</li>
                    <li>White-label models as platform investment strategies</li>
                    <li>Use Rebalancer API to automate account rebalancing</li>
                    <li>Leverage direct indexing for tax-optimized versions</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("**Results:**")
            st.metric("Launch Time", "Weeks", delta="vs. months")
            st.metric("Scale", "33,080", delta="accounts supported")

            st.success("✅ Professional-grade models")
            st.success("✅ Tax optimization features")

    elif use_case == "Existing Client Enhancing Offering":
        st.markdown("### 💼 Use Case 3: Existing Rebalancer Client Enhancing Offering")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(0,102,204,0.1) 0%, rgba(59,130,246,0.1) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['blue']}; margin-bottom: 15px;'>
                <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0; font-size: 18px;'>👤 Client Profile</h4>
                <p style='margin: 0;'>Wealth management firm already using Apex Rebalancer with custom models</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(251,191,36,0.1) 0%, rgba(245,158,11,0.1) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['gold']}; margin-bottom: 15px;'>
                <h4 style='color: {APEX_COLORS['gold']}; margin-top: 0; font-size: 18px;'>⚡ Challenge</h4>
                <p style='margin: 0;'>Clients requesting access to specific institutional strategies (thematic ETFs, ESG models)</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.05) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['amethyst']}; margin-bottom: 15px;'>
                <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                           -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                           margin-top: 0; font-size: 18px; font-weight: 700;'>💡 Solution with Model Marketplace</h4>
                <ol style='margin: 5px 0 0 0; padding-left: 20px;'>
                    <li>Subscribe to complementary marketplace models alongside existing custom models</li>
                    <li>Create blended goals using both custom and marketplace models</li>
                    <li>Offer clients choice between proprietary and third-party strategies</li>
                    <li>Use asset class management to optimize across all models</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("**Results:**")

            st.success("✅ Expanded investment menu")
            st.success("✅ No research overhead")
            st.success("✅ Client retention")
            st.success("✅ Competitive advantage")

    else:  # Sub-Advisory
        st.markdown("### 🏦 Use Case 4: Sub-Advisory Relationship (Provider Perspective)")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(0,102,204,0.1) 0%, rgba(59,130,246,0.1) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['blue']}; margin-bottom: 15px;'>
                <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0; font-size: 18px;'>👤 Provider Profile</h4>
                <p style='margin: 0;'>Large asset manager (like Voya Investment Management) distributing models to advisor network</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(251,191,36,0.1) 0%, rgba(245,158,11,0.1) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['gold']}; margin-bottom: 15px;'>
                <h4 style='color: {APEX_COLORS['gold']}; margin-top: 0; font-size: 18px;'>⚡ Challenge</h4>
                <p style='margin: 0;'>Need scalable distribution platform for model portfolios to reach more advisors</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.05) 100%);
                        padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['amethyst']}; margin-bottom: 15px;'>
                <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                           -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                           margin-top: 0; font-size: 18px; font-weight: 700;'>💡 Solution with Model Marketplace</h4>
                <ol style='margin: 5px 0 0 0; padding-left: 20px;'>
                    <li>Partner with Apex as Model Marketplace provider</li>
                    <li>Upload model portfolios to marketplace</li>
                    <li>Apex advisors subscribe and implement across client accounts</li>
                    <li>Provider updates models as market conditions change</li>
                    <li>Automatic propagation to all subscribed accounts</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("**Results:**")
            st.metric("Distribution", "41", delta="RIA firms")
            st.metric("Accounts", "33,080", delta="potential reach")

            st.success("✅ Automated updates")
            st.success("✅ Reduced operational burden")
            st.success("✅ Usage analytics")

elif section == "🔧 Rebalancer Integration":
    st.title("🔧 Rebalancer Capabilities & Integration")

    # Overview section
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(0,102,204,0.05) 0%, rgba(0,32,96,0.05) 100%);
                padding: 25px; border-radius: 12px; margin-bottom: 25px; border-left: 5px solid {APEX_COLORS['blue']};'>
        <h3 style='color: {APEX_COLORS['navy']}; margin-top: 0; font-size: 20px; font-weight: 600;'>What is Apex Rebalancer?</h3>
        <p style='color: {APEX_COLORS['charcoal']}; font-size: 15px; line-height: 1.6; margin-bottom: 15px;'>
            Rebalancing is the process of adjusting a portfolio's asset allocations to align with levels advisors
            specify in an investment plan. Apex's Rebalancer allows advisors to manage portfolios based on asset types,
            expected returns, and risk levels.
        </p>
        <div style='background: white; padding: 18px; border-radius: 8px; border-left: 4px solid {APEX_COLORS['amethyst']};'>
            <p style='margin: 0; font-size: 14px; color: {APEX_COLORS['charcoal']};'>
                <strong style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                               font-size: 15px;'>🔗 Model Marketplace Integration:</strong><br>
                Subscribed models from the marketplace become available in Rebalancer for portfolio construction, rebalancing proposals, and ongoing management.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Features Section Header
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 24px; margin-bottom: 20px;'>
        🎯 Key Rebalancer Features
    </h3>
    """, unsafe_allow_html=True)

    # Gradient styling for expanders
    st.markdown(f"""
    <style>
        .rebalancer-expander div[data-testid="stExpander"] details summary p {{
            background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['navy']} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
            font-size: 15px;
        }}
    </style>
    <div class="rebalancer-expander">
    """, unsafe_allow_html=True)

    features = [
        ("⚙️ 1. Firm-Level Settings", "Minimum trade size constraints, trade-off preferences (drift vs. tax), tax-loss harvesting configuration, organization API keys"),
        ("📊 2. Asset Class Management", "Create asset class trees, map securities to classes, REQUIRED for Model Marketplace, categorize equities, fixed income, commodities"),
        ("🎯 3. Models, Frameworks & Goals", "Custom models (in-house), Model Marketplace subscribed models, goal-based investing automation, direct indexing"),
        ("📏 4. Threshold Management", "Asset class thresholds, securities thresholds, model target cash & mandatory cash, absolute & relative difference percentages"),
        ("👥 5. Client & Investor Settings", "Security restrictions (add/lift), wash sale restrictions, optimization preferences, minimum cash settings, account quarantine"),
        ("📈 6. Direct Indexing", "Replicate index fund performance, own individual securities outright, portfolio customization & exclusions, tax-loss harvesting optimization"),
        ("💼 7. Trade Management", "Generate proposals from SOD files, review and submit trades, trade blotter analysis, historical trade exploration"),
        ("⭐ 8. Advanced Features", "Completion portfolios, cash generation via min cash, position liquidation, compliance monitoring")
    ]

    col1, col2 = st.columns(2)

    for idx, (title, description) in enumerate(features):
        with col1 if idx % 2 == 0 else col2:
            with st.expander(title):
                st.markdown(description)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature Deep Dive Section
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 24px; margin-top: 40px; margin-bottom: 20px;'>
        🔍 Feature Deep Dive
    </h3>
    """, unsafe_allow_html=True)

    selected_feature = st.selectbox(
        "Select a feature to learn more:",
        ["Asset Class Management", "Tax-Loss Harvesting", "Direct Indexing", "Threshold Management", "Trade Management"]
    )

    if selected_feature == "Asset Class Management":
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(251,191,36,0.15) 0%, rgba(245,158,11,0.1) 100%);
                    padding: 25px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['gold']}; margin-top: 20px;'>
            <h4 style='color: {APEX_COLORS['gold']}; margin-top: 0; font-size: 20px;'>⚠️ CRITICAL for Model Marketplace</h4>
            <p style='margin: 0; font-size: 15px;'>All securities in Model Marketplace models must be mapped to appropriate asset classes for proper Rebalancer functioning.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown(f"""
            <div style='background: white; padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['light_gray']}; height: 100%;'>
                <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0;'>📋 How it works</h4>
                <ol style='line-height: 1.8;'>
                    <li>Create asset class tree (e.g., Equities → US Equities → Large Cap)</li>
                    <li>Map each security to appropriate class</li>
                    <li>Example: SPDR Gold Trust (GLD) → Commodity asset class</li>
                    <li>Enables optimization across asset types</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(0,102,204,0.05) 0%, rgba(0,32,96,0.05) 100%);
                        padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['blue']}; height: 100%;'>
                <h4 style='color: {APEX_COLORS['navy']}; margin-top: 0;'>✨ Benefits</h4>
                <ul style='line-height: 1.8;'>
                    <li>Proper portfolio optimization</li>
                    <li>Accurate rebalancing proposals</li>
                    <li>Asset allocation tracking</li>
                    <li>Compliance with investment policies</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif selected_feature == "Tax-Loss Harvesting":
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(40,167,69,0.1) 0%, rgba(40,167,69,0.05) 100%);
                    padding: 25px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['green']}; margin-top: 20px;'>
            <h4 style='color: {APEX_COLORS['green']}; margin-top: 0; font-size: 20px;'>💰 Tax-Loss Harvesting</h4>
            <p style='margin: 0; font-size: 15px;'><strong>Purpose:</strong> Sell securities at a loss to offset capital gains, improving after-tax returns</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown(f"""
            <div style='background: white; padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['light_gray']}; height: 100%;'>
                <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0;'>⚙️ How it works</h4>
                <ul style='line-height: 1.8;'>
                    <li>Configure at firm or client level</li>
                    <li>Rebalancer identifies loss opportunities</li>
                    <li>Proposes replacement securities</li>
                    <li>Manages wash sale restrictions (30-day rule)</li>
                    <li>Maintains portfolio allocation targets</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(40,167,69,0.05) 0%, rgba(40,167,69,0.02) 100%);
                        padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['green']}; height: 100%;'>
                <h4 style='color: {APEX_COLORS['green']}; margin-top: 0;'>✅ Benefits</h4>
                <ul style='line-height: 1.8;'>
                    <li>Improved after-tax returns</li>
                    <li>Automated identification of opportunities</li>
                    <li>Compliance with IRS wash sale rules</li>
                    <li>Enhanced client value proposition</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif selected_feature == "Direct Indexing":
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(128,44,192,0.1) 0%, rgba(236,0,117,0.05) 100%);
                    padding: 25px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['amethyst']}; margin-top: 20px;'>
            <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                       margin-top: 0; font-size: 20px; font-weight: 600;'>📈 Direct Indexing</h4>
            <p style='margin: 0; font-size: 15px;'><strong>Purpose:</strong> Own individual securities instead of index funds for tax optimization and customization</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown(f"""
            <div style='background: white; padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['light_gray']}; height: 100%;'>
                <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0;'>⚙️ How it works</h4>
                <ul style='line-height: 1.8;'>
                    <li>Replicate index fund performance with individual securities</li>
                    <li>Own stocks directly instead of ETFs</li>
                    <li>Customize holdings (exclude specific companies/sectors)</li>
                    <li>Harvest tax losses on individual positions</li>
                    <li>Standard (3 BPS) or Custom (6 BPS) options</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.02) 100%);
                        padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['amethyst']}; height: 100%;'>
                <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                           -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                           margin-top: 0; font-weight: 600;'>✅ Benefits</h4>
                <ul style='line-height: 1.8;'>
                    <li>Superior tax-loss harvesting opportunities</li>
                    <li>Portfolio personalization & exclusions</li>
                    <li>No ETF expense ratios</li>
                    <li>Track index performance with customization</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif selected_feature == "Threshold Management":
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(0,102,204,0.1) 0%, rgba(59,130,246,0.05) 100%);
                    padding: 25px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['blue']}; margin-top: 20px;'>
            <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0; font-size: 20px;'>📏 Threshold Management</h4>
            <p style='margin: 0; font-size: 15px;'><strong>Purpose:</strong> Control when rebalancing occurs by setting drift tolerances</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown(f"""
            <div style='background: white; padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['light_gray']}; height: 100%;'>
                <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0;'>⚙️ How it works</h4>
                <ul style='line-height: 1.8;'>
                    <li>Set asset class thresholds (e.g., ±5% drift tolerance)</li>
                    <li>Set individual security thresholds</li>
                    <li>Configure model target cash levels</li>
                    <li>Define mandatory cash requirements</li>
                    <li>Use absolute or relative percentage differences</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(0,102,204,0.05) 0%, rgba(59,130,246,0.02) 100%);
                        padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['blue']}; height: 100%;'>
                <h4 style='color: {APEX_COLORS['navy']}; margin-top: 0;'>✅ Benefits</h4>
                <ul style='line-height: 1.8;'>
                    <li>Reduce unnecessary trading</li>
                    <li>Balance drift vs. transaction costs</li>
                    <li>Maintain portfolio discipline</li>
                    <li>Customize per client risk tolerance</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif selected_feature == "Trade Management":
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(0,32,96,0.1) 0%, rgba(0,102,204,0.05) 100%);
                    padding: 25px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['navy']}; margin-top: 20px;'>
            <h4 style='color: {APEX_COLORS['navy']}; margin-top: 0; font-size: 20px;'>💼 Trade Management</h4>
            <p style='margin: 0; font-size: 15px;'><strong>Purpose:</strong> Generate, review, and execute rebalancing trades</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown(f"""
            <div style='background: white; padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['light_gray']}; height: 100%;'>
                <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0;'>⚙️ How it works</h4>
                <ul style='line-height: 1.8;'>
                    <li>Generate proposals from SOD (Start of Day) files</li>
                    <li>Review proposed trades for accuracy</li>
                    <li>Accept proposals to move to Accepted Proposals tab</li>
                    <li>Submit trades to execution</li>
                    <li>View trade blotter to track executed trades (status, fill quantity, fill price)</li>
                    <li>Analyze trades by individual account or basket view</li>
                    <li>Review historical trade data for compliance and reporting</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(0,32,96,0.05) 0%, rgba(0,102,204,0.02) 100%);
                        padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['navy']}; height: 100%;'>
                <h4 style='color: {APEX_COLORS['navy']}; margin-top: 0;'>✅ Benefits</h4>
                <ul style='line-height: 1.8;'>
                    <li>Streamlined rebalancing workflow</li>
                    <li>Review before execution</li>
                    <li>Compliance disclosures built-in</li>
                    <li>Trade history tracking</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

elif section == "📝 Onboarding Checklist":
    st.title("📝 Client Onboarding Checklist")

    st.markdown("### Track Your Onboarding Progress")

    # Gradient styling for expander titles
    st.markdown(f"""
    <style>
        div[data-testid="stExpander"] details summary p {{
            background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
            font-size: 16px;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Interactive checklist with session state
    if 'checklist' not in st.session_state:
        st.session_state.checklist = {
            'pre_onboarding': [False] * 4,
            'technical_setup': [False] * 3,
            'client_enablement': [False] * 4,
            'first_use': [False] * 13,
            'go_live': [False] * 3
        }

    # Pre-Onboarding
    with st.expander("📋 Pre-Onboarding", expanded=True):
        st.session_state.checklist['pre_onboarding'][0] = st.checkbox("Confirm client is Rebalancer customer", st.session_state.checklist['pre_onboarding'][0])
        st.session_state.checklist['pre_onboarding'][1] = st.checkbox("Confirm client is on Ascend (not Classic)", st.session_state.checklist['pre_onboarding'][1])
        st.session_state.checklist['pre_onboarding'][2] = st.checkbox("If mid-migration, confirm client acceptance of partial rebalancing", st.session_state.checklist['pre_onboarding'][2])
        st.session_state.checklist['pre_onboarding'][3] = st.checkbox("Identify which users need subscribe permissions", st.session_state.checklist['pre_onboarding'][3])

        progress = sum(st.session_state.checklist['pre_onboarding']) / len(st.session_state.checklist['pre_onboarding'])
        st.progress(progress)
        st.caption(f"Pre-Onboarding: {int(progress * 100)}% complete")

    # Technical Setup
    with st.expander("⚙️ Technical Setup"):
        st.session_state.checklist['technical_setup'][0] = st.checkbox("Onboarding team enables Model Marketplace in Client Configurator", st.session_state.checklist['technical_setup'][0])
        st.session_state.checklist['technical_setup'][1] = st.checkbox("Configure subscribe permissions for authorized users", st.session_state.checklist['technical_setup'][1])
        st.session_state.checklist['technical_setup'][2] = st.checkbox("Validate access in Ascend environment", st.session_state.checklist['technical_setup'][2])

        progress = sum(st.session_state.checklist['technical_setup']) / len(st.session_state.checklist['technical_setup'])
        st.progress(progress)
        st.caption(f"Technical Setup: {int(progress * 100)}% complete")

    # Client Enablement
    with st.expander("📚 Client Enablement"):
        st.session_state.checklist['client_enablement'][0] = st.checkbox("Share Model Marketplace documentation", st.session_state.checklist['client_enablement'][0])
        st.session_state.checklist['client_enablement'][1] = st.checkbox("Provide this framework document", st.session_state.checklist['client_enablement'][1])
        st.session_state.checklist['client_enablement'][2] = st.checkbox("Schedule walkthrough/demo (if needed)", st.session_state.checklist['client_enablement'][2])
        st.session_state.checklist['client_enablement'][3] = st.checkbox("Share provider fact sheets", st.session_state.checklist['client_enablement'][3])

        progress = sum(st.session_state.checklist['client_enablement']) / len(st.session_state.checklist['client_enablement'])
        st.progress(progress)
        st.caption(f"Client Enablement: {int(progress * 100)}% complete")

    # First Use
    with st.expander("🚀 First Use"):
        items = [
            "Client accepts Apex T&Cs (User Agreement)",
            "Client browses available models",
            "Client reviews model details (holdings, weights, summary, resources)",
            "Client subscribes to first model",
            "Accept provider-specific T&Cs",
            "Verify status changes to SUBSCRIBED",
            "🔴 CRITICAL: Verify each security assigned to correct asset class",
            "Create goals using subscribed model",
            "Assign model to fund goals in test account",
            "Configure thresholds and optimization preferences",
            "Execute test rebalance",
            "Review trade proposals",
            "Submit trade orders"
        ]

        for i, item in enumerate(items):
            st.session_state.checklist['first_use'][i] = st.checkbox(item, st.session_state.checklist['first_use'][i])

        progress = sum(st.session_state.checklist['first_use']) / len(st.session_state.checklist['first_use'])
        st.progress(progress)
        st.caption(f"First Use: {int(progress * 100)}% complete")

    # Go-Live
    with st.expander("✅ Go-Live"):
        st.session_state.checklist['go_live'][0] = st.checkbox("Roll out to additional users/accounts", st.session_state.checklist['go_live'][0])
        st.session_state.checklist['go_live'][1] = st.checkbox("Monitor for issues in first 30 days", st.session_state.checklist['go_live'][1])
        st.session_state.checklist['go_live'][2] = st.checkbox("Collect feedback for improvements", st.session_state.checklist['go_live'][2])

        progress = sum(st.session_state.checklist['go_live']) / len(st.session_state.checklist['go_live'])
        st.progress(progress)
        st.caption(f"Go-Live: {int(progress * 100)}% complete")

    # Overall Progress
    st.markdown("---")
    st.markdown("### Overall Progress")

    total_items = sum(len(v) for v in st.session_state.checklist.values())
    completed_items = sum(sum(v) for v in st.session_state.checklist.values())
    overall_progress = completed_items / total_items

    st.progress(overall_progress)
    st.markdown(f"**{completed_items} of {total_items} items complete ({int(overall_progress * 100)}%)**")

    if overall_progress == 1.0:
        st.balloons()
        st.success("🎉 Congratulations! Onboarding complete!")

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
        ("What if we're still on Classic?", "Model Marketplace is Ascend-only. Let's discuss your Ascend migration timeline and prioritize Model Marketplace access post-migration."),
        ("We're not Rebalancer clients. Can we still use Model Marketplace?", "No, Model Marketplace requires Rebalancer subscription. Let's explore if Rebalancer is right for your firm first."),
        ("Do we have to pay for Model Marketplace?", "Rebalancer fees apply: 3 BPS of AUM assigned to rebalancing goals (billed monthly) + $0.20 per funded account per month. Direct indexing features have additional fees. Contact your RM for detailed pricing."),
        ("Can we customize the models after subscribing?", "Subscribed models from providers cannot be edited, but you can create custom models in Rebalancer and use marketplace models as a starting point/reference."),
        ("How often are models updated?", "Providers update their models on their own schedule. Franklin Templeton provides daily performance reporting. Model composition updates vary by provider."),
        ("Does Apex automatically rebalance our accounts?", "Not currently. You must manually initiate rebalancing or call our API."),
        ("What if we want a specific provider added?", "Contact your RM. We're actively seeking new provider partnerships (current bottleneck: no dedicated BD resource)."),
        ("Are there regulatory/compliance concerns?", "Each provider has their own T&Cs that clients accept. Apex provides disclosure language on all trade orders. Clients maintain full responsibility for trade execution."),
        ("What happens if a model provider leaves the marketplace?", "You would be notified in advance. Already-assigned accounts would continue with the last known model composition, but new subscriptions would not be available."),
        ("What happens if I unsubscribe from a model?", "Unsubscribing stops automatic updates from the provider, but your portfolios continue using the last subscribed weights. To fully discontinue, you must delete the model from Rebalancer. Your T&C acceptance is retained for future re-subscription."),
        ("Do I need to configure anything after subscribing?", "Yes, two critical steps: (1) Verify each security in the model is assigned to the correct asset class in Rebalancer for optimal performance, and (2) Create goals and assign the model to fund those goals in your client accounts."),
        ("What if I have issues or questions?", "Open an Apex Service Center ticket and navigate to the Rebalancer category. Provide as much detail as possible about your issue. Support is handled by Park (primary) with engineering escalation available."),
        ("What Rebalancer features work with Model Marketplace models?", "All standard Rebalancer features apply: firm settings, thresholds, tax-loss harvesting, optimization between drift reduction and tax sensitivity, direct indexing, asset class management, and trade blotter analysis.")
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

elif section == "📈 Success Metrics":
    st.title("📈 Success Metrics & KPIs")

    # Adoption Journey Chart
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 22px; margin-bottom: 15px;'>
        📊 Adoption Journey
    </h3>
    """, unsafe_allow_html=True)

    # Custom gradient bar chart
    import streamlit.components.v1 as components

    html_content = f"""
    <div style='background: white; padding: 20px; border-radius: 12px;'>
        <h4 style='color: {APEX_COLORS['navy']}; margin-top: 0; margin-bottom: 25px; font-size: 20px;'>Adoption Journey (Target 2026)</h4>

        <div style='margin-bottom: 20px;'>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;'>
                <span style='font-weight: 600; color: {APEX_COLORS['charcoal']}; font-size: 14px;'>Total Rebalancer Clients</span>
                <span style='font-weight: 700; color: {APEX_COLORS['navy']}; font-size: 16px;'>41</span>
            </div>
            <div style='background: #E0E0E0; border-radius: 8px; height: 35px; position: relative; overflow: hidden;'>
                <div style='background: linear-gradient(90deg, {APEX_COLORS['navy']} 0%, {APEX_COLORS['blue']} 100%); height: 100%; width: 7.6%; border-radius: 8px; display: flex; align-items: center; justify-content: flex-start; padding-left: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);'></div>
            </div>
        </div>

        <div style='margin-bottom: 20px;'>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;'>
                <span style='font-weight: 600; color: {APEX_COLORS['charcoal']}; font-size: 14px;'>MM Enabled</span>
                <span style='font-weight: 700; color: {APEX_COLORS['navy']}; font-size: 16px;'>30</span>
            </div>
            <div style='background: #E0E0E0; border-radius: 8px; height: 35px; position: relative; overflow: hidden;'>
                <div style='background: linear-gradient(90deg, {APEX_COLORS['bright_blue']} 0%, {APEX_COLORS['sky_blue']} 100%); height: 100%; width: 6%; border-radius: 8px; display: flex; align-items: center; justify-content: flex-start; padding-left: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);'></div>
            </div>
        </div>

        <div style='margin-bottom: 20px;'>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;'>
                <span style='font-weight: 600; color: {APEX_COLORS['charcoal']}; font-size: 14px;'>Users with Subscribe</span>
                <span style='font-weight: 700; color: {APEX_COLORS['navy']}; font-size: 16px;'>100</span>
            </div>
            <div style='background: #E0E0E0; border-radius: 8px; height: 35px; position: relative; overflow: hidden;'>
                <div style='background: linear-gradient(90deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['bright_blue']} 100%); height: 100%; width: 20%; border-radius: 8px; display: flex; align-items: center; justify-content: flex-start; padding-left: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);'></div>
            </div>
        </div>

        <div style='margin-bottom: 20px;'>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;'>
                <span style='font-weight: 600; color: {APEX_COLORS['charcoal']}; font-size: 14px;'>Active Subscriptions</span>
                <span style='font-weight: 700; color: {APEX_COLORS['navy']}; font-size: 16px;'>500</span>
            </div>
            <div style='background: #E0E0E0; border-radius: 8px; height: 35px; position: relative; overflow: hidden;'>
                <div style='background: linear-gradient(90deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%); height: 100%; width: 100%; border-radius: 8px; display: flex; align-items: center; justify-content: flex-start; padding-left: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);'></div>
            </div>
        </div>
    </div>
    """

    components.html(html_content, height=400)

    st.markdown("<br>", unsafe_allow_html=True)

    # Gradient styling for tabs
    st.markdown(f"""
    <style>
        button[data-baseweb="tab"] div {{
            background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['navy']} 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            font-weight: 600 !important;
            font-size: 15px !important;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Metrics categories in tabs
    tab1, tab2, tab3 = st.tabs(["📊 Adoption Metrics", "📈 Usage Metrics", "💼 Business Impact"])

    with tab1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(0,102,204,0.05) 0%, rgba(0,32,96,0.03) 100%);
                    padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['blue']}; margin-bottom: 20px;'>
            <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0;'>Adoption Metrics</h4>
            <p style='color: {APEX_COLORS['charcoal']}; margin: 0; font-size: 14px;'>Track how clients are discovering and adopting Model Marketplace</p>
        </div>

        <table style='width: 100%; border-collapse: collapse; margin: 20px 0;'>
            <thead>
                <tr style='background: {APEX_COLORS['navy']}; color: white;'>
                    <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>Metric</th>
                    <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>Description</th>
                    <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>Target (2026)</th>
                </tr>
            </thead>
            <tbody>
                <tr style='background: white;'>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['navy']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Correspondents with Model Marketplace enabled
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; color: {APEX_COLORS['charcoal']};'>
                        Number of firms with access configured
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        30+
                    </td>
                </tr>
                <tr style='background: #f9f9f9;'>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['navy']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Users with subscribe permissions
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; color: {APEX_COLORS['charcoal']};'>
                        Authorized users who can subscribe to models
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        100+
                    </td>
                </tr>
                <tr style='background: white;'>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['navy']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Active model subscriptions
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; color: {APEX_COLORS['charcoal']};'>
                        Total number of model subscriptions across all clients
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        500+
                    </td>
                </tr>
                <tr style='background: #f9f9f9;'>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['navy']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Accounts utilizing marketplace models
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; color: {APEX_COLORS['charcoal']};'>
                        Client accounts with marketplace model assignments
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        10,000+
                    </td>
                </tr>
                <tr style='background: white;'>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['navy']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Subscription conversion rate
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; color: {APEX_COLORS['charcoal']};'>
                        Browsers → subscribers conversion
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        40%
                    </td>
                </tr>
            </tbody>
        </table>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(40,167,69,0.05) 0%, rgba(40,167,69,0.03) 100%);
                    padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['green']}; margin-bottom: 20px;'>
            <h4 style='color: {APEX_COLORS['green']}; margin-top: 0;'>Usage Metrics</h4>
            <p style='color: {APEX_COLORS['charcoal']}; margin: 0; font-size: 14px;'>Measure active engagement and product stickiness</p>
        </div>

        <table style='width: 100%; border-collapse: collapse; margin: 20px 0;'>
            <thead>
                <tr style='background: {APEX_COLORS['navy']}; color: white;'>
                    <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>Metric</th>
                    <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>Description</th>
                    <th style='padding: 12px; text-align: left; border: 1px solid #ddd;'>Insight</th>
                </tr>
            </thead>
            <tbody>
                <tr style='background: white;'>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['green']} 0%, {APEX_COLORS['blue']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Models subscribed per client (average)
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; color: {APEX_COLORS['charcoal']};'>
                        Average number of models each client subscribes to
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Product stickiness
                    </td>
                </tr>
                <tr style='background: #f9f9f9;'>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['green']} 0%, {APEX_COLORS['blue']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Most popular providers
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; color: {APEX_COLORS['charcoal']};'>
                        Provider ranking by subscription count
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Provider value to users
                    </td>
                </tr>
                <tr style='background: white;'>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['green']} 0%, {APEX_COLORS['blue']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Most popular models
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; color: {APEX_COLORS['charcoal']};'>
                        Top 10 models by adoption
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Strategy preferences
                    </td>
                </tr>
                <tr style='background: #f9f9f9;'>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['green']} 0%, {APEX_COLORS['blue']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Rebalance frequency using marketplace models
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; color: {APEX_COLORS['charcoal']};'>
                        How often clients rebalance with marketplace models
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Active usage
                    </td>
                </tr>
                <tr style='background: white;'>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['green']} 0%, {APEX_COLORS['blue']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        AUM in marketplace-model-based accounts
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; color: {APEX_COLORS['charcoal']};'>
                        Total assets under management using marketplace models
                    </td>
                    <td style='padding: 12px; border: 1px solid #ddd; background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 600;'>
                        Business impact
                    </td>
                </tr>
            </tbody>
        </table>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(128,44,192,0.05) 0%, rgba(236,0,117,0.03) 100%);
                    padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['amethyst']}; margin-bottom: 20px;'>
            <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                       margin-top: 0; font-weight: 600;'>Business Impact</h4>
            <p style='color: {APEX_COLORS['charcoal']}; margin: 0; font-size: 14px;'>Quantify the value created by Model Marketplace</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(0,102,204,0.08) 0%, rgba(0,32,96,0.05) 100%);
                        padding: 25px; border-radius: 12px; border: 2px solid {APEX_COLORS['blue']}; margin-bottom: 20px;'>
                <h5 style='color: {APEX_COLORS['blue']}; margin-top: 0; font-size: 16px;'>💰 Incremental AUM</h5>
                <div style='font-size: 14px; color: {APEX_COLORS['charcoal']}; margin-top: 10px;'>Track AUM growth from Model Marketplace adoption</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(40,167,69,0.08) 0%, rgba(40,167,69,0.05) 100%);
                        padding: 25px; border-radius: 12px; border: 2px solid {APEX_COLORS['green']};'>
                <h5 style='color: {APEX_COLORS['green']}; margin-top: 0; font-size: 16px;'>⚡ Time-to-Value</h5>
                <div style='font-size: 14px; color: {APEX_COLORS['charcoal']}; margin-top: 10px;'>Reduce onboarding time for new clients</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(128,44,192,0.08) 0%, rgba(236,0,117,0.05) 100%);
                        padding: 25px; border-radius: 12px; border: 2px solid {APEX_COLORS['amethyst']}; margin-bottom: 20px;'>
                <h5 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                           -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                           margin-top: 0; font-size: 16px; font-weight: 600;'>🔄 Client Retention</h5>
                <div style='font-size: 14px; color: {APEX_COLORS['charcoal']}; margin-top: 10px;'>Compare retention across cohorts</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(251,191,36,0.08) 0%, rgba(245,158,11,0.05) 100%);
                        padding: 25px; border-radius: 12px; border: 2px solid {APEX_COLORS['gold']};'>
                <h5 style='color: {APEX_COLORS['gold']}; margin-top: 0; font-size: 16px;'>⭐ NPS Score</h5>
                <div style='font-size: 14px; color: {APEX_COLORS['charcoal']}; margin-top: 10px;'>Measure user satisfaction for marketplace</div>
            </div>
            """, unsafe_allow_html=True)

elif section == "🗺️ Roadmap":
    st.title("🗺️ Roadmap & Future Enhancements")

    # Timeline visual with custom HTML
    st.markdown(f"""
    <h3 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
               font-weight: 700; font-size: 22px; margin-bottom: 20px; margin-top: 20px;'>
        📅 Product Roadmap Timeline
    </h3>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, rgba(0,102,204,0.1) 0%, rgba(0,32,96,0.1) 100%);
                    border-radius: 12px; border: 2px solid {APEX_COLORS['blue']};'>
            <div style='font-size: 18px; font-weight: 700; color: {APEX_COLORS['blue']}; margin-bottom: 10px;'>Q2 2026</div>
            <div style='font-size: 14px; color: {APEX_COLORS['charcoal']};'>Marketing Launch & Press Release</div>
            <div style='margin-top: 15px; padding: 8px; background: {APEX_COLORS['green']}; color: white; border-radius: 20px; font-size: 12px; font-weight: 600;'>
                ✅ IN PROGRESS
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, {APEX_COLORS['navy']} 0%, {APEX_COLORS['blue']} 100%);
                    border-radius: 12px; border: 2px solid {APEX_COLORS['navy']};'>
            <div style='font-size: 18px; font-weight: 700; color: white; margin-bottom: 10px;'>Coming Soon</div>
            <div style='font-size: 14px; color: white;'>Enhanced Model Analytics & Performance Tracking</div>
            <div style='margin-top: 15px; padding: 8px; background: rgba(255,255,255,0.2); color: white; border-radius: 20px; font-size: 12px; font-weight: 600;'>
                🚀 PLANNED
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, rgba(112,48,160,0.1) 0%, rgba(112,48,160,0.05) 100%);
                    border-radius: 12px; border: 2px solid {APEX_COLORS['purple']};'>
            <div style='font-size: 18px; font-weight: 700; color: {APEX_COLORS['purple']}; margin-bottom: 10px;'>Q4 2026+</div>
            <div style='font-size: 14px; color: {APEX_COLORS['charcoal']};'>Revenue Model & Provider Expansion</div>
            <div style='margin-top: 15px; padding: 8px; background: {APEX_COLORS['gray']}; color: white; border-radius: 20px; font-size: 12px; font-weight: 600;'>
                💡 FUTURE
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Gradient styling for tabs
    st.markdown(f"""
    <style>
        button[data-baseweb="tab"] div {{
            background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            font-weight: 600 !important;
            font-size: 15px !important;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Detailed roadmap tabs
    tab1, tab2, tab3 = st.tabs(["📅 Current Focus", "🚀 Coming Soon", "💡 Future Vision"])

    with tab1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(40,167,69,0.1) 0%, rgba(40,167,69,0.05) 100%);
                    padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['green']}; margin-bottom: 25px;'>
            <h3 style='color: {APEX_COLORS['green']}; margin-top: 0;'>Q2 2026 - Current Focus</h3>
            <div style='padding: 8px 16px; background: {APEX_COLORS['green']}; color: white; border-radius: 20px; font-size: 14px; font-weight: 600; display: inline-block;'>
                ✅ Status: In Progress
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
            <div style='background: white; padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['light_gray']}; margin-bottom: 15px;'>
                <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0; font-size: 16px;'>👥 Client Acquisition</h4>
                <ul style='margin: 0; padding-left: 20px;'>
                    <li>Onboard Titan</li>
                    <li>Onboard Range Finance</li>
                    <li>Other new Rebalancer clients</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: white; padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['light_gray']};'>
                <h4 style='color: {APEX_COLORS['blue']}; margin-top: 0; font-size: 16px;'>🏢 Provider Expansion</h4>
                <ul style='margin: 0; padding-left: 20px;'>
                    <li>Add State Street models (pending holdings data)</li>
                    <li>Stabilize current functionality</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(128,44,192,0.08) 0%, rgba(236,0,117,0.04) 100%);
                        padding: 20px; border-radius: 10px; border: 2px solid {APEX_COLORS['amethyst']};'>
                <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                           -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                           margin-top: 0; font-size: 16px; font-weight: 600;'>🎯 Marketing & Launch</h4>
                <ul style='margin: 0; padding-left: 20px;'>
                    <li><strong>Marketing launch</strong></li>
                    <li><strong>Press release</strong></li>
                    <li>Sales enablement</li>
                    <li>Client outreach campaign</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(0,32,96,0.1) 0%, rgba(0,102,204,0.05) 100%);
                    padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['navy']}; margin-bottom: 25px;'>
            <h3 style='background: linear-gradient(135deg, {APEX_COLORS['navy']} 0%, {APEX_COLORS['blue']} 100%);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                       margin-top: 0; font-weight: 600;'>Coming Soon - Planned Enhancements</h3>
            <div style='padding: 8px 16px; background: linear-gradient(135deg, {APEX_COLORS['navy']} 0%, {APEX_COLORS['blue']} 100%); color: white; border-radius: 20px; font-size: 14px; font-weight: 600; display: inline-block;'>
                🚀 Priority: High
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(128,44,192,0.1) 0%, rgba(236,0,117,0.05) 100%);
                    padding: 25px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['amethyst']}; margin-bottom: 20px;'>
            <h4 style='background: linear-gradient(135deg, {APEX_COLORS['amethyst']} 0%, {APEX_COLORS['amethyst_pink']} 100%);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
                       margin-top: 0; font-size: 18px; font-weight: 700;'>🎯 Top Priority: Enhanced Model Analytics & Performance Tracking</h4>
        </div>
        """, unsafe_allow_html=True)

        # Gradient styling for expanders
        st.markdown(f"""
        <style>
            div[data-testid="stExpander"] details summary p {{
                background: linear-gradient(135deg, {APEX_COLORS['blue']} 0%, {APEX_COLORS['navy']} 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-weight: 600;
                font-size: 15px;
            }}
        </style>
        """, unsafe_allow_html=True)

        with st.expander("📋 Details on Enhanced Analytics", expanded=True):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"""
                <h5 style='color: {APEX_COLORS['blue']};'>✨ Capabilities</h5>
                <ul>
                    <li>Model performance tracking and comparisons</li>
                    <li>Historical performance data visualization</li>
                    <li>Drift analysis and monitoring dashboards</li>
                </ul>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <h5 style='color: {APEX_COLORS['green']};'>✅ Benefits</h5>
                <ul>
                    <li>Data-driven model selection</li>
                    <li>Better client reporting capabilities</li>
                    <li>Performance benchmarking across providers</li>
                    <li>Enhanced due diligence tools</li>
                </ul>
                """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(251,191,36,0.1) 0%, rgba(245,158,11,0.05) 100%);
                        padding: 15px; border-radius: 8px; margin-top: 15px; border-left: 4px solid {APEX_COLORS['gold']};'>
                <strong style='color: {APEX_COLORS['gold']};'>💡 What's Coming:</strong><br>
                Advanced analytics to help advisors make informed model selection decisions
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <h4 style='color: {APEX_COLORS['navy']}; margin-top: 30px;'>📌 Other Planned Initiatives</h4>
        <ul>
            <li>Enhanced provider onboarding process</li>
            <li>Dedicated BD resource for provider acquisition</li>
            <li>Provider relationship management improvements</li>
        </ul>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(112,48,160,0.1) 0%, rgba(112,48,160,0.05) 100%);
                    padding: 20px; border-radius: 12px; border-left: 5px solid {APEX_COLORS['purple']}; margin-bottom: 25px;'>
            <h3 style='color: {APEX_COLORS['purple']}; margin-top: 0;'>Future Vision</h3>
            <div style='padding: 8px 16px; background: {APEX_COLORS['purple']}; color: white; border-radius: 20px; font-size: 14px; font-weight: 600; display: inline-block;'>
                💡 Future
            </div>
        </div>
        """, unsafe_allow_html=True)

        initiatives = [
            ("💰 Revenue Model Implementation", "Provider fees based on marketplace adoption"),
            ("📊 Expanded Provider Catalog", "Target: 10+ providers across asset classes"),
            ("📈 Model Performance Analytics Dashboard", "Compare provider performance, track AUM"),
            ("🔍 Advanced Filtering and Search", "Filter by asset class, strategy, performance"),
            ("⚖️ Model Comparison Tools", "Side-by-side comparison of holdings, weights, performance")
        ]

        for title, desc in initiatives:
            with st.expander(title):
                st.markdown(desc)

elif section == "📞 Contact Directory":
    st.title("📞 Contact Directory")

    st.markdown("### Support Process")

    st.markdown(f"""
    <div style='background-color: #E3F2FD; padding: 20px; border-radius: 10px;'>
    <h4>How to Get Support:</h4>
    <ol>
        <li><strong>Open Apex Service Center ticket</strong></li>
        <li><strong>Category:</strong> Select "Rebalancer"</li>
        <li><strong>Provide detailed information:</strong>
            <ul>
                <li>Description of issue</li>
                <li>Steps to reproduce</li>
                <li>Expected vs. actual behavior</li>
                <li>Screenshots if applicable</li>
            </ul>
        </li>
        <li><strong>Support Flow:</strong> Park (Primary) → Engineering Escalation (as needed)</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Documentation Resources")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Official Documentation:**")
        st.markdown("""
        - 📚 Apex Support Portal: support.apexfintechsolutions.com
        - 🔧 Developer Portal
        - 📋 This Framework Document
        """)

    with col2:
        st.markdown("**Additional Resources:**")
        st.markdown("""
        - Provider fact sheets
        - Video tutorials (coming soon)
        - FAQ documents
        - Training materials
        """)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: {APEX_COLORS['gray']}; padding: 20px;'>
    <p><strong>Document Version:</strong> 1.1 | <strong>Last Updated:</strong> March 24, 2026</p>
    <p><strong>Owner:</strong> Product Marketing / Business Development</p>
    <p><strong>Review Cycle:</strong> Quarterly or as material changes occur</p>
    <p style='margin-top: 20px; font-style: italic;'>This framework is intended for internal Apex use and approved client/prospect sharing.<br>
    Not for public distribution without Marketing approval.</p>
</div>
""", unsafe_allow_html=True)
