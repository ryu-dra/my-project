# Project Context

## Purpose
A simple command-line ToDo application for personal task management with basic add, list, and done functionality.

## Tech Stack
- Python 3.8+
- JSON for data persistence
- argparse for command-line interface

## Project Conventions

### Code Style
- Use Python PEP 8 style guidelines
- Use descriptive variable and function names
- Include docstrings for functions and classes
- Use type hints where appropriate

### Architecture Patterns
- Simple command-line application structure
- Separation of concerns: data model, storage, commands, CLI
- File-based persistence using JSON format

### Testing Strategy
- Manual testing of all commands
- Test error handling scenarios
- Verify data persistence across sessions

### Git Workflow
- Use descriptive commit messages
- Create feature branches for major changes
- Keep commits focused and atomic

## Domain Context
This is a personal productivity tool for managing daily tasks. The application should be simple, reliable, and easy to use from the command line.

## Important Constraints
- Must work on Windows, macOS, and Linux
- Should not require external dependencies beyond Python standard library
- Data should be stored locally in a simple format
- Application should be lightweight and fast

## External Dependencies
- Python standard library only
- No external packages required
