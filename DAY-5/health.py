# import subprocess
# import datetime
 
# def run_cmd(cmd):
#     """Helper to run a command and return its output as string"""
#     result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
#     return result.stdout.strip()
 
# def generate_health_report():
#     now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 
#     report = f"""
# ╔══════════════════════════════════════════╗
# ║        SYSTEM HEALTH REPORT              ║
# ╚══════════════════════════════════════════╝
# Generated: {now}
 
# ── CPU USAGE ──────────────────────────────
# {run_cmd('top -bn1 | grep "Cpu(s)"')}
 
# ── MEMORY USAGE ───────────────────────────
# {run_cmd('free -h')}
 
# ── DISK USAGE ─────────────────────────────
# {run_cmd('df -h /')}
 
# ── TOP 5 PROCESSES BY CPU ──────────────────
# {run_cmd('ps aux --sort=-%cpu | head -6')}
# """
#     return report
 
# # Generate and save
# health_report = generate_health_report()
# print(health_report)
 
# filename = f"health_{datetime.date.today()}.txt"

# with open(filename, 'w', encoding='utf-8') as f:
#     f.write(health_report)

# print(f"Report saved: {filename}")
import subprocess
import datetime


def run_cmd(cmd):
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    return result.stdout.strip() 


def generate_health_report():
    now = datetime.datetime.now() #.strftime('%Y-%m-%d %H:%M:%S')

    report = f"""
╔══════════════════════════════════════════╗
║         SYSTEM HEALTH REPORT             ║
╚══════════════════════════════════════════╝
Generated: {now}

── CPU USAGE ──────────────────────────────
{run_cmd('wmic cpu get loadpercentage')} 

── MEMORY USAGE ───────────────────────────
{run_cmd('systeminfo | findstr /C:"Total Physical Memory" /C:"Available Physical Memory"')}

── DISK USAGE ─────────────────────────────
{run_cmd('wmic logicaldisk get caption,freespace,size')}

── TOP 5 PROCESSES ────────────────────────
{run_cmd('tasklist')}
"""
    return report


health_report = generate_health_report()
# print(health_report)

filename = f"health_{datetime.date.today()}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(health_report)

print(f"Report saved: {filename}")

