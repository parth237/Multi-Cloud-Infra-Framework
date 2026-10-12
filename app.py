"""
Streamlit Web Dashboard for Multi-Cloud Infrastructure Optimization Framework.
Provides unified Grafana-style observability, SRE telemetry, health validation,
and visual multi-cloud topology with Terraform execution simulation.
"""
import time
import numpy as np
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Multi-Cloud Infrastructure & SRE Dashboard",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom High-Contrast Styling
st.markdown(
    """
<style>
    div[data-testid="stMetric"] {
        background-color: #F8FAFC;
        border: 1px solid #CBD5E1;
        padding: 16px 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.06);
    }
    div[data-testid="stMetric"] label {
        color: #334155 !important;
        font-size: 14px !important;
        font-weight: 600 !important;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #0F172A !important;
        font-size: 28px !important;
        font-weight: 800 !important;
    }
    div[data-testid="stMetricDelta"] {
        font-weight: 700 !important;
        font-size: 13px !important;
    }
    .topology-card-aws {
        background-color: #FFFBEB;
        border: 2px solid #F59E0B;
        padding: 18px;
        border-radius: 10px;
    }
    .topology-card-azure {
        background-color: #EFF6FF;
        border: 2px solid #3B82F6;
        padding: 18px;
        border-radius: 10px;
    }
</style>
""",
    unsafe_allow_html=True,
)


def generate_mock_telemetry():
  """Generates synthetic multi-cloud telemetry for AWS and Azure nodes."""
  timestamps = pd.date_range(end=pd.Timestamp.now(), periods=24, freq="h")

  aws_cpu = [
      25.4,
      28.1,
      31.0,
      38.5,
      55.2,
      68.4,
      72.1,
      65.0,
      58.2,
      51.0,
      48.2,
      42.1,
      39.5,
      36.2,
      41.0,
      62.5,
      78.4,
      82.1,
      74.5,
      63.2,
      52.0,
      41.5,
      33.2,
      29.0,
  ]

  azure_cpu = [
      22.1,
      24.5,
      27.8,
      34.2,
      49.0,
      62.1,
      68.5,
      61.2,
      54.0,
      47.5,
      44.1,
      39.0,
      36.8,
      33.5,
      38.2,
      58.0,
      74.2,
      79.5,
      71.0,
      59.8,
      48.5,
      38.2,
      30.5,
      26.2,
  ]

  df = pd.DataFrame({
      "Timestamp": timestamps,
      "AWS Compute Fleet (us-east-1)": aws_cpu,
      "Azure Compute Fleet (eastus)": azure_cpu,
  }).set_index("Timestamp")

  return df


