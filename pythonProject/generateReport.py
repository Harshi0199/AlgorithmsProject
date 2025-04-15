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
The execution time (in nanoseconds) is measured only for the solution code when the “--skip-tests” flag is provided.
Results are summarized via a grouped bar chart (aggregated over tasks) and an HTML report with a table showing each task's Pass/Fail results and execution times.
"""

import os
import subprocess
import concurrent.futures
import time  # For high-resolution timing

# Force matplotlib to use the 'Agg' backend for non-interactive use.
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt


def get_tasks_from_folder():
    """
    Dynamically generates the tasks list from the folder structure.
    Assumes that the base folder 'generated_solutions' contains the canonical file names,
    and that corresponding files in other folders (ChatGPT, Gemini, Claude) follow the pattern:
       <base_name>_<folder_lowercase>.py
    Returns a list of dictionaries where each dictionary has:
         "problem_name": <base_name>
         and keys for each folder with the expected filename.
    """
    solution_folders = ["generated_solutions", "ChatGPT", "Gemini", "Claude"]
    base_folder = solution_folders[0]
    # List .py files in the base folder
    base_files = [f for f in os.listdir(base_folder) if f.endswith(".py")]
    tasks = []
    for file in base_files:
        base_name = file[:-3]  # Remove '.py'
        task = {"problem_name": base_name}
        for folder in solution_folders:
            if folder == base_folder:
                task[folder] = file
            else:
                # Construct file name as: <base_name>_<folder_lowercase>.py
                task[folder] = f"{base_name}_{folder.lower()}.py"
        tasks.append(task)
    return tasks


def run_script(filepath):
    """
    Executes a Python file with the '--skip-tests' argument and returns a tuple:
      (filepath, return_code, exec_time_ns, stdout, stderr).
    A return code of 0 indicates a pass; execution time is measured in nanoseconds.
    The '--skip-tests' argument should instruct the file to run only the solution code.
    """
    start_ns = time.perf_counter_ns()
    try:
        # Pass '--skip-tests' to run only the solution code (not the test cases)
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
    exec_time_ns = end_ns - start_ns
    return (filepath, return_code, exec_time_ns, stdout, stderr)


def main():
    # Dynamically build the tasks list from the folder structure.
    tasks = get_tasks_from_folder()
    print("Generated tasks:")
    for t in tasks:
        print(t)

    # Define the folder names in the desired order.
    folders = ["generated_solutions", "ChatGPT", "Gemini", "Claude"]

    # Aggregated statistics per folder for the bar chart.
    aggregate_stats = {folder: {"pass": 0, "fail": 0} for folder in folders}

    # Results per task for the HTML summary table.
    # Structure: { problem_name: { folder: {"pass": value, "fail": value, "time": value}, ... } }
    task_results = {}

    # Execute all tasks concurrently.
    futures = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for task in tasks:
            problem_name = task["problem_name"]
            task_results[problem_name] = {}
            for folder in folders:
                file_name = task.get(folder)
                if not file_name:
                    continue
                filepath = os.path.join(folder, file_name)
                future = executor.submit(run_script, filepath)
                futures.append((future, problem_name, folder, file_name))

        # Process the results as they complete.
        for future, problem_name, folder, file_name in futures:
            fp, return_code, exec_time_ns, stdout, stderr = future.result()
            passed = 1 if return_code == 0 else 0
            failed = 0 if return_code == 0 else 1
            task_results[problem_name][folder] = {"pass": passed, "fail": failed, "time": exec_time_ns}
            aggregate_stats[folder]["pass"] += passed
            aggregate_stats[folder]["fail"] += failed
            print(
                f"[DEBUG] Problem: {problem_name} | Folder: {folder} | File: {file_name} | Return Code: {return_code} | Time: {exec_time_ns} ns")

    # Create a grouped bar chart (aggregated stats).
    agg_pass_counts = [aggregate_stats[f]["pass"] for f in folders]
    agg_fail_counts = [aggregate_stats[f]["fail"] for f in folders]
    x = range(len(folders))
    width = 0.35
    fig, ax = plt.subplots(figsize=(8, 4))
    rects_pass = ax.bar([i - width / 2 for i in x], agg_pass_counts, width, label='Pass', color='green')
    rects_fail = ax.bar([i + width / 2 for i in x], agg_fail_counts, width, label='Fail', color='red')
    ax.set_ylabel('Count')
    ax.set_title('Pass/Fail Comparison Across Folders (Aggregated over Tasks)')
    ax.set_xticks(list(x))
    ax.set_xticklabels(folders)
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects_pass)
    autolabel(rects_fail)
    plt.tight_layout()
    graph_file = "comparison_graph.png"
    plt.savefig(graph_file)
    plt.close()
    if os.path.exists(graph_file):
        print(f"[INFO] Graph generated and saved as: {graph_file}")
    else:
        print("[ERROR] Graph file was not generated!")

    # Build HTML report with a summary table including execution time.
    html_file = "comparison_report.html"
    html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Python Solutions Comparison Report</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 20px;
    }}
    table {{
      border-collapse: collapse;
      width: 90%;
      margin-top: 20px;
    }}
    th, td {{
      border: 1px solid #ccc;
      padding: 8px;
      text-align: center;
    }}
    th {{
      background-color: #f2f2f2;
    }}
  </style>
</head>
<body>
  <h1>Python Solutions Comparison Report</h1>
  <!--
      Comparing multiple Python solutions (tasks) across four folders:
          generated_solutions, ChatGPT, Gemini, and Claude.
  -->
  <h2>Pass/Fail Bar Chart (Aggregated over Tasks)</h2>
  <img src="{graph_file}" alt="Pass/Fail Comparison Graph" style="max-width: 600px;">
  <h2>Summary Table</h2>
  <table>
    <thead>
      <tr>
        <th rowspan="2">File</th>
        <th colspan="3">generated_solutions</th>
        <th colspan="3">ChatGPT</th>
        <th colspan="3">Gemini</th>
        <th colspan="3">Claude</th>
      </tr>
      <tr>
        <th>Pass</th>
        <th>Fail</th>
        <th>Time (ns)</th>
        <th>Pass</th>
        <th>Fail</th>
        <th>Time (ns)</th>
        <th>Pass</th>
        <th>Fail</th>
        <th>Time (ns)</th>
        <th>Pass</th>
        <th>Fail</th>
        <th>Time (ns)</th>
      </tr>
    </thead>
    <tbody>
"""
    for task in tasks:
        problem_name = task["problem_name"]
        html_content += f"      <tr>\n"
        html_content += f"        <td>{problem_name}</td>\n"
        for folder in folders:
            result = task_results.get(problem_name, {}).get(folder, {"pass": "N/A", "fail": "N/A", "time": "N/A"})
            html_content += f"        <td>{result['pass']}</td>\n"
            html_content += f"        <td>{result['fail']}</td>\n"
            html_content += f"        <td>{result['time']}</td>\n"
        html_content += "      </tr>\n"
    html_content += """    </tbody>
  </table>
</body>
</html>
"""
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[INFO] Comparison report generated: {html_file}")


if __name__ == "__main__":
    main()

