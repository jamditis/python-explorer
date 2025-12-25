---
name: data-validator
description: Expert knowledge for validating Python Explorer data integrity, finding inconsistencies, and ensuring all library/collection references are correct.
---

# DATA VALIDATOR

## When to Activate

- After bulk importing libraries
- Before committing data changes
- Debugging "library not found" issues
- Checking collection references
- Verifying category mappings

## Mental Model

Think like a **quality assurance engineer** running comprehensive checks before deployment. Data integrity failures create silent bugs—libraries that don't appear, filters that don't work, charts that show wrong counts.

## Validation Layers

```
Layer 1: Schema Validation
    ↓ Does each entry have required fields?
Layer 2: Reference Validation
    ↓ Do categories/libraries exist?
Layer 3: Consistency Validation
    ↓ Are formats uniform across entries?
Layer 4: Display Validation
    ↓ Will data render correctly?
```

## Schema Checks

### Library Entry

Required fields:
```javascript
{
    n: string,  // Name (non-empty)
    c: string,  // Category (in domainMap)
    d: string,  // Description (non-empty)
    l: string   // Link (valid URL)
}
```

### Validation Code

```javascript
function validateLibrary(lib) {
    const errors = [];

    if (!lib.n || typeof lib.n !== 'string')
        errors.push('Missing or invalid name (n)');

    if (!lib.c || typeof lib.c !== 'string')
        errors.push('Missing or invalid category (c)');

    if (!lib.d || typeof lib.d !== 'string')
        errors.push('Missing or invalid description (d)');

    if (!lib.l || !lib.l.startsWith('http'))
        errors.push('Missing or invalid link (l)');

    return errors;
}
```

## Reference Checks

### Category → Domain Mapping

Every category MUST exist in domainMap:

```javascript
const validCategories = new Set(Object.keys(domainMap));

rawLibraries.forEach(lib => {
    if (!validCategories.has(lib.c)) {
        console.error(`Invalid category: "${lib.c}" for ${lib.n}`);
    }
});
```

### Collection → Library References

Every library name in collections MUST exist:

```javascript
const libraryNames = new Set(rawLibraries.map(lib => lib.n));

collections.forEach(col => {
    col.libraries.forEach(name => {
        if (!libraryNames.has(name)) {
            console.error(`Collection "${col.name}" references non-existent library: "${name}"`);
        }
    });
});
```

## Consistency Checks

### Duplicates

```javascript
const seen = new Map();
rawLibraries.forEach(lib => {
    const key = lib.n.toLowerCase();
    if (seen.has(key)) {
        console.warn(`Duplicate library: "${lib.n}" (also "${seen.get(key)}")`);
    }
    seen.set(key, lib.n);
});
```

### Description Length

```javascript
rawLibraries.forEach(lib => {
    if (lib.d.length > 200) {
        console.warn(`Long description (${lib.d.length}): ${lib.n}`);
    }
    if (lib.d.length < 20) {
        console.warn(`Short description (${lib.d.length}): ${lib.n}`);
    }
});
```

### Journalism Tag Format

```javascript
const tagPattern = /\[JOURNALISM\]\s*$/;
rawLibraries.forEach(lib => {
    if (lib.d.includes('[JOURNALISM]') && !tagPattern.test(lib.d)) {
        console.warn(`Malformed journalism tag: ${lib.n}`);
    }
});
```

## Display Checks

### Tag Stripping

Verify tags don't appear in display:

```javascript
// Tags should be stripped by:
lib.d.replace(/\[JOURNALISM\]\s*/g, '')

// Check for any bracket patterns that might leak:
if (/\[[A-Z]+\]/.test(displayedDescription)) {
    console.error('Tag visible in display!');
}
```

### Special Characters

```javascript
rawLibraries.forEach(lib => {
    // Check for problematic characters in HTML context
    if (/[<>"]/.test(lib.d)) {
        console.warn(`Special chars in description: ${lib.n}`);
    }
});
```

## Collection Validation

### Schema Check

```javascript
function validateCollection(col) {
    const errors = [];

    if (!col.name || col.name !== col.name.toUpperCase())
        errors.push('Name must be ALL CAPS');

    if (!['acid', 'ice', 'signal'].includes(col.color))
        errors.push('Invalid color (must be acid, ice, or signal)');

    if (!col.icon || typeof col.icon !== 'string')
        errors.push('Missing icon');

    if (!Array.isArray(col.libraries) || col.libraries.length < 1)
        errors.push('Must have at least one library');

    return errors;
}
```

### Size Guidelines

```javascript
collections.forEach(col => {
    if (col.libraries.length < 4) {
        console.warn(`Small collection (${col.libraries.length}): ${col.name}`);
    }
    if (col.libraries.length > 10) {
        console.warn(`Large collection (${col.libraries.length}): ${col.name}`);
    }
});
```

## Validation Report Template

```markdown
# Data Validation Report

## Summary
- Total Libraries: X
- Total Collections: Y
- Errors Found: Z

## Schema Errors
- [lib name]: Missing field X
- ...

## Reference Errors
- [collection]: References non-existent [library]
- [library]: Uses non-existent category [category]
- ...

## Consistency Warnings
- Duplicate: [lib1] and [lib2]
- Long description: [lib] (250 chars)
- ...

## Recommendations
1. Fix schema errors before deployment
2. Update collection references
3. Consider shortening long descriptions
```

## Automated Validation Script

### Browser Console Version

```javascript
// Paste in browser console on the site
(function validateData() {
    const errors = [];
    const warnings = [];

    // Check libraries
    libraries.forEach((lib, i) => {
        if (!domainColors[lib.domain]) {
            errors.push(`Library ${lib.name}: Unknown domain "${lib.domain}"`);
        }
    });

    // Check collections
    const libNames = new Set(libraries.map(l => l.name));
    collections.forEach(col => {
        col.libraries.forEach(name => {
            if (!libNames.has(name)) {
                errors.push(`Collection "${col.name}": Unknown library "${name}"`);
            }
        });
    });

    console.log('=== VALIDATION RESULTS ===');
    console.log('Errors:', errors.length);
    errors.forEach(e => console.error(e));
    console.log('Warnings:', warnings.length);
    warnings.forEach(w => console.warn(w));
})();
```

## Common Issues

### "0 Libraries" in Collection

**Cause**: Library names don't match exactly
**Fix**: Check case sensitivity, compare to n field

### Library Not in Filters

**Cause**: Category not in domainMap
**Fix**: Use valid category or add to domainMap

### Wrong Domain Color

**Cause**: Category maps to unexpected domain
**Fix**: Check domainMap mapping

### Chart Data Mismatch

**Cause**: Filtered data not passed to updateCharts
**Fix**: Ensure updateCharts(filtered) called in renderGrid

## File Locations

- **Library data**: `/docs/assets/data/libraries.js`
- **Collections**: `/docs/assets/data/collections.js`
- **Domain mapping**: `/docs/assets/data/libraries.js` (domainMap)
- **App logic**: `/docs/assets/js/app.js`

---
**Version**: 1.0
**Last Updated**: 2025-12-25
