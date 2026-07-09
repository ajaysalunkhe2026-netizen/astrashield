"""
AstraShield - PQC Migration Scanner (v1.3 - Regex Powered)
Author: Ajay Salunkhe
"""

import os
import re
from datetime import datetime

class AstraShield:
    def __init__(self):
        self.name = "AstraShield"
        self.version = "1.3"
        self.author = "Ajay Salunkhe"  # यह लाइन जोड़ना जरूरी है
        self.patterns = {
            'RSA': re.compile(r'(import|from)\s+.*rsa', re.IGNORECASE),
            'ECDSA/ECC': re.compile(r'(import|from)\s+.*(ecdsa|ecc)', re.IGNORECASE),
            'PYCRYPTODOME': re.compile(r'(import|from)\s+.*pycryptodome', re.IGNORECASE)
        }
    
    def scan_folder(self, folder_path):
        findings = []
        valid_ext = ('.py', '.js', '.yaml', '.yml', '.env', '.json', '.txt')
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(valid_ext):
                    filepath = os.path.join(root, file)
                    findings.extend(self.analyze_file(filepath))
        return findings
    
    def analyze_file(self, filepath):
        findings = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for i, line in enumerate(f, 1):
                    for threat, pattern in self.patterns.items():
                        if pattern.search(line):
                            findings.append({
                                'file': filepath,
                                'line': i,
                                'threat': f'{threat} usage detected',
                                'suggestion': 'Replace with NIST PQC standard (ML-KEM/ML-DSA)'
                            })
        except: pass
        return findings

def generate_report(results):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AstraShield Report v1.3</title>
    <style>
        body {{ font-family: Arial; padding: 30px; background: #f8f9fa; }}
        .finding {{ background: white; padding: 15px; margin: 10px 0; border-left: 6px solid #e74c3c; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
    <h1>🛡️ AstraShield Report v1.3</h1>
    <p>Total Threats: {len(results)}</p>
"""
    for r in results:
        html += f"""
    <div class="finding">
        <h3>📁 {r['file']} (Line: {r['line']})</h3>
        <p><strong>Threat:</strong> {r['threat']}</p>
        <p><strong>Suggestion:</strong> {r['suggestion']}</p>
    </div>
"""
    html += "</body></html>"
    with open("astrashield_report.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    shield = AstraShield()
    print(f"🛡️ {shield.name} v{shield.version} | Author: {shield.author}")
    folder = input("Enter folder path to scan: ") or "test"
    results = shield.scan_folder(folder)
    if results:
        generate_report(results)
        print("✅ Report generated: astrashield_report.html")
    else:
        print("✅ No threats found!")