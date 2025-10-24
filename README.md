# ToDo Application

A simple command-line ToDo application with add, list, and done commands.

## Features

- **Add tasks**: Create new tasks with name and optional details
- **List tasks**: View all tasks with ID, name, details, and status
- **Mark done**: Mark tasks as completed
- **Persistent storage**: Tasks are saved to JSON file
- **Cross-platform**: Works on Windows, macOS, and Linux

## Usage

### Add a new task
```bash
python todo.py add "Task Name" "Task Details"
python todo.py add "Task Name"  # Details are optional
```

### List all tasks
```bash
python todo.py list
```

### Mark a task as done
```bash
python todo.py done <task-id>
```

### Get help
```bash
python todo.py --help
```

## Examples

```bash
# Add tasks
python todo.py add "Buy groceries" "Get milk, bread, and eggs"
python todo.py add "Call mom"
python todo.py add "Finish project" "Complete the OpenSpec implementation"

# List tasks
python todo.py list

# Mark task as done
python todo.py done 1

# List tasks again to see status change
python todo.py list
```

## Output Example

```
ID   Name                 Details                         Status    
----------------------------------------------------------------------
1    Buy groceries        Get milk, bread, and eggs       ○ Pending
2    Call mom                                              ○ Pending
3    Finish project       Complete the OpenSpec implem... ○ Pending

Task 1 marked as done: Buy groceries

ID   Name                 Details                         Status    
----------------------------------------------------------------------
1    Buy groceries        Get milk, bread, and eggs       ✓ Done
2    Call mom                                              ○ Pending
3    Finish project       Complete the OpenSpec implem... ○ Pending
```

## Data Storage

Tasks are stored in `todos.json` file in the same directory as the application. The file contains:

```json
{
  "tasks": [
    {
      "id": 1,
      "name": "Buy groceries",
      "details": "Get milk, bread, and eggs",
      "status": "done",
      "created_at": "2024-01-01T12:00:00.000000"
    }
  ],
  "next_id": 2
}
```

## Requirements

- Python 3.8 or higher
- No external dependencies (uses only Python standard library)

## Error Handling

The application handles various error scenarios:

- Invalid commands show help message
- Missing task ID for done command shows error
- Non-existent task ID shows "Task not found"
- File I/O errors are handled gracefully
- Keyboard interrupt (Ctrl+C) is handled
