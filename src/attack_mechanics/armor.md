> This page might be outdated.

# Armor

<https://liquipedia.net/dota2/Armor>

## Formulas

\\[ H_e = \frac{H_c}{D_m} \\]
\\[ D_m = 1 - \frac{0.06 A}{1 + 0.06 |A| } \\]

## Graphs

#### Armor -> Damage Multiplier

```desmos
{
  "expr": [
    { "latex": "D_m = 1 - \\frac{0.06 * A}{1 + 0.06 * \\abs(A) }" }
  ],
  "bounds": [-40, 40, 0, 2],
  "xLabel": "Armor",
  "yLabel": "Damage Multiplier"
}
```

#### Armor -> Effective Health %

```desmos
{
  "expr": [
    { "latex": "H_e = \\frac{100}{D_m}" },
    { "latex": "D_m = 1 - \\frac{0.06 * A}{1 + 0.06 * \\abs(A) }", "hidden": true }
  ],
  "bounds": [-40, 40, 0, 350],
  "xLabel": "Armor",
  "yLabel": "Effective Health %"
}
```
