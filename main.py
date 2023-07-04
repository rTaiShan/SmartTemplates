from tools.io import preview_html
from tools.task import get_tasks


if __name__ == "__main__":
    # Get tasks in tasks\\tasks.json
    tasks = get_tasks(path="tasks\\tasks.json", filter_enabled=True)

    for task in tasks:
        # Render and preview Smart Templates from tasks
        html = task.run(force=False)
        preview_html(html)
    