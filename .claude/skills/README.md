# Python Explorer - Claude Skills

This directory contains specialized Claude Code skills for the Python Explorer project. Each skill encapsulates expert knowledge to help Claude think like a domain expert rather than follow generic instructions.

## Philosophy

Based on the **4 Core Truths** of skill design:

| Truth | Meaning |
|-------|---------|
| **Expertise Transfer, Not Instructions** | Make Claude *think* like an expert, not follow steps |
| **Flow, Not Friction** | Produce output directly, not intermediate documents |
| **Voice Matches Domain** | Sound like a practitioner, not documentation |
| **Focused Beats Comprehensive** | Constrain ruthlessly. Every section earns its place |

## Available Skills

### library-manager.md

**Purpose**: Add, edit, and validate Python library entries

**Use when**:
- Adding new libraries to the database
- Editing existing library entries
- Bulk importing from external sources
- Validating data integrity

**Key expertise**: Data schemas, category mapping, journalism tags, validation patterns

---

### collection-editor.md

**Purpose**: Create and manage curated library collections

**Use when**:
- Creating themed collections
- Adding/removing libraries from collections
- Fixing broken references
- Choosing styling (colors, icons)

**Key expertise**: Collection schema, naming conventions, library reference validation

---

### description-writer.md

**Purpose**: Write beginner-friendly library descriptions

**Use when**:
- Writing descriptions for new libraries
- Improving unclear descriptions
- Batch processing descriptions
- Adding journalism tags

**Key expertise**: Voice guidelines, length rules, jargon avoidance, tag formatting

---

### data-validator.md

**Purpose**: Validate data integrity across the project

**Use when**:
- After bulk imports
- Before committing changes
- Debugging display issues
- Checking references

**Key expertise**: Schema validation, reference checking, consistency verification

---

### filter-testing.md

**Purpose**: Test filter combinations and state management

**Use when**:
- Testing after filter changes
- Debugging "no results" issues
- Adding new filter types
- Verifying chart synchronization

**Key expertise**: State clearing matrix, test cases, debugging techniques

---

### codebase-navigator.md

**Purpose**: Navigate and understand the codebase architecture

**Use when**:
- First time on project
- Finding where to make changes
- Planning modifications
- Debugging cross-module issues

**Key expertise**: File map, module responsibilities, data flow, modification patterns

---

## Usage

Skills are designed for Claude Code to reference when working on related tasks. They provide:

1. **Mental Models** - How to think about the problem
2. **Schemas** - Data structures and valid values
3. **Patterns** - Common approaches that work
4. **Anti-Patterns** - What to avoid
5. **Troubleshooting** - How to debug issues

## Skill Format

Each skill follows this structure:

```markdown
---
name: skill-name
description: Brief description for activation detection
---

# SKILL NAME

## When to Activate
- Trigger conditions

## Mental Model
- How to think about this domain

## [Domain-Specific Sections]
- Schemas, patterns, guidelines

## Anti-Patterns
- What NOT to do

## Troubleshooting
- Common issues and fixes

## File Locations
- Where to find relevant code
```

## Adding New Skills

1. Create `skill-name.md` in this directory
2. Follow the format above
3. Keep under 500 lines for context efficiency
4. Focus on *how to think* not *what to do*
5. Include practical examples and anti-patterns

## Related Documentation

- `/CLAUDE.md` - Project overview
- `/.clinerules` - Development patterns
- `/.clinerules-lessons` - Lessons learned

---
**Version**: 1.0
**Skills Count**: 5
**Last Updated**: 2025-12-25
