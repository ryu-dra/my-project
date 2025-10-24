@echo off
REM ToDo Application Launcher for Windows

if "%1"=="" (
    echo Usage: todo.bat [command] [arguments]
    echo.
    echo Commands:
    echo   add "task name" "task details"  - Add a new task
    echo   list                            - List all tasks
    echo   done [task-id]                  - Mark task as done
    echo   help                            - Show help
    echo.
    echo Examples:
    echo   todo.bat add "Buy groceries" "Get milk and bread"
    echo   todo.bat list
    echo   todo.bat done 1
    goto :eof
)

if "%1"=="help" (
    python todo.py --help
    goto :eof
)

python todo.py %*
