# Operational Runbook: Incident Triage & Multi-Cloud DR Failover

**Target Service:** Multi-Cloud Application & Core Infrastructure Tier  
**SLO Target:** 99.9% Availability | Target RTO: < 15 mins | Target RPO: < 5 mins  
**Owner:** Cloud Reliability & Hosting Operations Team  

---

## 1. Incident Severity Classification

| Severity | Definition | Notification SLA | Target Resolution |
| :--- | :--- | :--- | :--- |
| **SEV-1 (Critical)** | Complete outage in primary cloud region; user transactions failing. | Immediate (< 5 min) | < 30 minutes |
| **SEV-2 (High)** | Degradation in telemetry, high latency (>500ms), partial service failure. | < 15 minutes | < 2 hours |
| **SEV-3 (Moderate)** | Non-critical background task failure, disk utilization > 80%. | < 1 hour | Next business day |

---

## 2. Immediate Triage & Blast Radius Isolation

1. **Verify Grafana Fleet Dashboard:**
   * Check `Fleet Availability` and identify which cloud provider (AWS or Azure) is failing.
2. **Identify Failure Layer:**
   * **Network/DNS:** Test public endpoints via curl or Route 53 / Azure DNS status.
   * **Compute:** Check node CPU/Memory saturation on port 9100 metrics.
   * **Database:** Check database connection pool and replication lag.

---

## 3. Disaster Recovery (DR) Failover Procedure

If the primary cloud region is unresponsive for > 10 minutes:

### Step 3.1: Trigger Global DNS Cutover
* Update Global Traffic Manager / Route 53 Weighted Routing:
  * Drain traffic from Primary Cloud (Weight: `0`).
  * Shift 100% production traffic to Secondary Cloud (Weight: `100`).

### Step 3.2: Verify Standby Workload Capacity
* In Secondary Cloud (e.g. Azure VNet):
  * Pre-scale Auto Scaling / VMSS minimum instance count:
    ```bash
    az vmss scale --resource-group rg-multicloud-framework --name app-vmss --new-capacity 8
    ```

### Step 3.3: Validate Database Read/Write Status
* Promote secondary database replica to standalone primary.
* Confirm zero replication lag and test read/write queries.

---

## 4. Post-Incident Review (RCA & 5-Whys)

Within 24 hours of incident resolution:
1. Document the exact timeline of events in Azure DevOps / Jira.
2. Conduct the **5-Whys Root Cause Analysis**.
3. Identify whether a runbook or automation rule needs updating to prevent recurrence.