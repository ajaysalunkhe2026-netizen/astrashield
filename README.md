

```markdown
# 🛡️ AstraShield - PQC Migration Scanner

**AstraShield** is a lightweight and powerful **Static Application Security Testing (SAST)** tool designed specifically for **Post-Quantum Cryptography (PQC)** migration. It helps developers identify legacy and quantum-vulnerable cryptographic algorithms (such as RSA, ECC) within their projects.

## 🚀 Key Features
* **PQC-Focused:** Specifically scans for libraries and algorithms vulnerable to future quantum computer attacks.
* **Regex-Powered:** Targets actual security risks (e.g., `import rsa`) while minimizing false positives from variable names or comments.
* **Actionable Reporting:** Provides clear security threats and suggests replacements based on **NIST FIPS 203/204** standards.
* **Professional Reporting:** Generates a clean, modern HTML report that can be viewed in any web browser.
* **Portable:** Runs directly with Python with no complex installation required.

## 🛠️ Installation and Usage

### Prerequisites
* Python 3.x must be installed on your system.

### How to use
1. Navigate to the project folder:
   ```bash
   cd astrashield

```

2. Run the tool:
```bash
python astrashield.py

```


3. Enter the folder path you wish to scan (e.g., `test`).
4. Once the scan is complete, open `astrashield_report.html` in your web browser to view the results.

## 📋 Why is this necessary?

The development of quantum computing poses a significant threat known as **"Harvest Now, Decrypt Later" (HNDL)** attacks. Algorithms currently considered secure (like RSA/ECC) will not withstand future quantum threats. **AstraShield** helps you take the first step toward making your codebase 'Quantum-Resistant' today.

## 👤 Author

* Ajay Salunkhe

## 📜 License

This project is available under the MIT License.

```



```