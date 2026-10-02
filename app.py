import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PromptIQ — AI-Augmented TPM Prototype",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Corporate Polish
st.markdown("""
<style>
    .metric-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px 18px;
        margin-bottom: 12px;
    }
    .disclaimer-banner {
        background-color: #fefce8;
        border: 1px solid #fef08a;
        color: #854d0e;
        padding: 10px 14px;
        border-radius: 6px;
        font-size: 0.88rem;
        margin-bottom: 16px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        background-color: #f1f5f9;
        border-radius: 6px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1e3a8a !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Mandatory Protection Banner
st.markdown(
    '<div class="disclaimer-banner">'
    '<strong>Notice for Evaluation:</strong> Illustrative synthetic dataset created for prototype demonstration; '
    'not Vantara actuals. Baseline financial parameters (₹374 Cr trade spend, ₹2,200 Cr revenue, KPI targets) '
    'match the submitted Round 2 case deliverables.'
    '</div>',
    unsafe_allow_html=True
)

st.title("PromptIQ — AI-Augmented TPM Operating Engine")
st.caption("A closed-loop, AI-augmented redesign of Vantara Consumer Products' trade promotion lifecycle")

# --- REFERENCE LOOKUP TABLES ---
ELASTICITY_MAP = {
    'Foods': 1.40,
    'Beverages': 1.55,
    'Home Care': 1.15,
    'Personal Care': 1.25,
    'Snacks': 1.50
}

MECHANIC_MULTIPLIERS = {
    'Price Discount': 1.00,
    'Volume Scheme': 1.15,
    'Bundle': 0.90,
    'Display + Discount': 1.45,
    'JBP Support': 1.25
}

COMPETITOR_INDEX_MAP = {
    'LOW (Index 95)': 95.0,
    'MEDIUM (Index 102)': 102.0,
    'HIGH (Index 108)': 108.0
}

# --- NAVIGATION TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Executive Control Tower",
    "2. Promotion Decision Simulator",
    "3. Trade Spend Leakage Recovery",
    "4. AI Viability Architecture",
    "5. Synthetic Data & Competitor Panel"
])

# TAB 1: EXECUTIVE CONTROL TOWER
with tab1:
    st.subheader("Vantara Commercial Baseline vs. PromptIQ Target State")
    col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
    col_kpi1.metric("Gross Turnover", "₹2,200 Cr", "General Trade: 70%")
    col_kpi2.metric("Trade Spend Pool", "₹374 Cr", "17.0% of Gross Revenue")
    col_kpi3.metric("Annual Value at Risk", "₹159 Cr", "Unmeasured & Leaking (~42%)")
    col_kpi4.metric("3-Yr Cumulative Net Benefit", "₹226 Cr", "Payback: 4–6 Months")
    st.markdown("---")
    
    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("#### Operational Bottlenecks: Round 2 Diagnostic")
        kpi_df = pd.DataFrame({
            "Lifecycle Area": ["Planning & Forecasting", "Process & Approval", "Execution & In-Flight", "Settlement & Claims", "Route-to-Market"],
            "Metric / KPI": ["Forecast MAPE (promoted SKUs)", "Approval Cycle Time", "Issue Detection Latency", "Trade Spend with Zero ROI", "Outlet Universe Staleness"],
            "Current State": ["40% – 70%", "3 – 4 weeks", "60% – 70% elapsed", "15% – 30%", "15% – 25%"],
            "PromptIQ Target": ["15% – 20%", "< 1 week", "< 20% elapsed", "< 10%", "< 5%"]
        })
        st.dataframe(kpi_df, hide_index=True, use_container_width=True)
        
    with col_right:
        st.markdown("#### Projected Net Value Realization (₹ Cr)")
        net_df = pd.DataFrame({
            "Milestone": ["Year 1 (Capex ₹9 Cr)", "Year 2", "Year 3", "3-Year Total"],
            "Net Benefit (₹ Cr)": [47.5, 78.0, 103.0, 226.0],
            "Primary Driver": ["Deductions Recovery & Leakage Stop", "Demand Forecast Tuning & Inventory Reduction", "Trade Mix Optimization & Dynamic Promotion Allocation", "Enterprise Scale & Closed-Loop Feedback"]
        })
        fig_bar = px.bar(
            net_df[:-1], x="Milestone", y="Net Benefit (₹ Cr)",
            text="Net Benefit (₹ Cr)", color_discrete_sequence=["#1e3a8a"]
        )
        fig_bar.update_traces(texttemplate='₹%{text:.1f} Cr', textposition='outside')
        fig_bar.update_layout(yaxis_range=[0, 125], height=310, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_bar, use_container_width=True)

# TAB 2: SIMULATOR
with tab2:
    st.subheader("Promotion Decision Simulator: Before (Manual) vs. After (PromptIQ)")
    with st.expander("Promotion Parameter Configuration", expanded=True):
        p_col1, p_col2, p_col3, p_col4 = st.columns(4)
        cat_select = p_col1.selectbox("Category", list(ELASTICITY_MAP.keys()), index=0)
        mech_select = p_col2.selectbox("Promotion Mechanic", list(MECHANIC_MULTIPLIERS.keys()), index=3)
        comp_select = p_col3.selectbox("Competitor Price Pressure", list(COMPETITOR_INDEX_MAP.keys()), index=1)
        discount_depth = p_col4.slider("Discount Depth (%)", 5, 30, 15)
        
        p2_col1, p2_col2, p2_col3, p2_col4 = st.columns(4)
        duration_weeks = p2_col1.slider("Duration (Weeks)", 1, 6, 2)
        baseline_weekly_units = p2_col2.number_input("Baseline Weekly Units", 5000, 100000, 25000, step=5000)
        unit_mrp = p2_col3.number_input("Unit Price (₹ MRP)", 20.0, 500.0, 120.0, step=10.0)
        unit_margin = p2_col4.slider("Unit Contribution Margin (%)", 15, 60, 35) / 100.0

    total_baseline_units = baseline_weekly_units * duration_weeks
    comp_index = COMPETITOR_INDEX_MAP[comp_select]
    trade_spend = total_baseline_units * unit_mrp * (discount_depth / 100.0) * 0.70
    
    before_uplift_pct = float(discount_depth)
    before_incremental_units = total_baseline_units * (before_uplift_pct / 100.0)
    before_gross_margin = before_incremental_units * unit_mrp * unit_margin
    before_roi = (before_gross_margin - trade_spend) / trade_spend
    
    cat_factor = ELASTICITY_MAP[cat_select]
    mech_factor = MECHANIC_MULTIPLIERS[mech_select]
    duration_days = duration_weeks * 7
    compliance_factor = 0.82 ** 1.2
    
    raw_after_uplift = (
        (discount_depth * cat_factor * mech_factor * compliance_factor)
        - ((comp_index - 100.0) * 0.45)
        - max(0.0, (duration_days - 14) * 0.15)
    )
    after_raw_uplift = max(2.0, raw_after_uplift)
    after_cannibalization = after_raw_uplift * 0.22
    after_halo = after_raw_uplift * 0.08
    after_net_uplift = after_raw_uplift - after_cannibalization + after_halo
    
    after_incremental_units = total_baseline_units * (after_net_uplift / 100.0)
    after_gross_margin = after_incremental_units * unit_mrp * unit_margin
    after_roi = (after_gross_margin - trade_spend) / trade_spend
    
    np.random.seed(42)
    sim_uplifts = np.random.normal(after_net_uplift, after_net_uplift * 0.18, 500)
    sim_uplifts = np.clip(sim_uplifts, 1.0, None)
    sim_inc_units = total_baseline_units * (sim_uplifts / 100.0)
    sim_margins = sim_inc_units * unit_mrp * unit_margin
    sim_rois = (sim_margins - trade_spend) / trade_spend
    
    p10_uplift, p50_uplift, p90_uplift = np.percentile(sim_uplifts, [10, 50, 90])
    p10_roi, p50_roi, p90_roi = np.percentile(sim_rois, [10, 50, 90])
    
    st.markdown("### Side-by-Side Model Comparison")
    b_col, a_col = st.columns(2)
    
    with b_col:
        st.error("BEFORE: Current Manual Approach (Static Analogy)")
        st.write(f"• **Baseline Volume:** {total_baseline_units:,.0f} units")
        st.write(f"• **Manual Uplift Estimate:** +{before_uplift_pct:.1f}%")
        st.write(f"• **Cannibalization / Halo:** Ignored (0.0% / 0.0%)")
        st.write(f"• **Incremental Volume:** {before_incremental_units:,.0f} units")
        st.write(f"• **Trade Spend Committed:** ₹{trade_spend / 1e5:.2f} Lakh")
        st.markdown(f"#### **Expected Realized ROI:** `{before_roi:.2f}x`")
        st.caption("Assumes linear 1:1 lift; ignores competitor price changes and portfolio cannibalization.")

    with a_col:
        st.success("AFTER: PromptIQ AI Engine (Multi-Variable Cross-Elasticity)")
        st.write(f"• **AI Modeled Raw Uplift:** +{after_raw_uplift:.1f}%")
        st.write(f"• **Cross-Effects:** -{after_cannibalization:.1f}% Cannibalization | +{after_halo:.1f}% Halo Basket Lift")
        st.write(f"• **Net Incremental Uplift:** +{after_net_uplift:.1f}%")
        st.write(f"• **Incremental Volume:** {after_incremental_units:,.0f} units")
        st.write(f"• **Trade Spend Committed:** ₹{trade_spend / 1e5:.2f} Lakh")
        st.markdown(f"#### **Expected ROI (P50 Median):** `{p50_roi:.2f}x`")
        st.caption("Accounts for category pricing elasticity, mechanic power, competitor pressure, and compliance.")

    st.markdown("---")
    st.markdown("### Monte Carlo Simulation (500 Stochastic Runs)")
    mc_c1, mc_c2 = st.columns([1, 2])
    with mc_c1:
        st.markdown("#### Confidence Risk Tiers")
        ci_table = pd.DataFrame({
            "Confidence Tier": ["P10 (Pessimistic / Downside)", "P50 (Median Expected)", "P90 (Optimistic / Upside)"],
            "Net Uplift": [f"+{p10_uplift:.1f}%", f"+{p50_uplift:.1f}%", f"+{p90_uplift:.1f}%"],
            "Realized ROI": [f"{p10_roi:.2f}x", f"{p50_roi:.2f}x", f"{p90_roi:.2f}x"]
        })
        st.dataframe(ci_table, hide_index=True, use_container_width=True)
        if p10_roi < 0:
            st.warning("⚠️️ **Risk Alert:** Downside P10 returns negative ROI. Require >85% display compliance or bundle mechanic before releasing budget.")
        else:
            st.success("🟢 **Commercial Greenlight:** Returns positive ROI across entire 80% confidence interval.")
            
    with mc_c2:
        fig_hist = px.histogram(
            sim_rois, nbins=35, labels={'value': 'Simulated Promotion ROI (x)'},
            title="Probabilistic Distribution of Commercial Return (P10 to P90)",
            color_discrete_sequence=['#16a34a']
        )
        fig_hist.add_vline(x=0.0, line_dash="dash", line_color="red", annotation_text="Break-even (0.0x)")
        fig_hist.add_vline(x=p50_roi, line_color="blue", annotation_text=f"P50: {p50_roi:.2f}x")
        fig_hist.update_layout(height=280, showlegend=False, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig_hist, use_container_width=True)

# TAB 3: LEAKAGE RECOVERY
with tab3:
    st.subheader("Trade Spend Leakage & Value-at-Risk Simulator")
    st.caption("Stress-test trade spend leakage against Vantara's ₹374 Cr budget pool.")
    sl_col1, sl_col2, sl_col3 = st.columns(3)
    no_roi_pct = sl_col1.slider("No-ROI Spend Ratio (%)", 15, 30, 22) / 100.0
    deduction_pct = sl_col2.slider("Unverified Deductions / Disputes (%)", 20, 40, 30) / 100.0
    stale_outlet_pct = sl_col3.slider("Stale / Inactive Outlet Universe (%)", 15, 25, 20) / 100.0
    
    base_spend = 374.0
    leak_no_roi = base_spend * no_roi_pct
    leak_deductions = (base_spend * 0.40) * deduction_pct
    leak_inventory = 18.0
    leak_stale_outlets = (base_spend * 0.15) * stale_outlet_pct
    total_var = leak_no_roi + leak_deductions + leak_inventory + leak_stale_outlets
    
    st.markdown("---")
    res_l, res_r = st.columns([1, 1])
    with res_l:
        st.metric("Total Annual Value at Risk", f"₹{total_var:.1f} Cr", f"{(total_var / base_spend) * 100:.1f}% of Total Trade Spend")
        leak_breakdown = pd.DataFrame({
            "Leakage Component": ["No-ROI Promotion Spend", "Unreconciled Claims / Deductions", "Forecast-Error Buffer Inventory", "Stale Outlet Coverage Waste"],
            "Current Exposure": [f"₹{leak_no_roi:.1f} Cr", f"₹{leak_deductions:.1f} Cr", f"₹{leak_inventory:.1f} Cr", f"₹{leak_stale_outlets:.1f} Cr"],
            "Submitted Target": ["Cut to <10% (Save ~₹46 Cr)", "OCR Auto-Audit (Save ~₹25 Cr)", "MAPE to 15%–20% (Save ~₹11 Cr)", "Geo-Clustering (Save ~₹7 Cr)"]
        })
        st.dataframe(leak_breakdown, hide_index=True, use_container_width=True)
    with res_r:
        wf_data = pd.DataFrame({
            "Stage": ["Total Spend Pool", "No-ROI Leak", "Deductions", "Inventory Holding", "Stale Outlets"],
            "Amount": [base_spend, -leak_no_roi, -leak_deductions, -leak_inventory, -leak_stale_outlets]
        })
        fig_wf = go.Figure(go.Waterfall(
            name="Leakage Sizing",
            orientation="v",
            measure=["relative", "relative", "relative", "relative", "relative"],
            x=wf_data["Stage"],
            textposition="outside",
            text=[f"₹{abs(v):.1f} Cr" for v in wf_data["Amount"]],
            y=wf_data["Amount"],
            connector={"line": {"color": "#64748b"}},
        ))
        fig_wf.update_layout(height=320, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_wf, use_container_width=True)

# TAB 4: ARCHITECTURE
with tab4:
    st.subheader("Algorithmic Pragmatism: The AI vs. Rules Decision Box")
    st.caption("Addressing executive panel rigor: Deploying ML where justified by high-dimensional data, and deterministic rules elsewhere.")
    matrix_data = [
        {
            "Lifecycle Area": "Promotion Forecasting & Lift",
            "Tool / Archetype": "Machine Learning (GBM)",
            "AI Justified?": "🟢 Yes (High dimensional; non-linear cross-elasticities; external competitor signals)",
            "Human Override": "Yes — Commercial Lead override before release"
        },
        {
            "Lifecycle Area": "Workflow & Budget Routing",
            "Tool / Archetype": "Deterministic Rules Engine",
            "AI Justified?": "🔴 No (Strict policy compliance; <₹5L auto-approved, >₹25L VP Finance review)",
            "Human Override": "Mandatory"
        },
        {
            "Lifecycle Area": "Deductions Reconciliation",
            "Tool / Archetype": "OCR + Fuzzy Two-Way Match",
            "AI Justified?": "🟡 Hybrid (OCR for document parsing; strict mathematical ledger matching)",
            "Human Override": "Exception queue for >5% claim mismatches"
        },
        {
            "Lifecycle Area": "In-Flight Compliance",
            "Tool / Archetype": "Computer Vision + SPC Anomaly",
            "AI Justified?": "🟢 Yes (Image classification on SFA display photos; z-score sell-out drift alerts)",
            "Human Override": "ASM dashboard alerts"
        }
    ]
    st.dataframe(pd.DataFrame(matrix_data), hide_index=True, use_container_width=True)

# TAB 5: SYNTHETIC DATA
with tab5:
    st.subheader("Synthetic Historical Promotions & Competitor Panel")
    st.caption("Sample extract of the 300+ promotion training history used to calibrate the uplift response models.")
    sample_df = pd.DataFrame([
        {"Promo ID": "PROMO_001", "Category": "Foods", "SKU": "FOOD_021", "Region": "Hyderabad", "Channel": "Quick Commerce", "Mechanic": "Display + Discount", "Discount": "20%", "Baseline": 58500, "Actual": 71671, "Uplift": "+22.5%", "Comp Index": 108},
        {"Promo ID": "PROMO_002", "Category": "Personal Care", "SKU": "PERS_026", "Region": "Kolkata", "Channel": "Modern Trade", "Mechanic": "JBP Support", "Discount": "15%", "Baseline": 69200, "Actual": 81359, "Uplift": "+17.6%", "Comp Index": 95},
        {"Promo ID": "PROMO_003", "Category": "Snacks", "SKU": "SNK_003", "Region": "Hyderabad", "Channel": "Modern Trade", "Mechanic": "Price Discount", "Discount": "30%", "Baseline": 69500, "Actual": 89738, "Uplift": "+29.1%", "Comp Index": 102},
        {"Promo ID": "PROMO_004", "Category": "Snacks", "SKU": "SNK_027", "Region": "Bengaluru", "Channel": "Quick Commerce", "Mechanic": "Volume Scheme", "Discount": "15%", "Baseline": 16500, "Actual": 20507, "Uplift": "+24.3%", "Comp Index": 102},
        {"Promo ID": "PROMO_005", "Category": "Foods", "SKU": "FOOD_023", "Region": "Chennai", "Channel": "Quick Commerce", "Mechanic": "Bundle", "Discount": "25%", "Baseline": 41200, "Actual": 49596, "Uplift": "+20.4%", "Comp Index": 95}
    ])
    st.dataframe(sample_df, hide_index=True, use_container_width=True)
    
    st.markdown("#### Competitor Price Benchmarking Panel")
    comp_df = pd.DataFrame({
        "SKU ID": ["SKU 01", "SKU 02", "SKU 03"],
        "Vantara Price": [100, 50, 120],
        "Competitor A": [98, 52, 115],
        "Competitor B": [105, 49, 125],
        "Competitor C": [102, 51, 119],
        "Market Benchmark (Avg)": [101.7, 50.7, 119.7],
        "Price Index": [98.4, 98.7, 100.3]
    })
    st.dataframe(comp_df, hide_index=True, use_container_width=True)
