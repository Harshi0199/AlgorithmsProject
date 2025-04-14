"""
This script compares multiple Python solutions across four folders:
    Folders:
       - generated_solutions
       - ChatGPT
       - Gemini
       - Claude

For each task, the same problem is implemented in different folders. For example:
  Task: lexicographically_smallest_string_after_substring_operation
       - generated_solutions/lexicographically_smallest_string_after_substring_operation.py
       - ChatGPT/lexicographically_smallest_string_after_substring_operation_chatgpt.py
       - Gemini/lexicographically_smallest_string_after_substring_operation_gemini.py
       - Claude/lexicographically_smallest_string_after_substring_operation_claude.py

  Task: maximum_strength_of_a_group
       - generated_solutions/maximum_strength_of_a_group.py
       - ChatGPT/maximum_strength_of_a_group_chatgpt.py
       - Gemini/maximum_strength_of_a_group_gemini.py
       - Claude/maximum_strength_of_a_group_claude.py

  Task: maximum_xor_product
       - generated_solutions/maximum_xor_product.py
       - ChatGPT/maximum_xor_product_chatgpt.py
       - Gemini/maximum_xor_product_gemini.py
       - Claude/maximum_xor_product_claude.py

  Task: minimum_number_of_arrows_to_burst_balloons
       - generated_solutions/minimum_number_of_arrows_to_burst_balloons.py
       - ChatGPT/minimum_number_of_arrows_to_burst_balloons_chatgpt.py
       - Gemini/minimum_number_of_arrows_to_burst_balloons_gemini.py
       - Claude/minimum_number_of_arrows_to_burst_balloons_claude.py

  Task: minimum_operations_to_make_the_array_alternating
       - generated_solutions/minimum_operations_to_make_the_array_alternating.py
       - ChatGPT/minimum_operations_to_make_the_array_alternating_chatgpt.py
       - Gemini/minimum_operations_to_make_the_array_alternating_gemini.py
       - Claude/minimum_operations_to_make_the_array_alternating_claude.py

  Task: most_profit_assigning_work
       - generated_solutions/most_profit_assigning_work.py
       - ChatGPT/most_profit_assigning_work_chatgpt.py
       - Gemini/most_profit_assigning_work_gemini.py
       - Claude/most_profit_assigning_work_claude.py

  Task: the_number_of_weak_characters_in_the_game
       - generated_solutions/the_number_of_weak_characters_in_the_game.py
       - ChatGPT/the_number_of_weak_characters_in_the_game_chatgpt.py
       - Gemini/the_number_of_weak_characters_in_the_game_gemini.py
       - Claude/the_number_of_weak_characters_in_the_game_claude.py

  Task: smallest_subsequence_of_distinct_characters
       - generated_solutions/smallest_subsequence_of_distinct_characters.py
       - ChatGPT/smallest_subsequence_of_distinct_characters_chatgpt.py
       - Gemini/smallest_subsequence_of_distinct_characters_gemini.py
       - Claude/smallest_subsequence_of_distinct_characters_claude.py

  Task: wiggle_subsequence
       - generated_solutions/wiggle_subsequence.py
       - ChatGPT/wiggle_subsequence_chatgpt.py
       - Gemini/wiggle_subsequence_gemini.py
       - Claude/wiggle_subsequence_claude.py

  Task: average_height_of_buildings_in_each_segment
       - generated_solutions/average_height_of_buildings_in_each_segment.py
       - ChatGPT/average_height_of_buildings_in_each_segment_chatgpt.py
       - Gemini/average_height_of_buildings_in_each_segment_gemini.py
       - Claude/average_height_of_buildings_in_each_segment_claude.py

Each file is executed concurrently with a timeout (10 seconds), and a return code of 0 is considered a Pass.
The results are summarized via a grouped bar chart (aggregated over tasks) and an HTML report
with a table showing each task's Pass/Fail results and execution time (in nanoseconds) for each folder.
"""

import os
import subprocess
import concurrent.futures
import time  # For high-resolution timing

# Force matplotlib to use the 'Agg' backend for non-interactive use.
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt


