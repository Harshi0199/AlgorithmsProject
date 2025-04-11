"""
This script compares two Python solutions:
    - generated_solutions/advantage_shuffle.py
    - LLM_generated_solutions/advantage_shuffle_chatgpt.py

Each file is executed concurrently and its return code is recorded.
A pass (exit code 0) is considered “Pass”, otherwise it is “Fail.”

The results are summarized and a bar chart showing the pass/fail counts is generated,
then an HTML report is built embedding both the graph and a summary table.

Note:
- The file names (used as task names) and problem description are provided in the file comments.
- Matplotlib's non-interactive backend ('Agg') is enforced to guarantee the graph is saved.
"""

import os
import subprocess
import concurrent.futures

# Force matplotlib to use the 'Agg' backend, which is good for scripts that only generate files.
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt


def run_script(filepath):
    """
    Executes a Python file and returns a tuple:
    (filepath, return_code, stdout, stderr)

    A return code of 0 is interpreted as a pass.
    """
    try:
        result = subprocess.run(
            ["python", filepath],
            capture_output=True,
            text=True,
            timeout=10
        )
        return (filepath, result.returncode, result.stdout, result.stderr)
    except Exception as e:
        # Mark any exception (e.g., timeout or execution error) as a failure with returncode -1.
        return (filepath, -1, "", str(e))


def main():
    # Define manually provided file names
    file_generated = os.path.join("generated_solutions", "advantage_shuffle.py")
    file_llm = os.path.join("LLM_generated_solutions", "advantage_shuffle_chatgpt.py")

    # Create a list of files to test
    files = [file_generated, file_llm]

    # Execute both files in parallel using ThreadPoolExecutor.
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(run_script, f): f for f in files}
        for future in concurrent.futures.as_completed(future_to_file):
            res = future.result()
            results.append(res)

    # Prepare statistics per folder.
    stats = {"generated_solutions": (0, 0, 0), "LLM_generated_solutions": (0, 0, 0)}
    # Count each file and mark whether it passed (return code 0) or failed.
    for filepath, retcode, stdout, stderr in results:
        folder = os.path.basename(os.path.dirname(filepath))
        total, passes, fails = stats.get(folder, (0, 0, 0))
        total += 1
        if retcode == 0:
            passes += 1
        else:
            fails += 1
        stats[folder] = (total, passes, fails)

    # Print out each file's result for debugging.
    for filepath, retcode, stdout, stderr in results:
        print(f"File: {filepath} | Return Code: {retcode}")

    # Create a bar chart to show the pass and fail counts per folder.
    folders = list(stats.keys())
    pass_counts = [stats[f][1] for f in folders]
    fail_counts = [stats[f][2] for f in folders]

    x = range(len(folders))
    width = 0.35

    fig, ax = plt.subplots(figsize=(6, 4))
    rects_pass = ax.bar([i - width / 2 for i in x], pass_counts, width, label='Pass', color='green')
    rects_fail = ax.bar([i + width / 2 for i in x], fail_counts, width, label='Fail', color='red')

    ax.set_ylabel('Count')
    ax.set_title('Pass/Fail Comparison for Solutions')
    ax.set_xticks(x)
    ax.set_xticklabels(folders)
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects_pass)
    autolabel(rects_fail)

    plt.tight_layout()
    graph_file = "comparison_graph.png"
    plt.savefig(graph_file)
    plt.close()

    # Check if the graph file exists and print the outcome.
    if os.path.exists(graph_file):
        print(f"Graph generated and saved as: {graph_file}")
    else:
        print("Graph file was not generated!")

    # Build an HTML report that embeds the graph and a summary table.
    html_file = "comparison_report.html"
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Python Solutions Comparison Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        table {{ border-collapse: collapse; width: 80%; margin-top: 20px; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: center; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>Python Solutions Comparison Report</h1>
    <!-- File Descriptions (from file comments):
         Task (Generated): advantage_shuffle.py
         Task (LLM Generated): advantage_shuffle_chatgpt.py
         Note: The description is provided as comments in each file.
    -->
    <h2>Pass/Fail Graph</h2>
    <img src="{graph_file}" alt="Pass/Fail Comparison Graph" style="max-width: 600px;">
    <h2>Summary Table</h2>
    <table>
      <tr>
        <th>Folder</th>
        <th>Total Files</th>
        <th>Pass</th>
        <th>Fail</th>
        <th>Pass Percentage</th>
        <th>Fail Percentage</th>
      </tr>
"""
    for folder, (total, passes, fails) in stats.items():
        pass_perc = (passes / total * 100) if total > 0 else 0
        fail_perc = (fails / total * 100) if total > 0 else 0
        html_content += f"""      <tr>
        <td>{folder}</td>
        <td>{total}</td>
        <td>{passes}</td>
        <td>{fails}</td>
        <td>{pass_perc:.2f}%</td>
        <td>{fail_perc:.2f}%</td>
      </tr>
"""
    html_content += """    </table>
</body>
</html>
"""
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Comparison report generated:", html_file)


if __name__ == "__main__":
    main()
