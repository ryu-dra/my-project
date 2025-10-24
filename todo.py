#!/usr/bin/env python3
"""
Simple ToDo Application

A command-line ToDo application with add, list, and done commands.
Supports task name and task details with persistent JSON storage.
"""

import json
import os
import sys
import argparse
from datetime import datetime
from typing import Dict, List, Optional


class Task:
    """Represents a single task with ID, name, details, and status."""
    
    def __init__(self, task_id: int, name: str, details: str = "", status: str = "pending"):
        self.id = task_id
        self.name = name
        self.details = details
        self.status = status
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "details": self.details,
            "status": self.status,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create task from dictionary loaded from JSON."""
        task = cls(data["id"], data["name"], data.get("details", ""), data.get("status", "pending"))
        task.created_at = data.get("created_at", datetime.now().isoformat())
        return task


class TodoApp:
    """Main ToDo application class."""
    
    def __init__(self, data_file: str = "todos.json"):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load_tasks()
    
    def load_tasks(self) -> None:
        """Load tasks from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
                    self.next_id = data.get("next_id", 1)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
                self.next_id = 1
    
    def save_tasks(self) -> None:
        """Save tasks to JSON file."""
        data = {
            "tasks": [task.to_dict() for task in self.tasks],
            "next_id": self.next_id
        }
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, name: str, details: str = "") -> None:
        """Add a new task."""
        task = Task(self.next_id, name, details)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Added task {task.id}: {name}")
    
    def list_tasks(self) -> None:
        """List all tasks."""
        if not self.tasks:
            print("No tasks found.")
            return
        
        print(f"{'ID':<4} {'Name':<20} {'Details':<30} {'Status':<10}")
        print("-" * 70)
        
        for task in self.tasks:
            status_display = "✓ Done" if task.status == "done" else "○ Pending"
            details_display = task.details[:27] + "..." if len(task.details) > 30 else task.details
            print(f"{task.id:<4} {task.name:<20} {details_display:<30} {status_display:<10}")
    
    def mark_done(self, task_id: int) -> None:
        """Mark a task as done."""
        for task in self.tasks:
            if task.id == task_id:
                task.status = "done"
                self.save_tasks()
                print(f"Task {task_id} marked as done: {task.name}")
                return
        
        print(f"Task {task_id} not found.")


def main():
    """Main application entry point."""
    parser = argparse.ArgumentParser(description="Simple ToDo Application")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('name', help='Task name')
    add_parser.add_argument('details', nargs='?', default='', help='Task details (optional)')
    
    # List command
    subparsers.add_parser('list', help='List all tasks')
    
    # Done command
    done_parser = subparsers.add_parser('done', help='Mark a task as done')
    done_parser.add_argument('task_id', type=int, help='Task ID to mark as done')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    app = TodoApp()
    
    try:
        if args.command == 'add':
            app.add_task(args.name, args.details)
        elif args.command == 'list':
            app.list_tasks()
        elif args.command == 'done':
            app.mark_done(args.task_id)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
