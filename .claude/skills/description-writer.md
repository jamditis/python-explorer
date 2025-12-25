---
name: description-writer
description: Expert knowledge for writing beginner-friendly library descriptions that are clear, practical, and jargon-free. Use when adding or improving library descriptions.
---

# DESCRIPTION WRITER

## When to Activate

- Writing descriptions for new libraries
- Improving unclear or technical descriptions
- Batch processing library descriptions
- Ensuring consistent tone across database
- Adding journalism relevance tags

## Mental Model

Think like a **friendly teacher** explaining tools to someone who just started coding. Your goal: help them understand what a library does and why they'd use it, not impress them with technical vocabulary.

## Voice Guidelines

### Target Audience

Beginner to intermediate Python developers who:
- Know basic Python syntax
- Are exploring what's possible
- Want practical solutions, not theory
- Appreciate plain language

### Tone Spectrum

```
Technical ◀━━━━━━━━━━━●━━━━━━▶ Oversimplified
                    HERE
```

Aim for: Clear but not dumbed down.

## Structure Formula

### Pattern A: What + Why

```
[What it does] + [why you'd use it]
```

Example:
> "Makes it easy to work with spreadsheet-like data in Python—sort it, filter it, analyze it, and create charts all in code."

### Pattern B: Problem + Solution

```
[The problem it solves] + [how it helps]
```

Example:
> "Takes the pain out of HTTP requests by handling cookies, sessions, and retries automatically."

### Pattern C: Category + Standout

```
[Category label] + [what makes it special]
```

Example:
> "A web framework that emphasizes simplicity and minimalism—perfect for small projects that don't need Django's complexity."

## Length Guidelines

| Length | Characters | When to Use |
|--------|-----------|-------------|
| Short | 50-80 | Simple, focused libraries |
| Medium | 80-120 | Most libraries |
| Long | 120-150 | Complex tools needing context |

**Hard limit**: 150 characters (enforced in tools)

## Word Choice

### Replace Technical Jargon

| Instead of | Write |
|------------|-------|
| "ORM" | "talk to databases using Python objects" |
| "serialization" | "converting data to/from files" |
| "async" | "handles many tasks at once" |
| "middleware" | "processing layer" |
| "API" | "connects to web services" |
| "parsing" | "reading and understanding" |

### Avoid Marketing Words

| Avoid | Why |
|-------|-----|
| "best", "amazing", "powerful" | Empty superlatives |
| "industry-leading" | Marketing speak |
| "revolutionary" | Overpromises |
| "enterprise-grade" | Vague |
| "blazing fast" | Unmeasurable |

### Use Action Words

- "Makes it easy to..."
- "Helps you..."
- "Handles..."
- "Automates..."
- "Creates..."
- "Turns... into..."

## Examples by Category

### Web Frameworks

```
Flask: "A lightweight web framework that gives you just what you need to build websites without extra complexity."

Django: "A full-featured web framework that handles most of what you need for professional websites out of the box."
```

### Data Science

```
pandas: "Makes it easy to work with spreadsheet-like data in Python—sort it, filter it, analyze it, and create charts all in code."

NumPy: "The foundation for scientific computing in Python—handles large arrays of numbers efficiently."
```

### Machine Learning

```
scikit-learn: "A beginner-friendly toolkit for machine learning that includes everything from simple predictions to complex models."

TensorFlow: "Google's library for building and training machine learning models, especially neural networks."
```

### DevOps

```
Fabric: "Automates running commands on remote servers—perfect for deployments and system administration."

Ansible: "Manages server configurations and deployments using simple YAML files instead of complex scripts."
```

## Journalism Tag

### When to Add

Add `[JOURNALISM]` to libraries useful for:
- Data journalism and analysis
- Web scraping and data collection
- Document processing (PDFs, images)
- Data visualization
- Media handling (images, video, audio)
- Content management

### Format

```javascript
d: "Description text goes here. [JOURNALISM]"
```

Tag is always at the END, after the period.

### Currently Tagged Categories

- Data Analysis (pandas, numpy)
- Web Scraping (BeautifulSoup, Scrapy, requests)
- Visualization (matplotlib, seaborn, altair, bokeh)
- Document Processing (PyPDF2, python-docx, pytesseract)
- Image/Video (OpenCV, Pillow, moviepy)
- CMS/Admin (Django, Flask-Admin, Wagtail)

## Batch Processing

### Workflow

1. **Identify**: List libraries needing descriptions
2. **Research**: Quick PyPI/docs check for each
3. **Draft**: Write using patterns above
4. **Review**: Check length, tone, accuracy
5. **Tag**: Add journalism tags where relevant

### Batch Format

```javascript
// Generate multiple entries at once
const newDescriptions = [
    { n: "library1", d: "Description here." },
    { n: "library2", d: "Another description. [JOURNALISM]" },
    // ...
];
```

## Quality Checklist

For each description:

- [ ] Under 150 characters
- [ ] Starts with action verb or "A/An..."
- [ ] No jargon (or jargon explained)
- [ ] No marketing superlatives
- [ ] Tells what it does AND why
- [ ] Would make sense to a beginner
- [ ] Journalism tag if relevant

## Anti-Patterns

| Don't | Do |
|-------|-----|
| Copy from official docs | Rewrite in plain language |
| List features | Focus on one main benefit |
| Use abbreviations | Spell out or explain |
| Write academic prose | Write conversationally |
| Assume knowledge | Explain context briefly |

## Consistency Checks

### Casing

- Sentence case for descriptions
- Library names match original casing

### Punctuation

- End with period (before any tags)
- No trailing spaces
- No quotes around the description text

### Length Variance

Descriptions should vary naturally:
- Don't force all to same length
- Simpler tools get shorter descriptions
- Complex tools may need more context

## File Locations

- **Library data**: `/docs/assets/data/libraries.js`
- **Enhancement tools**: `/tools/merge_enhanced_descriptions.py`
- **Batch files**: `/tools/batch_*_libs.json`

---
**Version**: 1.0
**Last Updated**: 2025-12-25
