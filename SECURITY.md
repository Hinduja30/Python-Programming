# Security Policy

## Supported Versions

We actively monitor and provide security updates for the following versions of the project. We recommend all users stay on the latest stable release to ensure the highest level of security.

| Version | Supported          | Notes                                         |
| ------- | ------------------ | --------------------------------------------- |
| 5.1.x   | :white_check_mark: | Current Stable Release                        |
| 5.0.x   | :x:                | End of Life (Upgrade to 5.1.x)                |
| 4.0.x   | :white_check_mark: | Long-Term Support (LTS)                       |
| < 4.0   | :x:                | No longer supported                           |

## Reporting a Vulnerability

We take the security of our code and our users' data seriously. If you find a security vulnerability, please do not open a public issue. Instead, follow the steps below:

### How to report
1. **Email:** Please send a detailed report to **[Your-Email-Here]** (e.g., your GitHub-linked email).
2. **Details to include:** - A description of the vulnerability.
   - Steps to reproduce the issue (PoC).
   - Potential impact if exploited.

### What to expect
- **Acknowledgement:** You will receive an initial response within **48 hours** confirming we have received the report.
- **Updates:** We will provide status updates at least once every **week** until the issue is resolved.
- **Public Disclosure:** Once a fix is verified and merged, we will coordinate a public disclosure and give you credit for the discovery (if desired).

## Preferred Practices
- **Dependency Security:** We use automated tools (like Dependabot) to monitor vulnerabilities in Python packages. Please ensure your local environment is updated regularly.
- **Code Review:** All pull requests are subject to security reviews to prevent the injection of malicious scripts or insecure coding patterns.
