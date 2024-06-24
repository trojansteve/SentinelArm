# SentinelArm
SentinelArm is a versatile and powerful macOS security research tool designed to assist security researchers in assessing and enhancing the security posture of macOS ARM64 systems. It provides comprehensive features for gathering system information, identifying vulnerabilities, and conducting reconnaissance tasks.
## Features

- **System Information Gathering**: Retrieve detailed hardware and software information including CPU details, memory, network configuration, and more.
  
- **Vulnerability Assessment**: Scan for system vulnerabilities, check for outdated software versions, and identify potential security risks.

- **Network Security**: Perform port scanning, monitor active network connections, and analyze network traffic for anomalies.

- **Error Handling**: Robust error handling to manage exceptions and ensure smooth operation across various macOS configurations.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/trojansteve/sentinelarm.git
   cd sentinelarm
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   This installs necessary Python libraries like `psutil` and `nmap`.

## Usage

### Running the tool:

```bash
python sentinelarm.py
```

### Example Output:

```
Running reconnaissance on macOS ARM64 (12.0.1)

=== System Information ===
hw.model: MacBookAir10,1
hw.machine: arm64
hw.memsize: 17179869184
machdep.cpu.brand_string: Apple M1
kern.version: Darwin Kernel Version 21.0.0
kern.osproductversion: 12.0.1
hw.physicalcpu: 8
hw.logicalcpu: 8
hw.cpufrequency: 3200000000
...

=== Process Management ===
PID: 1234, Name: Safari, User: johndoe
PID: 5678, Name: Terminal, User: johndoe
Total running processes: 10

...

```

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to submit a pull request or open an issue.

1. Fork the repository (`git clone https://github.com/trojansteve/sentinelarm.git`)
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -am 'Add new feature: NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Submit a pull request

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [psutil](https://github.com/giampaolo/psutil) - Cross-platform library for system and process utilities in Python.
- [nmap](https://github.com/nmap/nmap) - Network exploration tool and security/port scanner.

---

This README provides an overview of SentinelArm, highlighting its capabilities and guiding users on installation, usage, and contribution. Adjust it as needed to best showcase the unique features and functionality of your macOS security research tool.
