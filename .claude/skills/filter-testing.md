---
name: filter-testing
description: Expert knowledge for testing all filter combinations in Python Explorer. Use when verifying filter logic, debugging state issues, or testing new filter features.
---

# FILTER TESTING

## When to Activate

- Testing filter combinations after changes
- Debugging "no results" issues
- Verifying state management works correctly
- Adding new filter types
- Checking chart synchronization

## Mental Model

Think like a **QA tester** systematically covering all interaction paths. The filter system has multiple entry points that can conflict—your job is to verify they play nice together.

## Filter System Architecture

```
User Action
    ↓
State Update + Clear Conflicts
    ↓
Filtering Pipeline:
    1. Primary Filter (one only)
       ├─ journalismFilter → Direct tag match
       ├─ activeCollection → Collection lookup
       └─ search → Fuzzy search (Fuse.js)

    2. Secondary Filter (optional)
       └─ activeCategories → Category multi-select

    ↓
Filtered Results
    ↓
Render Grid + Update Charts
```

## State Object

```javascript
state = {
    search: "",              // Fuzzy search input
    activeCategories: [],    // Multi-select categories
    sortBy: "relevance",     // Sort mode
    journalismFilter: false, // Journalism toolkit flag
    activeCollection: null   // Selected collection name
}
```

## State Clearing Matrix

| When User... | Clear |
|--------------|-------|
| Types in search | collection, journalismFilter |
| Clicks category | collection, journalismFilter |
| Selects collection | search, categories, journalismFilter |
| Clicks journalism | search, categories, collection |
| Clicks reset | ALL |

## Test Cases

### Primary Filter Tests

#### T1: Search Only

```
Action: Type "django" in search
Expect:
  - state.search = "django"
  - Grid shows Django-related libraries
  - Charts update to show filtered domains
  - No journalism/collection active
```

#### T2: Journalism Filter

```
Action: Click "VIEW TOOLKIT"
Expect:
  - state.journalismFilter = true
  - state.search = "" (cleared)
  - state.activeCategories = [] (cleared)
  - state.activeCollection = null (cleared)
  - Grid shows only [JOURNALISM] tagged libraries (39)
  - Charts show journalism subset
```

#### T3: Collection Filter

```
Action: Click "DATA JOURNALISM TOOLKIT" collection
Expect:
  - state.activeCollection = "DATA JOURNALISM TOOLKIT"
  - state.search = "" (cleared)
  - state.activeCategories = [] (cleared)
  - state.journalismFilter = false (cleared)
  - Grid shows only collection's libraries
  - Charts show collection subset
```

### Combined Filter Tests

#### T4: Search + Categories

```
Action:
  1. Type "data" in search
  2. Check "Data Analysis" category
Expect:
  - Both filters applied
  - Results: libraries matching "data" AND in "Data Analysis"
  - Charts reflect combined filter
```

#### T5: Collection → Search (Clear Test)

```
Action:
  1. Select "AI & MACHINE LEARNING" collection
  2. Type "tensor" in search
Expect:
  - Collection cleared when search starts
  - state.activeCollection = null
  - Search takes over
```

#### T6: Journalism → Category (Clear Test)

```
Action:
  1. Click "VIEW TOOLKIT" (journalism)
  2. Check "Web Frameworks" category
Expect:
  - Journalism cleared when category selected
  - state.journalismFilter = false
  - Category filter takes over
```

### Edge Case Tests

#### T7: Reset Button

```
Action: Apply multiple filters, then click RESET
Expect:
  - state = initial values
  - All checkboxes unchecked
  - Search input empty
  - Grid shows all 345+ libraries
  - Charts show full dataset
```

#### T8: Empty Results

```
Action: Search for "xyznonexistent123"
Expect:
  - Grid shows "No libraries found" message
  - Charts handle empty data gracefully
  - Filter can be cleared
```

#### T9: Case Sensitivity

