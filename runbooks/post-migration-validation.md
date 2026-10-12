# Operational Framework: Post-Migration Validation Checklist

**Purpose:** Standardized validation framework executed immediately after migrating workloads across hybrid data center and cloud environments to guarantee zero configuration drift.

---

## 1. Network & Routing Verification
- [ ] Subnet routing verified against target CIDR blocks (AWS `10.100.0.0/16`, Azure `10.200.0.0/16`).
- [ ] Hybrid VPN / Interconnect gateway status is active and healthy.
- [ ] Network Security Groups (NSGs) and AWS Security Groups restrict SSH (22) and only permit HTTPS (443).
- [ ] DNS resolution operates with latency < 15ms.

## 2. Operating System & Baseline Hardening
- [ ] Ansible `os_hardening` role executed with zero failed tasks.
- [ ] SSH root login is verified disabled (`PermitRootLogin no`).
- [ ] Local firewall (UFW/Windows Firewall) is active with default DENY policy.

## 3. Observability & Telemetry Verification
- [ ] Prometheus `node_exporter` is active and listening on port 9100.
- [ ] Target nodes appear as `UP (1)` in Grafana Fleet Health Dashboard.
- [ ] Log Analytics workspace is receiving syslog / event streams.

## 4. Automated Validation Sign-Off
Execute the automated health validation test suite:
```bash
python scripts/validate_health.py