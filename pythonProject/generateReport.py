"""
This script compares multiple Python solutions across four folders:
    Folders:
       - generated_solutions
       - ChatGPT
       - Gemini
       - Claude

For each task, the same problem is implemented in different folders. For example,
if a file named "wiggle_subsequence.py" exists in generated_solutions then the script
expects the following files (if they exist):
  - generated_solutions/wiggle_subsequence.py
  - ChatGPT/wiggle_subsequence_chatgpt.py
  - Gemini/wiggle_subsequence_gemini.py
  - Claude/wiggle_subsequence_claude.py

Each file is executed concurrently with a timeout (10 seconds) and a return code of 0 is considered a Pass.
The execution time (in milliseconds) is measured only for the solution code when the “--skip-tests” flag is provided.
Results are summarized via a grouped bar chart (aggregated over tasks) and an HTML report with a table showing
each task's Difficulty, Pass/Fail results, and execution times.
"""

import os
import re
import subprocess
import concurrent.futures
import time

# Force matplotlib to use the 'Agg' backend for non-interactive use.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


BASE_FOLDER = "generated_solutions"
OTHER_FOLDERS = ["ChatGPT", "Gemini", "Claude"]
ALL_FOLDERS = [BASE_FOLDER] + OTHER_FOLDERS


def extract_difficulty(path):
    """
    Read the file at path and extract the difficulty from a comment line like "# Difficulty: Medium".
    Returns the difficulty string or 'Unknown' if not found.
    """
    pattern = re.compile(r'^\s*#\s*Difficulty:\s*(.+)', re.IGNORECASE)
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                m = pattern.match(line)
                if m:
                    return m.group(1).strip()
    except FileNotFoundError:
        pass
    return "Unknown"


def get_tasks_from_folder():
    """
    Dynamically generates the tasks list from the folder structure.
    Assumes that BASE_FOLDER contains the canonical filenames,
    and that corresponding files in OTHER_FOLDERS follow the pattern:
       <base_name>_<folder_lowercase>.py
    Each task dict includes:
       - problem_name
       - difficulty (extracted from base file)
       - one entry per folder with the expected filename
    """
    base_files = [f for f in os.listdir(BASE_FOLDER) if f.endswith(".py")]
    tasks = []
    for file in base_files:
        base_name = file[:-3]
        difficulty = extract_difficulty(os.path.join(BASE_FOLDER, file))
        task = {
            "problem_name": base_name,
            "difficulty": difficulty
        }
        for folder in ALL_FOLDERS:
            if folder == BASE_FOLDER:
                task[folder] = file
            else:
                task[folder] = f"{base_name}_{folder.lower()}.py"
        tasks.append(task)
    return tasks


def run_script(filepath):
    """
    Executes a Python file with the '--skip-tests' argument and returns a tuple:
      (filepath, return_code, exec_time_ms, stdout, stderr).
    Execution time is measured in milliseconds.
    """
    start_ns = time.perf_counter_ns()
    try:
        result = subprocess.run(
            ["python", filepath, "--skip-tests"],
            capture_output=True,
            text=True,
            timeout=10
        )
        return_code = result.returncode
        stdout = result.stdout
        stderr = result.stderr
    except Exception as e:
        return_code = -1
        stdout = ""
        stderr = str(e)
    end_ns = time.perf_counter_ns()
    exec_time_ms = (end_ns - start_ns) / 1_000_000
    return (filepath, return_code, exec_time_ms, stdout, stderr)


def main():
    tasks = get_tasks_from_folder()

    # Print out the generated tasks for verification
    print("Generated tasks:")
    for t in tasks:
        print(f"  - {t['problem_name']} (Difficulty: {t['difficulty']})")

    folders = ALL_FOLDERS
    aggregate_stats = {f: {"pass": 0, "fail": 0} for f in folders}
    task_results = {t["problem_name"]: {} for t in tasks}

    # Run all scripts in parallel
    futures = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for t in tasks:
            name = t["problem_name"]
            for folder in folders:
                filename = t.get(folder)
                if not filename:
                    continue
                filepath = os.path.join(folder, filename)
                futures.append((executor.submit(run_script, filepath), name, folder, filename))

        for future, name, folder, filename in futures:
            _, code, time_ms, _, _ = future.result()
            passed = int(code == 0)
            failed = int(code != 0)
            task_results[name][folder] = {"pass": passed, "fail": failed, "time": f"{time_ms:.2f}"}
            aggregate_stats[folder]["pass"] += passed
            aggregate_stats[folder]["fail"] += failed
            print(f"[DEBUG] {name:<40} | {folder:<17} | {filename:<30} | Pass={passed} | Time={time_ms:.2f}ms")

    # Build bar chart
    x = range(len(folders))
    pass_counts = [aggregate_stats[f]["pass"] for f in folders]
    fail_counts = [aggregate_stats[f]["fail"] for f in folders]
    width = 0.35
    fig, ax = plt.subplots(figsize=(8,4))
    ax.bar([i - width/2 for i in x], pass_counts, width, label="Pass", color="green")
    ax.bar([i + width/2 for i in x], fail_counts, width, label="Fail", color="red")
    ax.set_xticks(list(x))
    ax.set_xticklabels(folders)
    ax.set_ylabel("Count")
    ax.set_title("Pass/Fail Comparison Across Folders")
    ax.legend()
    for rect in ax.patches:
        height = rect.get_height()
        ax.annotate(f'{height}', (rect.get_x()+rect.get_width()/2, height),
                    ha='center', va='bottom', fontsize=8)
    plt.tight_layout()
    graph_file = "comparison_graph.png"
    plt.savefig(graph_file)
    plt.close()

    # Generate HTML report
    html = ["""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Python Solutions Comparison Report</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    table { border-collapse: collapse; width: 95%; margin-top: 20px; }
    th, td { border: 1px solid #ccc; padding: 6px; text-align: center; }
    th { background-color: #f2f2f2; }
  </style>
</head><body>
  <h1>Python Solutions Comparison Report</h1>
  <h2>Pass/Fail Bar Chart</h2>
  <img src="comparison_graph.png" alt="Bar Chart">
  <h2>Summary Table</h2>
  <table>
    <thead>
      <tr>
        <th rowspan="2">File</th>
        <th rowspan="2">Difficulty</th>"""]
    for f in folders:
        html.append(f'        <th colspan="3">{f}</th>')
    html.append("      </tr>\n      <tr>")
    for _ in folders:
        html.append("        <th>Pass</th><th>Fail</th><th>Time (ms)</th>")
    html.append("      </tr>\n    </thead>\n    <tbody>")
    for t in tasks:
        name = t["problem_name"]
        difficulty = t["difficulty"]
        html.append("      <tr>")
        html.append(f"        <td>{name}</td>")
        html.append(f"        <td>{difficulty}</td>")
        for f in folders:
            r = task_results[name].get(f, {"pass":"N/A","fail":"N/A","time":"N/A"})
            html.append(f"        <td>{r['pass']}</td>")
            html.append(f"        <td>{r['fail']}</td>")
            html.append(f"        <td>{r['time']}</td>")
        html.append("      </tr>")
    html.append("""    </tbody>
  </table>
</body>
</html>""")

    with open("comparison_report.html", "w", encoding="utf-8") as f:
        f.write("\n".join(html))

    print("Comparison report generated: comparison_report.html")


if __name__ == "__main__":
    main()