```
Action: Search for "DJANGO" vs "django"
Expect:
  - Same results (Fuse.js case-insensitive)
  - Journalism tag matching case-sensitive
```

### Chart Synchronization Tests

#### T10: Chart Updates

```
Action: Apply any filter
Verify:
  - Domain doughnut chart reflects filtered libraries
  - Category bar chart reflects filtered libraries
  - Counts match visible grid items
```

## Manual Testing Checklist

### Basic Flows

- [ ] Search returns expected results
- [ ] Category filter narrows results
- [ ] Collection shows only its libraries
- [ ] Journalism shows tagged libraries only
- [ ] Reset clears everything

### State Clearing

- [ ] Search clears collection
- [ ] Search clears journalism
- [ ] Category clears collection
- [ ] Category clears journalism
- [ ] Collection clears search
- [ ] Collection clears categories
- [ ] Collection clears journalism
- [ ] Journalism clears search
- [ ] Journalism clears collection
- [ ] Journalism clears categories

### Visual Verification

- [ ] Charts update with filters
- [ ] Active filter pills appear
- [ ] Category checkboxes sync
- [ ] Result count updates
- [ ] [JOURNALISM] tags hidden

## Debugging Techniques

### Console State Check

```javascript
// Check current state in browser console
console.log(state);
```

### Filter Pipeline Debug

```javascript
// Add to renderGrid() for debugging
console.log('Filter pipeline:', {
    journalism: state.journalismFilter,
    collection: state.activeCollection,
    search: state.search,
    categories: state.activeCategories,
    resultCount: filtered.length
});
```

### Chart Data Debug

```javascript
// Add to updateCharts() for debugging
console.log('Chart data:', {
    domains: Object.keys(domains),
    categories: topCategories.map(c => c[0])
});
```

## Common Bugs

### Bug: Filter Returns 0 Results

**Symptom**: Collection or journalism shows 0 libraries

**Causes**:
1. Library names don't match (case-sensitive)
2. Tag not present in description
3. State not cleared properly

**Debug**:
```javascript
// Check collection library names
collections.find(c => c.name === "COLLECTION NAME").libraries
// Compare with actual library names
libraries.map(l => l.name)
```

### Bug: Charts Don't Update

**Symptom**: Charts show stale data after filtering

**Cause**: updateCharts() not called with filtered data

**Fix**: Ensure renderGrid() calls:
```javascript
updateCharts(filtered); // Must pass filtered array
```

### Bug: State Conflicts

**Symptom**: Multiple filters active simultaneously

**Cause**: State clearing missing in handler

**Check**: Each filter handler should clear others:
```javascript
// In filter handler
state.activeCollection = null;
state.journalismFilter = false;
// etc.
```

## Automated Test Script

```javascript
// Run in browser console
(function testFilters() {
    const results = [];

    // Test 1: Initial state
    resetFilters();
    results.push({
        test: 'Initial state',
        pass: state.search === "" &&
              state.activeCategories.length === 0 &&
              state.journalismFilter === false &&
              state.activeCollection === null
    });

    // Test 2: Search clears others
    state.activeCollection = "TEST";
    state.search = "django";
    // Trigger renderGrid
    results.push({
        test: 'Search clears collection',
        pass: state.activeCollection === null
    });

    // Add more tests...

    console.table(results);
})();
```

## Performance Considerations

- Fuse.js handles 345+ libraries efficiently
- Threshold 0.4 balances accuracy/speed
- Chart updates are lightweight
- Avoid unnecessary re-renders

## File Locations

- **State management**: `/docs/assets/js/app.js`
- **Filter logic**: `/docs/assets/js/app.js` (renderGrid)
- **Chart updates**: `/docs/assets/js/charts.js` (updateCharts)
- **Collection filter**: `/docs/assets/js/app.js` (filterByCollection)
- **Journalism filter**: `/docs/assets/js/app.js` (filterJournalismLibs)

---
**Version**: 1.0
**Last Updated**: 2025-12-25
