import streamlit as st
import numpy as np
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import requests
import json

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Agriculture System",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
def load_css():
    st.markdown("""
    <style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    # .stApp {
    #     background-image: url("");
    #     background-size: cover;
    #     background-position: center;
    #     background-attachment: fixed;
    # }
                
#     .stApp {
#     background-image: url("background.jpg");
#     background-size: cover;
#     background-repeat: no-repeat;
#     background-position: center;
#     background-attachment: fixed;
# }
    
    /* Custom card styling */
    .custom-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin: 1rem 0;
    }
    
    /* Gradient text */
    .gradient-text {
        background: linear-gradient(45deg, #f3ec78, #af4261);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        color: white;
        text-align: center;
        transition: transform 0.3s;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    /* Animated button */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
    
    /* Input field styling */
    .stNumberInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 0.5rem;
    }
    
    /* Success message styling */
    .stSuccess {
        background: linear-gradient(45deg, #84fab0 0%, #8fd3f4 100%);
        padding: 1rem;
        border-radius: 10px;
        color: #1a1a1a;
        font-weight: 600;
    }
    .footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: rgba(0,0,0,0.7);
    color: white;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------- LOAD MODEL AND DATA ----------------
@st.cache_resource
def load_model():
    return pickle.load(open("RandomForest.pkl", "rb"))

@st.cache_data
def load_data():
    fertilizer_df = pd.read_csv("Data/fertilizer.csv")
    # Sample crop data for demonstration
    crop_data = pd.DataFrame({
        'Crop': ['Rice', 'Wheat', 'Maize', 'Cotton', 'Sugarcane', 'Groundnuts'],
        'N': [80, 120, 100, 150, 70, 40],
        'P': [40, 60, 50, 80, 35, 20],
        'K': [40, 50, 50, 70, 40, 30],
        'Temperature': [25, 22, 24, 28, 30, 27],
        'Humidity': [80, 65, 70, 60, 75, 70],
        'pH': [6.5, 7.0, 6.8, 7.2, 6.3, 6.0],
        'Rainfall': [150, 80, 100, 70, 180, 90]
    })
    return fertilizer_df, crop_data

# ---------------- FERTILIZER DICTIONARY ----------------
fertilizer_dic = {
    "Nlow": "🌱 Add Nitrogen fertilizer like Urea or Ammonium Nitrate.",
    "NHigh": "⚠️ Nitrogen is high. Consider reducing Nitrogen fertilizer or planting nitrogen-fixing cover crops.",
    "Plow": "🌿 Add Phosphorus fertilizer like DAP or Superphosphate.",
    "PHigh": "⚠️ Phosphorus is high. Avoid adding more Phosphorus; consider crops with lower P requirements.",
    "Klow": "🍂 Add Potassium fertilizer like MOP or Potash.",
    "KHigh": "⚠️ Potassium is high. Reduce Potassium application and monitor soil levels."
}

# ---------------- 3D VISUALIZATION FUNCTIONS ----------------
def create_3d_scatter(data):
    fig = go.Figure(data=[go.Scatter3d(
        x=data['N'],
        y=data['P'],
        z=data['K'],
        mode='markers+text',
        marker=dict(
            size=12,
            color=data['Temperature'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Temperature")
        ),
        text=data['Crop'],
        textposition="top center"
    )])
    
    fig.update_layout(
        title="3D Nutrient Requirements by Crop",
        scene=dict(
            xaxis_title='Nitrogen (N)',
            yaxis_title='Phosphorus (P)',
            zaxis_title='Potassium (K)',
            bgcolor='rgba(0,0,0,0)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    return fig

def create_gauge_chart(value, title, min_val, max_val):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        title = {'text': title},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [min_val, max_val]},
            'bar': {'color': "#667eea"},
            'steps': [
                {'range': [min_val, max_val*0.3], 'color': "lightgray"},
                {'range': [max_val*0.3, max_val*0.7], 'color': "gray"},
                {'range': [max_val*0.7, max_val], 'color': "darkgray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': max_val*0.8
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white', 'size': 12}
    )
    return fig

# ---------------- LOAD ANIMATION ----------------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------------- MAIN APP ----------------
def main():
    load_css()
    
    # Load data
    crop_model = load_model()
    fertilizer_df, crop_data = load_data()
    
    # Sidebar with animation
    with st.sidebar:
        st.markdown("<h1 style='text-align: center; color: white;'>🌾 FarmAIQ</h1>", unsafe_allow_html=True)
        
        # Animated menu
        selected = option_menu(
            menu_title=None,
            options=["Dashboard", "Crop Recommendation", "Fertilizer Recommendation", "Weather & Insights"],
            icons=["house", "tree", "flower1", "cloud-sun"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "rgba(255,255,255,0.1)"},
                "icon": {"color": "white", "font-size": "20px"},
                "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "0px"},
                "nav-link-selected": {"background-color": "#667eea"},
            }
        )
        
        # Weather widget
        st.markdown("---")
        st.markdown("### 🌤️ Live Weather")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Temperature", "28°C", "2°C")
        with col2:
            st.metric("Humidity", "65%", "-5%")
    
    # Main content area
    if selected == "Dashboard":
        st.markdown("<h1 class='gradient-text'>Smart Agriculture AI Dashboard</h1>", unsafe_allow_html=True)
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("""
            <div class='metric-card'>
                <h3>🌾 Active Crops</h3>
                <h2>156</h2>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class='metric-card'>
                <h3>📊 Yield Forecast</h3>
                <h2>+12%</h2>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class='metric-card'>
                <h3>💧 Water Saved</h3>
                <h2>2.5M L</h2>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown("""
            <div class='metric-card'>
                <h3>🌍 CO2 Reduced</h3>
                <h2>1.2T</h2>
            </div>
            """, unsafe_allow_html=True)
        
        # 3D Visualization
        st.markdown("### 📊 3D Crop Analysis")
        fig = create_3d_scatter(crop_data)
        st.plotly_chart(fig, use_container_width=True)
        
        # Crop distribution
        col1, col2 = st.columns(2)
        with col1:
            fig_pie = px.pie(values=crop_data['N'], names=crop_data['Crop'], 
                           title="Nitrogen Distribution by Crop",
                           color_discrete_sequence=px.colors.sequential.Viridis)
            fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            fig_bar = px.bar(crop_data, x='Crop', y=['N', 'P', 'K'], 
                           title="Nutrient Requirements",
                           barmode='group',
                           color_discrete_sequence=['#667eea', '#764ba2', '#84fab0'])
            fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
            st.plotly_chart(fig_bar, use_container_width=True)
    
    elif selected == "Crop Recommendation":
        st.markdown("<h1 class='gradient-text'>🌱 AI Crop Recommendation</h1>", unsafe_allow_html=True)
        
        # Background image overlay
        col1, col2 = st.columns([1, 1])
        
        with col1:
            with st.container():
                st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
                st.markdown("### 🌿 Soil Parameters")
                
                N = st.slider("Nitrogen (N) - kg/ha", 0, 200, 50, help="Essential for leaf growth")
                P = st.slider("Phosphorus (P) - kg/ha", 0, 200, 50, help="Important for root development")
                K = st.slider("Potassium (K) - kg/ha", 0, 200, 50, help="Key for flowering and fruiting")
                temperature = st.slider("Temperature (°C)", 0, 50, 25)
                humidity = st.slider("Humidity (%)", 0, 100, 70)
                ph = st.slider("Soil pH", 0.0, 14.0, 7.0, 0.1)
                rainfall = st.slider("Rainfall (mm)", 0, 300, 100)
                
                if st.button("🔮 Predict Best Crop"):
                    with st.spinner("Analyzing soil conditions..."):
                        time.sleep(2)
                        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
                        prediction = crop_model.predict(data)[0]
                        
                        st.balloons()
                        st.success(f"✅ Recommended Crop: **{prediction.upper()}**")
                        
                        # Additional crop information
                        st.info(f"""
                        **Crop Details for {prediction}:**
                        - Optimal Growing Temperature: 20-30°C
                        - Water Requirement: Medium
                        - Growing Season: 90-120 days
                        - Expected Yield: 2-3 tons/acre
                        """)
                st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            # 3D Gauge Charts
            st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
            st.markdown("### 📊 Real-time Analysis")
            
            col_a, col_b = st.columns(2)
            with col_a:
                fig_n = create_gauge_chart(N, "Nitrogen Level", 0, 200)
                st.plotly_chart(fig_n, use_container_width=True)
            with col_b:
                fig_p = create_gauge_chart(P, "Phosphorus Level", 0, 200)
                st.plotly_chart(fig_p, use_container_width=True)
            
            col_c, col_d = st.columns(2)
            with col_c:
                fig_k = create_gauge_chart(K, "Potassium Level", 0, 200)
                st.plotly_chart(fig_k, use_container_width=True)
            with col_d:
                fig_temp = create_gauge_chart(temperature, "Temperature", 0, 50)
                st.plotly_chart(fig_temp, use_container_width=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    elif selected == "Fertilizer Recommendation":
        st.markdown("<h1 class='gradient-text'>🧪 Smart Fertilizer Advisor</h1>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            with st.container():
                st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
                st.markdown("### 🌾 Crop & Soil Analysis")
                
                crop_name = st.selectbox("Select Crop", options=crop_data['Crop'].tolist())
                N_current = st.number_input("Current Nitrogen Level (kg/ha)", 0, 200, 50)
                P_current = st.number_input("Current Phosphorus Level (kg/ha)", 0, 200, 50)
                K_current = st.number_input("Current Potassium Level (kg/ha)", 0, 200, 50)
                
                if st.button("💡 Get Fertilizer Advice"):
                    with st.spinner("Calculating nutrient requirements..."):
                        time.sleep(1.5)
                        
                        try:
                            # Get recommended values
                            crop_info = crop_data[crop_data['Crop'] == crop_name].iloc[0]
                            nr = crop_info['N']
                            pr = crop_info['P']
                            kr = crop_info['K']
                            
                            n_diff = nr - N_current
                            p_diff = pr - P_current
                            k_diff = kr - K_current
                            
                            # Create comparison chart
                            fig_compare = go.Figure(data=[
                                go.Bar(name='Current', x=['N', 'P', 'K'], y=[N_current, P_current, K_current], 
                                       marker_color='#667eea'),
                                go.Bar(name='Recommended', x=['N', 'P', 'K'], y=[nr, pr, kr], 
                                       marker_color='#84fab0')
                            ])
                            
                            fig_compare.update_layout(
                                title="Nutrient Comparison",
                                barmode='group',
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                font={'color': 'white'}
                            )
                            
                            st.plotly_chart(fig_compare, use_container_width=True)
                            
                            # Determine recommendation
                            diffs = {'N': n_diff, 'P': p_diff, 'K': k_diff}
                            max_diff_key = max(diffs, key=lambda x: abs(diffs[x]))
                            max_diff = diffs[max_diff_key]
                            
                            if max_diff_key == 'N':
                                key = "NHigh" if max_diff < 0 else "Nlow"
                            elif max_diff_key == 'P':
                                key = "PHigh" if max_diff < 0 else "Plow"
                            else:
                                key = "KHigh" if max_diff < 0 else "Klow"
                            
                            st.success(f"### 🌿 Recommendation")
                            st.info(fertilizer_dic[key])
                            
                            # Additional tips
                            st.markdown("""
                            **💡 Pro Tips:**
                            - Apply fertilizer in the evening for better absorption
                            - Water immediately after application
                            - Consider organic alternatives
                            """)
                            
                        except Exception as e:
                            st.error(f"❌ Error: {str(e)}")
                
                st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
            st.markdown("### 📈 Nutrient Deficiency Guide")
            
            # Create deficiency heatmap
            if 'crop_name' in locals():
                crop_info = crop_data[crop_data['Crop'] == crop_name].iloc[0]
                deficiency_matrix = pd.DataFrame({
                    'Nutrient': ['N', 'P', 'K'],
                    'Current': [N_current, P_current, K_current],
                    'Required': [crop_info['N'], crop_info['P'], crop_info['K']]
                })
                
                fig_heatmap = px.imshow([deficiency_matrix['Current'].values, 
                                        deficiency_matrix['Required'].values],
                                       x=['N', 'P', 'K'],
                                       y=['Current', 'Required'],
                                       color_continuous_scale='Viridis',
                                       title="Nutrient Deficiency Heatmap")
                
                fig_heatmap.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
                st.plotly_chart(fig_heatmap, use_container_width=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    elif selected == "Weather & Insights":
        st.markdown("<h1 class='gradient-text'>🌤️ Weather & Agricultural Insights</h1>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
            st.markdown("### 📊 7-Day Weather Forecast")
            
            # Sample weather data
            days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            temps = [28, 30, 27, 26, 29, 31, 28]
            rainfall = [10, 5, 20, 15, 0, 5, 10]
            
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            
            fig.add_trace(
                go.Scatter(x=days, y=temps, name="Temperature", line=dict(color='#ff6b6b', width=3)),
                secondary_y=False,
            )
            
            fig.add_trace(
                go.Bar(x=days, y=rainfall, name="Rainfall", marker_color='#4ecdc4'),
                secondary_y=True,
            )
            
            fig.update_layout(
                title="Temperature & Rainfall Forecast",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font={'color': 'white'}
            )
            
            fig.update_xaxes(title_text="Day")
            fig.update_yaxes(title_text="Temperature (°C)", secondary_y=False)
            fig.update_yaxes(title_text="Rainfall (mm)", secondary_y=True)
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
            st.markdown("### 💡 Smart Insights")
            
            insights = [
                "🌱 Best time to plant: Next 3 days",
                "💧 Irrigation needed: Low",
                "⚠️ Pest risk: Moderate",
                "📈 Market prices: Rising",
                "🌾 Harvest forecast: Good"
            ]
            
            for insight in insights:
                st.markdown(f"""
                <div style='background: rgba(102, 126, 234, 0.2); padding: 0.8rem; border-radius: 10px; margin: 0.5rem 0;'>
                    {insight}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
st.markdown("""
<div class="footer">
🌾 Smart Agriculture System | Developed with ❤️ using Streamlit By Codexshami | © 2026
</div>
""", unsafe_allow_html=True)
# ---------------- RUN APP ----------------
if __name__ == "__main__":
    main()