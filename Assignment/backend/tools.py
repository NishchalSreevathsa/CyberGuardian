import random
import time

def calculate_risk_score(open_ports, critical_vulns, server_importance_score):
    """
    Calculates a risk score based on vulnerability data.
    Args:
        open_ports (int): Number of open ports found.
        critical_vulns (int): Number of Critical CVEs.
        server_importance_score (int): 1-10 scale of asset value.
    Returns:
        dict: Risk analysis including score and category.
    """
    # Formula: (Ports * 0.5) + (Vulns * 5) * (Importance / 2)
    base_score = (open_ports * 0.5) + (critical_vulns * 5)
    final_score = base_score * (server_importance_score / 2.0)
    
    category = "LOW"
    if final_score > 50:
        category = "MEDIUM"
    if final_score > 100:
        category = "HIGH"
    if final_score > 200:
        category = "CRITICAL"
        
    return {
        "risk_score": round(final_score, 2),
        "category": category,
        "action_required": category in ["HIGH", "CRITICAL"]
    }

def check_threat_intel(domain):
    """
    Checks a domain against (mock) threat intelligence feeds.
    Args:
        domain (str): The domain to check.
    Returns:
        dict: Threat report.
    """
    print(f"[ThreatIntel] Checking {domain}...")
    # Mock logic
    malicious_domains = ["phishing.com", "attack.net", "malware.org"]
    
    if domain in malicious_domains:
        return {
            "domain": domain,
            "status": "MALICIOUS",
            "source": "MockIntelDB",
            "confidence": "99%"
        }
    else:
        # Random chance of being suspicious for demo purposes
        if random.random() < 0.3:
             return {
                "domain": domain,
                "status": "SUSPICIOUS",
                "source": "MockIntelDB",
                "reason": "Recently registered, high entropy name"
            }
            
    return {"domain": domain, "status": "CLEAN"}

def monitor_logs(target_event, threshold, duration_seconds=10):
    """
    Monitors (simulated) logs for a specific event exceeding a threshold.
    Args:
        target_event (str): Event name (e.g., "failed_login").
        threshold (int): Count to trigger alert.
        duration_seconds (int): How long to monitor (for demo).
    Returns:
        dict: Monitoring result.
    """
    print(f"[Monitor] Watching for '{target_event}' > {threshold} for {duration_seconds}s...")
    start_time = time.time()
    count = 0
    
    # Simulate monitoring loop
    while time.time() - start_time < duration_seconds:
        time.sleep(1)
        # Randomly simulate events
        if random.random() > 0.5:
            count += 1
            print(f"[Monitor] Detected {target_event} ({count})")
            
        if count >= threshold:
            return {
                "alert": True,
                "message": f"THRESHOLD BREACHED: {target_event} count {count} exceeded limit {threshold}!",
                "timestamp": time.time()
            }
            
    return {
        "alert": False,
        "message": f"Monitoring finished. {count} events detected. Threshold not breached."
    }
