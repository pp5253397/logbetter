# 🪶 logbetter

**logbetter** is a lightweight Python logging utility that enhances console logging with **clean, colored, and readable output**.  
It extends Python's built-in `logging` module with:

- ✨ Colored console output  
- 🕒 Automatic timestamps  
- ✅ Success log level  
- 📁 Optional file logging  
- 🚀 Developer-friendly API  

Ideal for CLI tools, scripts, automation, and backend services.

---

## 🔧 Installation

Install via PyPI:

```bash
pip install logbetter
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/pp5253397/logbetter.git
```

---

## 🧩 Quick Start

```python
from logbetter import log

log.info("Application started")
log.success("Data processed successfully")
log.warning("Low disk space")
log.error("Connection failed")
log.debug("Debug details here")
```

**Example Output:**
```
[2025-10-25 20:42:10] [ℹ️ INFO] Application started
[2025-10-25 20:42:10] [✅ SUCCESS] Data processed successfully
[2025-10-25 20:42:10] [⚠️ WARNING] Low disk space
[2025-10-25 20:42:10] [❌ ERROR] Connection failed
[2025-10-25 20:42:10] [🐞 DEBUG] Debug details here
```

---

## 🆕 Version History / Changelog

### v0.0.3
- ✅ Added `success()` log level  
- ✅ Optional file logging (`log_to_file=True`)  
- ✅ Improved timestamp formatting  
- ✅ Enhanced colored output  
- ✅ Customizable log format and timestamp

### v0.0.2
- Initial release  
- Basic colored log levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`  
- Timestamps with default format  
- Global `log` object for simple usage  

---

## ⚙️ Logging Levels

| Level      | Emoji | Description                     |
|------------|-------|---------------------------------|
| DEBUG      | 🐞    | Debugging messages              |
| INFO       | ℹ️    | General informational messages  |
| SUCCESS    | ✅    | Successful operations           |
| WARNING    | ⚠️    | Warning messages                |
| ERROR      | ❌    | Errors                          |
| CRITICAL   | 🚨    | Critical failures               |

---

## ⚙️ Configuration Options

```python
from logbetter import LogBetter

custom_log = LogBetter()
custom_log.set_format("{time} | {level} | {message}")  # Custom log format
custom_log.set_time_format("%H:%M:%S")                  # Custom timestamp format
custom_log.disable_time()                               # Hide timestamps if desired
```

| Parameter      | Type | Default         | Description |
|----------------|------|----------------|-------------|
| `name`         | str  | `"logbetter"`  | Logger name |
| `level`        | str  | `"INFO"`       | Logging level (`DEBUG`, `INFO`, `SUCCESS`, `WARNING`, `ERROR`, `CRITICAL`) |
| `log_to_file`  | bool | `False`        | Save logs to a file |
| `filename`     | str  | `"logbetter.log"` | Log file name |

---

## 🧩 File Logging

Enable file logging:

```python
log = LogBetter(log_to_file=True, filename="app.log")
log.info("This message is printed and saved to app.log")
```

All messages are automatically written to the file alongside console output.

---

## 🛠️ Customization

### Custom Log Format

```python
log.set_format("{time} - {level} >>> {message}")
```

### Custom Timestamp Format

```python
log.set_time_format("%Y-%m-%d %H:%M:%S")
```

### Disable Timestamps

```python
log.disable_time()
```

---

## 📦 Project Info

| Field       | Details |
|------------ |---------|
| **Author**  | Parth Patel |
| **Email**   | pp5253397@gmail.com |
| **License** | MIT |
| **Repository** | [GitHub](https://github.com/pp5253397/logbetter) |
| **PyPI**      | [PyPI](https://pypi.org/project/logbetter) |

---

## 💡 Contributing

We welcome contributions!  

1. Fork the repository  
2. Create a new branch (`feature/my-feature`)  
3. Commit your changes (`git commit -m "Add feature"`)  
4. Push your branch (`git push origin feature/my-feature`)  
5. Open a Pull Request  

Please follow PEP8 style and include tests for new features.

---

## 🪶 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

> Made with ❤️ by Parth Patel  
> Clean, colorful, and better logs — because your console deserves style.
