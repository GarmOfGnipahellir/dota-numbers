# Dark Seer

## Facets

### Heart of Battle

#### Formulas

\\[ M_b = 275 \\]
\\[ M = M_b + M_n * 0.08 \\]

#### Nearby heroes move speed sum -> Total move speed

```desmos
{
  "expr": [
    { "latex": "M_b = 275" },
    {
      "latex": "(0, M_b)",
      "color": "#2d70b3",
      "dragMode": "NONE",
      "showLabel": true
    },
    { "latex": "M = M_b + x * 0.08", "color": "#2d70b3" }
  ],
  "bounds": [-50, 3000, 200, 550],
  "xLabel": "Nearby heroes move speed sum",
  "yLabel": "Total move speed"
}
```
