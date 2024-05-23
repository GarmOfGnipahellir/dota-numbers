# Movement Speed

<https://liquipedia.net/dota2game/Movement_Speed>

## Formulas

\\[ M = (M_0 + M_b) * M_f \\]
\\[ M_f = 1 + (\frac{M_p}{100}) \\]
\\[ 100 \le \mathit{M} \le 550 \\]

## Graph

#### Flat Bonus -> Movement Speed

```desmos
{
  "expr": [
    {
      "latex": "M = \\min(\\max((M_0 + M_b) * M_f, 100), 550)"
    },
    {
      "latex": "M_b=x",
      "hidden": true
    },
    {
      "latex": "M_f = 1 + (\\frac{M_p}{100})",
      "hidden": true
    },
    {
      "latex": "M_0=300",
      "sliderBounds": { "min": 200, "max": 400, "step": 5 }
    },
    {
      "latex": "M_p=0",
      "sliderBounds": { "min": -200, "max": 200, "step": 5 }
    }
  ],
  "bounds": [-250, 300, 0, 600],
  "xLabel": "Flat Bonus",
  "yLabel": "Movement Speed"
}
```
