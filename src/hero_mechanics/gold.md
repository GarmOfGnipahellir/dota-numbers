# Gold

<https://liquipedia.net/dota2/Gold>

## Gold Loss

### Formula

\\[ G = \frac{N}{40} \\]

### Graph

#### Net Worth -> Unreliable Gold Lost

```desmos
{
  "expr": [
    { "latex": "G = \\frac{N}{40}" }
  ],
  "bounds": [0, 40000, 0, 1000],
  "xLabel": "Net Worth",
  "yLabel": "Unreliable Gold Lost"
}
```

## Kill Bounty

### Formulas

\\[ B_s = 5 S^2 + 5 S \\]
\\[ B = 125 + 8 L + B_s \\]

### Graphs

#### Kill Streak -> Streak Bonus

```desmos
{
  "expr": [
    { "latex": "B_s = 5 S^2 + 5 S" },
    { "latex": "S = \\ceil(\\frac{\\max(x - 2.99, 0)}{x}) * \\min(x, 10)", "hidden": true },
    {
      "type": "table",
      "columns": [
        {
          "latex": "x",
          "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        },
        {
          "latex": "B_s",
          "color": "#2d70b3"
        }
      ]
    }
  ],
  "bounds": [0, 11, 0, 600],
  "xLabel": "Kill Streak",
  "yLabel": "Streak Bonus"
}
```

#### Killed Hero Level -> Kill Bounty

```desmos
{
  "expr": [
    { "latex": "B = 125 + 8 L + B_s" },
    { "latex": "B_s = 5 S^2 + 5 S" },
    { "latex": "S = \\ceil(\\frac{\\max(S_i - 2.99, 0)}{S_i}) * \\min(S_i, 10)" },
    { "latex": "L = x", "hidden": true },
    {
      "latex": "S_i = 1",
      "sliderBounds": { "min": 1, "max": 10, "step": 1 }
    },
    {
      "type": "table",
      "columns": [
        {
          "latex": "x",
          "values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        },
        {
          "latex": "B",
          "color": "#2d70b3"
        }
      ]
    }
  ],
  "bounds": [0, 34, 0, 1000],
  "xLabel": "Killed Hero Level",
  "yLabel": "Kill Bounty"
}
```
