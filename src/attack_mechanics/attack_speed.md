# Attack Speed

<https://liquipedia.net/dota2/Attack_Speed>

## Formulas

\\[ T = \frac{1}{S} \\]
\\[ S = \frac{T_b}{1 + (\frac{S_i}{100})} \\]
\\[ 20 \le \mathit{S_i} \le 700 \\]

## Graph

#### Attack Speed -> Attacks Per Second

```desmos
{
  "expr": [
    {
      "latex": "T = \\frac{1}{S}"
    },
    {
      "latex": "S = \\frac{T_b}{1 + (\\frac{S_i}{100})}",
      "hidden": true
    },
    {
      "latex": "S_i=\\min(\\max(x, 20), 700)",
      "hidden": true
    },
    {
      "latex": "T_b=1.7",
      "sliderBounds": { "min": 0, "max": 2, "step": 0.1 }
    }
  ],
  "bounds": [0, 700, 0, 8],
  "xLabel": "Attack Speed",
  "yLabel": "Attacks Per Second"
}
```