def main():
  st.title("🌐 Multi-Cloud Infrastructure & SRE Observability Platform")
  st.markdown(
      "**Centralized Telemetry, SRE Metrics & Operational Reliability across"
      " AWS and Microsoft Azure**"
  )
  st.divider()

  # Top KPI Metrics Row
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.metric(
        label="Multi-Cloud Fleet Availability",
        value="99.94%",
        delta="99.9% SLO Target Met",
        delta_color="normal",
    )
  with col2:
    st.metric(
        label="Mean Time to Resolution (MTTR)",
        value="18.5 mins",
        delta="-30.2% MTTR Reduction",
        delta_color="inverse",
    )
  with col3:
    st.metric(
        label="Active Infrastructure Nodes",
        value="4 Nodes",
        delta="2 AWS | 2 Azure",
        delta_color="normal",
    )
  with col4:
    st.metric(
        label="Infrastructure Drift Status",
        value="0 Drift",
        delta="Terraform In-Sync",
        delta_color="normal",
    )

  st.write("")

  # Dashboard Tabs
  tab1, tab2, tab3, tab4 = st.tabs([
      "📊 Unified Observability (Grafana Single Pane)",
      "🗺️ Multi-Cloud Topology & Terraform Visualizer",
      "🧪 Post-Migration Validation Test Suite",
      "🚨 DR Failover & Incident Runbook",
  ])

  # TAB 1: Unified Observability
  with tab1:
    st.subheader("Real-Time Compute Utilization (AWS vs Azure)")
    st.caption(
        "Prometheus node_exporter scraping telemetry across AWS VPC and Azure"
        " VNet on port 9100."
    )

    df_telemetry = generate_mock_telemetry()
    st.line_chart(df_telemetry, use_container_width=True)

    st.subheader("Multi-Cloud Host Fleet Status")
    fleet_data = [
        {
            "Host Name": "aws-app-server-01",
            "Provider": "AWS",
            "Region": "us-east-1",
            "Private IP": "10.100.1.10",
            "Node Exporter": "Port 9100 (UP)",
            "CPU %": "29.0%",
            "Status": "HEALTHY",
        },
        {
            "Host Name": "aws-app-server-02",
            "Provider": "AWS",
            "Region": "us-east-1",
            "Private IP": "10.100.1.11",
            "Node Exporter": "Port 9100 (UP)",
            "CPU %": "31.2%",
            "Status": "HEALTHY",
        },
        {
            "Host Name": "azure-app-server-01",
            "Provider": "Azure",
            "Region": "eastus",
            "Private IP": "10.200.1.10",
            "Node Exporter": "Port 9100 (UP)",
            "CPU %": "26.2%",
            "Status": "HEALTHY",
        },
        {
            "Host Name": "azure-app-server-02",
            "Provider": "Azure",
            "Region": "eastus",
            "Private IP": "10.200.1.11",
            "Node Exporter": "Port 9100 (UP)",
            "CPU %": "28.5%",
            "Status": "HEALTHY",
        },
    ]
    st.dataframe(pd.DataFrame(fleet_data), use_container_width=True)

  # TAB 2: Multi-Cloud Topology & Terraform Execution Visualizer
  with tab2:
    st.subheader("Multi-Cloud Network Architecture Mapping")
    st.caption(
        "Visual representation of the provisioned AWS and Azure environments"
        " generated by Terraform."
    )

    col_map_aws, col_map_azure = st.columns(2)
    with col_map_aws:
      st.markdown("""
            <div class="topology-card-aws">
                <h3 style="color: #B45309; margin-top:0;">🟠 AWS Cloud Tier (Region: us-east-1)</h3>
                <p><b>VPC:</b> <code>10.100.0.0/16</code> (Name: <code>dev-aws-vpc</code>)</p>
                <ul>
                    <li><b>Public Subnet:</b> <code>10.100.1.0/24</code> (Attached to Internet Gateway)</li>
                    <li><b>Private App Subnet:</b> <code>10.100.2.0/24</code> (Internal Services)</li>
                    <li><b>Security Group:</b> <code>dev-app-sg</code> (Inbound: 443 HTTPS, 9100 Telemetry)</li>
                    <li><b>Active Compute:</b> <code>aws-app-01</code>, <code>aws-app-02</code></li>
                </ul>
                <p><b>State Backend:</b> AWS S3 + DynamoDB State Locking Table</p>
            </div>
            """, unsafe_allow_html=True)

    with col_map_azure:
      st.markdown("""
            <div class="topology-card-azure">
                <h3 style="color: #1D4ED8; margin-top:0;">🔵 Microsoft Azure Tier (Region: eastus)</h3>
                <p><b>Resource Group:</b> <code>dev-rg-multicloud-framework</code></p>
                <p><b>VNet:</b> <code>10.200.0.0/16</code> (Name: <code>dev-azure-vnet</code>)</p>
                <ul>
                    <li><b>Application Subnet:</b> <code>10.200.1.0/24</code></li>
                    <li><b>Database Subnet:</b> <code>10.200.2.0/24</code></li>
                    <li><b>Network Security Group (NSG):</b> <code>dev-app-nsg</code> (Inbound: 443, 9100)</li>
                    <li><b>Centralized Telemetry:</b> Azure Log Analytics Workspace (30-day retention)</li>
                </ul>
                <p><b>State Backend:</b> Azure Blob Storage with Native Lease Locking</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.subheader("Terraform Deployment Execution Simulator")
    st.write(
        "Click the button below to simulate how Terraform provisions these"
        " multi-cloud resources from code:"
    )

    if st.button("▶ Run Terraform Deployment Simulator", type="primary"):
      tf_status = st.empty()
      tf_bar = st.progress(0)

      deployment_steps = [
          (
              "Initializing Terraform Providers (hashicorp/aws &"
              " hashicorp/azurerm)..."
          ),
          (
              "Acquiring State Lock from S3 DynamoDB / Azure Blob Storage"
              " backend..."
          ),
          (
              "module.aws_network.aws_vpc.main: Creating... [CIDR:"
              " 10.100.0.0/16]"
          ),
          (
              "module.azure_network.azurerm_resource_group.rg: Creating..."
              " [Region: eastus]"
          ),
          (
              "module.aws_network.aws_subnet.public: Creating... [CIDR:"
              " 10.100.1.0/24]"
          ),
          (
              "module.azure_network.azurerm_virtual_network.vnet: Creating..."
              " [CIDR: 10.200.0.0/16]"
          ),
          (
              "module.aws_network.aws_security_group.app_sg: Creating..."
              " [Enforcing Least Privilege]"
          ),
          (
              "module.azure_network.azurerm_network_security_group.app_nsg:"
              " Creating... [Ports 443, 9100]"
          ),
          (
              "module.azure_network.azurerm_log_analytics_workspace.logs:"
              " Creating... [Telemetry Workspace]"
          ),
          (
              "Running Ansible Playbook (site.yml): Applying OS Hardening &"
              " node_exporter on all 4 nodes..."
          ),
      ]

      for idx, step in enumerate(deployment_steps):
        tf_status.code(f"EXEC: {step}", language="bash")
        time.sleep(0.3)
        tf_bar.progress((idx + 1) / len(deployment_steps))

      tf_status.empty()
      st.success(
          "🎉 **Apply Complete! Resources: 12 added, 0 changed, 0 destroyed.**"
          " State locked and saved to remote backend."
      )

      st.code(
          """
Outputs:
aws_security_group_id = "sg-0987654321fedcba0"
aws_vpc_id            = "vpc-0123456789abcdef0"
azure_vnet_id         = "/subscriptions/.../virtualNetworks/dev-azure-vnet"
azure_log_analytics   = "/subscriptions/.../workspaces/dev-log-analytics"
        """,
          language="hcl",
      )

  # TAB 3: Post-Migration Validation Suite
  with tab3:
    st.subheader("Automated Post-Migration Health Verification")
    st.info(
        "Execute automated verification probes across networking, security"
        " baselines, database sync, and telemetry streams."
    )

    if st.button("▶ Run Automated Validation Test Suite"):
      progress_bar = st.progress(0)
      status_text = st.empty()

      checks = [
          (
              "AWS VPC Gateway & Ingress Connectivity",
              "10.100.1.10",
              "PASS",
              "12ms",
          ),
          (
              "Azure VNet Peering & Subnet Routing",
              "10.200.1.10",
              "PASS",
              "14ms",
          ),
          (
              "Security Group & NSG Firewall Rules (Least Privilege)",
              "Port 443/9100",
              "PASS",
              "Enforced",
          ),
          (
              "SSH Root Login Disabled Compliance",
              "sshd_config",
              "PASS",
              "Compliant",
          ),
          (
              "Prometheus node_exporter Telemetry Stream",
              "Port 9100",
              "PASS",
              "Streaming",
          ),
          (
              "Database Connection Pool & Synchronization",
              "PostgreSQL / Azure SQL",
              "PASS",
              "Synced (<1s lag)",
          ),
          (
              "Azure Log Analytics Workspace Ingestion",
              "Workspace Agent",
              "PASS",
              "Active",
          ),
      ]

      results = []
      for i, (desc, target, status, latency) in enumerate(checks):
        status_text.text(f"Auditing: {desc}...")
        time.sleep(0.15)
        results.append({
            "Verification Check": desc,
            "Target Layer": target,
            "Status": status,
            "Result / Latency": latency,
        })
        progress_bar.progress((i + 1) / len(checks))

      status_text.empty()
      st.success(
          "✅ **100% READINESS ACHIEVED — ALL 7 CHECKS PASSED! APPROVED FOR"
          " PRODUCTION CUTOVER.**"
      )
      st.dataframe(pd.DataFrame(results), use_container_width=True)

  # TAB 4: DR Runbook & Incident Management
  with tab4:
    st.subheader("Disaster Recovery (DR) & Incident Triage Procedures")
    st.markdown(
        "**Target RTO: < 15 mins | Target RPO: < 5 mins | Availability Target:"
        " 99.9%**"
    )

    col_dr1, col_dr2 = st.columns(2)
    with col_dr1:
      st.markdown("### 1. Incident Severity Matrix")
      sev_data = [
          {
              "Severity": "SEV-1 (Critical)",
              "Trigger": "Primary cloud region total outage",
              "Notification SLA": "< 5 min",
              "Target RTO": "< 30 min",
          },
          {
              "Severity": "SEV-2 (High)",
              "Trigger": "Latency > 500ms or telemetry degradation",
              "Notification SLA": "< 15 min",
              "Target RTO": "< 2 hours",
          },
          {
              "Severity": "SEV-3 (Moderate)",
              "Trigger": "Non-critical batch failure, disk > 80%",
              "Notification SLA": "< 1 hour",
              "Target RTO": "Next business day",
          },
      ]
      st.dataframe(pd.DataFrame(sev_data), use_container_width=True)

    with col_dr2:
      st.markdown("### 2. Multi-Cloud Failover Workflow")
      st.markdown("""
            1. **Detect & Triage:** Identify failing cloud provider in Grafana telemetry.
            2. **DNS Traffic Shift:** Drain primary cloud (Weight: `0`), route 100% to secondary cloud (Weight: `100`).
            3. **Capacity Auto-Scale:** Pre-scale standby compute fleet (+4 instances).
            4. **Database Verification:** Promote secondary read-replica to primary.
            5. **RCA Post-Mortem:** Conduct 5-Whys root cause analysis within 24 hours.
            """)


if __name__ == "__main__":
  main()