def run_script(filepath):
    """
    Executes a Python file and returns a tuple:
      (filepath, return_code, exec_time_ns, stdout, stderr).
    A return code of 0 indicates a pass; otherwise, a failure.
    Execution time is measured in nanoseconds.
    """
    start_ns = time.perf_counter_ns()
    try:
        result = subprocess.run(
            ["python", filepath],
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
    # List of tasks with expected file names per folder.
    tasks = [
        {
            "problem_name": "lexicographically_smallest_string_after_substring_operation",
            "generated_solutions": "lexicographically_smallest_string_after_substring_operation.py",
            "ChatGPT": "lexicographically_smallest_string_after_substring_operation_chatgpt.py",
            "Gemini": "lexicographically_smallest_string_after_substring_operation_gemini.py",
            "Claude": "lexicographically_smallest_string_after_substring_operation_claude.py"
        },
        {
            "problem_name": "maximum_strength_of_a_group",
            "generated_solutions": "maximum_strength_of_a_group.py",
            "ChatGPT": "maximum_strength_of_a_group_chatgpt.py",
            "Gemini": "maximum_strength_of_a_group_gemini.py",
            "Claude": "maximum_strength_of_a_group_claude.py"
        },
        {
            "problem_name": "maximum_xor_product",
            "generated_solutions": "maximum_xor_product.py",
            "ChatGPT": "maximum_xor_product_chatgpt.py",
            "Gemini": "maximum_xor_product_gemini.py",
            "Claude": "maximum_xor_product_claude.py"
        },
        {
            "problem_name": "minimum_number_of_arrows_to_burst_balloons",
            "generated_solutions": "minimum_number_of_arrows_to_burst_balloons.py",
            "ChatGPT": "minimum_number_of_arrows_to_burst_balloons_chatgpt.py",
            "Gemini": "minimum_number_of_arrows_to_burst_balloons_gemini.py",
            "Claude": "minimum_number_of_arrows_to_burst_balloons_claude.py"
        },
        {
            "problem_name": "minimum_operations_to_make_the_array_alternating",
            "generated_solutions": "minimum_operations_to_make_the_array_alternating.py",
            "ChatGPT": "minimum_operations_to_make_the_array_alternating_chatgpt.py",
            "Gemini": "minimum_operations_to_make_the_array_alternating_gemini.py",
            "Claude": "minimum_operations_to_make_the_array_alternating_claude.py"
        },
        {
            "problem_name": "most_profit_assigning_work",
            "generated_solutions": "most_profit_assigning_work.py",
            "ChatGPT": "most_profit_assigning_work_chatgpt.py",
            "Gemini": "most_profit_assigning_work_gemini.py",
            "Claude": "most_profit_assigning_work_claude.py"
        },
        {
            "problem_name": "the_number_of_weak_characters_in_the_game",
            "generated_solutions": "the_number_of_weak_characters_in_the_game.py",
            "ChatGPT": "the_number_of_weak_characters_in_the_game_chatgpt.py",
            "Gemini": "the_number_of_weak_characters_in_the_game_gemini.py",
            "Claude": "the_number_of_weak_characters_in_the_game_claude.py"
        },
        {
            "problem_name": "smallest_subsequence_of_distinct_characters",
            "generated_solutions": "smallest_subsequence_of_distinct_characters.py",
            "ChatGPT": "smallest_subsequence_of_distinct_characters_chatgpt.py",
            "Gemini": "smallest_subsequence_of_distinct_characters_gemini.py",
            "Claude": "smallest_subsequence_of_distinct_characters_claude.py"
        },
        {
            "problem_name": "wiggle_subsequence",
            "generated_solutions": "wiggle_subsequence.py",
            "ChatGPT": "wiggle_subsequence_chatgpt.py",
            "Gemini": "wiggle_subsequence_gemini.py",
            "Claude": "wiggle_subsequence_claude.py"
        },
        {
            "problem_name": "average_height_of_buildings_in_each_segment",
            "generated_solutions": "average_height_of_buildings_in_each_segment.py",
            "ChatGPT": "average_height_of_buildings_in_each_segment_chatgpt.py",
            "Gemini": "average_height_of_buildings_in_each_segment_gemini.py",
            "Claude": "average_height_of_buildings_in_each_segment_claude.py"
        }
    ]

    # Define the folder names in the desired order.
    folders = ["generated_solutions", "ChatGPT", "Gemini", "Claude"]

    # Aggregated statistics per folder (for the bar chart).
    aggregate_stats = {folder: {"pass": 0, "fail": 0} for folder in folders}

    # Results per task for the HTML summary table.
    # Structure: { problem_name: { folder: {"pass": value, "fail": value, "time": value}, ... } }
    task_results = {}

    # Create a list of futures to run all tasks concurrently.
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
            # Save results including execution time.
            task_results[problem_name][folder] = {
                "pass": passed,
                "fail": failed,
                "time": exec_time_ns
            }
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

    # Build HTML report with an updated summary table including execution time.
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
